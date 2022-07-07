import pywhatkit

from datetime import datetime 
import time

seconds = time.time() + 60
date = datetime.fromtimestamp(seconds)

pywhatkit.sendwhatmsg("+595#########", "Hola, Soy el bot", date.hour, date.minute)

time.sleep(15)

pywhatkit.sendwhats_image("+595##########", 'yo.jpg')
