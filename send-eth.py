import json
from web3 import Web3

g = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(g))

# Check Connection
stat = web3.isConnected()
print(stat)

# Get Current Block on ETH
block = web3.eth.blockNumber
print(block)

acc1 = "0x392Fc35CCb29Dc0Bd0304fBc9377cC2dB07C08fa"
acc2 = "0xf82b692b357fD4d6797D0E2Eb5B83508afE5BF0f"
prv1 = "0d9a797c59d9fce5c6188daa14a83ca16ca461b46054efd18546289f6e2557ed"

nonce = web3.eth.getTransactionCount(acc1)

tx = {
    'nonce': nonce,
    'to': acc2,
    'value': web3.toWei(10, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, prv1)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))

# Get Current Block on ETH
block = web3.eth.blockNumber
print(block)
