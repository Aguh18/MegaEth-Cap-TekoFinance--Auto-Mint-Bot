from web3 import Web3
from config import config
from display import loging
import time
import random
from datetime import datetime, timedelta


def wait_until_next_day():
    now = datetime.now()

    # Random waktu antara jam 14:00 sampai 17:00
    random_hour = random.randint(14, 17)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)

    next_run_time = datetime(now.year, now.month, now.day, random_hour, random_minute, random_second)

    # Cek apakah waktu sekarang > next_run_time atau selisihnya < 8 jam
    if now > next_run_time or (next_run_time - now).total_seconds() < 8 * 60 * 60:
        next_run_time += timedelta(days=1)

    # Log jadwal berikutnya menggunakan f-string
    loging.log_info(f"Next run scheduled at {next_run_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    while True:
        now = datetime.now()
        time_remaining = next_run_time - now

        if time_remaining.total_seconds() <= 0:
            break

        # Tampilkan countdown menggunakan print karena logging tidak mendukung end='\r'
        countdown = str(time_remaining).split('.')[0]
        print(f"Countdown: {countdown}", end='\r')
        time.sleep(1)

    # Newline dan pesan sukses menggunakan logging
    print
    loging.log_info(f"('It is now time to run the next transaction!'")

def check_connection(web3):
    try:
        # Check if connected
        if web3.is_connected():
            loging.log_success("Connected to MegaETH node")
            return True
        else:
            loging.log_error("Failed to connect to MegaETH node")
            return False
    except Exception as e:
        loging.log_error(f"Error checking connection: {e}")
        return False

def is_valid_address(address):
    return Web3.is_checksum_address(address)
import logging

def check_token_balance(address, web3, token=None):
    try:
        if not web3.is_address(address):
            raise ValueError("Invalid Ethereum address")

        address = web3.to_checksum_address(address)

        if token:
            token_data = config.TOKENS.get(token)
         
            if not token_data:
                raise ValueError(f"Token '{token}' not found in config")

            token_contract = web3.eth.contract(address=web3.to_checksum_address(token_data["address"]), abi=config.ERC20_ABI)
            raw_balance = token_contract.functions.balanceOf(address).call()
            decimals = token_data.get("decimals", 18)
            balance = raw_balance / 10**decimals
            return balance
        
        decimals= config.TOKENS["ETH"]["decimals"]
        raw_eth_balance = web3.eth.get_balance(address)
        eth_balance = raw_eth_balance / 10**decimals
        return eth_balance

    except Exception as e:
        logging.error(f"Error checking balance: {e}")
        return None

    
def show_balance(address, web3, token=None):
    if token and token != "ETH":
        balance = check_token_balance(address, web3, token)
        if balance is not None:
            loging.log_info(f"{token} Balance: {balance:.18f} {token}")
           
    else:
        balance = check_token_balance(address, web3)
        loging.log_info(f"ETH Balance: {balance:.18f} ETH".rstrip('0').rstrip('.'))
        
def mint_tokens(private_key, w3, token):
    try:
        # Initialize wallet
        account = w3.eth.account.from_key(private_key)
        wallet_address = account.address
        recipient_address = w3.to_checksum_address(wallet_address)
        
        # Create contract instance
        contract = w3.eth.contract(address=config.TOKENS[token]["address"], abi=config.CONTRACT_ABI)
        
        # Build transaction
        tx = contract.functions.mint(recipient_address, config.TOKENS[token]["token_amount"]).build_transaction({
            'chainId': config.CHAIN_ID,
            'gas': 100000,
            'gasPrice': w3.eth.gas_price,
            'nonce': w3.eth.get_transaction_count(wallet_address),
        })
        
        # Sign and send transaction
        signed_tx = w3.eth.account.sign_transaction(tx, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)  # Fixed: raw_transaction
        tx_hash_hex = w3.to_hex(tx_hash)
        
        loging.log_debug(f"Transaction sent: {tx_hash_hex}")
        loging.log_debug(f"View on explorer: {config.EXPLORER_URL}/tx/{tx_hash_hex}")
        
        # Wait for confirmation
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        
        if receipt.status == 1:
            loging.log_success(f"Mint successful! {token} credited.")
            return True
        else:
            loging.log_error("Mint failed!")
            return False
    except Exception as e:
        loging.log_error(f"Error: {str(e)}")
        return False
   
   





    
