#!/usr/bin/env python3

from typing import Any, Callable, List
from captum._utils.typing import TargetType, TensorOrTupleOfTensorsGeneric
from torch import Tensor, stack
from captum.attr import Saliency

import nubilum.utils.nubilum_utils as nu

import numpy as np

import plotly.express as px
import k3d
from k3d.colormaps import matplotlib_color_maps

class NubilumSaliency(Saliency):
    """
    Saliency implementation dedicated to point cloud
    """
    def __init__(self, forward_func: Callable[..., Any]) -> None:
        super().__init__(forward_func)
    
    def attribute(self,
                  inputs: TensorOrTupleOfTensorsGeneric,
                  target: TargetType = None,
                  abs: bool = True,
                  additional_forward_args: Any = None
        ) -> TensorOrTupleOfTensorsGeneric:
        """
        Calls the attribute method from Captum Saliency.
        """
        return super().attribute(inputs, target, abs, additional_forward_args)
    
    def sum_point_attributes(self, attributes: TensorOrTupleOfTensorsGeneric, target_dim: int = -1) -> Tensor:
        """
        Performs an element-wise summation over the attributes, followed by a sum of the elements in the target
        dimension in the resulted tensor.
        
        It's useful to aggregate attribution for any kind of point features.
        
        TODO: Check with Pedro if this function can be generalized to any kind of feature (other than 3 numbers, otherwise,
        the element-wise sum will fail because of the 3rd assert). Also, if this type of funcion is useful for more
        attribution algorithms, it should be better if we can transfer this to the utils section.

        Args:
            attributes (TensorOrTupleOfTensorsGeneric): Tuple of tensors that describes each point attributes.
            The tensors must have the same shape.
            target_dim (int, optional): Target dimension where the last sum will occour. Defaults to -1, the last dimension.

        Returns:
            Tensor: Sum of all tensors element-wise and with the last dimension added.
        """
        
        assert isinstance(attributes, tuple), \
            "Parameter 'attributes' must be a tuple of tensors."    # TODO: Check if this is useless, since the type in the parameters probably already guarantees that 'attributes' is a tuple of tensors.
        
        assert len(attributes) > 0, \
            "'attributes' tuple must contain at least one tensor."
        
        assert nu.check_tensor_shapes(attributes), \
            "Attributes must have the same shape."
        
        assert len(attributes[0].shape) > 1, \
            "Attributes shapes must have at least two dimensions."
            
        return (stack(attributes).sum(dim=0)).sum(axis=target_dim)
    
    def show_poi(self, poi_index: int, coords: Tensor) -> None:
        """Shows the point cloud with the point of interest in evidence
        
        TODO: Check if this function can be moved to utils if there are more algorithms that need poi.

        Args:
            poi_index (int): Index of the point of interest
            coords (Tensor): Coordinates of each point. 
        """
        np_coords = coords.detach().cpu().numpy()
        num_points = np_coords.shape[0]
        colors = np.ones(num_points)
        colors[poi_index] = 0.0
        #colors_hex = (colors[:,0]<<16) + (colors[:,1]<<8) + (colors[:,2])
        
        fig = k3d.plot(grid_visible=False)
        
        fig += k3d.points(positions = np_coords,
                        shader = '3d',
                        color_map = matplotlib_color_maps.Coolwarm,
                        attribute = colors,
                        color_range = [0.0, 1.0],
                        point_sizes = [0.03 if color == 1.0 else 0.08 for color in colors],
                        name = "Point of interest")
        fig.display()
        
        
    
    def explain_plotly(self, attributes: Tensor, coords: Tensor) -> None:
        """
        Plots the point cloud with a color discretization over the attributes values

        Args:
            attributes (TensorOrTupleOfTensorsGeneric): Attributes for each point.
            coords (Tensor): Coordinates of each point.
        """
        
        np_coords = coords.detach().cpu().numpy()
        
        min_size = 1   # Min size of a point
        max_size = 5   # Max size of a point
        num_sizes = 5  # Number of discrete sizes

        np_attr = attributes.detach().cpu().numpy()
        normalized_attr = (np_attr - np.min(np_attr)) / (np.max(np_attr) - np.min(np_attr))
        size_indices = np.round(normalized_attr * (num_sizes - 1)).astype(int)
        sizes = np.linspace(min_size, max_size, num_sizes)
        
        fig = px.scatter_3d(x = np_coords[:,0], y = np_coords[:,1], z = np_coords[:,2],
                            size = [sizes[idx] for idx in size_indices],
                            color = np_attr,
                            opacity = 1.0,
                            color_continuous_scale = nu.plotly_red_custom_colorscale)
            
        fig.show()
        
            
    def explain_k3d(self, attributes: Tensor, coords: Tensor, attribute_name = None) -> None:
        """_summary_

        Args:
            attributes (TensorOrTupleOfTensorsGeneric): Attributes for each point.
            coords (Tensor): Coordinates of each point.
            attribute_name (str, optional): Name of the point data in the plot. Defaults to None.
        """
        
        if attribute_name == None:
            attribute_name = "Attributes"
        
        fig = k3d.plot(grid_visible=False)
        
        min_size = 0.02
        max_size = 0.1
        
        np_attr = attributes.detach().cpu().numpy()
        
        sizes = (np_attr - np.min(np_attr)) / (np.max(np_attr) - np.min(np_attr)) * (max_size - min_size) + min_size
        
        fig += k3d.points(positions = coords,
                        shader = 'flat',
                        color_map = nu.k3d_red_custom_colorscale,
                        attribute = np_attr,
                        color_range = [np.min(np_attr), np.max(np_attr)],
                        point_sizes = sizes,
                        name = attribute_name)
        fig.display()