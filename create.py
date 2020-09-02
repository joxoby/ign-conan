import os
from pathlib import Path

import yaml

root_dir = Path("recipes")

# get all subdirs (non-recursive)
packages_path = Path.glob(root_dir, "./*/")

# loop through all packages
for package_path in packages_path:

    # get the package config
    config_file = package_path / "config.yml"
    with open(config_file) as fh:
        config = yaml.load(fh)

    # loop through all the versions to build
    versions = config["versions"]
    for version in versions:
        os.environ["CONAN_PACKAGE_VERSION"] = version
        folder = versions[version]["folder"]
        path_to_folder = str(package_path / folder)
        os.system(f"conan create {path_to_folder} demo/testing")
