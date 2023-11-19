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
    dist_to_center = np.sqrt(np.square(x-x_0)+np.square(y-y_0)+np.square(z-z_0))
    signed_dist = dist_to_center - r
    return signed_dist
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
    a = np.sqrt(np.square(x-x_0)+np.square(z-z_0))-R
    signed_dist = np.sqrt(np.square(y-y_0)+np.square(a))-r
    return signed_dist
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
    proton_signed_dist = np.square(x-proton_center[0])+np.square(y-proton_center[1])+np.square(z-proton_center[2])
    proton_signed_dist = np.sqrt(proton_signed_dist)-proton_radius
    
    electron_signed_dist = np.square(x-electron_center[0])+np.square(y-electron_center[1])+np.square(z-electron_center[2])
    electron_signed_dist = np.sqrt(electron_signed_dist)-electron_radius
    
    a = np.sqrt(np.square(x-proton_center[0])+np.square(z-proton_center[2]))-orbit_radius
    orbit_signed_dist = np.sqrt(np.square(y-proton_center[1])+np.square(a))-orbit_thickness
    
    all_signed_dist = np.stack((proton_signed_dist,electron_signed_dist,orbit_signed_dist))
    signed_dist = np.amin(all_signed_dist, axis=0)
    return signed_dist
    # ###############
