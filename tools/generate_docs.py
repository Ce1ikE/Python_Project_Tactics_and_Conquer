"""Lightweight docs generator: extracts module and class docstrings to Markdown."""
from pathlib import Path
import inspect
import importlib
import pkgutil
import sys

ROOT = Path(__file__).resolve().parent.parent
PKG = "tactics_and_conquer.classes"
OUT = ROOT / "docs" / "reference"


def ensure_out():
    OUT.mkdir(parents=True, exist_ok=True)


def module_objects(module_name: str):
    mod = importlib.import_module(module_name)
    for name, obj in inspect.getmembers(mod, inspect.isclass):
        # only local classes
        if obj.__module__ == module_name:
            yield name, obj


def write_class_md(cls, out_path: Path):
    lines = []
    lines.append(f"# {cls.__name__}\n")
    if cls.__doc__:
        lines.append(cls.__doc__.strip() + "\n")
    lines.append("## Public methods\n")
    for name, func in inspect.getmembers(cls, inspect.isfunction):
        if func.__qualname__.split(".")[0] == cls.__name__:
            sig = str(inspect.signature(func))
            doc = (func.__doc__ or "").strip()
            lines.append(f"### ```{name}{sig}```\n\n{doc}\n")
    out_path.write_text("\n".join(lines), encoding="utf8")


def main():
    ensure_out()
    # ensure project root is on sys.path so package can be imported
    project_root = str(ROOT)
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    # import package to ensure path
    pkg = importlib.import_module(name=PKG)
    for finder, name, ispkg in pkgutil.iter_modules(pkg.__path__):
        full = PKG + "." + name
        try:
            mod = importlib.import_module(full)
        except Exception as e:
            print(f"skip module {full}: {e}")
            continue
        for cname, cls in module_objects(full):
            write_class_md(cls, OUT / f"{cname}.md")


if __name__ == "__main__":
    main()
