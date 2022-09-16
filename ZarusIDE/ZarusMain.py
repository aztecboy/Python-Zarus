import clr,time,sys,os,shutil,time
from colorama import init,Fore,Back,Style
init(convert=True)
option=sys.argv[1]
infile=sys.argv[2]
def Scan(temp):
    print(Fore.GREEN)
    print("Scanning syntax")
    print(Fore.RESET)
    dllfiles=[]
    zar=[]
    type="ZarusEXE"
    exscript=""
    for i in range(0,len(temp)):

        if temp[i]=="":
            pass
        else:
            temp2=temp[i].replace(" ","")
            temp3=temp[i].replace("		","")




            if ";" in temp2:
                pass


            elif ":" in temp2:
                pass
            else:
                print(Fore.RED+f"Syntax error in line {i}")
                time.sleep(3)
                quit()
    print(Fore.GREEN)
    print("Scanning Compiler Code")
    print(Fore.RESET)
    for i in range(0,len(temp)):
        temp2=temp[i]
        if "--" in temp2:
            if "Type" in temp2:

                temp2=temp2.replace("--Type ","")
                temp2=temp2.replace(";","")
                temp2=temp2.replace(" ","")

                if temp2=="ZarusLibrary":
                    type="ZarusLibrary"
                elif temp2=="ZarusEXE":
                    type="ZarusEXE"
                else:
                    print(Fore.RED+f"Unkown type on line {i}")
                    time.sleep(3)
                    quit()

            elif "Include" in temp2:

                temp2=temp2.replace("--Include ","")
                if "zar" in temp2:
                    temp2=temp2.replace("zar ","")

                    try:

                        f=open("interpreter/lib/"+temp2.replace(";",""),"r")
                        zar.append(temp2.replace(";",""))
                        temp10="\n"+f.read()
                        temp10=temp10.replace("#","#**")
                        exscript+=temp10



                    except Exception as err:

                        print(Fore.RED+f"Unkown file on line {i}")
                        print(err)
                        time.sleep(3)
                        quit()

                    with open("interpreter/lib/"+temp2.replace(";",""),"r") as f:
                        e=f.read()


                    temp7=e.split("\n")
                    for i in range(0,len(temp7)):
                        temp8=temp7[i]
                        if "#@" in temp8:
                            temp9=temp8.replace("#@","")
                            if "@" in temp9:
                                pass
                            else:
                                if ".net" in temp9:
                                    temp9=temp8.replace("#@.net ","")
                                    try:
                                        f=open("interpreter/lib/"+temp9.replace(";",""),"r")
                                        if temp9.replace(";","") in dllfiles:
                                            pass
                                        else:
                                            dllfiles.append(temp9.replace(";",""))



                                    except Exception as err:

                                        print(Fore.RED+f"Missing required files")
                                        print(err)
                                        time.sleep(3)
                                        quit()


                elif ".net" in temp2:
                    temp2=temp2.replace(".net ","")
                    try:
                        print(temp2)
                        f=open("interpreter/lib/"+temp2.replace(";",""),"r")
                        dllfiles.append(temp2.replace(";",""))


                    except Exception as err:

                        print(Fore.RED+f"Unkown file on line {i}")
                        print(err)
                        time.sleep(3)
                        quit()

                else:
                    print(Fore.RED+f"Unkown language on line {i}")
                    time.sleep(3)
                    quit()
            else:
                if "\"" in temp2:
                    pass
                else:
                    print(Fore.RED+f"Unkown command on line {i}")
                    time.sleep(3)
                    quit()
    print(Fore.GREEN)
    print("Success")
    print(Fore.RESET)
    return dllfiles,type,exscript

