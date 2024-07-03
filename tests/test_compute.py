# Copyright © 2024 Daniele Tricoli <eriol@mornie.org>
# SPDX-License-Identifier: BSD-3-Clause


from urdf_mesh_inertia.mesh import compute_inertial_parameters


def test_inertia_sphere(sphere_mesh_path):
    """Compute center of mass and inertial parameters for a sphere.

    The sphere has radius 5m and mass 1 kg.
    """

    inertial_parameters = compute_inertial_parameters(sphere_mesh_path, 1)

    assert inertial_parameters.round(6).center_of_mass[0] == 0
    assert inertial_parameters.round(6).center_of_mass[1] == 0
    assert inertial_parameters.round(6).center_of_mass[2] == 0

    assert inertial_parameters.round(6).inertia_tensor[0][0] == 9.998421
    assert inertial_parameters.round(6).inertia_tensor[0][1] == 0
    assert inertial_parameters.round(6).inertia_tensor[0][2] == 0

    assert inertial_parameters.round(6).inertia_tensor[1][0] == 0
    assert inertial_parameters.round(6).inertia_tensor[1][1] == 9.998421
    assert inertial_parameters.round(6).inertia_tensor[1][2] == 0

    assert inertial_parameters.round(6).inertia_tensor[2][0] == 0
    assert inertial_parameters.round(6).inertia_tensor[2][1] == 0
    assert inertial_parameters.round(6).inertia_tensor[2][2] == 9.997895


def test_inertia_ellipsoid(ellipsoid_mesh_path):
    """Copute center of mass and inertial parameters for an ellipsoid.

    The ellipsoid has semiaxes a = 5m, b = 10m and c = 15m and mass 1 kg.
    """

    inertial_parameters = compute_inertial_parameters(ellipsoid_mesh_path, 1)

    assert inertial_parameters.round(6).center_of_mass[0] == 0
    assert inertial_parameters.round(6).center_of_mass[1] == 0
    assert inertial_parameters.round(6).center_of_mass[2] == 0

    # I_x = 1/5 * m * (b**2 + c**2) = 65
    assert inertial_parameters.round(6).inertia_tensor[0][0] == 65.001317
    assert inertial_parameters.round(6).inertia_tensor[0][1] == 0
    assert inertial_parameters.round(6).inertia_tensor[0][2] == 0

    # I_y = 1/5 * m * (a**2 + c**2) = 50
    assert inertial_parameters.round(6).inertia_tensor[1][0] == 0
    assert inertial_parameters.round(6).inertia_tensor[1][1] == 50.001317
    assert inertial_parameters.round(6).inertia_tensor[1][2] == 0

    # I_y = 1/5 * m * (a**2 + b**2) = 25
    assert inertial_parameters.round(6).inertia_tensor[2][0] == 0
    assert inertial_parameters.round(6).inertia_tensor[2][1] == 0
    assert inertial_parameters.round(6).inertia_tensor[2][2] == 24.997895
