# MegaEth Cap ANDS TekoFinance Auto Mint Bot

## Overview
The **MegaEth TekoFinance and cap  Auto Mint Bot** is a simple Python tool to get  mint token in TekoFinance and cap . Mint once or daily, choose how many times, and check your balances. It’s easy, shows transaction links, and is great for testing Cap on MegaEth’s fast testnet!

## Features
- Mint 1000 cUSDC.
- Mint 2000 tkUsdc .
- Mint 1 tkETH .
- Mint 0.02 tkWBTC .
- Run multiple mints in one go.
- Shows transaction links and status.


## Prerequisites
- **Python 3.8+**.
- **MegaEth testnet wallet** with testnet ETH.

## Installation

1. **Get the Code**  
   Clone or create a folder for the code:

   ```bash
   git clone https://github.com/Aguh18/MegaEth-Cap-TekoFinance-Auto-Mint-Bot.git
   cd MegaEth-Cap-TekoFinance-Auto-Mint-Bot.git
   ```


2. **Set Up Virtual Environment**  

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Tools**  
   Install from `requirements.txt`:

   ```bash
   pip install -r requirements.txt

4. **Add Private Key**  
   Create `.env` in the project folder:

   ```env
   PRIVATE_KEY=your_private_key
   ```

   - Use your 64-character testnet private key (no `0x`). Example:
     ```env
     PRIVATE_KEY=abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890
     ```
   

5. **Get Testnet ETH**  
   Claim **0.005 ETH/day** at [MegaETH Testnet Faucet](https://testnet.megaeth.com/).

## Usage

1. **Check Wallet**  
   Ensure you have ~0.001–0.005 testnet ETH for fees.

2. **Run Bot**  

   ```bash
   python main.py
   ```

3. **Answer Prompts**  
   - **Mode**: Type `once` to mint once or `auto` for daily (needs a running server).
   - **Count**: Enter number of mints (e.g., `3`).

   


## Safety Tips
- Don’t share your private key or `.env`.
- Use a testnet wallet, not mainnet.
- Check code before adding your key.



## Disclaimer
For Education only. Use at your own risk. Creators aren’t liable for issues.

## License
MIT License

## Community

- [AutoDropz Telegram](https://t.me/+V_JQTTMVZVU3YTM9)
