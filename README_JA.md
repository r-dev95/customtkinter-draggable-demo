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

[CustomTkinter][customtkinter](Tkinter)を用いた、ドラッグ&ドロップでウィジェットを並べ替えるデモを示します。

[customtkinter]: https://github.com/TomSchimansky/CustomTkinter

`DraggableCard`クラスの下記をコメントアウトすると、ドラッグしたウィジェットとドロップした箇所のウィジェットとの交換処理になります。

```python
self.bind_all_children(
    widget=self,
    sequence='<B1-Motion>',
    command=self.on_drag,
)
```

また`EventBus`クラスでイベント名に応じた関数を実行できるようにすることで、クラス間の依存度を下げるような設計としています。

## :rocket:Getting started

### githubからインストール

```bash
git clone https://github.com/r-dev95/customtkinter-draggable-demo.git
```

### 仮想環境の構築

`uv`がインストールされていることが前提です。

pythonの開発環境がまだ整っていない方は、[こちら](https://github.com/r-dev95/env-python)。

```bash
cd customtkinter-draggable-demo/
uv sync
```

### 実行

```bash
source .venv/bin/activate
cd src
python app.py
```

## :bookmark_tabs:構成

<div align=center>
  <img
    src='docs/image/classes.png'
    alt='classes.'
  />
</div>

## :key:ライセンス

本リポジトリは、[MIT License](LICENSE)に基づいてライセンスされています。