def CompileExe():
    try:
        outloca=sys.argv[3]
        print(Fore.GREEN)
        print("Attempting to read script")
        print(Fore.RESET)
        with open(infile,"r") as f:
            script2=f.read()
            temp9=script2.split("\n")
            temp10=False
            for i in range(0,len(temp9)):
                if "{{}}" in temp9[i]:
                    if temp10:
                        pass
                    else:
                        temp9[i]=temp9[i].replace("{{}}","Program()")
                        temp10=True

            if temp10:
                pass
            else:
                print(Fore.RED+f"Cant find entry point {i}")
                time.sleep(3)
                quit()
            script2=""
            for i in range(0,len(temp9)):
                script2+=temp9[i]+"\n"
            print(Fore.GREEN)
            print("Successfully read script")
            print(Fore.RESET)
            print(f"{infile}---")
            print(script2)
            print(f"---{infile}")
            time.sleep(0.5)
            temp=script2.split("\n")


            dlls,type,ex=Scan(temp)
            print(f"Type >> {type}")
            print(f"Included .net files >> {dlls}")
            print(f"Library Script---")
            print(ex)
            print(f"---Library Script")
            time.sleep(0.5)
    except Exception as err:
        print(Fore.RED+"Cant open or find file/folder")
        print(Fore.RESET)
        print(err)
        time.sleep(3)
        quit()

    try:



        if type=="ZarusEXE":
            print(Fore.GREEN)
            print("Attempting to compile into ZarusEXE")
            print(Fore.RESET)
            with open("interpreter/data/compileradd.zar","r") as x:
                script=x.read()




            print(Fore.GREEN)
            print("Including dll files")
            print(Fore.RESET)
            for i in range(0,len(dlls)):

                temp6=dlls[i].replace(".dll","")
                temp6="/lib/"+temp6
                script=script.replace("#$",f"#{temp6}---\nclr.AddReference(\"{temp6}\")\n#$")


            script=script+("        "+script2.replace("\n","\n        "))


            script=script.split("\n");
            temp=""
            for i in range(0,len(script)):

                if "\"" in script:
                    temp+=script[i]+"\n"
                else:
                    temp+=script[i].replace("--","#")+"\n"
            script=temp

            print(Fore.GREEN)
            print("Including Librarys")
            print(Fore.RESET)
            script=script.replace("#$",f"{ex}\n#$")
            print(Fore.GREEN)
            print("Writing python code")
            print(Fore.RESET)
            if "/" in outloca:
                outloca+="/"
            elif "\\" in outloca:
                outloca+="\\"
            with open(f"{outloca}ZarusScript.py","w") as f:

                f.write(script)
            print(Fore.GREEN)
            print("Success writing ZarusScript.py")
            print(Fore.RESET)
            with open(f"{outloca}Zarus.py","w") as f:
                with open("interpreter/Zarus.py","r") as x:
                    zar=x.read()

                f.write(zar)
            print(Fore.GREEN)
            print("Success writing Zarus.py")
            print(Fore.RESET)
            os.mkdir(f"{outloca}lib")
            with open(f"{outloca}Run.py","w") as f:
                with open("interpreter/Run.py","r") as x:
                    run=x.read()
                f.write(run)

            print(Fore.GREEN)
            print("Success writing Run.py")
            print(Fore.RESET)
            src_path = "interpreter/lib/ZarusBase.dll"
            dst_path = f"{outloca}lib/ZarusBase.dll"
            shutil.copy(src_path, dst_path)
            src_path = "interpreter/lib/SystemNotifications.dll"
            dst_path = f"{outloca}lib/SystemNotifications.dll"
            shutil.copy(src_path, dst_path)
            print(Fore.GREEN)
            print("Success writing SytemNotifications.dll")
            print(Fore.RESET)
            for i in range(0,len(dlls)):
                src_path = f"interpreter/lib/{dlls[i]}"
                dst_path = f"{outloca}lib/{dlls[i]}"
                shutil.copy(src_path, dst_path)
                print(Fore.GREEN)
                print(f"Success writing {dlls[i]}")
                print(Fore.RESET)
        elif type=="ZarusLibrary":
            print(Fore.GREEN)
            print("Attempting to compile into ZarusLibrary")
            print(Fore.RESET)
            with open("interpreter/data/compilerlib.zar","r") as x:
                script=x.read()
            with open(infile,"r") as f:



                script=script+f.read();
                script=script.replace("--","#")
            print(Fore.GREEN)
            print("Success reading script")
            print(Fore.RESET)
            for i in range(0,len(dlls)):
                script=script.replace("#@@",f"#@.net {dlls[i]}\n#@@")
            script=script.replace("#@@",ex+"\n#@@")
            print(Fore.GREEN)
            print("Success including .net and librarys")
            print(Fore.RESET)
            name=input("Library Name >> ")
            script=script.replace("{{}}",name)
            with open(f"{outloca}{name}.zar","w") as f:
                f.write(script)
            print(Fore.GREEN)
            print(f"Success writing {name}.zar")
            print(Fore.RESET)




    except Exception as err:
        print(Fore.RED+"Cant open or find file/folder")
        print(Fore.RESET)
        print(err)
        time.sleep(3)
        quit()


if option=="pyexe":
    CompileExe()
else:
    print(Fore.RED+"Invalid option")
    print(Fore.RESET)
while True:
    print("Type c to close")
    e=input(" >> ")
    if e=="c":
        break
