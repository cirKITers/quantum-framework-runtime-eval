# import pennylane as qml
# from pennylane import numpy as np
# import qiskit as q
from qiskit.circuit.random import random_circuit
from qiskit.compiler import transpile
import cirq

# import config


def get_random_qasm_circuit(qubits, depth, seed, measure=True):
    qc = random_circuit(qubits, depth, max_operands=3, measure=measure, seed=seed)
    qc = transpile(
        qc,
        basis_gates=[
            "u2",
            "u3",
            "cx",
            "id",
            "x",
            "y",
            "z",
            "h",
            "s",
            "t",
            "rx",
            "ry",
            "rz",
            "cx",
            # "cy", #not in qibo framework
            "cz",
            # "ch", #not in qibo framework
            "swap",
            "ccx",
            # "cswap", #not in qibo framework
        ],
    )
    return qc.qasm()
