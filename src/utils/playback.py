import json
import pigpio
import time
from time import gmtime, strftime
from logging import getLogger
from os import getenv
from dotenv import load_dotenv

logger = getLogger(__name__)

load_dotenv()
GPIO = int(getenv('PB_GPIO'))
FILE = getenv('PB_FILE')
FREQ = float(getenv('PB_FREQ'))
GAP_S = float(getenv('PB_GAP_S'))

pi = pigpio.pi() # Connect to Pi.

if not pi.connected:
  exit(0)

def carrier(gpio, frequency, micros):
  """
  Generate carrier square wave.
  """
  wf = []
  cycle = 1000.0 / frequency
  cycles = int(round(micros/cycle))
  on = int(round(cycle / 2.0))
  sofar = 0
  for c in range(cycles):
    target = int(round((c+1)*cycle))
    sofar += on
    off = target - sofar
    sofar += off
    wf.append(pigpio.pulse(1<<gpio, 0, on))
    wf.append(pigpio.pulse(0, 1<<gpio, off))
  return wf

def send_signal(code_id: str):
  try:
    f = open(FILE, "r")
  except:
    now = strftime("%Y/%m/%d %H:%M:%S +0000", gmtime())
    logger.error(f"{now}: Could't open \"{FILE}\" ")
    exit(0)

  try:
    records = json.load(f)
    f.close()
    pi.set_mode(GPIO, pigpio.OUTPUT) # IR TX connected to this GPIO
    pi.wave_add_new()
    emit_time = time.time()

    if not code_id in records:
      now = strftime("%Y/%m/%d %H:%M:%S +0000", gmtime())
      logger.error(f"{now}: Could't find \"{code_id}\" in recodes ")
      exit(0)

    code = records[code_id]

    # Create wave
    marks_wid = {}
    spaces_wid = {}

    wave = [0]*len(code)

    for i in range(0, len(code)):
      ci = code[i]
      if i & 1: # Space
        if ci not in spaces_wid:
          pi.wave_add_generic([pigpio.pulse(0, 0, ci)])
          spaces_wid[ci] = pi.wave_create()

        wave[i] = spaces_wid[ci]
      else: # Mark
        if ci not in marks_wid:
          wf = carrier(GPIO, FREQ, ci)
          pi.wave_add_generic(wf)
          marks_wid[ci] = pi.wave_create()

        wave[i] = marks_wid[ci]

    delay = emit_time - time.time()
    if delay > 0.0:
      time.sleep(delay)
    pi.wave_chain(wave)

    while pi.wave_tx_busy():
      time.sleep(0.002)

    emit_time = time.time() + GAP_S

    for i in marks_wid:
      pi.wave_delete(marks_wid[i])

    marks_wid = {}

    for i in spaces_wid:
      pi.wave_delete(spaces_wid[i])

    spaces_wid = {}
    
    return 0
  except:
    return 1