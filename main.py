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

def auto_mode(web3, address, PRIVATE_KEY):
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
            
            for token in config.TOKENS.keys():
                if token != "ETH":
                    is_succes = mint_tokens(PRIVATE_KEY, web3, token  )
                
            if is_succes:
                loging.log_success(f"minting {i+1} of {mint_count} completed successfully.")
            else:
                loging.log_error(f"Minting {i+1} of {mint_count} failed.")
                
            print("-" * 50)
            
            for token in config.TOKENS.keys():
                show_balance(address, web3, token=token)
                
            print("-" * 50)
        if is_auto:
            loging.log_info("Waiting for the next day to run the next transaction...")
            wait_until_next_day()
        else:
            loging.log_info("Minting process completed.")
            break
        

def minting(private_key, web3 ,token,  address ):
    while True:
        try:
            mint_count = int(input("How much minting do you want to do? : "))
            break  
        except ValueError:
            loging.log_warning("Invalid input. Please enter a number.")
            continue
    
    for i in range(mint_count):
        loging.log_info(f"Minting {i+1} of {mint_count}...")
        is_succes = mint_tokens(private_key, web3, token)
        if is_succes:
            loging.log_success(f"Minting {i+1} of {mint_count} completed successfully.")
        else:
            loging.log_error(f"Minting {i+1} of {mint_count} failed.")
    print("\n=== BALANCE CHECK ===")
    print("-" * 50)
    for token in config.TOKENS.keys():
        show_balance(address, web3, token=token)
    print("-" * 50)

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
    
    # menu
    while True:
        loging.log_info("====MENU====")
        loging.log_info("-" * 50)
        loging.log_info("1. Mint cUSDC tokens")
        loging.log_info("2. Mint tkUSDC tokens")
        loging.log_info("3. Mint tkWBTC tokens")
        loging.log_info("4. Mint tkETH tokens")
        loging.log_info("5. Mint All")
        loging.log_info("3. Exit")
        loging.log_info("-" * 50)
        
        choice = input("Enter your choice: ")
        if choice == "1":
            minting(PRIVATE_KEY, web3, "cUSD", address=address)
        elif choice == "2":
            minting(PRIVATE_KEY, web3, "tkUSDC", address=address)
        elif choice == "3":
            minting(PRIVATE_KEY, web3, "tkWBTC", address=address)
        elif choice == "4":
            minting(PRIVATE_KEY, web3, "tkETH", address=address)
        elif choice == "5":
            auto_mode(web3, address, PRIVATE_KEY)
        elif choice == "6":
            loging.log_info("Exiting the program.")
            break
        else:
            loging.log_warning("Invalid choice. Please try again.")
    
            
    
if __name__ == "__main__":
    try:
        
        main()
    except KeyboardInterrupt:
        loging.log_warning("Program interrupted by user.")


