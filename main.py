import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

def play_music(folder, song_name):
    file_path = os.path.join(folder, song_name)

    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist")
        return
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    print(f"\n Playing {song_name}")
    print("Commands: [P]ause, [R]esume, [S]top ")

    while True:
        command = input("> ").upper()

        if command == "P":
            pygame.mixer.music.pause()
            print("Paused")
        elif command == "R":
            pygame.mixer.music.unpause()
            print("Resumed")
        elif command == "S":
            pygame.mixer.music.stop()
            print("Stopped")
            return
        else:
            print("Invalid command")


def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("Audio initialization failed:", e)
        return
    folder = "music"

    if not os.path.exists(folder):
        print(f"Folder {folder} does not exist")
        return

    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]
    if len(mp3_files) == 0:
        print(f"No mp3 files found in folder {folder}")
        return

    while True:
        for index, song in enumerate(mp3_files, start=1):
            print(f"{index}. {song}")
        choice_input = input("Select an mp3 file: ")
        if choice_input.upper() == "Q":
            print("Quitting...")
            break
        if not choice_input.isdigit():
            print("Invalid choice")
            continue
        choice = int(choice_input) - 1

        if 0 <= choice < len(mp3_files):
            play_music(folder, mp3_files[choice])
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()