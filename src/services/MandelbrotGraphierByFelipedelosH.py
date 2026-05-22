"""
FelipedelosH
2026

Using Tkinter.Canvas and Maths Drawing to see a Mandelbrot set.
"""
from tkinter import Canvas
import math

class MandelbrotGraphierByFelipedelosH:
    @staticmethod
    def drawMandelbrot(canvas, colors, definition, scaleX, scaleY, zoom):
        print("Drawing Mandelbrot...")
        print(f"Definition: {definition} || ScaleX: {scaleX} | ScaleY: {scaleY} | Zoom: {zoom}")
        canvas.delete("pixels")
        for i in range(1, 420):
            for j in range(1, 230):
                x = ((i/420)*(3)) - 2 # [-2, 1]
                y = ((j/230)*(3.6)) - 2 # [-2, 1.6]

                #print(f"Calculating convergence for point ({x}, {y})...")
                if MandelbrotGraphierByFelipedelosH.excludePoint(x, y):
                    canvas.create_rectangle(3+(i*3), 3+(j*3), 6+(i*3), 6+(j*3), fill='gray6', tags='pixels')
                else:
                    if x < 0.5:
                        _levelOfConvergence = MandelbrotGraphierByFelipedelosH.levelOfConvergence(x, y, definition)
                        #print(f"Point ({x}, {y}) has convergence level: {_levelOfConvergence}")
                        color_index = int((_levelOfConvergence / definition) * (len(colors) - 1))
                        pixel_color = colors[color_index]
                        canvas.create_rectangle(3+(i*3), 3+(j*3), 6+(i*3), 6+(j*3), fill=pixel_color, tags='pixels') 


    @staticmethod
    def levelOfConvergence(x, y, definition):
        """
        FelipedelosH

        Return QTY of convergence levels in:
        Zo = 0
        Zn = (Zn-1*Zn-1) + C
        """
        Z = 0
        C = complex(x, y)

        convergence = []
        for _ in range(definition):
            Z = (Z*Z) + C

            if Z not in convergence:
                convergence.append(Z)
            
        return len(convergence)

    
    @staticmethod
    def excludePoint(x, y):
        """
        Mandelbrot DONT live in all PLANE...
        if point is divergence
        Mandelbrot is only X(-1.9, 0.5] Y[1, -1] for any ponits converge
        so many ponits divergen
        """
        if x<-1.9 or x > 0.5:
            return True

        if y < -1.3 or y > 1.3:
            return True

        if x < -1 and y > 0.6:
            return True

        if x < -1 and y < -0.6:
            return True

        if x < -1.5 and y > 0.05:
            return True

        if x < -1.5 and y < -0.05:
            return True

        if x < -0.3 and y > 0.7:
            return True

        if x < -0.3 and y < -0.7:
            return True

        if x > 0.2 and y > 0.7:
            return True

        if x > 0.2 and y < -0.7:
            return True
        
        return False