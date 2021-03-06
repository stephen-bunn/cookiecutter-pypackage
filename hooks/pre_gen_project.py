# Copyright (c) 2018 Stephen Bunn <stephen@bunn.io>
# ISC License <https://opensource.org/licenses/isc>

import shutil

if not shutil.which("git"):
    raise EnvironmentError(f"this cookiecutter requires git")

if not shutil.which("pipenv"):
    raise EnvironmentError(f"this cookiecutter requires pipenv")

if not shutil.which("python3.7"):
    raise EnvironmentError(f"this cookiecutter requires that python3.7 can be found")
