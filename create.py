import os
import subprocess
from pathlib import Path

import yaml

root_dir = Path("recipes")

# Get all the packages to build. This list should be
# in topological order.
with open("build.txt") as fh:
    packages = fh.readlines()
packages = [x.strip() for x in packages]

# loop through all packages
for package in packages:
    # get the package config
    config_file = root_dir / package / "config.yml"
    with open(config_file) as fh:
        config = yaml.load(fh, Loader=yaml.FullLoader)

    # loop through all the versions to build
    versions = config["versions"]
    for version in versions:
        folder = versions[version]["folder"]
        path_to_folder = str(root_dir / package / folder)
        ret = subprocess.call(["conan", "create", path_to_folder, f"{package}/{version}@"])
        if ret is not 0:
            exit(1)
