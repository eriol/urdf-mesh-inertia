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
