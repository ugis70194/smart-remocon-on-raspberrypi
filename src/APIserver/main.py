import uvicorn
from fastapi import FastAPI

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.playback import send_signal
from utils.encode import encode


app = FastAPI()

@app.get("/light_on")
async def request_light_on():
  try:
    res = send_signal("light:on")
    if res == 0:
      return {"response_code": "OK"}
    else:
      return {"response_code": "NG"}
  except: 
    return {"response_code": "NG"}
  

@app.get("/light_off")
async def request_light_off():
  try:
    res = send_signal("light:off")
    if res == 0:
      return {"response_code": "OK"}
    else:
      return {"response_code": "NG"}
  except: 
    return {"response_code": "NG"}
  
def send_aircon_signal():
  try:
    res = send_signal("aircon:op")
    if res == 0:
      return {"response_code": "OK"}
    else:
      return {"response_code": "NG"}
  except: 
    return {"response_code": "NG"}

@app.get("/aircon_on")
async def request_aircon_on():
  try:
    encode("cool", "28")
    send_aircon_signal()
  except: 
    return {"response_code": "Can't Generate Signal"}

@app.get("/aircon_off")
async def request_aircon_off():
  try:
    encode("off", "28")
    send_aircon_signal()
  except: 
    return {"response_code": "NG"}  

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=3000)