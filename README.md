# Darwin
[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) [![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

Meta-heuristics optimization python module designed to support batch execution using local or clusterized backends with discretized variables, i.e. mappings to compilation flags, strings, or any kind of data that can be organized in a discrete set of values.

## Table of Contents
- [Install](#install)
- [Features](#features)
- [License](#license)

## Install
First you need to install the module's requirements
```bash 
$ pip install -r requirements.txt
```
> Note that `htcondor` module may be unavailable in some plataforms.

After all requirements are installed, you just need to enter the directory and execute
```bash
$ pip install .
```
or 
```bash
$ python3 setup.py install
```
## Features
Optimization algorithms supported in current version:
- Genetic Algorithm
- Particle Swarm Optimization
- Bat Algorithm

Execution backends implemented:
- HTCondor cluster execution

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
