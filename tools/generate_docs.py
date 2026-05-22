"""Lightweight docs generator: extracts module and class docstrings to Markdown."""
from __future__ import annotations
from pathlib import Path
import ast
# https://greentreesnakes.readthedocs.io/en/latest/
#
# "Green Tree Snakes - the missing Python AST docs"
# "Abstract Syntax Trees, ASTs, are a powerful feature of Python. 
# You can write programs that inspect and modify Python code, after the syntax has been parsed, 
# but before it gets compiled to byte code. That opens up a world of possibilities for introspection, testing, and mischief.""
#
# For us we can use it as a way to extract the docstrings from the classes and methods in our codebase,
# and then write them to markdown files in the "docs/reference" folder, this way we can implement as kinda docs as code approach, 
# where the documentation is generated from the code itself, and we can keep the documentation up to date with the code changes, 
# without having to manually update the documentation every time we make a change to the codebase.

ROOT = Path(__file__).resolve().parent.parent
PKG_DIR = ROOT / "tactics_and_conquer" / "classes"
OUT = ROOT / "docs" / "reference"


def ensure_out():
    OUT.mkdir(parents=True, exist_ok=True)

def format_args(args: ast.arguments) -> str:
    parts: list[str] = []
    positional = list(args.posonlyargs) + list(args.args)
    defaults = [None] * (len(positional) - len(args.defaults)) + list(args.defaults)
    for arg, default in zip(positional, defaults, strict=True):
        piece = arg.arg
        if default is not None:
            piece += f"={ast.unparse(default)}"
        parts.append(piece)
    if args.posonlyargs:
        parts.insert(len(args.posonlyargs), "/")
    if args.vararg:
        parts.append(f"*{args.vararg.arg}")
    elif args.kwonlyargs:
        parts.append("*")
    for arg, default in zip(args.kwonlyargs, args.kw_defaults, strict=True):
        piece = arg.arg
        if default is not None:
            piece += f"={ast.unparse(default)}"
        parts.append(piece)
    if args.kwarg:
        parts.append(f"**{args.kwarg.arg}")
    return ", ".join(parts)


def module_objects(module_path: Path):
    module = ast.parse(module_path.read_text(encoding="utf8"), filename=str(module_path))
    for node in module.body:
        if isinstance(node, ast.ClassDef):
            yield node

def write_class_md(cls: ast.ClassDef, out_path: Path):
    lines = []
    lines.append(f"# {cls.name}\n")
    doc = ast.get_docstring(cls)
    if doc:
        lines.append(doc.strip() + "\n")
    lines.append("## Public methods\n")
    for node in cls.body:
        if isinstance(node, ast.FunctionDef):
            sig = f"({format_args(node.args)})"
            method_doc = ast.get_docstring(node) or ""
            lines.append(f"### ```{node.name}{sig}```\n\n{method_doc.strip()}\n")
    out_path.write_text("\n".join(lines), encoding="utf8")


def main():
    ensure_out()
    for module_path in sorted(PKG_DIR.glob("*.py")):
        if module_path.name == "__init__.py":
            continue
        for cls in module_objects(module_path):
            write_class_md(cls, OUT / f"{cls.name}.md")

if __name__ == "__main__":
    main()
