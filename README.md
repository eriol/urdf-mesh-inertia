# urdf-mesh-inertia

Compute inertial parameters for a mesh using pymeshlab and return the URDF
inertial tag for links.


## Installation

### Using pipx

The best way to install urdf-mesh-inertia is using [pipx](https://pypa.github.io/pipx/):
```console
$ pipx install urdf-mesh-inertia
```

### Using pip

*When using pip it's suggested to work inside a virtualenv.*

```console
$ python -m pip install urdf-mesh-inertia
```

### From source

urdf-mesh-inertia uses [Poetry](https://python-poetry.org) as dependency
management and packaging tool, you need to install it first.

Then:

1. Clone this repository.
2. From the root of the repository run:
   ```console
   $ poetry build
   ```
3. Install using pipx or pip (it's better to use pipx):
   ```console
   $ pipx install dist/urdf_mesh_inertia-0.1.0-py3-none-any.whl
   ```

## Usage

```console
 Usage: urdf-mesh-inertia [OPTIONS] MESH_PATH MASS

 Compute inertial parameters for a mesh.
 Calculation is made using pymeshlab and the URDF inertial tag for links is
 returned.

╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    mesh_path      PATH   Path of the mesh. [default: None] [required]      │
│ *    mass           FLOAT  Mass of the mesh in kg. [default: None]           │
│                            [required]                                        │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --precision        INTEGER  Rounding at specified decimal digit.             │
│                             [default: None]                                  │
│ --help                      Show this message and exit.                      │
╰──────────────────────────────────────────────────────────────────────────────╯
```

For example:

```console
$ urdf-mesh-inertia --precision 8 ~/devel/ros/darwin_description/meshes/head_coll.stl 0.158
```

Will give us:

```xml
<inertial>
  <origin xyz="0.0025258 -0.0244761 6.7e-07"/>
  <mass value="0.158"/>
  <inertia ixx="0.0001567" ixy="2.494e-05" ixz="-0.0" iyy="0.00016806" iyz="0.0" izz="0.00017144"/>
</inertial>
```

`--precision` round at the specified decimal position. If you don't want
rounding run the command without it.
