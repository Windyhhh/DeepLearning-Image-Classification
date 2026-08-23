# 快速开始指南

## 安装依赖

```bash
pip install numpy scipy matplotlib
```

## 基本使用

### 1. 导入和创建插值器

```python
import numpy as np
from interpolation import Interpolator3D

# 准备数据（x, y, z, t 四个数组）
x_data = np.array([...])
y_data = np.array([...])
z_data = np.array([...])
t_data = np.array([...])

# 创建插值器
interpolator = Interpolator3D(x_data, y_data, z_data, t_data, grid_spacing=0.01)
```

### 2. 单点查询

```python
# 查询点 (x=5.0, y=5.0) 的 z 和 t 值
result = interpolator.query(5.0, 5.0)

if result:
    print(f"Z = {result['z']}, T = {result['t']}")
```

### 3. 范围查询（核心功能）

```python
# 查询满足条件的所有点：0.2 < z < 0.5 且 8.0 < t < 12.0
results = interpolator.query_by_range(
    z_min=0.2, z_max=0.5,
    t_min=8.0, t_max=12.0
)

print(f"找到 {len(results)} 个点")

# 遍历结果
for result in results:
    print(f"({result['x']:.2f}, {result['y']:.2f}): "
          f"z={result['z']:.4f}, t={result['t']:.4f}")
```

### 4. 三维可视化

```python
# 显示所有数据的三维图形
interpolator.plot_3d()

# 显示满足条件的点的三维图形
interpolator.plot_3d(
    z_min=0.2, z_max=0.5,
    t_min=8.0, t_max=12.0
)
```

### 5. 热力图

```python
# Z 值热力图
interpolator.plot_2d_heatmap(value_type='z')

# T 值热力图
interpolator.plot_2d_heatmap(value_type='t')
```

## 完整示例

```python
import numpy as np
from interpolation import Interpolator3D

# 创建示例数据
np.random.seed(42)
n = 50
x = np.random.uniform(0, 10, n)
y = np.random.uniform(0, 10, n)
z = np.sin(x/5) * np.cos(y/5)
t = x + y

# 创建插值器
interp = Interpolator3D(x, y, z, t, grid_spacing=0.1)

# 范围查询
results = interp.query_by_range(0.2, 0.5, 8.0, 12.0)
print(f"找到 {len(results)} 个点")

# 显示前 5 个结果
for r in results[:5]:
    print(f"({r['x']:.2f}, {r['y']:.2f}): z={r['z']:.4f}, t={r['t']:.4f}")

# 可视化
interp.plot_3d(z_min=0.2, z_max=0.5, t_min=8.0, t_max=12.0)
```

## 交互式工具

运行交互式查询工具：

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

## 常用参数

### Interpolator3D 初始化参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| x_data | array | 必需 | X 坐标数组 |
| y_data | array | 必需 | Y 坐标数组 |
| z_data | array | 必需 | Z 值数组 |
| t_data | array | 必需 | T 值数组 |
| grid_spacing | float | 0.01 | 网格间距 |

### query_by_range 参数

| 参数 | 类型 | 说明 |
|------|------|------|
| z_min | float | Z 的最小值 |
| z_max | float | Z 的最大值 |
| t_min | float | T 的最小值 |
| t_max | float | T 的最大值 |

### plot_3d 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| z_min | float | None | Z 范围最小值（可选） |
| z_max | float | None | Z 范围最大值（可选） |
| t_min | float | None | T 范围最小值（可选） |
| t_max | float | None | T 范围最大值（可选） |
| title | str | "3D..." | 图形标题 |
| save_path | str | None | 保存路径（可选） |

## 返回值格式

### query() 返回值

```python
{
    'x': float,  # X 坐标
    'y': float,  # Y 坐标
    'z': float,  # Z 值
    't': float   # T 值
}
```

### query_by_range() 返回值

```python
[
    {'x': float, 'y': float, 'z': float, 't': float},
    {'x': float, 'y': float, 'z': float, 't': float},
    ...
]
```

## 性能提示

1. **网格间距**：
   - 间距小 → 精度高，但内存占用大
   - 间距大 → 内存占用小，但精度低
   - 推荐值：0.01 - 0.1

2. **数据点数**：
   - 至少需要 3 个点
   - 10+ 个点时使用 cubic 插值
   - 少于 10 个点时使用 linear 插值

3. **查询优化**：
   - 单点查询：O(1)
   - 范围查询：O(n)，n 为网格点数

## 故障排除

**问题：查询返回 None**
- 检查查询点是否在数据范围内
- 使用 `get_grid_info()` 查看范围

**问题：范围查询返回空列表**
- 检查范围条件是否过于严格
- 查看数据的实际 Z 和 T 范围

**问题：内存不足**
- 增加 `grid_spacing` 值
- 减少数据点数

## 更多信息

详见 `README.md` 文档。

