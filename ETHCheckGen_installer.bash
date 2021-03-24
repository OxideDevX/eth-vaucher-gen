#!/bin/bash
apt update -y && apt upgrade -y
apt install git python -y
pip install requests
git clone https://github.com/OxideDevX/eth-vaucher-gen/
cd ETHVoucherGen
python ETHCheckGen.py