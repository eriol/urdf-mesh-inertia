# Copyright © 2024 Daniele Tricoli <eriol@mornie.org>
# SPDX-License-Identifier: BSD-3-Clause


INERTIAL_TEMPLATE = """<inertial>
  <origin xyz="{{p.center_of_mass[0]}} {{p.center_of_mass[1]}} {{p.center_of_mass[2]}}"/>
  <mass value="{{p.mass}}"/>
  <inertia ixx="{{p.inertia_tensor[0][0]}}" ixy="{{p.inertia_tensor[0][1]}}" ixz="{{p.inertia_tensor[0][2]}}" iyy="{{p.inertia_tensor[1][1]}}" iyz="{{p.inertia_tensor[1][2]}}" izz="{{p.inertia_tensor[2][2]}}"/>
</inertial>
"""  # noqa: E501
