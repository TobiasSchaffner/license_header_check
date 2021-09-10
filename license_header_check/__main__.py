"""License header checker.

Copyright (c) 2021 Mixed Mode GmbH
ALL RIGHTS RESERVED - Unauthorized copying of this file, via any medium is strictly prohibited.
"""
from types import ModuleType
import pkgutil
import importlib
import argparse


def load_modules(package_name: str) -> list[ModuleType]:
    package = importlib.import_module(package_name)
    modules = [package]
    for _, modname, __ in pkgutil.walk_packages(path=package.__path__,
                                                        prefix=package.__name__+'.',
                                                        onerror=lambda x: None):
        modules.append(importlib.import_module(modname))
    return modules


def check_modules_for_license(modules: list[ModuleType], license: str) -> None:
    for module in modules:
        assert module.__doc__, f"Module {module.__name__} has no or empty documentation string"
        assert license in module.__doc__, f"Module {module.__name__} does not have the correct copyright notice"


def check_licenses(license_file, package_name) -> None:
    """This tool checks all modules of a python package for license headers."""
    modules = load_modules(package_name)
    license = open(license_file, 'r').read()
    check_modules_for_license(modules, license)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("license_file")
    parser.add_argument("package_name")
    args = parser.parse_args()
    check_licenses(args.license_file, args.package_name)