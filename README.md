
# 1D Transverse Field Ising Model (TFIM) Quantum Circuit Generator

This repository contains Python code for generating quantum circuits implementing the 1D Transverse Field Ising Model (TFIM) using Qiskit.

## Overview

The 1D TFIM is a model in quantum physics that describes interactions between spins (qubits) in a chain structure. This repository provides tools to construct quantum circuits representing the TFIM Hamiltonian using Qiskit, a quantum computing framework in Python.

## Features

- **Custom Gate Definitions**: Includes custom gates like the square root of the Y gate (`sqrt(Y)`) and its inverse (`sqrt(Y)^dag`).
- **Trotterization Implementation**: Utilizes Trotterization technique to approximate the evolution of TFIM Hamiltonian over time steps.
- **Visualization**: Generates visual representations of quantum circuits using Matplotlib.

## Installation

To use this project, ensure you have Python 3.x and install the required dependencies using pip:

```bash
pip install qiskit matplotlib numpy
from qiskit import QuantumCircuit as circuit
from qiskit import QuantumRegister
from qiskit.circuit.library import UnitaryGate, YGate
from matplotlib import pyplot as plt
from numpy import pi

# Define custom gates
SYGate = UnitaryGate(YGate().power(1/2), label=r"$\sqrt{Y}$")
SYdgGate = UnitaryGate(SYGate.inverse(), label=r"$\sqrt{Y}^\dag$")

def generate1dTfimCircuit(qubits, num_steps, rx_angle):
    qubit = QuantumRegister(qubits)
    qc = circuit(qubit)
    for steps in range(num_steps):
        add1dTfimTrotterLayer(qc, rx_angle)
    return qc

def add1dTfimTrotterLayer(qc, rx_angle):
    for i in range(0, qc.num_qubits - 1, 2):
        qc.sdg([i, i+1])
        qc.append(SYGate, [i+1])
        qc.cx(i, i+1)
        qc.append(SYdgGate, [i+1])
    
    for i in range(1, qc.num_qubits - 1, 2):
        qc.sdg([i, i+1])
        qc.append(SYGate, [i+1])
        qc.cx(i, i+1)
        qc.append(SYdgGate, [i+1])
    
    qc.rx(rx_angle, list(range(qc.num_qubits)))

# Example usage
num_qubits = 6
num_steps = 1
rx_angle = 0.5 * pi

qc = generate1dTfimCircuit(num_qubits, num_steps, rx_angle)
qc.draw(output="mpl")


Certainly! Here's a README.md file template you can use for your project:

markdown
نسخ الكود
# 1D Transverse Field Ising Model (TFIM) Quantum Circuit Generator

This repository contains Python code for generating quantum circuits implementing the 1D Transverse Field Ising Model (TFIM) using Qiskit.

## Overview

The 1D TFIM is a model in quantum physics that describes interactions between spins (qubits) in a chain structure. This repository provides tools to construct quantum circuits representing the TFIM Hamiltonian using Qiskit, a quantum computing framework in Python.

## Features

- **Custom Gate Definitions**: Includes custom gates like the square root of the Y gate (`sqrt(Y)`) and its inverse (`sqrt(Y)^dag`).
- **Trotterization Implementation**: Utilizes Trotterization technique to approximate the evolution of TFIM Hamiltonian over time steps.
- **Visualization**: Generates visual representations of quantum circuits using Matplotlib.

## Installation

To use this project, ensure you have Python 3.x and install the required dependencies using pip:

```bash
pip install qiskit matplotlib numpy
```
# Usage
```Example Code
python
from qiskit import QuantumCircuit as circuit
from qiskit import QuantumRegister
from qiskit.circuit.library import UnitaryGate, YGate
from matplotlib import pyplot as plt
from numpy import pi
```
# Define custom gates
```SYGate = UnitaryGate(YGate().power(1/2), label=r"$\sqrt{Y}$")
SYdgGate = UnitaryGate(SYGate.inverse(), label=r"$\sqrt{Y}^\dag$")

def generate1dTfimCircuit(qubits, num_steps, rx_angle):
    qubit = QuantumRegister(qubits)
    qc = circuit(qubit)
    for steps in range(num_steps):
        add1dTfimTrotterLayer(qc, rx_angle)
    return qc

def add1dTfimTrotterLayer(qc, rx_angle):
    for i in range(0, qc.num_qubits - 1, 2):
        qc.sdg([i, i+1])
        qc.append(SYGate, [i+1])
        qc.cx(i, i+1)
        qc.append(SYdgGate, [i+1])
    
    for i in range(1, qc.num_qubits - 1, 2):
        qc.sdg([i, i+1])
        qc.append(SYGate, [i+1])
        qc.cx(i, i+1)
        qc.append(SYdgGate, [i+1])
    
    qc.rx(rx_angle, list(range(qc.num_qubits)))

# Example usage
num_qubits = 6
num_steps = 1
rx_angle = 0.5 * pi

qc = generate1dTfimCircuit(num_qubits, num_steps, rx_angle)
qc.draw(output="mpl")
```
# Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or create a pull request.
