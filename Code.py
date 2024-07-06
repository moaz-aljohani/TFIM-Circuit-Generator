# Import necessary classes and functions from Qiskit
from qiskit import QuantumCircuit as circuit  # Import QuantumCircuit and alias it as 'circuit'
from qiskit import QuantumRegister  # Import QuantumRegister
from qiskit.circuit.library import UnitaryGate, YGate  # Import UnitaryGate and YGate
from matplotlib import pyplot as plt  # Import pyplot from matplotlib for plotting
from numpy import pi  # Import pi from numpy

# Define a unitary gate equivalent to the square root of the Y gate
SYGate = UnitaryGate(YGate().power(1/2), label=r"$\sqrt{Y}$")

# Define the inverse of the square root of the Y gate
SYdgGate = UnitaryGate(SYGate.inverse(), label=r"$\sqrt{Y}^\dag$")

# Function to generate a 1D Transverse Field Ising Model (TFIM) quantum circuit
def generate1dTfimCircuit(qubits, num_steps, rx_angle):
    qubit = QuantumRegister(qubits)  # Create a quantum register with the specified number of qubits
    qc = circuit(qubit)  # Initialize a quantum circuit with the quantum register
    for steps in range(num_steps):  # Loop over the number of Trotter steps
        add1dTfimTrotterLayer(qc, rx_angle)  # Add a Trotter layer to the circuit
    return qc  # Return the constructed quantum circuit

# Function to add a Trotter layer to the quantum circuit
def add1dTfimTrotterLayer(qc, rx_angle):
    # Apply gates to even-indexed pairs of qubits
    for i in range(0, qc.num_qubits - 1, 2):
        qc.sdg([i, i+1])  # Apply the S-dagger gate to qubits i and i+1
        qc.append(SYGate, [i+1])  # Apply the square root of the Y gate to qubit i+1
        qc.cx(i, i+1)  # Apply the CNOT gate with control qubit i and target qubit i+1
        qc.append(SYdgGate, [i+1])  # Apply the inverse square root of the Y gate to qubit i+1
    
    # Apply gates to odd-indexed pairs of qubits
    for i in range(1, qc.num_qubits - 1, 2):
        qc.sdg([i, i+1])  # Apply the S-dagger gate to qubits i and i+1
        qc.append(SYGate, [i+1])  # Apply the square root of the Y gate to qubit i+1
        qc.cx(i, i+1)  # Apply the CNOT gate with control qubit i and target qubit i+1
        qc.append(SYdgGate, [i+1])  # Apply the inverse square root of the Y gate to qubit i+1
    
    # Apply RX rotation gate to all qubits
    qc.rx(rx_angle, list(range(qc.num_qubits)))

# Set the number of qubits, number of steps, and RX rotation angle
num_qubits = 6
num_steps = 1
rx_angle = 0.5 * pi

# Generate the 1D TFIM quantum circuit
qc = generate1dTfimCircuit(num_qubits, num_steps, rx_angle)

# Draw the quantum circuit
qc.draw(output="mpl")
