"""
FelipedelosH
2026

This is my version to see a Mandelbrot set.
"""
from tkinter import *
from src.controllers.controller import *

class Software:
    def __init__(self) -> None:
        self.controller = Controller()
        self._w = self.controller.config._data.get("window_w")
        self._h = self.controller.config._data.get("window_h")
        self.screem = Tk()
        self.canvas = Canvas(self.screem)
        self.txtScale = Entry(self.canvas)
        self.lblBannerProgram = Label(self.canvas, text=self.controller.config._data.get("main_banner_text"))
        self.lblInsertScale = Label(self.canvas, text="Insert a # Scale:")
        self.btnCalcular = Button(self.canvas, text="Calculate >>", command=self.calculate)
        self.lblScaleX = Label(self.canvas, text="Scale X:")
        self.sliderX = Scale(self.canvas, from_=1, to=100, orient=HORIZONTAL)
        self.lblScaleY = Label(self.canvas, text="Scale Y:")
        self.sliderY = Scale(self.canvas, from_=1, to=100, orient=HORIZONTAL)
        self.lblZoom = Label(self.canvas, text="Zoom:")
        self.sliderZ = Scale(self.canvas, from_=1, to=100, orient=HORIZONTAL)
        self.lblFooterProgram = Label(self.canvas, text=self.controller.config._data.get("main_footer_text"))

        self.vizualizedAndRun()


    def vizualizedAndRun(self):
        self.screem.title(self.controller.config._data.get("title_app"))
        self.screem.geometry(f"{self._w}x{self._h}")
        self.canvas['width'] = self._w
        self.canvas['height'] = self._h
        self.canvas['bg'] = "snow"
        self.canvas.place(x=0, y=0)
        self.lblBannerProgram.place(x=self._w * 0.45, y=self._h * 0.01)
        # Controls
        self.lblInsertScale.place(x=20, y=20)
        self.txtScale.place(x=20, y=50)
        self.btnCalcular.place(x=200, y=50)
        self.lblScaleX.place(x=10, y=100)
        self.sliderX.place(x=10, y=120)
        self.lblScaleY.place(x=10, y=160)
        self.sliderY.place(x=10, y=180)
        self.lblZoom.place(x=10, y=220)
        self.sliderZ.place(x=10, y=240)
        # END Controls
        self.lblFooterProgram.place(x=200, y=450)
        self.screem.after(0, self._refreshWindow)
        self.screem.mainloop()

    def _refreshWindow(self):
        self.screem.after(60, self._refreshWindow)

    def calculate(self):
        pass

s = Software()
