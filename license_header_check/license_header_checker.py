from types import ModuleType
import click
import pkgutil
import importlib


def load_modules(package_name: str) -> list[ModuleType]:
    package = importlib.import_module(package_name)
    modules = [package]
    for _, modname, __ in pkgutil.walk_packages(path=package.__path__,
                                                        prefix=package.__name__+'.',
                                                        onerror=lambda x: None):
        modules.append(importlib.import_module(modname))
    return modules


def check_modules_for_license(modules: list[ModuleType]):
    for module in modules:
        print(module.__doc__)

@click.command()
@click.argument('license_file', type=click.File('r'))
@click.argument('package_name')
def check_licenses(license_file, package_name):
    """This tool checks all modules of a python package for license headers."""
    modules = load_modules(package_name)
    check_modules_for_license(modules)


if __name__ == "__main__":
    check_licenses()