"""Export to disk"""


def export_mesh_to_obj(path, vertices, faces):
    """
    exports mesh as OBJ
    :param path: output path for the OBJ file
    :param vertices: Nx3 vertices
    :param faces: Mx3 faces
    :return: None
    """

    # write vertices starting with "v "
    # write faces starting with "f "

    # ###############
    mesh_file = open(path, 'w')
    for i in range(vertices.shape[0]):
        mesh_file.write("v {0} {1} {2}\n".format(vertices[i,0],vertices[i,1],vertices[i,2]))
    for j in range(faces.shape[0]):
        mesh_file.write("f {0} {1} {2}\n".format(faces[j,0]+1,faces[j,1]+1,faces[j,2]+1))
    mesh_file.close()
    print("done")
    return
    # ###############


def export_pointcloud_to_obj(path, pointcloud):
    """
    export pointcloud as OBJ
    :param path: output path for the OBJ file
    :param pointcloud: Nx3 points
    :return: None
    """

    # ###############
    point_cloud_file = open(path, 'w')
    for i in range(pointcloud.shape[0]):
        point_cloud_file.write("v {0} {1} {2}\n".format(pointcloud[i,0],pointcloud[i,1],pointcloud[i,2]))
    point_cloud_file.close()
    print("done")
    return
    # ###############
