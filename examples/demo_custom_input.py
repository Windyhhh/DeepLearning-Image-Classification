#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
演示如何在交互式工具中输入自定义数据
"""

from src.interpolation import Interpolator3D
import numpy as np

def demo_custom_input():
    """演示自定义数据输入"""
    
    print("=" * 70)
    print("三维插值算法 - 自定义数据输入演示")
    print("=" * 70)
    
    # 示例 1：简单线性数据
    print("\n【示例 1】简单线性数据")
    print("-" * 70)
    
    x_data = np.array([0, 1, 2, 3, 4])
    y_data = np.array([0, 1, 2, 3, 4])
    z_data = np.array([1, 2, 3, 4, 5])
    t_data = np.array([10, 20, 30, 40, 50])
    
    print("输入的数据:")
    print(f"{'X':>8} {'Y':>8} {'Z':>10} {'T':>10}")
    print("-" * 40)
    for i in range(len(x_data)):
        print(f"{x_data[i]:8.1f} {y_data[i]:8.1f} {z_data[i]:10.1f} {t_data[i]:10.1f}")
    
    try:
        interp1 = Interpolator3D(x_data, y_data, z_data, t_data, grid_spacing=0.5)
        print("\n✓ 插值器创建成功！")
        
        # 显示网格信息
        info = interp1.get_grid_info()
        print(f"\n网格信息:")
        print(f"  X 范围: {info['x_range']}")
        print(f"  Y 范围: {info['y_range']}")
        print(f"  Z 范围: {info['z_range']}")
        print(f"  T 范围: {info['t_range']}")
        print(f"  总网格点数: {info['total_points']}")
        
        # 范围查询
        results = interp1.query_by_range(1.5, 3.5, 15, 35)
        print(f"\n范围查询 (1.5 < z < 3.5, 15 < t < 35):")
        print(f"  找到 {len(results)} 个点")
        
    except Exception as e:
        print(f"✗ 错误: {e}")
    
    # 示例 2：随机数据
    print("\n\n【示例 2】随机分布数据")
    print("-" * 70)
    
    np.random.seed(42)
    n = 8
    x_data = np.random.uniform(0, 5, n)
    y_data = np.random.uniform(0, 5, n)
    z_data = np.random.uniform(10, 50, n)
    t_data = np.random.uniform(100, 500, n)
    
    print("输入的数据:")
    print(f"{'X':>8} {'Y':>8} {'Z':>10} {'T':>10}")
    print("-" * 40)
    for i in range(n):
        print(f"{x_data[i]:8.2f} {y_data[i]:8.2f} {z_data[i]:10.2f} {t_data[i]:10.2f}")
    
    try:
        interp2 = Interpolator3D(x_data, y_data, z_data, t_data, grid_spacing=0.5)
        print("\n✓ 插值器创建成功！")
        
        # 单点查询
        result = interp2.query(2.5, 2.5)
        if result:
            print(f"\n单点查询 (2.5, 2.5):")
            print(f"  z = {result['z']:.4f}")
            print(f"  t = {result['t']:.4f}")
        
        # 范围查询
        results = interp2.query_by_range(20, 40, 200, 400)
        print(f"\n范围查询 (20 < z < 40, 200 < t < 400):")
        print(f"  找到 {len(results)} 个点")
        if len(results) > 0:
            print(f"  前 3 个点:")
            for r in results[:3]:
                print(f"    ({r['x']:.2f}, {r['y']:.2f}): z={r['z']:.2f}, t={r['t']:.2f}")
        
    except Exception as e:
        print(f"✗ 错误: {e}")
    
    # 示例 3：网格数据
    print("\n\n【示例 3】规则网格数据")
    print("-" * 70)
    
    x_data = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])
    y_data = np.array([0, 1, 2, 0, 1, 2, 0, 1, 2])
    z_data = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50])
    t_data = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500])
    
    print("输入的数据:")
    print(f"{'X':>8} {'Y':>8} {'Z':>10} {'T':>10}")
    print("-" * 40)
    for i in range(len(x_data)):
        print(f"{x_data[i]:8.1f} {y_data[i]:8.1f} {z_data[i]:10.1f} {t_data[i]:10.1f}")
    
    try:
        interp3 = Interpolator3D(x_data, y_data, z_data, t_data, grid_spacing=0.5)
        print("\n✓ 插值器创建成功！")
        
        # 显示网格信息
        info = interp3.get_grid_info()
        print(f"\n网格信息:")
        print(f"  X 范围: {info['x_range']}")
        print(f"  Y 范围: {info['y_range']}")
        print(f"  总网格点数: {info['total_points']}")
        
        # 范围查询
        results = interp3.query_by_range(20, 40, 200, 400)
        print(f"\n范围查询 (20 < z < 40, 200 < t < 400):")
        print(f"  找到 {len(results)} 个点")
        
    except Exception as e:
        print(f"✗ 错误: {e}")
    
    print("\n" + "=" * 70)
    print("演示完成！")
    print("=" * 70)
    print("\n提示：")
    print("  • 运行 'python interactive_query.py' 启动交互式工具")
    print("  • 选择选项 7 可以输入自己的数据")
    print("  • 查看 INPUT_CUSTOM_DATA.md 了解详细说明")
    print("\n祝你使用愉快！🎉")

if __name__ == "__main__":
    demo_custom_input()

