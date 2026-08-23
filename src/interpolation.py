"""
三维插值算法模块
支持基于 x-y 平面的三维数据插值
"""

import numpy as np
from scipy.interpolate import griddata
from typing import Tuple, List, Dict, Optional
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Interpolator3D:
    """三维插值器类"""
    
    def __init__(self, x_data: np.ndarray, y_data: np.ndarray, 
                 z_data: np.ndarray, t_data: np.ndarray,
                 grid_spacing: float = 0.01):
        """
        初始化三维插值器
        
        Args:
            x_data: x 坐标数组
            y_data: y 坐标数组
            z_data: z 值数组
            t_data: t 值数组
            grid_spacing: 网格间距，默认 0.01
        """
        self.x_data = np.asarray(x_data, dtype=float)
        self.y_data = np.asarray(y_data, dtype=float)
        self.z_data = np.asarray(z_data, dtype=float)
        self.t_data = np.asarray(t_data, dtype=float)
        self.grid_spacing = grid_spacing
        
        # 验证数据长度一致
        n = len(self.x_data)
        assert len(self.y_data) == n, "y_data 长度必须与 x_data 一致"
        assert len(self.z_data) == n, "z_data 长度必须与 x_data 一致"
        assert len(self.t_data) == n, "t_data 长度必须与 x_data 一致"
        
        # 生成插值网格
        self._generate_grid()
        
        # 创建插值函数
        self._create_interpolators()
    
    def _generate_grid(self):
        """生成 x-y 平面的插值网格"""
        x_min, x_max = self.x_data.min(), self.x_data.max()
        y_min, y_max = self.y_data.min(), self.y_data.max()
        
        # 创建网格点
        x_grid = np.arange(x_min, x_max + self.grid_spacing, self.grid_spacing)
        y_grid = np.arange(y_min, y_max + self.grid_spacing, self.grid_spacing)
        
        self.x_grid, self.y_grid = np.meshgrid(x_grid, y_grid)
        self.grid_points = np.column_stack([self.x_grid.ravel(), self.y_grid.ravel()])
    
    def _create_interpolators(self):
        """创建 z 和 t 的插值函数"""
        points = np.column_stack([self.x_data, self.y_data])

        # 根据数据点数选择插值方法
        method = 'cubic' if len(self.x_data) >= 10 else 'linear'

        try:
            # 使用 griddata 进行插值
            self.z_interp = griddata(
                points, self.z_data, self.grid_points, method=method
            ).reshape(self.x_grid.shape)

            self.t_interp = griddata(
                points, self.t_data, self.grid_points, method=method
            ).reshape(self.x_grid.shape)
        except Exception as e:
            # 如果 cubic 失败，尝试 linear
            try:
                print(f"警告: {method} 插值失败，尝试 linear 方法")
                self.z_interp = griddata(
                    points, self.z_data, self.grid_points, method='linear'
                ).reshape(self.x_grid.shape)

                self.t_interp = griddata(
                    points, self.t_data, self.grid_points, method='linear'
                ).reshape(self.x_grid.shape)
            except Exception as e2:
                # 如果 linear 也失败，使用 nearest
                print(f"警告: linear 插值失败，使用 nearest 方法")
                self.z_interp = griddata(
                    points, self.z_data, self.grid_points, method='nearest'
                ).reshape(self.x_grid.shape)

                self.t_interp = griddata(
                    points, self.t_data, self.grid_points, method='nearest'
                ).reshape(self.x_grid.shape)
    
    def query(self, x: float, y: float) -> Optional[Dict[str, float]]:
        """
        根据 x-y 坐标查询 z 和 t 值

        Args:
            x: x 坐标
            y: y 坐标

        Returns:
            包含 z 和 t 值的字典，如果超出范围或无效返回 None
        """
        # 检查是否在网格范围内
        if not self._is_in_range(x, y):
            return None

        # 找到最近的网格点
        x_idx = np.argmin(np.abs(self.x_grid[0, :] - x))
        y_idx = np.argmin(np.abs(self.y_grid[:, 0] - y))

        z_val = float(self.z_interp[y_idx, x_idx])
        t_val = float(self.t_interp[y_idx, x_idx])

        # 检查是否为 NaN
        if np.isnan(z_val) or np.isnan(t_val):
            return None

        return {
            'x': x,
            'y': y,
            'z': z_val,
            't': t_val
        }
    
    def _is_in_range(self, x: float, y: float) -> bool:
        """检查坐标是否在网格范围内"""
        x_min, x_max = self.x_grid.min(), self.x_grid.max()
        y_min, y_max = self.y_grid.min(), self.y_grid.max()
        return x_min <= x <= x_max and y_min <= y <= y_max
    
    def batch_query(self, x_list: List[float], y_list: List[float]) -> List[Dict]:
        """
        批量查询多个 x-y 坐标
        
        Args:
            x_list: x 坐标列表
            y_list: y 坐标列表
            
        Returns:
            查询结果列表
        """
        results = []
        for x, y in zip(x_list, y_list):
            result = self.query(x, y)
            if result is not None:
                results.append(result)
        return results
    
    def get_grid_info(self) -> Dict:
        """获取网格信息"""
        return {
            'x_range': (float(self.x_grid.min()), float(self.x_grid.max())),
            'y_range': (float(self.y_grid.min()), float(self.y_grid.max())),
            'grid_spacing': self.grid_spacing,
            'grid_shape': self.x_grid.shape,
            'total_points': self.x_grid.size
        }

    def query_by_range(self, z_min: float, z_max: float,
                       t_min: float, t_max: float) -> List[Dict]:
        """
        根据 z 和 t 的范围查询对应的 x, y 坐标

        Args:
            z_min: z 的最小值
            z_max: z 的最大值
            t_min: t 的最小值
            t_max: t 的最大值

        Returns:
            满足条件的点列表，每个点包含 x, y, z, t 值
        """
        # 创建掩码：找出满足条件的网格点
        z_mask = (self.z_interp >= z_min) & (self.z_interp <= z_max)
        t_mask = (self.t_interp >= t_min) & (self.t_interp <= t_max)
        combined_mask = z_mask & t_mask

        # 获取满足条件的索引
        y_indices, x_indices = np.where(combined_mask)

        # 提取对应的坐标和值
        results = []
        for y_idx, x_idx in zip(y_indices, x_indices):
            result = {
                'x': float(self.x_grid[y_idx, x_idx]),
                'y': float(self.y_grid[y_idx, x_idx]),
                'z': float(self.z_interp[y_idx, x_idx]),
                't': float(self.t_interp[y_idx, x_idx])
            }
            results.append(result)

        return results

    def query_by_xy_range(self, x_min: float, x_max: float,
                          y_min: float, y_max: float) -> List[Dict]:
        """
        根据 x 和 y 的范围查询对应的 z 和 t 值

        Args:
            x_min: x 的最小值
            x_max: x 的最大值
            y_min: y 的最小值
            y_max: y 的最大值

        Returns:
            满足条件的点列表，每个点包含 x, y, z, t 值
        """
        # 创建掩码：找出满足条件的网格点
        x_mask = (self.x_grid >= x_min) & (self.x_grid <= x_max)
        y_mask = (self.y_grid >= y_min) & (self.y_grid <= y_max)
        combined_mask = x_mask & y_mask

        # 获取满足条件的索引
        y_indices, x_indices = np.where(combined_mask)

        # 提取对应的坐标和值
        results = []
        for y_idx, x_idx in zip(y_indices, x_indices):
            result = {
                'x': float(self.x_grid[y_idx, x_idx]),
                'y': float(self.y_grid[y_idx, x_idx]),
                'z': float(self.z_interp[y_idx, x_idx]),
                't': float(self.t_interp[y_idx, x_idx])
            }
            results.append(result)

        return results

    def plot_3d(self, z_min: Optional[float] = None, z_max: Optional[float] = None,
                t_min: Optional[float] = None, t_max: Optional[float] = None,
                title: str = "3D Interpolation Visualization",
                save_path: Optional[str] = None):
        """
        绘制三维图形，可选择性地显示满足条件的点

        Args:
            z_min: z 的最小值（可选）
            z_max: z 的最大值（可选）
            t_min: t 的最小值（可选）
            t_max: t 的最大值（可选）
            title: 图形标题
            save_path: 保存图形的路径（可选）
        """
        fig = plt.figure(figsize=(15, 5))

        # 绘制 z 曲面
        ax1 = fig.add_subplot(131, projection='3d')
        surf1 = ax1.plot_surface(self.x_grid, self.y_grid, self.z_interp,
                                 cmap='viridis', alpha=0.8)
        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.set_zlabel('Z')
        ax1.set_title('Z Surface')
        fig.colorbar(surf1, ax=ax1, shrink=0.5)

        # 绘制 t 曲面
        ax2 = fig.add_subplot(132, projection='3d')
        surf2 = ax2.plot_surface(self.x_grid, self.y_grid, self.t_interp,
                                 cmap='plasma', alpha=0.8)
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_zlabel('T')
        ax2.set_title('T Surface')
        fig.colorbar(surf2, ax=ax2, shrink=0.5)

        # 绘制满足条件的点（如果提供了条件）
        ax3 = fig.add_subplot(133, projection='3d')

        if z_min is not None and z_max is not None and t_min is not None and t_max is not None:
            # 获取满足条件的点
            results = self.query_by_range(z_min, z_max, t_min, t_max)

            if results:
                x_vals = [r['x'] for r in results]
                y_vals = [r['y'] for r in results]
                z_vals = [r['z'] for r in results]

                # 绘制满足条件的点
                ax3.scatter(x_vals, y_vals, z_vals, c='red', marker='o', s=20, alpha=0.6)
                ax3.set_xlabel('X')
                ax3.set_ylabel('Y')
                ax3.set_zlabel('Z')
                ax3.set_title(f'Points: {z_min}<Z<{z_max}, {t_min}<T<{t_max}')
                ax3.text2D(0.05, 0.95, f'Found {len(results)} points',
                          transform=ax3.transAxes, fontsize=10)
            else:
                ax3.text2D(0.5, 0.5, 'No points found',
                          transform=ax3.transAxes, fontsize=12, ha='center')
                ax3.set_title('Query Results')
        else:
            # 绘制原始数据点
            ax3.scatter(self.x_data, self.y_data, self.z_data,
                       c='red', marker='o', s=30, alpha=0.6)
            ax3.set_xlabel('X')
            ax3.set_ylabel('Y')
            ax3.set_zlabel('Z')
            ax3.set_title('Original Data Points')

        plt.suptitle(title, fontsize=14, fontweight='bold')
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            print(f"图形已保存到: {save_path}")

        plt.show()

    def plot_2d_heatmap(self, value_type: str = 'z',
                        save_path: Optional[str] = None):
        """
        绘制二维热力图

        Args:
            value_type: 'z' 或 't'，表示绘制哪个值的热力图
            save_path: 保存图形的路径（可选）
        """
        fig, ax = plt.subplots(figsize=(10, 8))

        if value_type.lower() == 'z':
            data = self.z_interp
            title = 'Z Value Heatmap'
            cmap = 'viridis'
        else:
            data = self.t_interp
            title = 'T Value Heatmap'
            cmap = 'plasma'

        im = ax.imshow(data, extent=[self.x_grid.min(), self.x_grid.max(),
                                      self.y_grid.min(), self.y_grid.max()],
                       origin='lower', cmap=cmap, aspect='auto')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title(title)

        # 添加原始数据点
        ax.scatter(self.x_data, self.y_data, c='red', marker='x', s=50, alpha=0.7)

        cbar = fig.colorbar(im, ax=ax)
        cbar.set_label(value_type.upper())

        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            print(f"热力图已保存到: {save_path}")

        plt.show()

