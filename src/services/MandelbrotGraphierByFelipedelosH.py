"""
FelipedelosH
2026

Using Tkinter.Canvas and Maths Drawing to see a Mandelbrot set.
"""
from tkinter import Canvas
import time

class MandelbrotGraphierByFelipedelosH:
    @staticmethod
    def drawMandelbrot(canvas: Canvas, colors, definition, scaleX, scaleY, zoom, config):
        start_time = time.perf_counter()

        print("Drawing Mandelbrot...")
        print(f"Definition: {definition} | ScaleX: {scaleX} | ScaleY: {scaleY} | Zoom: {zoom}")

        canvas.delete("pixels")

        plain_pixels_x = config._data.get("internal_plain_size_x_pixels")
        plain_pixels_y = config._data.get("internal_plain_size_y_pixels")
        pixel_size = config._data.get("internal_pixel_size")

        canvas_width = int(canvas["width"])
        canvas_height = int(canvas["height"])

        canvas_center_x = canvas_width / 2
        canvas_center_y = canvas_height / 2

        plain_center_x = plain_pixels_x / 2
        plain_center_y = plain_pixels_y / 2

        min_x = -2.0
        max_x = 1.0

        min_y = -1.3
        max_y = 1.3

        plain_width = max_x - min_x
        plain_height = max_y - min_y

        for i in range(1, plain_pixels_x):
            for j in range(1, plain_pixels_y):

                x = min_x + ((i / plain_pixels_x) * plain_width)
                y = min_y + ((j / plain_pixels_y) * plain_height)

                canvas_x1 = canvas_center_x + ((i - plain_center_x) * pixel_size)
                canvas_y1 = canvas_center_y + ((j - plain_center_y) * pixel_size)

                canvas_x2 = canvas_x1 + pixel_size
                canvas_y2 = canvas_y1 + pixel_size

                if config._data.get("paint_axis"):
                    tolerance_x = plain_width / plain_pixels_x
                    tolerance_y = plain_height / plain_pixels_y

                    is_y_axis = abs(x) <= tolerance_x / 2
                    is_x_axis = abs(y) <= tolerance_y / 2

                    if is_x_axis or is_y_axis:
                        axis_color = "white"

                        if is_x_axis and is_y_axis:
                            axis_color = "red"  # origen 0,0

                        canvas.create_rectangle(
                            canvas_x1,
                            canvas_y1,
                            canvas_x2,
                            canvas_y2,
                            fill=axis_color,
                            outline=axis_color,
                            tags="pixels"
                        )

                        continue

                if MandelbrotGraphierByFelipedelosH.excludePoint(x, y):
                    continue

                level = MandelbrotGraphierByFelipedelosH.levelOfConvergence(
                    x,
                    y,
                    definition
                )

                color_index = int((level / definition) * (len(colors) - 1))
                color_index = max(0, min(color_index, len(colors) - 1))

                pixel_color = colors[color_index]

                canvas.create_rectangle(
                    canvas_x1,
                    canvas_y1,
                    canvas_x2,
                    canvas_y2,
                    fill=pixel_color,
                    outline=pixel_color,
                    tags="pixels"
                )

        end_time = time.perf_counter()

        seconds = end_time - start_time
        minutes = seconds / 60

        print(f"Time to calculate it in seconds: {seconds:.4f}")
        print(f"Time to calculate it in minutes: {minutes:.4f}")


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

        convergence = set()
        for _ in range(definition):
            Z = (Z*Z) + C
            convergence.add(Z)
            
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
            
        return False
