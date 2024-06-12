import sys
from PIL import Image
from waveshare_epd import epd5in65f

epd = epd5in65f.EPD()
epd.init()
#Himage = Image.open(self.pp.config['gfx']['image_path']+'/front/'+self.current_folio['front'])
Himage=Image.open(sys.argv[1])
epd.display(epd.getbuffer(Himage))
epd.sleep()


