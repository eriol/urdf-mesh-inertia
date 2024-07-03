# Build urdf-mesh-inertia.
build:
    @poetry build

# Remove build artifacts.
[linux]
[macos]
clean:
    @rm -rf dist/

# poetry run ...
run +ARGS:
    @poetry run {{ARGS}}

# Run urdf-mesh-inertia tests.
test:
    @poetry run pytest -vv
