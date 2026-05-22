"""
FelipedelosH
2026

Using Tkinter.Canvas and Maths Drawing to see a Mandelbrot set.
"""
from tkinter import Canvas
import time

class MandelbrotGraphierByFelipedelosH:
    @staticmethod
    def drawMandelbrot(canvas: Canvas, colors, definition, scaleX, scaleY, zoom):
        start_time = time.perf_counter()
        print("Drawing Mandelbrot...")
        print(f"Definition: {definition} | ScaleX: {scaleX} | ScaleY: {scaleY} | Zoom: {zoom}")
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
        
        end_time = time.perf_counter()
        seconds = end_time - start_time
        minutes = seconds / 60

        print(f"Time to calcute it in seconds: {seconds:.4f}")
        print(f"Time to calcute it in minutes: {minutes:.4f}")


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

        empty_regions = [
            (-1.90, 0.02),
            (-1.85, 0.04),
            (-1.80, 0.06),
            (-1.75, 0.08),
            (-1.70, 0.11),
            (-1.65, 0.14),
            (-1.60, 0.17),
            (-1.55, 0.21),
            (-1.50, 0.25),
            (-1.45, 0.30),
            (-1.40, 0.34),
            (-1.35, 0.39),
            (-1.30, 0.44),
            (-1.25, 0.49),
            (-1.20, 0.54),
            (-1.15, 0.59),
            (-1.10, 0.64),
            (-1.05, 0.69),
            (-1.00, 0.73),
            (-0.95, 0.77),
            (-0.90, 0.81),
            (-0.85, 0.85),
            (-0.80, 0.88),
            (-0.75, 0.91),
            (-0.70, 0.94),
            (-0.65, 0.97),
            (-0.60, 1.00),
            (-0.55, 1.03),
            (-0.50, 1.06),
            (-0.45, 1.09),
            (-0.40, 1.12),
            (-0.35, 1.15),
            (-0.30, 1.18),
            (-0.25, 1.21),
            (-0.20, 1.24),
        ]

        for limit_x, limit_y in empty_regions:
            if x < limit_x and abs(y) > limit_y:
                return True
