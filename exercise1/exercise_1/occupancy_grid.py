"""SDF to Occupancy Grid"""
import numpy as np


def occupancy_grid(sdf_function, resolution):
    """
    Create an occupancy grid at the specified resolution given the implicit representation.
    :param sdf_function: A function that takes in a point (x, y, z) and returns the sdf at the given point.
    Points may be provides as vectors, i.e. x, y, z can be scalars or 1D numpy arrays, such that (x[0], y[0], z[0])
    is the first point, (x[1], y[1], z[1]) is the second point, and so on
    :param resolution: Resolution of the occupancy grid
    :return: An occupancy grid of specified resolution (i.e. an array of dim (resolution, resolution, resolution) with value 0 outside the shape and 1 inside.
    """

    # ###############
    x_coord = np.linspace(-0.5, 0.5, num=resolution)
    y_coord = np.linspace(-0.5, 0.5, num=resolution)
    z_coord = np.linspace(-0.5, 0.5, num=resolution)
    
    x, y, z = np.meshgrid(x_coord, y_coord, z_coord, indexing='ij')

    sdf_grid = sdf_function(x.flatten(), y.flatten(), z.flatten())
    sdf_grid = sdf_grid.reshape((resolution, resolution, resolution))
    
    occupancy_grid = np.where(sdf_grid < 0, 1, 0)
    
    return occupancy_grid
    # ###############
