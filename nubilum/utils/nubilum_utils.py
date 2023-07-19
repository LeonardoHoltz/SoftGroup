#!/usr/bin/env python3

from typing import Tuple
import numpy as np
import torch
from torch import Tensor

import k3d

"""
Custom Colorscales
"""

# Plotly:

plotly_red_custom_colorscale = [
            [0, 'seashell'],        # Lightest color for smallest value (usually 0)
            [0.25, 'lightcoral'],   # Lighter color for small values
            [0.5, 'coral'],         # Intermediate color for intermediate values
            [0.75, 'sienna'],       # Darker color for high values
            [1, 'crimson']          # Darkest color for highest value
        ]

# K3D:
# These color scales structure describe a list with one or more of the following pattern:
# A number from the interval [0, 1], describing a part from the scale,
# followed by the rgb color value in that part of the scale

k3d_red_custom_colorscale = [0.0, 1.0, 0.63, 0.48]
k3d_red_custom_colorscale.extend([0.1666, 1.0, 0.63, 0.48])

k3d_red_custom_colorscale.extend([0.1667, 0.87, 0.50, 0.38])
k3d_red_custom_colorscale.extend([0.3333, 0.87, 0.50, 0.38])

k3d_red_custom_colorscale.extend([0.3334, 0.73, 0.38, 0.28])
k3d_red_custom_colorscale.extend([0.5, 0.73, 0.38, 0.28])

k3d_red_custom_colorscale.extend([0.5001, 0.61, 0.26, 0.19])
k3d_red_custom_colorscale.extend([0.6666, 0.61, 0.26, 0.19])

k3d_red_custom_colorscale.extend([0.6667, 0.48, 0.15, 0.10])
k3d_red_custom_colorscale.extend([0.8333, 0.48, 0.15, 0.10])

k3d_red_custom_colorscale.extend([0.8334, 0.36, 0.0, 0.0])
k3d_red_custom_colorscale.extend([1.0, 0.36, 0.0, 0.0])

def check_tensor_shapes(tensors):
    reference_shape = tensors[0].shape

    for tensor in tensors[1:]:
        if tensor.shape != reference_shape:
            return False

    return True

def create_baseline_point_cloud(input_coords: Tensor) -> Tuple[Tensor]:
    """
    Baseline based on a cubic uniform point distribution.
    The colors returned will be all black.
    The volume used uses the same min and max bounds of the coordinates.
    If we can't perfectly divide the number of points in the rectangular volume,
    we add the remaining points randomly trough the volume.

    Args:
        input_coords (Tensor): Coordinates of the input in a size (N, 3).
    
    Returns:
        tuple(Tensor): Tuple containing the coordinates of the baseline points coordinates and its colors.
    """
    
    # Retrieve the maximum and minimum bounds
    max_values, _ = torch.max(input_coords, dim=0)
    min_values, _ = torch.min(input_coords, dim=0)
    
    x_min, y_min, z_min = min_values.tolist()
    x_max, y_max, z_max = max_values.tolist()
    
    # Retrive the number of points in input
    n_points = input_coords.size()[0]
    
    # Define colors as 0
    baseline_colors = torch.zeros(n_points, 3, requires_grad=True)

    # Defining grids for the volume
    grid_size = int(round(n_points ** (1/3.0)))
    
    x_grid = np.linspace(x_min, x_max, grid_size)
    y_grid = np.linspace(y_min, y_max, grid_size)
    z_grid = np.linspace(z_min, z_max, grid_size)
    
    x_points, y_points, z_points = np.meshgrid(x_grid, y_grid, z_grid, indexing='ij')
    
    points_np = np.vstack((x_points.flatten(), y_points.flatten(), z_points.flatten())).T
    
    num_grid_points = points_np.shape[0]

    # Generate additional random points if necessary
    if num_grid_points < n_points:
        remaining_points = n_points - num_grid_points
        random_points = np.random.uniform(low=[x_min, y_min, z_min],
                                        high=[x_max, y_max, z_max],
                                        size=(remaining_points, 3))
        points_np = np.concatenate((points_np, random_points), axis=0)
    
    baseline_coords = torch.tensor(points_np, requires_grad=True)
    
    return (baseline_coords, baseline_colors)




def show_point_cloud(coords: Tensor, colors: Tensor, size: float = 0.1) -> None:
    """Plots the Point Cloud.

    Args:
        coords (Tensor): Coordinates of the points, in the shape (N, 3)
        colors (Tensor): Colors of the points, in the shape (N, 3). It assumes that the colors are in the RGB format with interval [0, 255]
        size (float, optional): Points size in the plot. Defaults to 0.1.
    """
    rgb = colors.cpu().detach().numpy().astype(np.uint32)
    colors_hex = (rgb[:,0]<<16) + (rgb[:,1]<<8) + (rgb[:,2])
    np_coords = coords.cpu().detach().numpy()

    plot = k3d.plot(grid_visible=False)
    plot += k3d.points(np_coords, colors_hex, point_size=size, shader="simple", name="Point Cloud")
    plot.display()
