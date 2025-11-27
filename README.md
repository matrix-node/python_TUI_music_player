🎵 Python Terminal MP3 Player

A simple terminal-based MP3 player built with Python and Pygame.
It scans a music/ folder, lists available tracks, and gives you basic playback controls.


🚀 Features

Auto-detect .mp3 files

Pause, resume, stop controls

Clean terminal interaction

Handles missing folders/files gracefully



📦 Requirements

Install Pygame:

pip install pygame

Arch Linux (btw 🐧):

sudo pacman -S python-pygame



Setup

1. Create a folder named music/


2. Add .mp3 files


3. Run:



python main.py



🎮 Controls

Inside playback mode:

P → Pause

R → Resume

S → Stop

Q → Quit to menu



🧩 Structure

play_music() → Handles audio loading + controls

main() → Initializes audio + track selection




⚠️ Notes

Shows errors for missing folders or bad input

Gracefully exits on audio init failure