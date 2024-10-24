# **Digital Casting System Contoller**

![GitHub - License](https://img.shields.io/badge/License-MIT-blue.svg)
![Twincat version](https://img.shields.io/badge/TwinCAT-3.4-blue)

This repository is the submoudle of [Digital Casting System] for PLC controller and ABB robot.

[Digital Casting System]: https://github.com/USI-FMAA/digital_casting_system.git

## Requirements

- [TwinCAT](https://www.beckhoff.com/en-en/products/automation/twincat/?pk_campaign=AdWords-AdWordsSearch-TwinCAT_EN&pk_kwd=twincat&gclid=Cj0KCQjw9ZGYBhCEARIsAEUXITW5dmPmQ2629HIuFY7wfbSR70pi5uY2lkYziNmfKYczm1_YsK4hhPsaApjyEALw_wcB)
- [ABB RobotStudio](https://new.abb.com/products/robotics/robotstudio)
- [Docker](https://www.docker.com/)
- [Anaconda](https://www.anaconda.com/)

## Package Information

* `machines`: the dosing pump driver data.
* `plc`: the TwinCAT project for the PLC controller.
* `robot`: the ABB robot 4600 package for RobotStudio.
* `script`: the example script for control pysical and virtual robot via ROS package (Compas_RRC warpper).

## Usage
### Connect with TwinCAT
Install TwinCAT 3.4 and open the project in `plc\A061_DCS_ConcreteController_v1` folder.
Detailed setup instructions can be found [here](./plc/readme_plc.md).

### Connect with ABB robot 4600

Virtual Controller(RobotStudio Simulation)

```bash
docker
# clean the stopped container
docker container prune

# compose up and connect with docker container
docker-compose -f .\robot\docker_compas_rrc\virtual_controller\docker-compose.yml up

# run the wellcome script
python .\script\welcome_dcs.py

```
Real controller (Pysical Robot)

```bash
docker
# clean the stopped container
docker container prune

# compose up and connect with docker container
docker-compose -f .\robot\docker_compas_rrc\real_controller\docker-compose.yml up

# run the wellcome script
python .\script\welcome_dcs.py

```

## Credits

This package was created by [WeiTing Chen](https://github.com/WeiTing1991) at [USI-FMAA](https://github.com/USI-FMAA) and [ETHZurich DFab](https://dfab.ch/).

## Acknowledgment
compas_rrc is a wrapper for the ROS-Industrial abb driver. The original package can be found
[here](https://github.com/compas-rrc)
