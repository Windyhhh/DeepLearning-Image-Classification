# 🎯 三维插值算法系统 - 从这里开始

欢迎使用三维插值算法系统！本文档将帮助你快速了解和使用本项目。

## 📋 项目概述

这是一个完整的三维插值算法实现，支持：

✅ **三维插值** - 基于 x-y 平面的 z, t 值插值  
✅ **自动网格生成** - 间距 0.01 的规则网格  
✅ **单点查询** - 根据 x-y 查询 z, t  
✅ **范围查询** ⭐ - 查询满足 a<z<b 且 c<t<d 的所有点  
✅ **三维可视化** - 显示曲面和查询结果  
✅ **热力图** - 二维热力图展示分布  

## 🚀 5 分钟快速开始

### 1️⃣ 安装依赖
```bash
pip install numpy scipy matplotlib
```

### 2️⃣ 运行示例
```bash
python example_complete.py
```

### 3️⃣ 编写代码
```python
from interpolation import Interpolator3D
import numpy as np

# 准备数据
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 2, 3, 4])
z = np.array([1, 2, 3, 4, 5])
t = np.array([10, 20, 30, 40, 50])

# 创建插值器
interp = Interpolator3D(x, y, z, t)

# 范围查询（核心功能）
results = interp.query_by_range(2, 4, 20, 40)
print(f"找到 {len(results)} 个点")

# 可视化
interp.plot_3d(z_min=2, z_max=4, t_min=20, t_max=40)
```

## 📁 项目文件

| 文件 | 说明 | 用途 |
|------|------|------|
| **interpolation.py** | 核心算法 | 导入使用 |
| **example_complete.py** | 完整示例 | 学习使用 |
| **interactive_query.py** | 交互式工具 | 探索功能 |
| **test_interpolation.py** | 单元测试 | 验证功能 |
| **demo_visualization.py** | 可视化演示 | 查看效果 |

## 📚 文档导航

### 🔰 初学者
1. 阅读本文件（START_HERE.md）
2. 运行 `python example_complete.py`
3. 查看 QUICK_START.md

### 📖 详细学习
1. 阅读 USAGE_GUIDE.md（使用指南）
2. 阅读 README.md（详细文档）
3. 运行 `python interactive_query.py`

### 🔧 深入了解
1. 查看 PROJECT_SUMMARY.md（项目总结）
2. 查看 FILES_MANIFEST.md（文件清单）
3. 阅读源代码 interpolation.py

## 🎯 核心功能演示

### 范围查询（最重要的功能）

```python
# 查询满足条件的所有点：0.2 < z < 0.5 且 8.0 < t < 12.0
results = interpolator.query_by_range(
    z_min=0.2, z_max=0.5,
    t_min=8.0, t_max=12.0
)

# 结果是一个列表，每个元素包含 x, y, z, t
for r in results[:5]:
    print(f"({r['x']:.2f}, {r['y']:.2f}): z={r['z']:.4f}, t={r['t']:.4f}")
```

### 三维可视化

```python
# 显示满足条件的点的三维图形
interpolator.plot_3d(
    z_min=0.2, z_max=0.5,
    t_min=8.0, t_max=12.0
)
```

### 热力图

```python
# 显示 Z 值的热力图
interpolator.plot_2d_heatmap(value_type='z')

# 显示 T 值的热力图
interpolator.plot_2d_heatmap(value_type='t')
```

## 🎮 三种使用方式

### 方式 1：编程使用（推荐用于集成）
```bash
# 在你的 Python 脚本中导入和使用
from interpolation import Interpolator3D
```

### 方式 2：交互式工具（推荐用于探索）
```bash
python interactive_query.py
```

### 方式 3：运行示例（推荐用于学习）
```bash
python example_complete.py
```

## ✨ 主要特点

- 🎯 **完整实现** - 从数据到可视化的完整流程
- 🚀 **易于使用** - 简洁的 API 设计
- 📊 **强大功能** - 支持范围查询和三维可视化
- 📈 **高效性能** - 支持大规模数据集
- 📚 **详细文档** - 完善的文档和示例
- 🧪 **充分测试** - 包含单元测试和演示

## 🔍 常见任务速查

| 任务 | 代码 |
|------|------|
| 创建插值器 | `Interpolator3D(x, y, z, t)` |
| 单点查询 | `interp.query(5.0, 5.0)` |
| 范围查询 | `interp.query_by_range(z_min, z_max, t_min, t_max)` |
| 批量查询 | `interp.batch_query(x_list, y_list)` |
| 三维图形 | `interp.plot_3d()` |
| 热力图 | `interp.plot_2d_heatmap()` |
| 网格信息 | `interp.get_grid_info()` |

## 💡 提示

- 📌 **最重要的功能**：范围查询 `query_by_range()`
- 📌 **最常用的可视化**：三维图形 `plot_3d()`
- 📌 **快速验证**：运行 `example_complete.py`
- 📌 **交互式探索**：运行 `interactive_query.py`

## ❓ 常见问题

**Q: 如何开始使用？**
A: 运行 `python example_complete.py` 查看完整示例。

**Q: 如何进行范围查询？**
A: 使用 `query_by_range(z_min, z_max, t_min, t_max)` 方法。

**Q: 如何显示三维图形？**
A: 使用 `plot_3d()` 方法，可选择性地指定范围条件。

**Q: 如何保存图形？**
A: 使用 `save_path` 参数，如 `plot_3d(save_path='output.png')`。

**Q: 需要多少个数据点？**
A: 至少 3 个点，建议 10+ 个点以获得更好的插值效果。

## 📞 获取帮助

1. 查看 USAGE_GUIDE.md（使用指南）
2. 查看 README.md（详细文档）
3. 查看 QUICK_START.md（快速开始）
4. 运行 `python interactive_query.py`（交互式工具）

## 🎓 学习路径

```
初级 → 中级 → 高级
  ↓      ↓      ↓
运行示例 → 交互式工具 → 编写脚本
```

## ✅ 下一步

- [ ] 运行 `python example_complete.py`
- [ ] 阅读 QUICK_START.md
- [ ] 尝试 `python interactive_query.py`
- [ ] 编写自己的脚本

---

**祝你使用愉快！** 🎉

有任何问题，请查看相关文档或运行示例代码。

