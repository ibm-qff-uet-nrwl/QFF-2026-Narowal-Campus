import numpy as np
from qiskit.quantum_info import Statevector

def grade_lab1_single_qubit(circuit):
    try:
        circuit = circuit.remove_final_measurements(inplace=False)
        if circuit.num_qubits != 1:
            return {"score": 0, "max": 10, "msg": "❌ Need exactly 1 qubit."}
        sv = Statevector.from_instruction(circuit)
        expected = Statevector([1/np.sqrt(2), 1/np.sqrt(2)])
        if np.abs(sv.inner(expected))**2 > 0.99:
            return {"score": 10, "max": 10, "msg": "✅ Perfect! |+> state created."}
        return {"score": 5, "max": 10, "msg": "⚠️ Not the |+> state."}
    except Exception as e:
        return {"score": 0, "max": 10, "msg": f"❌ Error: {e}"}

def grade_lab2_multiqubit_cnot(circuit):
    """Grades the Multi-Qubit CNOT lab: H on qubit 0, then CNOT(0,1)."""
    try:
        circuit = circuit.remove_final_measurements(inplace=False)
        
        if circuit.num_qubits != 2:
            return {"score": 0, "max": 10, "msg": "❌ Need exactly 2 qubits."}
        
        ops = circuit.count_ops()
        
        if 'h' not in ops:
            return {"score": 3, "max": 10, "msg": "⚠️ Hadamard gate is missing. Apply H to qubit 0 first."}
        
        if 'cx' not in ops and 'cnot' not in ops:
            return {"score": 3, "max": 10, "msg": "⚠️ CNOT gate is missing. Apply cx(0, 1) after the Hadamard."}
        
        sv = Statevector.from_instruction(circuit)
        expected = Statevector([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
        fidelity = np.abs(sv.inner(expected))**2
        
        if fidelity > 0.99:
            return {"score": 10, "max": 10, "msg": "✅ Perfect! CNOT gate applied correctly. You have created a Bell State!"}
        else:
            return {"score": 6, "max": 10, "msg": "⚠️ Gates are present but order or target may be wrong. Remember: H on qubit 0, then CX with control=0, target=1."}
    except Exception as e:
        return {"score": 0, "max": 10, "msg": f"❌ Error: {e}"}

def grade_lab3_bell_state(circuit):
    try:
        circuit = circuit.remove_final_measurements(inplace=False)
        if circuit.num_qubits != 2:
            return {"score": 0, "max": 10, "msg": "❌ Need exactly 2 qubits."}
        sv = Statevector.from_instruction(circuit)
        expected = Statevector([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
        if np.abs(sv.inner(expected))**2 > 0.99:
            return {"score": 10, "max": 10, "msg": "✅ Perfect! Bell state created."}
        return {"score": 5, "max": 10, "msg": "⚠️ Not a Bell state."}
    except Exception as e:
        return {"score": 0, "max": 10, "msg": f"❌ Error: {e}"}

def grade_lab4_ghz_state(circuit):
    try:
        circuit = circuit.remove_final_measurements(inplace=False)
        if circuit.num_qubits != 3:
            return {"score": 0, "max": 10, "msg": "❌ Need exactly 3 qubits."}
        sv = Statevector.from_instruction(circuit)
        expected = Statevector([1/np.sqrt(2), 0, 0, 0, 0, 0, 0, 1/np.sqrt(2)])
        if np.abs(sv.inner(expected))**2 > 0.99:
            return {"score": 10, "max": 10, "msg": "✅ Perfect! GHZ state created."}
        return {"score": 5, "max": 10, "msg": "⚠️ Not a GHZ state."}
    except Exception as e:
        return {"score": 0, "max": 10, "msg": f"❌ Error: {e}"}
