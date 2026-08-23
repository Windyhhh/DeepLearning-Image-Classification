"""
三维插值算法测试模块
"""

import numpy as np
from src.interpolation import Interpolator3D


def test_basic_interpolation():
    """测试基本插值功能"""
    print("=" * 60)
    print("测试 1: 基本插值功能")
    print("=" * 60)
    
    # 创建示例数据
    np.random.seed(42)
    n_points = 50
    
    x_data = np.random.uniform(0, 10, n_points)
    y_data = np.random.uniform(0, 10, n_points)
    z_data = np.sin(x_data / 5) * np.cos(y_data / 5) + np.random.normal(0, 0.1, n_points)
    t_data = x_data + y_data + np.random.normal(0, 0.1, n_points)
    
    # 创建插值器
    interpolator = Interpolator3D(x_data, y_data, z_data, t_data, grid_spacing=0.01)
    
    # 获取网格信息
    grid_info = interpolator.get_grid_info()
    print(f"\n网格信息:")
    print(f"  X 范围: {grid_info['x_range']}")
    print(f"  Y 范围: {grid_info['y_range']}")
    print(f"  网格间距: {grid_info['grid_spacing']}")
    print(f"  网格形状: {grid_info['grid_shape']}")
    print(f"  总网格点数: {grid_info['total_points']}")
    
    # 单点查询
    print(f"\n单点查询:")
    result = interpolator.query(5.0, 5.0)
    if result:
        print(f"  查询点 (x={result['x']}, y={result['y']})")
        print(f"  插值结果: z={result['z']:.4f}, t={result['t']:.4f}")
    
    # 批量查询
    print(f"\n批量查询 (5 个点):")
    x_query = [2.0, 4.0, 6.0, 8.0, 9.5]
    y_query = [2.0, 4.0, 6.0, 8.0, 9.5]
    results = interpolator.batch_query(x_query, y_query)
    
    for i, result in enumerate(results):
        print(f"  点 {i+1}: (x={result['x']:.2f}, y={result['y']:.2f}) "
              f"-> z={result['z']:.4f}, t={result['t']:.4f}")


def test_multiple_datasets():
    """测试多组数据集"""
    print("\n" + "=" * 60)
    print("测试 2: 多组数据集")
    print("=" * 60)
    
    # 创建多组数据
    datasets = []
    for dataset_id in range(3):
        np.random.seed(dataset_id)
        n_points = 30
        
        x_data = np.random.uniform(0, 5, n_points)
        y_data = np.random.uniform(0, 5, n_points)
        z_data = np.random.uniform(0, 100, n_points)
        t_data = np.random.uniform(0, 50, n_points)
        
        datasets.append({
            'id': dataset_id,
            'x': x_data,
            'y': y_data,
            'z': z_data,
            't': t_data
        })
    
    # 为每个数据集创建插值器
    print(f"\n创建了 {len(datasets)} 个插值器")
    interpolators = []
    
    for dataset in datasets:
        interp = Interpolator3D(
            dataset['x'], dataset['y'], 
            dataset['z'], dataset['t'],
            grid_spacing=0.01
        )
        interpolators.append(interp)
        grid_info = interp.get_grid_info()
        print(f"  数据集 {dataset['id']}: 网格点数 = {grid_info['total_points']}")
    
    # 查询示例
    print(f"\n查询示例 (x=2.5, y=2.5):")
    for i, interp in enumerate(interpolators):
        result = interp.query(2.5, 2.5)
        if result:
            print(f"  数据集 {i}: z={result['z']:.4f}, t={result['t']:.4f}")


def test_edge_cases():
    """测试边界情况"""
    print("\n" + "=" * 60)
    print("测试 3: 边界情况")
    print("=" * 60)
    
    # 创建简单数据
    x_data = np.array([0, 1, 2, 3, 4])
    y_data = np.array([0, 1, 2, 3, 4])
    z_data = np.array([1, 2, 3, 4, 5])
    t_data = np.array([10, 20, 30, 40, 50])
    
    interpolator = Interpolator3D(x_data, y_data, z_data, t_data, grid_spacing=0.5)
    
    # 测试范围内的查询
    print(f"\n范围内查询:")
    result = interpolator.query(2.0, 2.0)
    print(f"  (2.0, 2.0): {result}")
    
    # 测试范围外的查询
    print(f"\n范围外查询:")
    result = interpolator.query(10.0, 10.0)
    print(f"  (10.0, 10.0): {result}")


def test_range_query():
    """测试范围查询功能"""
    print("\n" + "=" * 60)
    print("测试 4: 范围查询功能")
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

    print(f"\nZ 范围: [{z_min:.4f}, {z_max:.4f}]")
    print(f"T 范围: [{t_min:.4f}, {t_max:.4f}]")

    # 查询条件：0.2 < z < 0.5, 8 < t < 12
    z_query_min, z_query_max = 0.2, 0.5
    t_query_min, t_query_max = 8.0, 12.0

    print(f"\n查询条件: {z_query_min} < Z < {z_query_max}, {t_query_min} < T < {t_query_max}")

    results = interpolator.query_by_range(z_query_min, z_query_max,
                                          t_query_min, t_query_max)

    print(f"\n找到 {len(results)} 个满足条件的点:")
    print(f"{'X':>8} {'Y':>8} {'Z':>10} {'T':>10}")
    print("-" * 40)

    for i, result in enumerate(results[:10]):  # 只显示前 10 个
        print(f"{result['x']:8.4f} {result['y']:8.4f} {result['z']:10.4f} {result['t']:10.4f}")

    if len(results) > 10:
        print(f"... 还有 {len(results) - 10} 个点")


if __name__ == "__main__":
    test_basic_interpolation()
    test_multiple_datasets()
    test_range_query()
    print("\n" + "=" * 60)
    print("所有测试完成！")
    print("=" * 60)

