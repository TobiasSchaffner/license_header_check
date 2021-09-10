# Python Template

A template for python projects.

## Rename the project

To rename the project to your needs rename the folder and change all occurrences of the old name: 
```bash
mv template_module my_module
sed -i 's/template_module/my_module/g' tox.ini tests/test_echo_cli.py setup.cfg  docs/conf.py docs/package_doc.rst
```

Check setup.cfg and docs/conf.py to change additional information like author and description.

## Installing development dependencies

```bash
pip install -r requirements-dev.in
```

## Running tests

To run all tests, linters and to build the documentation run:
```bash
tox -e ALL
```

See https://tox.readthedocs.io/en/latest/ for more information on tox.