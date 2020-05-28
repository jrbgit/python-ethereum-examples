import json
from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/4ccf9863c7eb4cf7ac1b7ff895e54084"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check Connection
stat = web3.isConnected()
print(stat)

# Get Current Block on ETH
block = web3.eth.blockNumber
print(block)

# Get Account Balance
account = "0x8348176B6b7A2d2C575b74Bcf5daD83B53A3Af16"
balance = web3.eth.getBalance(account)
print(balance)

# Convert Blanace from Wei to ETH
bal2 = web3.fromWei(balance, 'ether')
print(bal2)


