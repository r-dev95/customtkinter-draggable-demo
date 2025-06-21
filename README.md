<!--
    README
 -->

 <div align=center>
  <img
    src='docs/image/demo.gif'
    alt='App Screen.'
    width=300
  />
</div>

# Customtkinter Draggable Demo

[![English](https://img.shields.io/badge/English-018EF5.svg?labelColor=d3d3d3&logo=readme)](./README.md)
[![Japanese](https://img.shields.io/badge/Japanese-018EF5.svg?labelColor=d3d3d3&logo=readme)](./README_JA.md)
[![license](https://img.shields.io/github/license/r-dev95/customtkinter-draggable-demo)](./LICENSE)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

[![Python](https://img.shields.io/badge/Python-3776AB.svg?labelColor=d3d3d3&logo=python)](https://github.com/python)
[![Sphinx](https://img.shields.io/badge/Sphinx-000000.svg?labelColor=d3d3d3&logo=sphinx&logoColor=000000)](https://github.com/sphinx-doc/sphinx)
[![Pytest](https://img.shields.io/badge/Pytest-0A9EDC.svg?labelColor=d3d3d3&logo=pytest)](https://github.com/pytest-dev/pytest)
[![Pydantic](https://img.shields.io/badge/Pydantic-ff0055.svg?labelColor=d3d3d3&logo=pydantic&logoColor=ff0055)](https://github.com/pydantic/pydantic)

This is a demo of drag-and-drop widget reorder using [CustomTkinter][customtkinter](Tkinter).

[customtkinter]: https://github.com/TomSchimansky/CustomTkinter

If you comment out the following in the `DraggableCard` class, the dragged widget will be swapped with the widget at the dropped location.

```python
self.bind_all_children(
    widget=self,
    sequence='<B1-Motion>',
    command=self.on_drag,
)
```

Also, the `EventBus` class can execute functions according to event names, reducing the dependency between classes.

## :rocket:Getting started

### Install from github

```bash
git clone https://github.com/r-dev95/customtkinter-draggable-demo.git
```

### Build virtual environment

It is assumed that `uv` is installed.

If you don't have a Python development environment yet, click [here](https://github.com/r-dev95/env-python).

```bash
cd customtkinter-draggable-demo/
uv sync
```

### Run

```bash
source .venv/bin/activate
cd src
python app.py
```

## :bookmark_tabs:Structure

<div align=center>
  <img
    src='docs/image/classes.png'
    alt='classes.'
  />
</div>

## :key:License

This repository is licensed under the [MIT License](LICENSE).
