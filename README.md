# 🖼️ Deep Learning Image Classification | 基于深度学习的图像分类系统

> **Complete deep learning image classification system from theory to practice. CNN architectures (LeNet, AlexNet, VGG, ResNet), transfer learning, data augmentation, training pipeline, and evaluation. PyTorch implementation.**
>
> 从理论到实战的完整深度学习图像分类系统。CNN 架构（LeNet、AlexNet、VGG、ResNet）、迁移学习、数据增强、训练流水线和评估。PyTorch 实现。

---

## 🌟 Features | 核心特性

- **Multiple Architectures** — LeNet, AlexNet, VGG16, ResNet18/50
- **Transfer Learning** — Pre-trained ImageNet models
- **Data Augmentation** — Random crop, flip, rotation, color jitter
- **Training Pipeline** — Complete train/val/test workflow
- **Evaluation** — Accuracy, confusion matrix, per-class metrics
- **Visualization** — Training curves, misclassification analysis
- **PyTorch** — Modern deep learning framework

---

## 🚀 Quick Start | 快速开始

```bash
pip install torch torchvision matplotlib numpy pandas

# Train from scratch
python train.py --model resnet18 --dataset cifar10 --epochs 50

# Transfer learning
python train.py --model resnet50 --pretrained --dataset custom --data_dir ./data

# Evaluate
python evaluate.py --model best_model.pth --dataset cifar10
```

---

## 📐 Models | 模型

| Model | Parameters | Input Size | Best For |
|-------|-----------|------------|----------|
| **LeNet** | 60K | 32x32 | MNIST, small datasets |
| **AlexNet** | 60M | 227x227 | Medium datasets |
| **VGG16** | 138M | 224x224 | High accuracy |
| **ResNet18** | 11M | 224x224 | Balanced speed/accuracy |
| **ResNet50** | 25M | 224x224 | Best accuracy |

---

## 📄 License | 许可证

MIT License.

[GitHub](https://github.com/Windyhhh/DeepLearning-Image-Classification)
