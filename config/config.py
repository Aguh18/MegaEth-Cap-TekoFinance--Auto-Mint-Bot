from web3 import Web3

RPC_URL='https://carrot.megaeth.com/rpc'
CONTRACT_ADDRESS = Web3.to_checksum_address("0xe9b6e75c243b6100ffcb1c66e8f78f96feea727f")
TOKEN_AMOUNT = Web3.to_wei(1000, 'ether')
CHAIN_ID=6342
EXPLORER_URL= "https://www.megaexplorer.xyz/"

TOKENS = {
    "cUSD": {"address": Web3.to_checksum_address("0xE9b6e75C243B6100ffcb1c66e8f78F96FeeA727F"), "decimals": 18},
    "ETH": {"address": None, "decimals": 18},
}

CONTRACT_ABI = '[{"constant":false,"inputs":[{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"}],"name":"mint","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'

ERC20_ABI = '[{"constant":true,"inputs":[{"name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"amount","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"type":"function"}]'

