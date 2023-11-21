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
    surface_areas = []
    for face in faces:
        vertex_one = vertices[face[0]]
        vertex_two = vertices[face[1]]
        vertex_three = vertices[face[2]]
        v1 = np.array([vertex_two[0]-vertex_one[0],vertex_two[1]-vertex_one[1],vertex_two[2]-vertex_one[2]])
        v2 = np.array([vertex_three[0]-vertex_one[0], vertex_three[1]-vertex_one[1],vertex_three[2]-vertex_one[2]])

        cross_product = np.cross(v1,v2)
        magnitude = np.linalg.norm(cross_product)

        surface_areas.append(magnitude*0.5)

    total_area = sum(surface_areas)
    normalized_areas = [area / total_area for area in surface_areas]
    selected_points = np.random.choice(len(surface_areas), size=n_points, p=normalized_areas)

    # bycentric formula , u = 1 - sqrt(r1) , v = sqrt(r1)*(1-r2) , w = sqrt(r1)*r2
    # P = u*A + v*B + w*C
    P  = []
    for i in range(len(faces)):

        face = faces[i]
        A = vertices[face[0]]
        B = vertices[face[1]]
        C = vertices[face[2]]

        num_of_points = selected_points[i]
        r1 = np.random.uniform(0,1,num_of_points)
        r2 = np.random.uniform(0,1,num_of_points)

        u = 1 - np.sqrt(r1)
        v = (np.sqrt(r1))*(1-r2)
        w = np.sqrt(r1)*r2
        for j in range(len(r1)):
            P.append(A*u[j]+B*v[j]+C*w[j])

    P = np.array(P)
    print(P)
    return P



    # ###############
