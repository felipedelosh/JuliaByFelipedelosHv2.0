"""
FelipedelosH
2026

Using Tkinter.Canvas and Maths Drawing to see a Mandelbrot set.
"""
from tkinter import Canvas
import math

class MandelbrotGraphierByFelipedelosH:
    @staticmethod
    def drawMandelbrot(canvas, scale, scaleX, scaleY, zoom):
        print("Drawing Mandelbrot...")
        print(f"Scale: {scale} | ScaleX: {scaleX} | ScaleY: {scaleY} | Zoom: {zoom}")
        canvas.delete("pixels")
