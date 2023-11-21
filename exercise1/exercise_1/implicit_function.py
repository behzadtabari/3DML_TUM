"""Definitions for Signed Distance Fields"""
import numpy as np


def signed_distance_sphere(x, y, z, r, x_0, y_0, z_0):
    """
    Returns the signed distance value of a given point (x, y, z) from the surface of a sphere of radius r, centered at (x_0, y_0, z_0)
    :param x: x coordinate(s) of point(s) at which the SDF is evaluated
    :param y: y coordinate(s) of point(s) at which the SDF is evaluated
    :param z: z coordinate(s) of point(s) at which the SDF is evaluated
    :param r: radius of the sphere
    :param x_0: x coordinate of the center of the sphere
    :param y_0: y coordinate of the center of the sphere
    :param z_0: z coordinate of the center of the sphere
    :return: signed distance from the surface of the sphere
    """
    # ###############
    # raise errors for when radius is zero or lesser than zero
    if r <= 0:
        raise ValueError(" radius (r) must be greater than 0")

    # calculate signed distance
    signed_distance = np.sqrt((x - x_0) ** 2 + (y - y_0) ** 2 + (z - z_0) ** 2) - r

    return signed_distance
    # ###############


def signed_distance_torus(x, y, z, R, r, x_0, y_0, z_0):
    """
    Returns the signed distance value of a given point (x, y, z) from the surface of a torus of minor radius r and major radius R, centered at (x_0, y_0, z_0)
    :param x: x coordinate(s) of point(s) at which the SDF is evaluated
    :param y: y coordinate(s) of point(s) at which the SDF is evaluated
    :param z: z coordinate(s) of point(s) at which the SDF is evaluated
    :param R: major radius of the torus
    :param r: minor radius of the torus
    :param x_0: x coordinate of the center of the torus
    :param y_0: y coordinate of the center of the torus
    :param z_0: z coordinate of the center of the torus
    :return: signed distance from the surface of the torus
    """
    # ###############
    # raise errors for when radius is zero or lesser than zero
    if r <= 0:
        raise ValueError(" radius (r) must be greater than 0")
    # raise error when minor radius is greater than major radius
    if R - r <= 0:
        raise ValueError("Minor radius (r) must be less than the major radius (R).")

    signed_distance = np.sqrt( (np.sqrt((x-x_0)**2 + (z-z_0)**2 ) - R)**2+ (y-y_0)**2) - r

    # Use np.isclose to set very small values to zero
    signed_distance = np.where(np.isclose(signed_distance, 0), 0, signed_distance)
    return signed_distance
    # ###############


def signed_distance_atom(x, y, z):
    """
    Returns the signed distance value of a given point (x, y, z) from the surface of a hydrogen atom consisting of a spherical proton, a torus orbit, and one spherical electron
    :param x: x coordinate(s) of point(s) at which the SDF is evaluated
    :param y: y coordinate(s) of point(s) at which the SDF is evaluated
    :param z: z coordinate(s) of point(s) at which the SDF is evaluated
    :return: signed distance from the surface of the hydrogen atom
    """
    proton_center = (0, 0, 0)
    proton_radius = 0.1
    orbit_radius = 0.35  # The major radius of the orbit torus
    orbit_thickness = 0.01  # The minor radius of the orbit torus
    electron_center = (orbit_radius, 0, 0)
    electron_radius = 0.05
    # ###############


    # signed distance of proton assuming it is a sphere
    signed_distance_proton = signed_distance_sphere(x,y,z,proton_radius,proton_center[0],proton_center[1],proton_center[2])

    # signed distance of electron assuming it is a sphere
    signed_distance_electron = signed_distance_sphere(x,y,z,electron_radius,electron_center[0],electron_center[1],electron_center[2])

    # signed distance of orbit assuming it is a torus
    # Assuming the center of proton is the centre of orbit
    signed_distance_orbit = signed_distance_torus(x,y,z,orbit_radius,orbit_thickness,proton_center[0],proton_center[1],proton_center[2])

    # To calculate the SDF we should use the Union operation Union: min 𝑓𝑖(𝑥)
    signed_distance = np.minimum.reduce([signed_distance_proton, signed_distance_orbit, signed_distance_electron])

    return signed_distance
