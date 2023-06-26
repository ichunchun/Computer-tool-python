import configparser
import winreg
import requests
import random,re

cfp = configparser.ConfigParser()
cfp.read("Config.ini")

netcard = cfp.get("Main","netcard")

print(netcard)