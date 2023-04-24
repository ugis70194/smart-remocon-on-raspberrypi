from fastapi import FastAPI

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.mock_playback import send_signal

app = FastAPI()

@app.get("/light_on")
async def request_light_on():
  try:
    res = send_signal("light_on")
    if res == 0:
      return {"response_code": "OK"}
    else:
      return {"response_code": "NG"}
  except: 
    return {"response_code": "NG"}
  

@app.get("/light_off")
async def request_light_off():
  try:
    res = send_signal("light_off")
    if res == 0:
      return {"response_code": "OK"}
    else:
      return {"response_code": "NG"}
  except: 
    return {"response_code": "NG"}