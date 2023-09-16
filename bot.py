import pywhatkit as what
from datetime import datetime
import time
seconds = time.time() + 60

date = datetime.fromtimestamp(seconds)
numero_manadar = input("ingresa el numero para el mensaje: ")
texto = input("ingresa el mensaje: ")
print("espera 60 segundos para el mensaje")

what.sendwhatmsg()
p1 = input("quieres poner una foto s/n")
if p1 == "s":
  p2 = input("pon la foto en la carpeta y escribe su nombre y extencion")
  what.sendwhat_image(numero_mandar,p2)
else:
  exit()
