from pypresence import Presence
import time
import asyncio
#from aioconsole import ainput
from threading import Thread
client_id = "434356416304906240"
RPC = Presence(client_id)
RPC.connect()
x = "Battlefield 1"
y = 0
async def ask_game():
        x = await ainput("Insert Game")
        if x == "":
            x = "At the menu"

while True:
    RPC.update(details="Playing " +x, large_image="madmrcrazy", large_text="PSN: MadMrCrazy")
    print("Set Presence @ " + str(y))
    x = input("What game are you playing?")
    
    
