import sys
import pkgutil
import importlib

assert(len(sys.argv) == 2)

target_package = importlib.import_module(sys.argv[1])
modules = [target_package]

for importer, modname, ispkg in pkgutil.walk_packages(path=target_package.__path__,
                                                      prefix=target_package.__name__+'.',
                                                      onerror=lambda x: None):
    modules.append(importlib.import_module(modname))

for module in modules:
    print(module.__doc__)