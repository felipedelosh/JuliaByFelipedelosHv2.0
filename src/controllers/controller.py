"""
FelipedelosH


main controller
"""
import sys
import os
from os import scandir
# SERVICES
from src.services.MandelbrotJuliaGraphierByFelipedelosH import MandelbrotJuliaGraphierByFelipedelosH

# INFRAESTRUCTURE
from src.infraestructure.configManager import ConfigManager


class Controller:
    def __init__(self) -> None:
        print("Initializing Controller...")
        self.path = str(os.path.abspath(os.path.dirname(sys.argv[0])))
        self.config = ConfigManager()
        print(f"total Colors: {len(self.config._colors_arr)}")
        pass

    def getTextInFile(self, path):
        info = None
        try:
            f = open(path, 'r', encoding="utf-8")
            return f.read()
        except:
            return info


    def getAllFilesNamesByExt(self, path, ext):
        """
        Return all files names of data folder with the specified extension
        """
        try:
            filesNames = []
            for i in scandir(path):
                if i.is_file():
                    if ext in i.name:
                        filesNames.append(i.name)

            return filesNames
        except:
            return None

    def drawMandelbrot(self, canvas, definition, x_offset, y_offset, zoom_factor):
        if self.config._data.get("black_and_white_mode"):
            print("Drawing mandelbrot in black and white mode...")
            MandelbrotJuliaGraphierByFelipedelosH.drawMandelbrotJuliaBlackAndWhite(canvas, definition, x_offset, y_offset, zoom_factor, self.config)
        else:
            print("Drawing mandelbrot in color mode...")
            MandelbrotJuliaGraphierByFelipedelosH.drawMandelbrotJuliaFullColor(canvas, self.config._colors_arr, definition, x_offset, y_offset, zoom_factor, self.config)
