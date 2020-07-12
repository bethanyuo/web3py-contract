import json
from solc import compile_source
from web3 import Web3, HTTPProvider

web3 = Web3(HTTPProvider("http://localhost:8545"))

# Solidity source code
contract_source_code = '''
pragma solidity ^0.4.0;

contract SimpleStorage {
    uint storedData;

    function set(uint x) public {
        storedData = x;
    }

    function get() public view returns (uint) {
        return storedData;
    }
}
'''

web3.eth.defaultAccount = web3.eth.accounts[0]

compiled_sol = compile_source(contract_source_code)
abi = compiled_sol['<stdin>:SimpleStorage']['abi']
bytecode = compiled_sol['<stdin>:SimpleStorage']['bin']

# txHash = web3.eth.contract(abi=abi,bytecode=bytecode).deploy(transaction={ 'from' : web3.eth.accounts[0], 'gas' : 500000 })
# print(txHash)


# Interact with the contract
contractAddress = Web3.toChecksumAddress('0xe3e43fed9f6dab22f923687896424acce15ba461')
contract = web3.eth.contract(address=contractAddress,abi=abi)

# get the data
print(contract.functions.get().call())

contract.functions.set(1234).transact()
