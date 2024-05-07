# Copyright © 2024 Daniele Tricoli <eriol@mornie.org>
# SPDX-License-Identifier: BSD-3-Clause

from dataclasses import dataclass

import numpy as np
import pymeshlab
from jinja2 import Template

from .xml import INERTIAL_TEMPLATE


@dataclass
class InertialParameters:
    """Keep track of inertial parameters."""

    center_of_mass: np.ndarray
    inertia_tensor: np.ndarray
    mass: float
    volume: float

    def to_xml(self):
        """Return inertial parameters as URDF XML snippet."""
        template = Template(INERTIAL_TEMPLATE)
        return template.render(p=self)

    def round(self, precision=8):
        center_of_mass = np.round(self.center_of_mass, decimals=precision)
        inertia_tensor = np.round(self.inertia_tensor, decimals=precision)
        mass = round(self.mass, precision)
        volume = round(self.volume, precision)
        return InertialParameters(center_of_mass, inertia_tensor, mass, volume)


def compute_inertial_parameters(mesh: str, mass: float) -> InertialParameters:
    """Compute inertial parameters for the specified mesh.

    If the mesh is not 'watertight' and so MeshLab is not able to calculate
    center of mass and the inertia tensor, we generate the convex hull and
    perform again the calculation.
    """

    mesh_set = pymeshlab.MeshSet()
    mesh_set.load_new_mesh(mesh)

    measures = mesh_set.get_geometric_measures()
    if not measures.keys() & {"center_of_mass", "inertia_tensor"}:
        mesh_set.generate_convex_hull()

    measures = mesh_set.get_geometric_measures()

    center_of_mass = measures["center_of_mass"]
    volume = measures["mesh_volume"]
    inertia_tensor = measures["inertia_tensor"] * mass / volume

    return InertialParameters(center_of_mass, inertia_tensor, mass, volume)
