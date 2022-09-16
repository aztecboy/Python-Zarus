import threading,time
from ZarusScript import *
from Zarus import Vars

def run():
    Main.Program()

threading.Thread(target=run).start()
while True:
    time.sleep(0.01)
    Misc.Runtime+=0.01
    if Vars.Closed:
        quit()
