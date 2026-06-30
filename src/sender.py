import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "turing-smart-screen-python"))

from library.lcd.lcd_comm import Orientation
from library.lcd.lcd_comm_rev_a import LcdCommRevA

from data import Layout
from layout import GetLayout

class Sender:
    def __init__(self, lcd_comm: LcdCommRevA):
        self.lcd: LcdCommRevA = LcdCommRevA(com_port="AUTO", display_width=320, display_height=480)
        self.layout: Layout = GetLayout()

        lcd_comm.Reset()
        lcd_comm.InitializeComm()  # Mandatory!
        lcd_comm.SetBrightness(level=25)  # Optional | Set brightness in % (⚠️ Turing / rev. A displays can get hot at high brightness!)
        lcd_comm.SetOrientation(orientation=Orientation.LANDSCAPE)  # PORTRAIT | LANDSCAPE | REVERSE_PORTRAIT | REVERSE_LANDSCAPE




    def set_thumbnail(self, path: str):
        self.lcd.DisplayBitmap(path, self.layout.thumb.x, self.layout.thumb.y, self.layout.thumb.w, self.layout.thumb.h)

    def set_title(self):
        self.lcd.DisplayText()

    def set_artist(self):
        self.lcd.DisplayText()

    def set_album(self):
        self.lcd.DisplayText()

    def set_progress(self):
        self.lcd.DisplayProgressBar()

    def set_background(self):
        return


    def refresh_all(self, path: str):
        self.set_thumbnail(path)
        self.set_title()
        self.set_artist()
        self.set_album()
        self.set_progress()
        return

    def refresh_progress():
        return
