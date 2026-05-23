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
