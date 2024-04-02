import asyncio
from functools import partial
from web3 import Web3

# Put your RPC link from provider
ETHEREUM_NODE_URL = "https://rpc.rpc/"

# Enter the gwei amount at which you would like to perform the transaction
GWEI = 20

# Put price that you want to bridge
eth_quantity_to_bridge = 0.001

# Put your private keys as shown => 'yourprivate',
PRIVATE_KEYS = ['privatekey',
                'privatekey',
                'privatekey',
                ]

w3 = Web3(Web3.HTTPProvider(ETHEREUM_NODE_URL))

CONTRACT_ABI = [{"anonymous": False, "inputs": [...], "name": "EthWithdrawalFinalized", "type": "event"}, ...]
CONTRACT_ADDRESS = w3.to_checksum_address('0x32400084C286CF3E17e7B677ea9583e60a000324')

zksync_contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)
eth_quantity = w3.to_wei(eth_quantity_to_bridge, 'ether')

async def interact_with_contract(wallet_address, private_key):
    # ... (rest of the function remains the same)

async def main():
    accounts = {w3.eth.account.from_key(KEY): KEY for KEY in PRIVATE_KEYS}

    while True:
        gas_price = w3.eth.gas_price
        gwei_gas_price = w3.from_wei(gas_price, 'gwei')

        if gwei_gas_price < GWEI:
            interact_with_contract_partial = partial(interact_with_contract, private_key=accounts[account])
            tasks = [interact_with_contract_partial(account) for account in accounts]
            await asyncio.gather(*tasks)

        await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())
