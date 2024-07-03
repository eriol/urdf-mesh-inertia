# Copyright © 2024 Daniele Tricoli <eriol@mornie.org>
# SPDX-License-Identifier: BSD-3-Clause

from pathlib import Path

import pytest


@pytest.fixture
def sphere_mesh_path(request):
    sphere_path = Path(request.config.rootpath) / "extras" / "sphere.stl"
    return str(sphere_path)


@pytest.fixture
def ellipsoid_mesh_path(request):
    ellipsoid_path = Path(request.config.rootpath) / "extras" / "ellipsoid.stl"
    return str(ellipsoid_path)
