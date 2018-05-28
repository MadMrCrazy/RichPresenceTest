from pypresence import Presence
import time
import asyncio
#from aioconsole import ainput
from threading import Thread
client_id = "434356416304906240"
RPC = Presence(client_id)
RPC.connect()
x = "At the menu"
username = input("username: ")
while True:
    RPC.update(details=x, large_image="madmrcrazy", large_text="PSN: "+username)
    print("Set Presence")
    x = input("What game are you playing? : ")
    if x == "":
            x = "At the menu"
    else:
        x = "Playing " + x
