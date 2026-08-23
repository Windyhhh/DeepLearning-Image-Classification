"""
完整示例：展示三维插值算法的所有功能
"""

import numpy as np
from src.interpolation import Interpolator3D


def main():
    print("=" * 70)
    print("三维插值算法 - 完整示例")
    print("=" * 70)
    
    # ========== 第一步：创建数据 ==========
    print("\n[步骤 1] 创建示例数据")
    print("-" * 70)
    
    np.random.seed(42)
    n_points = 100
    
    # 生成随机的 x, y 坐标
    x_data = np.random.uniform(0, 10, n_points)
    y_data = np.random.uniform(0, 10, n_points)
    
    # 生成 z 和 t 值（基于 x, y 的函数）
    z_data = np.sin(x_data / 5) * np.cos(y_data / 5) + np.random.normal(0, 0.1, n_points)
    t_data = x_data + y_data + np.random.normal(0, 0.1, n_points)
    
    print(f"生成了 {n_points} 个数据点")
    print(f"  X 范围: [{x_data.min():.4f}, {x_data.max():.4f}]")
    print(f"  Y 范围: [{y_data.min():.4f}, {y_data.max():.4f}]")
    print(f"  Z 范围: [{z_data.min():.4f}, {z_data.max():.4f}]")
    print(f"  T 范围: [{t_data.min():.4f}, {t_data.max():.4f}]")
    
    # ========== 第二步：创建插值器 ==========
    print("\n[步骤 2] 创建三维插值器")
    print("-" * 70)
    
    interpolator = Interpolator3D(x_data, y_data, z_data, t_data, grid_spacing=0.1)
    print("插值器创建成功！")
    
    # 获取网格信息
    grid_info = interpolator.get_grid_info()
    print(f"  网格形状: {grid_info['grid_shape']}")
    print(f"  总网格点数: {grid_info['total_points']}")
    print(f"  网格间距: {grid_info['grid_spacing']}")
    
    # ========== 第三步：单点查询 ==========
    print("\n[步骤 3] 单点查询")
    print("-" * 70)
    
    test_points = [(2.5, 2.5), (5.0, 5.0), (7.5, 7.5)]
    
    for x, y in test_points:
        result = interpolator.query(x, y)
        if result:
            print(f"点 ({x:.1f}, {y:.1f}): z={result['z']:.4f}, t={result['t']:.4f}")
        else:
            print(f"点 ({x:.1f}, {y:.1f}): 超出范围")
    
    # ========== 第四步：批量查询 ==========
    print("\n[步骤 4] 批量查询")
    print("-" * 70)
    
    x_batch = [1.0, 3.0, 5.0, 7.0, 9.0]
    y_batch = [1.0, 3.0, 5.0, 7.0, 9.0]
    
    results = interpolator.batch_query(x_batch, y_batch)
    print(f"查询了 {len(x_batch)} 个点，有效结果 {len(results)} 个")
    print(f"{'X':>8} {'Y':>8} {'Z':>10} {'T':>10}")
    print("-" * 40)
    for r in results:
        print(f"{r['x']:8.4f} {r['y']:8.4f} {r['z']:10.4f} {r['t']:10.4f}")
    
    # ========== 第五步：范围查询 ==========
    print("\n[步骤 5] 范围查询（核心功能）")
    print("-" * 70)
    
    # 定义查询条件
    z_min, z_max = 0.2, 0.5
    t_min, t_max = 8.0, 12.0
    
    print(f"查询条件: {z_min} < Z < {z_max} 且 {t_min} < T < {t_max}")
    
    results = interpolator.query_by_range(z_min, z_max, t_min, t_max)
    
    print(f"\n找到 {len(results)} 个满足条件的点")
    
    if results:
        # 显示前 10 个结果
        print(f"\n前 10 个结果:")
        print(f"{'X':>8} {'Y':>8} {'Z':>10} {'T':>10}")
        print("-" * 40)
        for r in results[:10]:
            print(f"{r['x']:8.4f} {r['y']:8.4f} {r['z']:10.4f} {r['t']:10.4f}")
        
        if len(results) > 10:
            print(f"... 还有 {len(results) - 10} 个点")
        
        # 统计信息
        x_vals = [r['x'] for r in results]
        y_vals = [r['y'] for r in results]
        z_vals = [r['z'] for r in results]
        t_vals = [r['t'] for r in results]
        
        print(f"\n统计信息:")
        print(f"  X 范围: [{min(x_vals):.4f}, {max(x_vals):.4f}]")
        print(f"  Y 范围: [{min(y_vals):.4f}, {max(y_vals):.4f}]")
        print(f"  Z 范围: [{min(z_vals):.4f}, {max(z_vals):.4f}]")
        print(f"  T 范围: [{min(t_vals):.4f}, {max(t_vals):.4f}]")
    
    # ========== 第六步：多条件查询 ==========
    print("\n[步骤 6] 多条件范围查询")
    print("-" * 70)
    
    queries = [
        (0.0, 0.3, 5.0, 10.0, "低 Z，中等 T"),
        (-0.2, 0.0, 10.0, 15.0, "负 Z，高 T"),
        (0.3, 0.6, 15.0, 20.0, "高 Z，很高 T"),
    ]
    
    for z_min, z_max, t_min, t_max, desc in queries:
        results = interpolator.query_by_range(z_min, z_max, t_min, t_max)
        print(f"  {desc}: 找到 {len(results)} 个点")
    
    # ========== 第七步：可视化 ==========
    print("\n[步骤 7] 可视化")
    print("-" * 70)
    print("注意：以下代码会显示图形窗口")
    print("取消注释下面的代码来显示可视化结果")
    
    # 取消注释以下代码来显示图形
    # print("\n显示三维图形（所有数据）...")
    # interpolator.plot_3d(title="3D Interpolation - All Data")
    
    # print("\n显示三维图形（范围查询结果）...")
    # interpolator.plot_3d(z_min=0.2, z_max=0.5, t_min=8.0, t_max=12.0,
    #                     title="3D Interpolation - Range Query")
    
    # print("\n显示 Z 值热力图...")
    # interpolator.plot_2d_heatmap(value_type='z')
    
    # print("\n显示 T 值热力图...")
    # interpolator.plot_2d_heatmap(value_type='t')
    
    # ========== 完成 ==========
    print("\n" + "=" * 70)
    print("示例完成！")
    print("=" * 70)
    print("\n提示：")
    print("  - 查看 README.md 了解详细文档")
    print("  - 查看 QUICK_START.md 了解快速开始")
    print("  - 运行 python interactive_query.py 使用交互式工具")
    print("  - 运行 python test_interpolation.py 运行单元测试")


if __name__ == "__main__":
    main()

