#!/usr/bin/env python3
#importing module
import atexit

#prompt user for hostname
hostname = input("What value should we set for hostname?")

#normalize hostname input and print message
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg\nhonstname matches expected config.")

#inform user that script is exiting
atexit.register(print,"Exiting the script!")
