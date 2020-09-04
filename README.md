# ign-conan
Conan recipes for Ignition Robotics libraries

[![Build Status](https://travis-ci.com/joxoby/ign-conan.svg?branch=master)](https://travis-ci.com/joxoby/ign-conan)

## Build all

Set up virtual environment:
```
pip install pipenv
pipenv install --dev
```

Build:
```
pipenv run python create.py
```

## TODO

- `grep -Rn "TODO:" recipes/`

- [x] sdformat
- [x] urdfdom
- [x] urdf_headers
- [x] console_bridge
- [ ] ign-cmake
- [x] ign-math
- [x] ign-tools
- [x] ign-msgs
- [ ] ign-transport
- [ ] ign-rendering
- [ ] ign-bazel
- [ ] ign-fuel-tools
- [ ] ign-gui
- [ ] ign-sensors
- [ ] ign-common
- [ ] ign-launch
- [ ] ign-physics
- [ ] ign-gazebo
