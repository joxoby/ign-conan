# ign-conan
Conan recipes for Ignition Robotics libraries

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

- `grep -R "TODO:" recipes/`

- [ ] ign-cmake
- [x] ign-math
- [ ] ign-tools
- [ ] ign-msgs
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
