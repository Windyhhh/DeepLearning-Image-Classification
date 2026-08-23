"""
三维插值算法可视化演示
"""

import numpy as np
from src.interpolation import Interpolator3D


def demo_basic_visualization():
    """演示基本的三维可视化"""
    print("=" * 60)
    print("演示 1: 基本三维可视化")
    print("=" * 60)
    
    # 创建示例数据
    np.random.seed(42)
    n_points = 50
    
    x_data = np.random.uniform(0, 10, n_points)
    y_data = np.random.uniform(0, 10, n_points)
    z_data = np.sin(x_data / 5) * np.cos(y_data / 5) + np.random.normal(0, 0.1, n_points)
    t_data = x_data + y_data + np.random.normal(0, 0.1, n_points)
    
    # 创建插值器
    interpolator = Interpolator3D(x_data, y_data, z_data, t_data, grid_spacing=0.1)
    
    # 绘制三维图形（不带条件）
    print("\n绘制三维曲面和原始数据点...")
    interpolator.plot_3d(title="3D Interpolation - All Data")


def demo_range_query_visualization():
    """演示范围查询的三维可视化"""
    print("\n" + "=" * 60)
    print("演示 2: 范围查询的三维可视化")
    print("=" * 60)
    
    # 创建示例数据
    np.random.seed(42)
    n_points = 50
    
    x_data = np.random.uniform(0, 10, n_points)
    y_data = np.random.uniform(0, 10, n_points)
    z_data = np.sin(x_data / 5) * np.cos(y_data / 5) + np.random.normal(0, 0.1, n_points)
    t_data = x_data + y_data + np.random.normal(0, 0.1, n_points)
    
    # 创建插值器
    interpolator = Interpolator3D(x_data, y_data, z_data, t_data, grid_spacing=0.1)
    
    # 获取 z 和 t 的范围
    z_min, z_max = z_data.min(), z_data.max()
    t_min, t_max = t_data.min(), t_data.max()
    
    # 设置查询条件
    z_query_min = z_min + (z_max - z_min) * 0.2
    z_query_max = z_min + (z_max - z_min) * 0.6
    t_query_min = t_min + (t_max - t_min) * 0.3
    t_query_max = t_min + (t_max - t_min) * 0.7
    
    print(f"\nZ 范围: [{z_min:.4f}, {z_max:.4f}]")
    print(f"T 范围: [{t_min:.4f}, {t_max:.4f}]")
    print(f"\n查询条件:")
    print(f"  {z_query_min:.4f} < Z < {z_query_max:.4f}")
    print(f"  {t_query_min:.4f} < T < {t_query_max:.4f}")
    
    # 查询并显示结果
    results = interpolator.query_by_range(z_query_min, z_query_max, 
                                          t_query_min, t_query_max)
    
    print(f"\n找到 {len(results)} 个满足条件的点")
    
    # 绘制三维图形（带条件）
    print("\n绘制满足条件的点...")
    interpolator.plot_3d(z_min=z_query_min, z_max=z_query_max,
                        t_min=t_query_min, t_max=t_query_max,
                        title="3D Interpolation - Range Query Results")


def demo_heatmap_visualization():
    """演示热力图可视化"""
    print("\n" + "=" * 60)
    print("演示 3: 热力图可视化")
    print("=" * 60)
    
    # 创建示例数据
    np.random.seed(42)
    n_points = 50
    
    x_data = np.random.uniform(0, 10, n_points)
    y_data = np.random.uniform(0, 10, n_points)
    z_data = np.sin(x_data / 5) * np.cos(y_data / 5) + np.random.normal(0, 0.1, n_points)
    t_data = x_data + y_data + np.random.normal(0, 0.1, n_points)
    
    # 创建插值器
    interpolator = Interpolator3D(x_data, y_data, z_data, t_data, grid_spacing=0.1)
    
    # 绘制 Z 值热力图
    print("\n绘制 Z 值热力图...")
    interpolator.plot_2d_heatmap(value_type='z')
    
    # 绘制 T 值热力图
    print("\n绘制 T 值热力图...")
    interpolator.plot_2d_heatmap(value_type='t')


def demo_detailed_query():
    """演示详细的范围查询"""
    print("\n" + "=" * 60)
    print("演示 4: 详细的范围查询")
    print("=" * 60)
    
    # 创建示例数据
    np.random.seed(123)
    n_points = 100
    
    x_data = np.random.uniform(0, 10, n_points)
    y_data = np.random.uniform(0, 10, n_points)
    z_data = np.sin(x_data / 5) * np.cos(y_data / 5) + np.random.normal(0, 0.1, n_points)
    t_data = x_data + y_data + np.random.normal(0, 0.1, n_points)
    
    # 创建插值器
    interpolator = Interpolator3D(x_data, y_data, z_data, t_data, grid_spacing=0.1)
    
    # 多个查询条件
    queries = [
        (0.0, 0.3, 5.0, 10.0),
        (-0.2, 0.0, 10.0, 15.0),
        (0.3, 0.6, 15.0, 20.0),
    ]
    
    for i, (z_min, z_max, t_min, t_max) in enumerate(queries, 1):
        print(f"\n查询 {i}: {z_min} < Z < {z_max}, {t_min} < T < {t_max}")
        results = interpolator.query_by_range(z_min, z_max, t_min, t_max)
        print(f"  找到 {len(results)} 个点")
        
        if results:
            # 显示统计信息
            x_vals = [r['x'] for r in results]
            y_vals = [r['y'] for r in results]
            z_vals = [r['z'] for r in results]
            t_vals = [r['t'] for r in results]
            
            print(f"  X 范围: [{min(x_vals):.4f}, {max(x_vals):.4f}]")
            print(f"  Y 范围: [{min(y_vals):.4f}, {max(y_vals):.4f}]")
            print(f"  Z 范围: [{min(z_vals):.4f}, {max(z_vals):.4f}]")
            print(f"  T 范围: [{min(t_vals):.4f}, {max(t_vals):.4f}]")


if __name__ == "__main__":
    # 注意：如果不想显示图形，可以注释掉 plot 相关的演示
    # demo_basic_visualization()
    # demo_range_query_visualization()
    # demo_heatmap_visualization()
    demo_detailed_query()
    
    print("\n" + "=" * 60)
    print("演示完成！")
    print("=" * 60)

