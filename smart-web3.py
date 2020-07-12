import json;
from web3 import Web3, HTTPProvider;

PROVIDER = "https://ropsten.infura.io/v3/<PROJECT_ID>";

ADDRESS = "0xDAcd20ebf370F9499ab49e155AeF74860F0ab457";
PRIVATE_KEY = "<PRIVATE_KEY>";

CONTRACT_ADDRESS = "0x3b1B379f51Fcdf4a9a1c05DFB251AFA0d1815b39";

w3 = Web3(HTTPProvider(PROVIDER));
w3.toChecksumAddress(CONTRACT_ADDRESS);

ABI = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"string","name":"newFact","type":"string"}],"name":"add","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"count","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getFact","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]';

CONTRACT_INSTANCE = w3.eth.contract(CONTRACT_ADDRESS, abi=json.loads(ABI));

def add_fact(contract_instance, private_key, address, fact):
      nonce = w3.eth.getTransactionCount(address) # this must be the account address from metamask.
      add_transaction = contract_instance.functions.add(fact).buildTransaction({
            'gas': 4600000,
            'nonce': nonce
      });

      print(add_transaction);
      signed_txn = w3.eth.account.signTransaction(add_transaction, private_key=private_key);
      w3.eth.sendRawTransaction(signed_txn.rawTransaction);


def get_fact(contract_instance, index):
      fact = contract_instance.functions.getFact(index).call();
      print(fact);

def facts_count(contract_instance):
      count = contract_instance.functions.count().call();
      print('Stored facts in the contract: ', count);

fact = 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks';
add_fact(CONTRACT_INSTANCE,PRIVATE_KEY, ADDRESS, fact);
# add_fact(CONTRACT_INSTANCE,PRIVATE_KEY,w3.toChecksumAddress(ADDRESS), fact);
get_fact(CONTRACT_INSTANCE, 0);
facts_count(CONTRACT_INSTANCE);
