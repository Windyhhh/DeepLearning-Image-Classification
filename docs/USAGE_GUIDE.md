# 三维插值算法 - 使用指南

## 🎯 核心功能概览

本项目实现了一个完整的三维插值系统，支持：

| 功能 | 说明 | 文件 |
|------|------|------|
| **三维插值** | 基于 x-y 平面的 z, t 值插值 | interpolation.py |
| **网格生成** | 自动生成间距 0.01 的规则网格 | interpolation.py |
| **单点查询** | 根据 x-y 查询对应的 z, t | interpolation.py |
| **范围查询** ⭐ | 查询满足 a<z<b 且 c<t<d 的所有点 | interpolation.py |
| **三维可视化** | 显示 z, t 曲面和查询结果 | interpolation.py |
| **热力图** | 二维热力图展示 z, t 分布 | interpolation.py |

## 📦 安装和准备

### 1. 安装依赖
```bash
pip install numpy scipy matplotlib
```

### 2. 验证安装
```bash
python example_complete.py
```

## 🚀 三种使用方式

### 方式 1：编程使用（推荐用于集成）

```python
from interpolation import Interpolator3D
import numpy as np

# 准备数据
x_data = np.array([...])
y_data = np.array([...])
z_data = np.array([...])
t_data = np.array([...])

# 创建插值器
interpolator = Interpolator3D(x_data, y_data, z_data, t_data)

# 范围查询（核心功能）
results = interpolator.query_by_range(
    z_min=0.2, z_max=0.5,
    t_min=8.0, t_max=12.0
)

# 显示结果
for r in results:
    print(f"({r['x']:.2f}, {r['y']:.2f}): z={r['z']:.4f}, t={r['t']:.4f}")

# 可视化
interpolator.plot_3d(z_min=0.2, z_max=0.5, t_min=8.0, t_max=12.0)
```

### 方式 2：交互式工具（推荐用于探索）

```bash
python interactive_query.py
```

菜单选项：
- 1: 显示数据范围
- 2: 单点查询
- 3: 范围查询
- 4: 显示三维图形
- 5: 显示热力图
- 6: 批量查询

### 方式 3：运行示例（推荐用于学习）

```bash
# 完整示例
python example_complete.py

# 单元测试
python test_interpolation.py

# 可视化演示
python demo_visualization.py
```

## 📊 常见任务

### 任务 1：创建插值器

```python
from interpolation import Interpolator3D

# 基本创建
interp = Interpolator3D(x, y, z, t)

# 自定义网格间距
interp = Interpolator3D(x, y, z, t, grid_spacing=0.05)
```

### 任务 2：单点查询

```python
# 查询单个点
result = interp.query(5.0, 5.0)

if result:
    print(f"Z={result['z']}, T={result['t']}")
else:
    print("点超出范围")
```

### 任务 3：范围查询（最重要）

```python
# 查询满足条件的所有点
results = interp.query_by_range(
    z_min=0.2, z_max=0.5,
    t_min=8.0, t_max=12.0
)

print(f"找到 {len(results)} 个点")

# 显示前 10 个
for r in results[:10]:
    print(f"({r['x']:.2f}, {r['y']:.2f}): "
          f"z={r['z']:.4f}, t={r['t']:.4f}")
```

### 任务 4：批量查询

```python
# 查询多个点
x_list = [1.0, 2.0, 3.0]
y_list = [1.0, 2.0, 3.0]

results = interp.batch_query(x_list, y_list)

for r in results:
    print(f"({r['x']:.2f}, {r['y']:.2f}): "
          f"z={r['z']:.4f}, t={r['t']:.4f}")
```

### 任务 5：三维可视化

```python
# 显示所有数据
interp.plot_3d()

# 显示满足条件的点
interp.plot_3d(
    z_min=0.2, z_max=0.5,
    t_min=8.0, t_max=12.0,
    title="Range Query Results"
)

# 保存为图片
interp.plot_3d(save_path='output.png')
```

### 任务 6：热力图

```python
# Z 值热力图
interp.plot_2d_heatmap(value_type='z')

# T 值热力图
interp.plot_2d_heatmap(value_type='t')

# 保存热力图
interp.plot_2d_heatmap(value_type='z', save_path='z_heatmap.png')
```

