import pip;modules=["pythonnet","pyfiglet","colorama","PySimpleGui","keyboard","mouse"]
for i in range(0,len(modules)):
    print(f"Installing module {modules[i]}")
    try:
        pip.main(["install",modules[i]])
        print(f"Success installing module")
    except Exception as err:
        print(f"Failed to install module")
        print(err)
