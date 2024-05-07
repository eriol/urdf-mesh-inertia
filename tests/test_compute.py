# Copyright © 2024 Daniele Tricoli <eriol@mornie.org>
# SPDX-License-Identifier: BSD-3-Clause


from urdf_mesh_inertia.mesh import compute_inertial_parameters


def test_center_mass_sphere(sphere_mesh_path):
    """Compute center of mass for a sphere with radius 5m and mass 1 kg."""


def test_inertia_sphere(sphere_mesh_path):
    """Compute inertial parameters for a sphere with radius 5m and mass 1 kg."""

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
