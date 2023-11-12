import pywhatkit as what
from datetime import datetime
import time
seconds = time.time() + 60

date = datetime.fromtimestamp(seconds)
def send_message(numero: int, mensaje: str):
  seconds = time.time() + 60
  date = datetime.fromtimestamp(seconds)
  what.sendwhatmsg(numero, mensaje, date.hour,date.minute)
def send_image(numero: int, imagen: str):
  seconds = time.time() + 60
  date = datetime.fromtimestamp(seconds)
  what.sendwhats_image(numero,imagen)

l = input("quieres mandar mensaje: ")
if l == "si" or "s":
  i2 = int(input("a que numero: "))
  i3 = str(input("mensaje: "))
  send_message(numero=i2, mensaje=i3)
if l == "no" or "n":
  i1 = int(input("a que numero: "))
  i2 = str(input("dirrecion de imagen: "))
  send_image(numero=i1, imagen=i2)
