import ctypes, os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import time, datetime
from apscheduler.schedulers.blocking import BlockingScheduler

# https://stackoverflow.com/a/41406282
# https://github.com/FinanceData/FinanceDataReader

    
def some_job():
    timestr = datetime.datetime.now().strftime("%I:%M%p\r\n %B %d, %Y")

    img = Image.open("starrynight.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Roboto.ttf", 50)
    draw.text((3200, 1720),timestr,(255,255,255),font=font) #rgb(255,255,255)
    img.save('sample-out.jpg')


    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, os.getcwd()+"/sample-out.jpg" , 0)
    print timestr

print Stock('CGNX').price
scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', seconds = 20)#minutes=1)
scheduler.start()