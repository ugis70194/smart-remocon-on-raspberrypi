import uvicorn
from fastapi import FastAPI

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.playback import send_signal

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
  
if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=3000)