### 任务 7：获取网格信息

```python
info = interp.get_grid_info()

print(f"X 范围: {info['x_range']}")
print(f"Y 范围: {info['y_range']}")
print(f"网格点数: {info['total_points']}")
print(f"网格形状: {info['grid_shape']}")
```

## 🔍 查询结果说明

### 单点查询返回值

```python
{
    'x': 5.0,      # 查询的 X 坐标
    'y': 5.0,      # 查询的 Y 坐标
    'z': 0.4066,   # 插值得到的 Z 值
    't': 10.0634   # 插值得到的 T 值
}
```

### 范围查询返回值

```python
[
    {'x': 5.26, 'y': 4.07, 'z': 0.4967, 't': 9.2549},
    {'x': 5.36, 'y': 4.07, 'z': 0.4926, 't': 9.3880},
    ...
]
```

## ⚙️ 参数说明

### Interpolator3D 初始化参数

```python
Interpolator3D(
    x_data,           # 必需：X 坐标数组
    y_data,           # 必需：Y 坐标数组
    z_data,           # 必需：Z 值数组
    t_data,           # 必需：T 值数组
    grid_spacing=0.01 # 可选：网格间距（默认 0.01）
)
```

### query_by_range 参数

```python
query_by_range(
    z_min,  # 必需：Z 的最小值
    z_max,  # 必需：Z 的最大值
    t_min,  # 必需：T 的最小值
    t_max   # 必需：T 的最大值
)
```

### plot_3d 参数

```python
plot_3d(
    z_min=None,           # 可选：Z 范围最小值
    z_max=None,           # 可选：Z 范围最大值
    t_min=None,           # 可选：T 范围最小值
    t_max=None,           # 可选：T 范围最大值
    title="...",          # 可选：图形标题
    save_path=None        # 可选：保存路径
)
```

## 💡 最佳实践

### 1. 数据准备
```python
# ✓ 好的做法
x = np.array([1.0, 2.0, 3.0, ...])
y = np.array([1.0, 2.0, 3.0, ...])
z = np.array([...])
t = np.array([...])

# ✗ 避免
x = [1, 2, 3, ...]  # 应该使用 numpy 数组
```

### 2. 网格间距选择
```python
# 精度优先
interp = Interpolator3D(x, y, z, t, grid_spacing=0.01)

# 速度优先
interp = Interpolator3D(x, y, z, t, grid_spacing=0.1)

# 平衡
interp = Interpolator3D(x, y, z, t, grid_spacing=0.05)
```

### 3. 范围查询优化
```python
# 先检查数据范围
info = interp.get_grid_info()
z_min, z_max = info['z_range']  # 获取实际范围

# 设置合理的查询条件
results = interp.query_by_range(
    z_min=z_min * 0.2,
    z_max=z_max * 0.8,
    t_min=...,
    t_max=...
)
```

## 🐛 常见问题

**Q: 查询返回 None？**
A: 检查查询点是否在数据范围内。使用 `get_grid_info()` 查看范围。

**Q: 范围查询返回空列表？**
A: 查询条件可能过于严格。检查数据的实际 Z 和 T 范围。

**Q: 内存占用过大？**
A: 增加 `grid_spacing` 值（如 0.1 或 0.2）。

**Q: 插值精度不够？**
A: 减小 `grid_spacing` 值（如 0.005）。

## 📚 文档导航

- **快速开始**：QUICK_START.md
- **详细文档**：README.md
- **项目总结**：PROJECT_SUMMARY.md
- **文件清单**：FILES_MANIFEST.md
- **本文件**：USAGE_GUIDE.md

## ✅ 验证清单

- [ ] 已安装依赖（numpy, scipy, matplotlib）
- [ ] 已运行 example_complete.py
- [ ] 已理解范围查询功能
- [ ] 已尝试三维可视化
- [ ] 已查看交互式工具

## 🎓 学习路径

1. **初级**：运行 example_complete.py
2. **中级**：使用 interactive_query.py
3. **高级**：编写自己的脚本集成该库

祝你使用愉快！🎉

