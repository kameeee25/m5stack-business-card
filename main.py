from m5stack import lcd
from m5stack import buttonA
from m5stack import buttonC
import uos
import utime

imageList = ["/sd/image1.jpg", "/sd/image2.jpg",
             "/sd/image3.jpg", "/sd/image4.jpg"]
position = 0

uos.mountsd()

lcd.clear()
lcd.image(0, 0, file=imageList[0], scale=0, type=lcd.JPG)

while True:
    if buttonA.wasPressed():
        position = position + 1
        lcd.clear()
        lcd.image(0, 0, file=imageList[position %
                                       len(imageList)], scale=0, type=lcd.JPG)
    if buttonC.wasPressed():
        position = position - 1
        lcd.clear()
        lcd.image(0, 0, file=imageList[position %
                                       len(imageList)], scale=0, type=lcd.JPG)

    utime.sleep(0.1)
