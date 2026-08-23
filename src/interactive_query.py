"""
交互式范围查询工具
"""

import numpy as np
from .interpolation import Interpolator3D


def create_sample_data():
    """创建示例数据"""
    np.random.seed(42)
    n_points = 100
    
    x_data = np.random.uniform(0, 10, n_points)
    y_data = np.random.uniform(0, 10, n_points)
    z_data = np.sin(x_data / 5) * np.cos(y_data / 5) + np.random.normal(0, 0.1, n_points)
    t_data = x_data + y_data + np.random.normal(0, 0.1, n_points)
    
    return x_data, y_data, z_data, t_data


def print_menu():
    """打印菜单"""
    print("\n" + "=" * 60)
    print("三维插值算法 - 交互式查询工具")
    print("=" * 60)
    print("1. 显示数据范围")
    print("2. 单点查询")
    print("3. Z-T 范围查询")
    print("4. X-Y 范围查询 ⭐ (按 X-Y 过滤 Z-T)")
    print("5. 显示三维图形")
    print("6. 显示热力图")
    print("7. 批量查询")
    print("8. 输入自己的数组数据 ⭐")
    print("0. 退出")
    print("=" * 60)


def show_data_range(interpolator):
    """显示数据范围"""
    grid_info = interpolator.get_grid_info()
    
    print("\n数据范围信息:")
    print(f"  X 范围: [{grid_info['x_range'][0]:.4f}, {grid_info['x_range'][1]:.4f}]")
    print(f"  Y 范围: [{grid_info['y_range'][0]:.4f}, {grid_info['y_range'][1]:.4f}]")
    print(f"  网格间距: {grid_info['grid_spacing']}")
    print(f"  网格形状: {grid_info['grid_shape']}")
    print(f"  总网格点数: {grid_info['total_points']}")
    
    # 计算 z 和 t 的范围
    z_min, z_max = interpolator.z_interp.min(), interpolator.z_interp.max()
    t_min, t_max = interpolator.t_interp.min(), interpolator.t_interp.max()
    
    print(f"\n插值结果范围:")
    print(f"  Z 范围: [{z_min:.4f}, {z_max:.4f}]")
    print(f"  T 范围: [{t_min:.4f}, {t_max:.4f}]")


def single_point_query(interpolator):
    """单点查询"""
    try:
        x = float(input("输入 X 坐标: "))
        y = float(input("输入 Y 坐标: "))
        
        result = interpolator.query(x, y)
        
        if result:
            print(f"\n查询结果:")
            print(f"  X: {result['x']:.4f}")
            print(f"  Y: {result['y']:.4f}")
            print(f"  Z: {result['z']:.4f}")
            print(f"  T: {result['t']:.4f}")
        else:
            print("查询点超出范围或无效！")
    except ValueError:
        print("输入错误！请输入数字。")


def range_query(interpolator):
    """范围查询"""
    try:
        z_min = float(input("输入 Z 最小值: "))
        z_max = float(input("输入 Z 最大值: "))
        t_min = float(input("输入 T 最小值: "))
        t_max = float(input("输入 T 最大值: "))

        results = interpolator.query_by_range(z_min, z_max, t_min, t_max)

        print(f"\n找到 {len(results)} 个满足条件的点")

        if results:
            print(f"\n前 10 个结果:")
            print(f"{'X':>8} {'Y':>8} {'Z':>10} {'T':>10}")
            print("-" * 40)

            for i, result in enumerate(results[:10]):
                print(f"{result['x']:8.4f} {result['y']:8.4f} "
                      f"{result['z']:10.4f} {result['t']:10.4f}")

            if len(results) > 10:
                print(f"... 还有 {len(results) - 10} 个点")

            # 显示统计信息
            x_vals = [r['x'] for r in results]
            y_vals = [r['y'] for r in results]
            z_vals = [r['z'] for r in results]
            t_vals = [r['t'] for r in results]

            print(f"\n统计信息:")
            print(f"  X 范围: [{min(x_vals):.4f}, {max(x_vals):.4f}]")
            print(f"  Y 范围: [{min(y_vals):.4f}, {max(y_vals):.4f}]")
            print(f"  Z 范围: [{min(z_vals):.4f}, {max(z_vals):.4f}]")
            print(f"  T 范围: [{min(t_vals):.4f}, {max(t_vals):.4f}]")
    except ValueError:
        print("输入错误！请输入数字。")


