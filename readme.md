<h1 align="center"> FelipedelosH </h1>
<br>
<h4>Julia By Loko V2.0</h4>

![Banner](Docs/banner.png)
<br>
:construction: IN CONSTRUCTION :construction:
<br><br>
A modern refactor of my first Mandelbrot and Julia Set renderer written in Python using Tkinter.

This project started years ago as an experimental mathematical visualization software and is now being rebuilt with a cleaner architecture, modular design, configurable rendering system, and scalable fractal engine.

## Preview

Julia by loko V2.0 renders the Mandelbrot Set using:
- Complex numbers
- Tkinter Canvas rendering
- Dynamic convergence coloring
- Mathematical plane mapping
- Manual optimization regions


## :hammer:Funtions:

- `Function 1`: Fractal geometry.<br>
- `Function 2`: Complex plane mathematics.<br>
- `Function 3`: Rendering optimization.<br>
- `Function 4`: Mathematical visualization.<br>
- `Function 5`: Python desktop applications.<br>


## Mathematical Plane Mapping

Transforms screen pixels into points inside the complex plane:
```
x = ((i / width) * plane_width) + min_x
y = ((j / height) * plane_height) + min_y
```

## Mathematical Theory

The Mandelbrot Set is generated using the recursive formula:
```
Z_n = (Z_{n-1} * Z_{n-1}) + C
```

Starting with:

```
Z_0 = 0
```

Z is a complex number
C is the point being evaluated in the complex plane

## Project Structure

```
Julia by loko V2.0/
│
├── main.py
├── config.json
├── README.md
├── requirements.txt
│
├── data/
│   └── colors.txt
│
├── Docs/
│   └── banner.png
│
└── src/
    ├── controllers/
    │   └── controller.py
    │
    ├── infraestructure/
    │   └── configManager.py
    │
    └── services/
        └── MandelbrotJuliaGraphierByFelipedelosH.py
```

## Configuration Table

| Key | Type | Description | Example |
|------|------|-------------|----------|
| `title_app` | string | Main application window title. | `"Mandelbrot:Julia v2.0.0"` |
| `env` | string | Environment name used for development or future deployment modes. | `"DEV"` |
| `black_and_white_mode` | boolean | Enables black and white rendering mode. If `false`, full color rendering is used. | `true` |
| `window_w` | integer | Width of the application window in pixels. | `1280` |
| `window_h` | integer | Height of the application window in pixels. | `720` |
| `background_color` | string | Background color of the canvas. | `"black"` |
| `paint_axis` | boolean | Enables mathematical X and Y axis rendering. | `true` |
| `internal_plain_size_x_pixels` | integer | Internal horizontal rendering resolution used for Mandelbrot calculations. | `400` |
| `internal_plain_size_y_pixels` | integer | Internal vertical rendering resolution used for Mandelbrot calculations. | `300` |
| `internal_pixel_size` | integer | Visual size of each rendered pixel block on the canvas. | `2` |
| `main_banner_text` | string | Text displayed at the top banner of the application. | `"Welcome to Mandelbrot viewer"` |
| `main_footer_text` | string | Text displayed at the bottom footer of the application. | `"FelipedelosH"` |


## :play_or_pause_button:How to execute a project

```
python main.py
```

## :hammer_and_wrench:Tech.

- Python
- tkinter
- Complex Numbers
- Mathematical Fractal Theory

## :warning:Warning.

- Fractal rendering is computationally expensive.
- Large definitions (iterations) may significantly increase processing time.

## Autor

| [<img src="https://avatars.githubusercontent.com/u/38327255?v=4" width=115><br><sub>Andrés Felipe Hernánez</sub>](https://github.com/felipedelosh)|
| :---: |
