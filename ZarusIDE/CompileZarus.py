import sys,os
name=sys.argv[1]
input=sys.argv[2]
output="scripts/"+name
if os.path.exists(output):
    print("Path Already Exists")
else:
    os.mkdir(output)
    os.system(f"ZarusMain.py pyexe {input} {output}")
