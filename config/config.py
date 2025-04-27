from web3 import Web3

RPC_URL='https://carrot.megaeth.com/rpc'
TOKEN_AMOUNT = Web3.to_wei(1000, 'ether')
CHAIN_ID=6342
EXPLORER_URL= "https://www.megaexplorer.xyz/"

TOKENS = {
   
    "tkUSDC": {"address": Web3.to_checksum_address("0xfaf334e157175ff676911adcf0964d7f54f2c424"), "decimals": 6, "token_amount":  Web3.to_wei(0.000000002, "ether")},
    "tkWBTC": {"address": Web3.to_checksum_address("0xf82ff0799448630eb56ce747db840a2e02cde4d8"), "decimals": 8, "token_amount":  Web3.to_wei(0.000000000002, "ether")},
    "tkETH": {"address": Web3.to_checksum_address("0x176735870dc6c22b4ebfbf519de2ce758de78d94"), "decimals": 18, "token_amount": Web3.to_wei(1, 'ether')},
    "cUSD": {"address": Web3.to_checksum_address("0xE9b6e75C243B6100ffcb1c66e8f78F96FeeA727F"), "decimals": 18, "token_amount": Web3.to_wei(1000, 'ether')},
    "ETH": {"address": None, "decimals": 18},
}

CONTRACT_ABI = '[{"constant":false,"inputs":[{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"}],"name":"mint","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'

ERC20_ABI = '[{"constant":true,"inputs":[{"name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"amount","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"type":"function"}]'

