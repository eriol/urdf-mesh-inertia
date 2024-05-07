# Build freakble.
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

# Run freakble repl.
test:
    @poetry run pytest -vv
