<div align="center">

# 🧠 DeepLearning-Image-Classification

### From theory to practice — CNN / ResNet image classification.

A complete deep-learning image classification system: principles, implementation and deployment, with custom-input support.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)

</div>

---

**DeepLearning-Image-Classification** is a complete image-classification system built on **CNN / ResNet** architectures with **transfer learning** — combining principles, implementation, custom-input inference and deployment guides, reaching **95%+ accuracy** on public datasets.

> [!NOTE]
> 中文项目：深度学习图像分类——CNN/ResNet + 迁移学习，从原理到工程部署，支持自定义输入。

---

## Features

- **CNN / ResNet** — modern architectures with transfer learning for high accuracy (95%+).
- **Custom input** — classify your own images (`examples/demo_custom_input.py`).
- **Visualization** — feature / result visualization (`examples/demo_visualization.py`).
- **Interactive query** — query the model interactively (`src/interactive_query.py`).
- **Deployment-ready** — Docker + API guidance in docs.

---

## Quickstart

```bash
git clone https://github.com/Windyhhh/DeepLearning-Image-Classification.git
cd DeepLearning-Image-Classification

pip install -r requirements.txt

# run the complete example
python examples/example_complete.py

# classify your own image
python examples/demo_custom_input.py
```

---

## Project Structure

```
DeepLearning-Image-Classification/
├── src/
│   ├── interactive_query.py
│   └── interpolation.py
├── examples/
│   ├── example_complete.py
│   ├── demo_custom_input.py
│   └── demo_visualization.py
├── tests/
└── docs/                   # quick start, usage, project summary
```

---

## License

MIT — free to use, modify and distribute.
