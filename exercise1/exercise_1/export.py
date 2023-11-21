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
    with open(path, "w") as obj_file:
        # Write vertex data
        for vertex in vertices:
            formatted_vertex = "v " + " ".join("{:.6f}".format(coord) for coord in vertex)
            obj_file.write(formatted_vertex + "\n")

        # Write face data
        for face in faces:
            obj_file.write("f " + " ".join(map(str, [i + 1 for i in face])) + "\n")

    # ###############


def export_pointcloud_to_obj(path, pointcloud):
    """
    export pointcloud as OBJ
    :param path: output path for the OBJ file
    :param pointcloud: Nx3 points
    :return: None
    """
    with open(path, "w") as obj_file:
        # Write vertex data
        for vertex in pointcloud:
            formatted_vertex = "v " + " ".join("{:.6f}".format(coord) for coord in vertex)
            obj_file.write(formatted_vertex + "\n")

    # ###############

    # ###############