def xy_range_query(interpolator):
    """根据 X-Y 范围查询 Z-T 值"""
    try:
        x_min = float(input("输入 X 最小值: "))
        x_max = float(input("输入 X 最大值: "))
        y_min = float(input("输入 Y 最小值: "))
        y_max = float(input("输入 Y 最大值: "))

        results = interpolator.query_by_xy_range(x_min, x_max, y_min, y_max)

        print(f"\n找到 {len(results)} 个满足条件的点")

        if results:
            print(f"\n前 10 个结果:")
            print(f"{'X':>8} {'Y':>8} {'Z':>10} {'T':>10}")
            print("-" * 40)

            for i, result in enumerate(results[:10]):
                print(f"{result['x']:8.4f} {result['y']:8.4f} "
                      f"{result['z']:10.4f} {result['t']:10.4f}")

            if len(results) > 10:
                print(f"... 还有 {len(results) - 10} 个点")

            # 显示统计信息
            x_vals = [r['x'] for r in results]
            y_vals = [r['y'] for r in results]
            z_vals = [r['z'] for r in results]
            t_vals = [r['t'] for r in results]

            print(f"\n统计信息:")
            print(f"  X 范围: [{min(x_vals):.4f}, {max(x_vals):.4f}]")
            print(f"  Y 范围: [{min(y_vals):.4f}, {max(y_vals):.4f}]")
            print(f"  Z 范围: [{min(z_vals):.4f}, {max(z_vals):.4f}]")
            print(f"  T 范围: [{min(t_vals):.4f}, {max(t_vals):.4f}]")
    except ValueError:
        print("输入错误！请输入数字。")


def show_3d_plot(interpolator):
    """显示三维图形"""
    try:
        use_range = input("是否使用范围条件？(y/n): ").lower() == 'y'
        
        if use_range:
            z_min = float(input("输入 Z 最小值: "))
            z_max = float(input("输入 Z 最大值: "))
            t_min = float(input("输入 T 最小值: "))
            t_max = float(input("输入 T 最大值: "))
            
            interpolator.plot_3d(z_min=z_min, z_max=z_max, 
                               t_min=t_min, t_max=t_max,
                               title="3D Interpolation - Range Query")
        else:
            interpolator.plot_3d(title="3D Interpolation - All Data")
    except ValueError:
        print("输入错误！")


def show_heatmap(interpolator):
    """显示热力图"""
    try:
        value_type = input("选择热力图类型 (z/t): ").lower()
        
        if value_type in ['z', 't']:
            interpolator.plot_2d_heatmap(value_type=value_type)
        else:
            print("无效的选择！")
    except Exception as e:
        print(f"错误: {e}")


def batch_query(interpolator):
    """批量查询"""
    try:
        # 询问是否使用 X-Y 范围过滤
        use_xy_filter = input("是否按 X-Y 范围过滤？(y/n): ").lower() == 'y'

        if use_xy_filter:
            # 输入 X-Y 范围
            x_min = float(input("输入 X 最小值: "))
            x_max = float(input("输入 X 最大值: "))
            y_min = float(input("输入 Y 最小值: "))
            y_max = float(input("输入 Y 最大值: "))

            results = interpolator.query_by_xy_range(x_min, x_max, y_min, y_max)

            print(f"\n查询结果 ({len(results)} 个有效点):")
            print(f"{'X':>8} {'Y':>8} {'Z':>10} {'T':>10}")
            print("-" * 40)

            for result in results[:100]:  # 显示前 100 个
                print(f"{result['x']:8.4f} {result['y']:8.4f} "
                      f"{result['z']:10.4f} {result['t']:10.4f}")

            if len(results) > 100:
                print(f"... 还有 {len(results) - 100} 个点")
        else:
            # 原有的批量查询方式
            n = int(input("输入查询点数: "))
            x_list = []
            y_list = []

            for i in range(n):
                x = float(input(f"点 {i+1} 的 X 坐标: "))
                y = float(input(f"点 {i+1} 的 Y 坐标: "))
                x_list.append(x)
                y_list.append(y)

            results = interpolator.batch_query(x_list, y_list)

            print(f"\n查询结果 ({len(results)} 个有效点):")
            print(f"{'X':>8} {'Y':>8} {'Z':>10} {'T':>10}")
            print("-" * 40)

            for result in results:
                print(f"{result['x']:8.4f} {result['y']:8.4f} "
                      f"{result['z']:10.4f} {result['t']:10.4f}")
    except ValueError:
        print("输入错误！")


