# Copyright (c) 2018 Stephen Bunn <stephen@bunn.io>
# ISC License <https://opensource.org/licenses/isc>

import os

if "{{ cookiecutter.initialize_git_repository }}".strip().lower() == "y":
    os.system("git init")

if "{{ cookiecutter.build_virtual_environment }}".strip().lower() == "y":
    os.system("pipenv install --dev")

if "{{ cookiecutter.initialize_pre_commit }}".strip().lower():
    os.system("pipenv run pre-commit install")
    