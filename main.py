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
        self.canvas = Canvas(self.screem, highlightthickness=0, bd=0)
        self.txtScale = Entry(self.canvas)
        self.lblBannerProgram = Label(self.canvas, text=self.controller.config._data.get("main_banner_text"))
        self.lblInsertScale = Label(self.canvas, text="Insert a number of definition:")
        self.btnCalcular = Button(self.canvas, text="Calculate >>", command=self.calculate)
        self.lblScaleX = Label(self.canvas, text="Scale X:")
        self.sliderX = Scale(self.canvas, from_=1, to=1000, orient=HORIZONTAL)
        self.sliderX.set(500)
        self.lblScaleY = Label(self.canvas, text="Scale Y:")
        self.sliderY = Scale(self.canvas, from_=1, to=1000, orient=HORIZONTAL)
        self.sliderY.set(500)
        self.lblZoom = Label(self.canvas, text="Zoom:")
        self.sliderZ = Scale(self.canvas, from_=1, to=1000, orient=HORIZONTAL)
        self.sliderZ.set(500)
        self.lblFooterProgram = Label(self.canvas, text=self.controller.config._data.get("main_footer_text"))

        self.vizualizedAndRun()


    def vizualizedAndRun(self):
        self.screem.title(self.controller.config._data.get("title_app"))
        self.screem.geometry(f"{self._w}x{self._h}")
        self.canvas['width'] = self._w
        self.canvas['height'] = self._h
        self.canvas['bg'] = self.controller.config._data.get("background_color")
        self.canvas.place(x=0, y=0)
        self.lblBannerProgram.place(x=self._w * 0.45, y=self._h * 0.01)
        # Controls
        self.canvas.create_rectangle(self._w * 0.01, self._h * 0.05, self._w * 0.19, self._h * 0.45, fill="green")

        self.lblInsertScale.place(x=self._w * 0.02, y=self._h * 0.06)
        self.txtScale.place(x=self._w * 0.02, y=self._h * 0.1)
        self.btnCalcular.place(x=self._w * 0.12, y=self._h * 0.095)

        self.lblScaleX.place(x=self._w * 0.02, y=self._h * 0.15)
        self.sliderX.place(x=self._w * 0.02, y=self._h * 0.18)

        self.lblScaleY.place(x=self._w * 0.02, y=self._h * 0.25)
        self.sliderY.place(x=self._w * 0.02, y=self._h * 0.28)

        self.lblZoom.place(x=self._w * 0.02, y=self._h * 0.35)
        self.sliderZ.place(x=self._w * 0.02, y=self._h * 0.38)
        # END Controls
        self.lblFooterProgram.place(x=self._w * 0.5, y=self._h * 0.95)
        #self.screem.after(0, self._refreshWindow)
        self.screem.mainloop()

    def _refreshWindow(self):
        self.screem.after(60, self._refreshWindow)

    def validateDefinition(self):
        try:
            definition = int(self.txtScale.get())
            if definition < 1:
                return False
            return True
        except:
            return False

    def calculate(self):
        if self.validateDefinition():
            definition = int(self.txtScale.get())
            scale_x = self.sliderX.get()
            scale_y = self.sliderY.get()
            zoom = self.sliderZ.get()
            self.controller.drawMandelbrot(self.canvas, definition, scale_x, scale_y, zoom)

s = Software()
