import pywhatkit as what
from datetime import datetime
import time
seconds = time.time() + 60

date = datetime.fromimestamp(seconds)
def send_message(numero, mensaje):
  seconds = time.time() + 60
  date = datetime.fromimestamp(seconds)
  what.sendwhatmsg(numero, mensaje, date.hour,date.minute)
def send_image(numero, imagen):
  seconds = time.time() + 60
  date = datetime.fromimestamp(seconds)
  what.sendwhats_image(numero,imagen)
  
