import os
import shutil

# Read Cookiecutter configuration.
package_name = "{{ cookiecutter.__package_name_snake_case }}"
with_typer_cli = int("{{ cookiecutter.with_typer_cli }}")
continuous_integration = "{{ cookiecutter.continuous_integration }}"
is_publishable_package = True

# Remove Typer if not selected.
if not with_typer_cli:
    os.remove(f"src/{package_name}/cli.py")
    os.remove("tests/test_cli.py")

# Remove the continuous integration provider that is not selected.
if continuous_integration != "GitHub":
    # TODO: remove continous_integration option entirely
    raise ValueError("Invalid configuration!")

# Remove unused GitHub Actions workflows.
if continuous_integration == "GitHub":
    if not is_publishable_package:
        os.remove(".github/workflows/publish.yml")
