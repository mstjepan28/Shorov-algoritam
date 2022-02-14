# kod preuzet sa https://quantumcomputinguk.org/tutorials/shors-algorithm-with-code
from qiskit import IBMQ
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import Shor

IBMQ.enable_account('ENTER API TOKEN HERE') 
provider = IBMQ.get_provider(hub='ibm-q')

backend = provider.get_backend('ibmq_qasm_simulator') 

print('\n Shors Algorithm')
print('--------------------')
print('\nExecuting...\n')

#Function to run Shor's algorithm where 21 is the integer to be factored
factors = Shor(21) 

result_dict = factors.run(QuantumInstance(backend, shots=1, skip_qobj_validation=False))
result = result_dict['factors'] # Get factors from results

print(result)
print('\nPress any key to close')
input()