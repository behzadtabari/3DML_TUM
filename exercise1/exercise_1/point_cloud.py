"""Triangle Meshes to Point Clouds"""
import numpy as np


def sample_point_cloud(vertices, faces, n_points):
    """
    Sample n_points uniformly from the mesh represented by vertices and faces
    :param vertices: Nx3 numpy array of mesh vertices
    :param faces: Mx3 numpy array of mesh faces
    :param n_points: number of points to be sampled
    :return: sampled points, a numpy array of shape (n_points, 3)
    """

    # ###############
    vertex1 = vertices[faces[:, 0]]
    vertex2 = vertices[faces[:, 1]]
    vertex3 = vertices[faces[:, 2]]
    triangle_vertices = np.dstack([vertex1, vertex2, vertex3])
    
    triangle_cross_product = np.cross(triangle_vertices[:, 1, :] - triangle_vertices[:, 0, :],
                                      triangle_vertices[:, 2, :] - triangle_vertices[:, 0, :])
    triangle_surfaces = 0.5 * np.linalg.norm(triangle_cross_product, axis=1)
    
    triangle_probabilities = triangle_surfaces / triangle_surfaces.sum()
    
    triangles_for_all_points = np.random.choice(range(len(triangle_surfaces)), size=n_points, p=triangle_probabilities)
    vertices_for_all_points = triangle_vertices[triangles_for_all_points, :, :]
    
    r1 = np.random.rand(n_points, 1)
    r2 = np.random.rand(n_points, 1)
    u = 1 - np.sqrt(r1)
    v = np.sqrt(r1) * (1 - r2)
    w = np.sqrt(r1) * r2
    
    return (u * vertices_for_all_points[:, :, 0]) + (v * vertices_for_all_points[:, :, 1]) + (w * vertices_for_all_points[:, :, 2])
    # ###############
