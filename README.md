# IOSXE_restconf
A starter project for interacting with the Cisco DevNet Sandbox IOS-XE router using RESTCONF

This project is intended to provide the scaffolding to start making RESTCONF requests to the always on sandbox IOS-XE router.
It is in no way a complete solution for Cisco RESTCONF in python, and is geared towards enabling more engineers to start testing the RESTCONF API to develop more code and identify what does and does not work. 

The example.py file will serve as documentation at this time. 

As I explore RESTCONF further and find more successes with interacting with the devices, I will add the methods and patterns here.

Installation: 


git clone https://github.com/dm-bell-networking/IOSXE_restconf

python3 -m venv <env_name>

source <env_name>/bin/activate

pip install -r requirements.txt

python example.py

