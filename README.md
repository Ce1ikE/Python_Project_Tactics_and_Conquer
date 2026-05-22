# Python-Project-YT6264
This folder contains all files regarding the project for this course

# Tactics & Conquer

Turn-based strategy game built with Python, Pygame, and pygame_gui.

## Requirements

- Python 3.14
- `uv`
- Linux SDL development packages if pygame needs to build from source

## Install

From the project root, install the Python dependencies with:

```bash
uv sync
```

If pygame fails to install with an SDL-related build error, install the native system libraries first and then run `uv sync` again.

### Ubuntu / Debian / Mint

```bash
sudo apt update
sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libfreetype6-dev libportmidi-dev libjpeg-dev
```

### Fedora / RHEL

```bash
sudo dnf install SDL2-devel SDL2_image-devel SDL2_mixer-devel SDL2_ttf-devel freetype-devel portmidi-devel
```

### Arch Linux

```bash
sudo pacman -S sdl2 sdl2_image sdl2_mixer sdl2_ttf portmidi
```

After installing those packages, retry:

```bash
uv sync
```

### Why this happens

Pygame usually installs as a prebuilt wheel, so no compilation is needed. On Python 3.14, wheels may not be available yet for every platform, which can force a source build. When that happens, the SDL development headers must already be installed on the system.

## Run

Once dependencies are installed, launch the game with:

```bash
uv run python main.py
```

## Project Layout

- `main.py` starts the game.
- `tactics_and_conquer/` contains the package code.
- `tactics_and_conquer/classes/` contains the gameplay, UI, and map classes.
- `assets/` contains styles, sprites and fonts.


## Authors
- Celik E.
- Crollet W.

```
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 ________                     __      __                             ___             ______                                                              
/        |                   /  |    /  |                           /   \           /      \                                                             
$$$$$$$$/______    _______  _$$ |_   $$/   _______   _______       /$$$  |         /$$$$$$  |  ______   _______    ______   __    __   ______    ______  
   $$ | /      \  /       |/ $$   |  /  | /       | /       |      $$ $$ \__       $$ |  $$/  /      \ /       \  /      \ /  |  /  | /      \  /      \ 
   $$ | $$$$$$  |/$$$$$$$/ $$$$$$/   $$ |/$$$$$$$/ /$$$$$$$/       /$$$     |      $$ |      /$$$$$$  |$$$$$$$  |/$$$$$$  |$$ |  $$ |/$$$$$$  |/$$$$$$  |
   $$ | /    $$ |$$ |        $$ | __ $$ |$$ |      $$      \       $$ $$ $$/       $$ |   __ $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
   $$ |/$$$$$$$ |$$ \_____   $$ |/  |$$ |$$ \_____  $$$$$$  |      $$ \$$  \       $$ \__/  |$$ \__$$ |$$ |  $$ |$$ \__$$ |$$ \__$$ |$$$$$$$$/ $$ |      
   $$ |$$    $$ |$$       |  $$  $$/ $$ |$$       |/     $$/       $$   $$  |      $$    $$/ $$    $$/ $$ |  $$ |$$    $$ |$$    $$/ $$       |$$ |      
   $$/  $$$$$$$/  $$$$$$$/    $$$$/  $$/  $$$$$$$/ $$$$$$$/         $$$$/$$/        $$$$$$/   $$$$$$/  $$/   $$/  $$$$$$$ | $$$$$$/   $$$$$$$/ $$/       
                                                                                                                       $$ |                              
                                                                                                                       $$ |                              
                                                                                                                       $$/                             
   
Python - Labo YT0744
+==========+========================+===========+
| Project: |  Game                  |           |
| Name:    |  Tactics & Conquer     |           |
| Authors: |  Crollet W.            | Celik E.  |
+==========+========================+===========+

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

```

## quick notes
while i had a joy making this project , it was quite a naive implementation of any game implementation out there. 
I didn't fully grasp that i accidently implementated a finite state machine for the main game loop and didn't know about design patterns.

while you don't neccesarly always require design patterns because it does require you to have knowledge and experience for it. 
it sure does make your codebase much cleaner in some instances (sometimes it abstracts code and thus it becomes actually less readbale and thus maintainable)

also when it comes to OOP (object oriented programming) it is not always done correctly , 
such as which class should contain what data (would actually use some type of ECS pattern now).

Lastly is probably the fact that their is no UML diagram that gives a clear overview on how the project's classes interact with each other, which can give a much better understanding on how to structure your codebase before doing any coding at all
docs as code would be quite uesfull for these things