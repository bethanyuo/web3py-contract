# Smart Contracts using Web3.py
Use the `web3.py` library for interacting with Ethereum. Its API is derived from the `Web3.js` JavaScript API and should be familiar to anyone who has used `web3.js`. The exercise will show how to interact with an already deployed contract on the Ethereum Ropsten Testnet.
## Set up environment
Web3.py requires Python 3. It can be installed using pip as follows:
```sh
$ pip install web3
```
Create a new Python file and import the following:
```py
from web3 import Web3, HTTPProvider
```
We will need `HTTPProvider` in order to create our connection to the Ropsten Testnet using `Infura.io`.
Now let’s get the necessary Infura.io provider. Go to https://infura.io/ and copy the Ropsten URL.
```py
PROVIDER = "https://rospten.infura.io/<ENDPOINT-ID>"
w3 = Web3(HTTPProvider(PROVIDER))
```
 
In order to get a contract instance of an already deployed contract, we will need its `address` and `application binary interface`. For this exercise’s purpose, deploy a simple contract storing an array of facts through `Remix IDE` using MetaMask Ropsten as a provider.

If you do not have ETHt, use the MetaMask faucet: https://faucet.metamask.io/ 

Then, copy its `address` and `ABI`, and create an instance of the contract. Json library will be needed to the decode the ABI:
```py
CONTRACT_INSTANCE = w3.eth.contract(CONTRACT_ADDRESS, abi=json.loads(ABI))
```
## Writing to the Smart Contract
Now that there is an instance of the contract, create a method for writing facts in the smart contract. It will need the instance, a `private key/wallet`, the address of the `private key/wallet` and the `fact`. The library `is not recommended` to work with Local Private Keys in `Production` at the moment, so for the exercise we will enable the _unaudited features_. 
```py
w3.eth.enable_unaudited_features()
```
Because the `contract owner` can only add facts to this contract, copy the private key and address. The address will be needed to easily calculate the `nonce`.
We will create a simple transaction, which `adds a fact` to the contract, `sign it` with the private key and `send it`.

Try adding a fact using another private key. _RESULT: `FAIL`_
## Reading from the Smart Contract
When reading from a Smart Contract, no wallets or private keys are needed. 
First, create a method which gets a fact by a given `index`. Then, create a method which gets `how many facts` are stored in the contract.
```
$ python3 main.py
Fact 1: The Times 03/Jan/2009 Chancellor on brink of second bailout for banks
Stored facts in the contract: 1
```
## Module
MI4: Module 5: E6