def input_custom_data():
    """输入自定义数据"""
    print("\n" + "=" * 60)
    print("输入自定义数据")
    print("=" * 60)

    try:
        # 输入数据点数
        n = int(input("\n输入数据点数: "))

        if n < 3:
            print("错误：至少需要 3 个数据点！")
            return None

        x_data = []
        y_data = []
        z_data = []
        t_data = []

        print(f"\n请输入 {n} 个数据点的 x, y, z, t 值:")
        print("(每个点输入一行，格式: x y z t，用空格分隔)")
        print("-" * 60)

        for i in range(n):
            while True:
                try:
                    line = input(f"点 {i+1}: ").strip()
                    if not line:
                        print("输入不能为空，请重新输入")
                        continue

                    values = line.split()
                    if len(values) != 4:
                        print(f"错误：需要输入 4 个值，你输入了 {len(values)} 个")
                        continue

                    x, y, z, t = map(float, values)
                    x_data.append(x)
                    y_data.append(y)
                    z_data.append(z)
                    t_data.append(t)
                    break
                except ValueError:
                    print("错误：请输入有效的数字")

        # 转换为 numpy 数组
        x_data = np.array(x_data)
        y_data = np.array(y_data)
        z_data = np.array(z_data)
        t_data = np.array(t_data)

        # 显示输入的数据
        print("\n" + "=" * 60)
        print("输入的数据:")
        print("=" * 60)
        print(f"{'X':>8} {'Y':>8} {'Z':>10} {'T':>10}")
        print("-" * 40)
        for i in range(n):
            print(f"{x_data[i]:8.4f} {y_data[i]:8.4f} {z_data[i]:10.4f} {t_data[i]:10.4f}")

        # 创建插值器
        print("\n创建插值器...")
        try:
            interpolator = Interpolator3D(x_data, y_data, z_data, t_data, grid_spacing=0.1)
            print("✓ 插值器创建成功！")
            return interpolator
        except Exception as e:
            print(f"✗ 创建插值器失败: {str(e)[:100]}")
            return None

    except ValueError:
        print("输入错误！请输入有效的数字。")
        return None
    except Exception as e:
        print(f"发生错误: {e}")
        return None


def main():
    """主函数"""
    print("初始化插值器...")

    # 创建示例数据
    x_data, y_data, z_data, t_data = create_sample_data()

    # 创建插值器
    interpolator = Interpolator3D(x_data, y_data, z_data, t_data, grid_spacing=0.1)

    print("✓ 插值器初始化完成！")
    print("提示：选择选项 7 可以输入自己的数据")

    while True:
        print_menu()
        choice = input("请选择操作 (0-8): ").strip()

        if choice == '0':
            print("退出程序。")
            break
        elif choice == '1':
            show_data_range(interpolator)
        elif choice == '2':
            single_point_query(interpolator)
        elif choice == '3':
            range_query(interpolator)
        elif choice == '4':
            xy_range_query(interpolator)
        elif choice == '5':
            show_3d_plot(interpolator)
        elif choice == '6':
            show_heatmap(interpolator)
        elif choice == '7':
            batch_query(interpolator)
        elif choice == '8':
            # 输入自定义数据
            new_interpolator = input_custom_data()
            if new_interpolator is not None:
                interpolator = new_interpolator
                print("\n✓ 已切换到新的插值器！")
            else:
                print("\n✗ 输入数据失败，继续使用原有数据")
        else:
            print("无效的选择！")


if __name__ == "__main__":
    main()

