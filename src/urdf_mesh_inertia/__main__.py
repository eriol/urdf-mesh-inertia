# Copyright © 2024 Daniele Tricoli <eriol@mornie.org>
# SPDX-License-Identifier: BSD-3-Clause

from pathlib import Path
from typing import Optional

import typer
from rich import print
from typing_extensions import Annotated

from .mesh import compute_inertial_parameters


def main(
    mesh_path: Annotated[Path, typer.Argument(help="Path of the mesh.")],
    mass: Annotated[float, typer.Argument(help="Mass of the mesh in kg.")],
    precision: Annotated[
        Optional[int], typer.Option(help="Rounding at specified decimal digit.")
    ] = None,
):
    """Compute inertial parameters for a mesh.

    Calculation is made using pymeshlab and the URDF inertial tag for links is
    returned.
    """
    parameters = compute_inertial_parameters(str(mesh_path), mass)

    if precision is not None:
        parameters = parameters.round(precision)

    print(parameters.to_xml())


typer.run(main)
