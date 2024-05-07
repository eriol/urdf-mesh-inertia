# Copyright © 2024 Daniele Tricoli <eriol@mornie.org>
# SPDX-License-Identifier: BSD-3-Clause

from pathlib import Path
from typing import Optional

import typer
from rich import print

from .mesh import compute_inertial_parameters


def main(mesh_path: Path, mass: float, precision: Optional[int] = None):
    """Compute inertial parameters for a mesh.

    Calculation is made using pymeshlab and the URDF inertial tag for links is
    returned.
    """
    parameters = compute_inertial_parameters(str(mesh_path), mass)

    if precision is not None:
        parameters = parameters.round(precision)

    print(parameters.to_xml())


typer.run(main)
