import random
from pypresence import Presence
import time
timeis = int(time.time())
import asyncio
cid = "471293364109705217"
RPC = Presence(cid)
RPC.connect()
print("Playing with Lemons are we? Let's not burn anything to necessary.")
x = 1

while x <= 100:
    num = random.randint(1,7)
    num2 = random.randint(1,7)
    RPC.update(state="Burning Lemons", start=timeis, large_image="lemon"+str(num), party_size=[x,100], small_image="lemon"+str(num2))
    time.sleep(random.randint(15, 120))
    x = x+1
