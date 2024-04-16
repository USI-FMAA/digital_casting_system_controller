# **Digital Casting System Contoller**

![GitHub - License](https://img.shields.io/badge/License-MIT-blue.svg)
![Twincat version](https://img.shields.io/badge/TwinCAT-3.4-blue)

This repository is the submoudle of [Digital Casting System] for PLC controller and ABB robot.

The main package is [Digital Casting System](https://github.com/USI-FMAA/digital_casting_system.git)

## **Requirements**

- [Windows 10]() or [Debian 12]()
- [TwinCAT](https://www.beckhoff.com/en-en/products/automation/twincat/?pk_campaign=AdWords-AdWordsSearch-TwinCAT_EN&pk_\
kwd=twincat&gclid=Cj0KCQjw9ZGYBhCEARIsAEUXITW5dmPmQ2629HIuFY7wfbSR70pi5uY2lkYziNmfKYczm1_YsK4hhPsaApjyEALw_wcB)
- [ABB RobotStudio]()
- [Docker](26.0.0)



## **Package Information**

```mermaid
%%{ init: { 'flowchart': { 'curve': 'stepAfter' } } }%%
graph TD
    A[Digital Casting System] --> B[Digital Casting System Controller]
    B --> C[ABB Robot]
    B --> D[Beckhoff PLC]
```
#### Main control flow

```mermaid

%%{ init: { 'flowchart': { 'curve': 'stepBefore' } } }%%
graph TD
    A[Digital Casting System Controller]
    A --- B[Manual Operatation]
    A --- C[Laptop Operatation]
    A --- D[Robot Operatation]

    D --- E[Reset]
    D --- F[Set Config]
    D --- G[Set output data to Machines]
    D --- H[Get output data from Machines]

```

#### Machine flow

Inline Mixer
```mermaid
%%{ init: { 'flowchart': { 'curve': 'stepBefore' } } }%%
graph TD
    A[Inline Mixer]
    A --- F[Set Config]
    A --- G[Set output data to Machines]
    A --- H[Get output data from Machines]

    F --- B[Max Speed]
    G --- C[Set Run]
    G --- D[Enable]

    H --- E[is Run]
    H --- I[is Ready]
    H --- J[Status SpeedM1]
    H --- K[Status SpeedM2]
    H --- L[Torque_M1]
    H --- M[Torque_M2]
    H --- N[Temperature_Funnel_Outlet]
    H --- O[Pressure_Funnel_Inlet]
    H --- P[Temperature_M1]
    H --- Q[Temperature_M2]
```

Concrete Pump
```mermaid
%%{ init: { 'flowchart': { 'curve': 'stepBefore' } } }%%
graph TD
    A[Inline Mixer]
    A --- F[Set Config]
    A --- G[Set output data to Machines]
    A --- H[Get output data from Machines]

    F --- B[Max Speed]
    G --- C[Set Run]
    G --- D[Enable]

    H --- E[is Run]
    H --- I[is Ready]
    H --- J[Status SpeedM1]
    H --- K[Status SpeedM2]
    H --- L[Torque_M1]
    H --- M[Torque_M2]
    H --- N[Temperature_Funnel_Outlet]
    H --- O[Pressure_Funnel_Inlet]
    H --- P[Temperature_M1]
    H --- Q[Temperature_M2]
```








## **Usage**

## Credits
This package was created by [WeiTing Chen](https://github.com/WeiTing1991)
at [USI-FMAA](https://github.com/USI-FMAA) and [ETHZurich DFab](https://dfab.ch/).

## Acknowledgment
