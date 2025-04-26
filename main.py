from web3 import Web3

from display import loging
from eth_account import Account
from config import config
from dotenv import load_dotenv
from display import appearance
from utils.utils import show_balance
from utils.utils import check_connection
from utils.utils import mint_tokens
from utils.utils import wait_until_next_day
import os

load_dotenv()

def main():
    
    print(appearance.ASCII_ART)
    print(appearance.CREDIT)
    
    PRIVATE_KEY = os.getenv("PRIVATE_KEY") 
    account = Account.from_key('0x' + PRIVATE_KEY)
    address = account.address
    web3 = Web3(Web3.HTTPProvider(config.RPC_URL))
    
    loging.log_info("Connecting to MegaETH node...")
    loging.log_info(f"Account Address: {address}")
   
    is_connect = check_connection(web3)
    if not is_connect:
        loging.log_error("Failed to connect to MegaETH node")
        return
    
    is_auto = False
    while True:
            # Minta input dari user
            mint_method = input("Do you want to auto run mint automatically every day or once? (auto/once): ").strip().lower()

            # Cek apakah input adalah "auto" atau "once"
            if mint_method == "auto":
                is_auto= True
                break
            elif mint_method == "once":
                is_auto= False
                break
            else:
                loging.log_warning("❌ Invalid input. Please enter 'auto' or 'once'.")
                continue
    
    while True:
        try:
            mint_count = int(input("How much minting do you want to do? : "))
            break  
        except ValueError:
            loging.log_warning("Invalid input. Please enter a number.")
            continue
    
    print("\n=== BALANCE CHECK ===")
    print("-" * 50)
    for token in config.TOKENS.keys():
        show_balance(address, web3, token=token)
    print("-" * 50)
    
    loging.log_debug("starting minting process...")
    while True:
        for i in range(mint_count):
            print("-" * 50)
            loging.log_info("Minting tokens...")
            
            is_succes = mint_tokens(PRIVATE_KEY, web3)
            
            if is_succes:
                loging.log_success(f"minting {i+1} of {mint_count} completed successfully.")
            else:
                loging.log_error(f"Minting {i+1} of {mint_count} failed.")
            
            
            for token in config.TOKENS.keys():
                show_balance(address, web3, token=token)
                
            print("-" * 50)
        if is_auto:
            loging.log_info("Waiting for the next day to run the next transaction...")
            wait_until_next_day()
        else:
            loging.log_info("Minting process completed.")
            break
            
    
if __name__ == "__main__":
    try:
        
        main()
    except KeyboardInterrupt:
        loging.log_warning("Program interrupted by user.")


