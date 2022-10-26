
import clr,time,sys,os,shutil,time,ctypes
from colorama import init,Fore,Back,Style

init(convert=True)
option=sys.argv[1]
infile=sys.argv[2]
def CIIS(temp2,a2):
    temp3=list(temp2)
    iis=False
    try:
        for i2 in range(0,len(temp3)):
            temp4=temp3[i2]
            if temp4=="\"":
                if iis==True:
                    iis=False

                else:
                    iis=True
            elif temp4==a2:
                break
    except Exception as err:
        print("!")
        print(i2)
        print(temp3)
        print(err)
        time.sleep(5)
        quit()
    return iis
def Scan(temp):
    print(Fore.GREEN)

    print(Fore.RESET)
    localprivates=[]
    dllfiles=[]
    zar=[]
    type="ZarusEXE"
    exscript=""
    threads=""
    files=[]
    hotrun=False
    libraryname=None
    instalib=False
    threadn=[]
    zigs=[]
    locals=[]
    rep=[]
    mv=[]
    keeps=[]
    for i3 in range(0,len(temp)):

        if temp[i3]=="":
            pass
        else:
            temp2=temp[i3].replace(" ","")
            temp3=temp[i3].replace("		","")
    print(Fore.GREEN)

    print(Fore.RESET)

    for i in range(0,len(temp)):

        temp2=temp[i]

        if temp2=="\n":
            pass
        elif temp2=="":
            pass
        else:
            iis=CIIS(temp2,"::")
            if iis==False:
                if "::" in temp2:

                    b=temp2.split("::")
                    var=b[0]
                    b2=b[1].split(" ")
                    pl=False
                    p=False
                    v=False
                    vv=False
                    k=False
                    for i in range(0,len(b2)):
                        b3=b2[i]

                        if "NoneVar" in b3:

                            if vv==True:
                                print(Fore.RED+f"Cannot assign multiple vars {i}")
                                time.sleep(3)
                                quit()
                            else:
                                pass
                            var=var+"=None"
                            vv=True
                            k=True
                            print(var)
                            mv.append([temp2,var])
                        if "StringVar" in b3:

                            if vv==True:
                                print(Fore.RED+f"Cannot assign multiple vars {i}")
                                time.sleep(3)
                                quit()
                            else:
                                pass
                            var=var+"=\"\""
                            vv=True
                            k=True
                            print(var)
                            mv.append([temp2,var])
                        elif "Local" in b3:
                            if pl==True:
                                print(Fore.RED+f"Cannot assign multiple locals {i}")

                                time.sleep(3)
                                quit()
                            if type=="ZarusLibrary":
                                print(Fore.RED+f"Cannot assign locals for ZarusLibrary {i}")

                                time.sleep(3)
                                quit()
                            locals.append(var)
                            pl=True
                            k=False

                        elif "Private" in b3:
                            if pl==True:
                                print(Fore.RED+f"Cannot assign multiple locals {i}")
                                print(err)
                                time.sleep(3)
                                quit()

                            localprivates.append(var)
                            pl=True
                            k=False
                    if k==True:
                        keeps.append(temp2)





        if "--" in temp2:

            if "LibraryName" in temp2:
                temp2=temp2.replace("--LibraryName ","")
                libraryname=temp2
                print(Fore.RED+f"Warning: You can only set library name on type ZarusLibrary: Line {i}")
            elif "Enable" in temp2:
                temp2=temp2.replace("--Enable ","")
                if temp2=="HotRun":
                    hotrun=True
                    print(Fore.RED+f"Warning: HotRun will only work on type ZarusEXE: Line {i}")
                elif temp2=="InstaLib":
                    instalib=True
                    print(Fore.RED+f"Warning: InstaLib will only work on type ZarusLibrary: Line {i}")
            elif "Thread" in temp2:
                temp2=temp2.replace("--Thread ","")
                threadn.append(temp2)
                with open("interpreter/data/thread.zar","r") as f:
                    threads+=f.read().replace("{--}",temp2).replace("{..}",temp2)

            elif "Type" in temp2:

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
                print(temp2)
                if "zig" in temp2.split(" ")[0]:
                    temp2=temp2.replace("zig ","")
                    try:
                        with open("interpreter/lib/"+temp2,"r") as f:
                            pass
                    except Exception as err:
                        print(Fore.RED+f"Unkown file on line {i}")
                        print(err)
                        time.sleep(3)
                        quit()
                    zigs.append(temp2)

                elif "zar" in temp2.split(" ")[0]:


                    try:
                        temp2=temp2.replace("zar ","")

                        path="interpreter/lib/"+temp2.replace(";","")
                        f=open(path,"r")
                        zar.append(temp2.replace(";",""))
                        temp10="\n"+f.read()
                        temp10=temp10.replace("#","#**")
                        exscript+=temp10



                    except Exception as err:

                        print(Fore.RED+f"Unkown file on line {i}")
                        print(err)
                        time.sleep(3)
                        quit()

                    
                    with open("interpreter/lib/"+temp2.replace(";","").replace("zar ",""),"r") as f:
                        e=f.read()




                    temp7=e.split("\n")
                    for i in range(0,len(temp7)):
                        temp8=temp7[i]
                        if "#@" in temp8:
                            temp9=temp8.replace("#@","")
                            if "@" in temp9:
                                pass
                            else:
                                if ".zig" in temp9:
                                    temp9=temp8.replace("#@.zig ","")
                                    try:
                                        f=open("interpreter/lib/"+temp9.replace(";",""),"r")
                                        if temp9.replace(";","") in dllfiles:
                                            pass
                                        else:
                                            zigs.append(temp9.replace(";",""))



                                    except Exception as err:

                                        print(Fore.RED+f"Missing required files")
                                        print(err)
                                        time.sleep(3)
                                        quit()
                                elif ".net" in temp9:
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

                elif "_" in temp2.split(" ")[0]:
                    temp2=temp2.replace("._ ","");temp2=temp2.replace(";","")

                    p
                    dllfiles.append(temp2.replace(";",""))



                elif "net" in temp2.split(" ")[0]:
                    temp2=temp2.replace(".net ","");temp2=temp2.replace(";","")
                    try:
                        print(temp2)
                        f=open("interpreter/lib/"+temp2.replace(";",""),"r")
                        dllfiles.append(temp2.replace(";",""))


                    except Exception as err:

                        print(Fore.RED+f"Unkown file on line {i}")
                        print(err)
                        time.sleep(3)
                        quit()
                elif "py" in temp2:
                    temp2=temp2.replace("py ","");temp2=temp2.replace(";","")
                    try:

                        f=open("interpreter/lib/"+temp2,"r")
                        dllfiles.append(temp2)


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
    return dllfiles,type,exscript,threads,files,hotrun,libraryname,instalib,threadn,zigs,locals,rep,localprivates,mv,keeps
def CompileExe():
    try:
        strings=[]
        stringsa=0
        outloca=sys.argv[3]
        print(Fore.GREEN)
        print("Attempting to read script")
        print(Fore.RESET)
        with open(infile,"r") as f:
            script2=f.read()
            temp9=script2.split("\n")
            temp10=False
            for i in range(0,len(temp9)):
                if "EntryPoint" in temp9[i]:
                    if temp10:
                        pass
                    else:
                        temp9[i]=temp9[i].replace("Main EntryPoint:","def Program():")
                        temp10=True
            for i in range(0,len(temp9)):
                if "~~" in temp9[i]:
                    b=""
                    a=temp9[i].split("~~")
                    a=a[1]
                    a=a.split("~")
                    strings.append([stringsa,a[0]])
                    temp9[i].replace(f"~~{a[0]}~",f"~~@@{stringsa}@@~")
                    stringsa+=1

            script2=""
            for i in range(0,len(temp9)):
                script2+=temp9[i]+"\n"
            print(script2)
            print(Fore.GREEN)
            print("Successfully read script")
            print(Fore.RESET)


            print("Replacing Shortcuts")
            script2=script2.replace(";;","Main.").replace(";z;","Zarus.").replace(";ztst;","Zarus.Terminal.StringTypes.").replace(";zt;","Zarus.Terminal.").replace(";s;","System.").replace(";m;","Misc.").replace("!@","")
            print(f"{infile}---")
            print(script2)
            print(f"---{infile}")
            temp=script2.split("\n")

            try:
                dlls,type,ex,thread,files,hotrun,libraryname,instalib,threadn,zigs,locals,rep,localprivates,mv,keeps=Scan(temp)
                print(rep)
            except Exception as err:
                print("bruh")
                print(err)
                time.sleep(10)

            for b2 in range(0,len(rep)):
                for b in range(0,len(temp)):
                    if rep[b2]==temp[b]:
                        temp[b]="\n"

            tamp=""
            for b3 in range(0,len(temp)):
                tamp+=temp[b3]+"\n"

            script2=tamp
            for i in range(0,len(threadn)):
                script2=script2.replace(f"def {threadn[i]}",f"def {threadn[i]}ZT")
            script2+=thread

            print(f"Type >> {type}")
            print(f"Included files >> {dlls}")
            print(f"Library Script---")
            print(ex)
            print(f"---Library Script")

    except Exception as err:
        print(Fore.RED+"Cant open or find file/folder")
        print(Fore.RESET)
        print(err)
        time.sleep(10)
        quit()

    try:



        if type=="ZarusEXE":

            print(Fore.GREEN)
            print("Attempting to compile into ZarusEXE")
            print(Fore.RESET)
            script2l=script2.split("\n")
            with open("interpreter/data/compileradd.zar","r") as x:
                script=x.read()
            for i in range(0,len(script2l)):
                if "::" in script2l[i]:
                    if script2l[i] in keeps:
                        pass
                    else:
                        script2l[i]="\n"
            script2=""
            for i in range(0,len(script2l)):
                script2+=(script2l[i]+"\n")
            for i in range(0,len(localprivates)):
                script2=script2.replace(localprivates[i].split("=")[0],"PrivateEXE."+localprivates[i].split("=")[0])
                script=script.replace("#LP",localprivates[i])+"\n        "
            for i in range(0,len(mv)):
                r=mv[i]
                print(script2)
                script2=script2.replace(r[0],r[1])
                print(script2)






            print(Fore.GREEN)
            print("Including dll files")
            print(Fore.RESET)
            for i in range(0,len(locals)):
                script=script.replace("#LL",f"{locals[i]}\n#LL\n")
            for i in range(0,len(dlls)):
                if dlls[i]=="EXE-Runtime":
                    dlls.pop(i)
                    dlls.append("Runtime.exe")
                if ".py" in dlls[i]:
                    pass
                else:
                    temp6=dlls[i].replace(".dll","")
                    temp6="/lib/"+temp6
                    script=script.replace("#$",f"#{temp6}---\nclr.AddReference(\"{temp6}\")\n#$")
            for i in range(0,len(zigs)):
                try:
                    temp6=zigs[i]
                    print(f"---- {zigs[i]}")
                    temp7=f"/lib/"+temp6
                    temp8=temp6.replace(".dll","")
                    path=os.getcwd()
                    t="""
from ctypes import *
if sys.platform == 'win32':


    cdll.LoadLibrary(r\"{..}\")
    {--} = WinDLL(r\"{..}\")
else:

    {--} = cdll.LoadLibrary(r\"{..}\")
                        """
                    if hotrun:
                        temp9=f"{path}/{outloca}lib/{temp6}".replace("/","\\")
                        t=t.replace("{--}",temp8).replace("{..}",temp9)
                        script=script.replace("#$",f"#{temp7}---\ntemp=os.path.dirname(os.path.realpath(\"Zarus.py\"))\nprint(temp)\n{t}\n#$")
                    else:
                        temp9=f"{path}/{outloca}lib/{temp6}".replace("/","\\")
                        t=t.replace("{--}",temp8).replace("{..}",temp7)
                        script=script.replace("#$",f"#{temp7}---\n\ntemp=os.path.dirname(os.path.realpath(\"Zarus.py\"))\nprint(temp)\n{t}\n#$")
                except Exception as err:
                    print(err)
                    time.sleep(5)




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
            strings=[]
            if "/" in outloca:
                outloca+="/"
            elif "\\" in outloca:
                outloca+="\\"
            q=script.split("\n")

            for i in range(0,len(q)):
                if "~~" in q[i]:
                    b=""
                    a=q[i].split("~~")
                    a=a[1]
                    a=a.split("~")
                    a=a[0].replace("@@","")
                    for i in range(0,len(strings)):
                        if int(strings[i][0])==a:
                            q[i].replace(f"@@{a}@@",strings[i][1])
            g=""
            for i in range(0,len(q)):
                g+=q[i]+"\n"
            script=g

            with open(f"{outloca}ZarusScript.py","w") as f:

                f.write(script.replace("~~","\"").replace("~","\""))
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
            for i in range(0,len(zigs)):
                src_path = f"interpreter/lib/{zigs[i]}"
                dst_path = f"{outloca}lib/{zigs[i]}"
                shutil.copy(src_path, dst_path)
                print(Fore.GREEN)
                print(f"Success writing {zigs[i]}")
                print(Fore.RESET)
            if hotrun:
                print(Fore.GREEN+"Starting Zarus Script")
                path=os.path.abspath("ZarusMain.py").replace("ZarusMain.py","")
                dir=outloca.replace("\\\\","\\")
                print(f"{path}\\{dir}Run.py")
                print(Fore.RESET)
                os.system(f"{path}\\{dir}Run.py")

        elif type=="ZarusLibrary":

            print(Fore.GREEN)
            print("Attempting to compile into ZarusLibrary")
            print(Fore.RESET)

            with open(infile,"r") as f:



                script=f.read()
                temp9=script.split("\n")
                for i in range(0,len(temp9)):
                    if "~~" in temp9[i]:
                        b=""
                        a=temp9[i].split("~~")
                        a=a[1]
                        a=a.split("~")
                        strings.append([stringsa,a[0]])
                        temp9[i].replace(f"~~{a[0]}~",f"~~@@{stringsa}@@~")
                        stringsa+=1
                script2=""
                for i in range(0,len(temp9)):
                    script2+=temp9[i]+"\n"
                script=script.replace("--","#").replace(";;","Main.").replace(";z;","Zarus.").replace(";ztst;","Zarus.Terminal.StringTypes.").replace(";zt;","Zarus.Terminal.").replace(";s;","System.").replace(";m;","Misc.").replace("!@","")
            if libraryname==None:
                name=input("Library Name >> ")
            else:
                name=libraryname

            for i in range(0,len(localprivates)):
                script=script.replace(localprivates[i].split("=")[0],f"Private{name}."+localprivates[i].split("=")[0])

            temp9=script.split("\n")


            for i in range(0,len(temp9)):
                if "::" in temp9[i]:
                    if temp9[i] in keeps:
                        pass
                    else:
                        temp9[i]="\n"
            script=""

            for i in range(0,len(temp9)):
                script+=(temp9[i]+"\n")
            for i in range(0,len(mv)):
                r=mv[i]
                print(script2)
                script2=script2.replace(r[0],r[1])
                print(script2)
            with open("interpreter/data/compilerlib.zar","r") as x:
                scriptb=x.read()
            scriptb=scriptb.replace("{!!}",name)
            script=scriptb+script
            print(Fore.GREEN)
            print("Success reading script")
            print(Fore.RESET)
            for i in range(0,len(dlls)):
                script=script.replace("#@@",f"#@.net {dlls[i]}\n#@@")
            for i in range(0,len(zigs)):
                script=script.replace("#@@",f"#@.zig {zigs[i]}\n#@@")
            script=script.replace("#@@",ex+"\n#@@")
            print(Fore.GREEN)
            print("Success including files and librarys")
            print(Fore.RESET)

            for i in range(0,len(localprivates)):
                script=script.replace("#LP",localprivates[i])+"\n        "
            script2l=script.split("\n")

            script=script.replace("EntryPoint:",("class "+name+":"))
            q=script.split("\n")

            for i in range(0,len(q)):
                if "~~" in q[i]:
                    b=""
                    a=q[i].split("~~")
                    a=a[1]
                    a=a.split("~")
                    a=a[0].replace("@@","")
                    for i in range(0,len(strings)):
                        if int(strings[i][0])==a:
                            q[i].replace(f"@@{a}@@",strings[i][1])
            g=""
            for i in range(0,len(q)):
                g+=q[i]+"\n"
            script=g
            with open(f"{outloca}{name}.zar","w") as f:
                f.write(script)
            print(Fore.GREEN)
            print(f"Success writing {name}.zar")
            print(Fore.RESET)
            if instalib:
                print(Fore.GREEN)
                print(f"Writing {name}.zar to lib")
                print(Fore.RESET)
                shutil.copy((outloca+name+".zar").replace("\\\\","\\"), f"interpreter/lib/{name}.zar")





    except Exception as err:
        print(Fore.RED+"Cant open or find file/folder")
        print(Fore.RESET)
        print(err)
        time.sleep(10)
        quit()


if option=="pyexe":
    try:
        CompileExe()
    except Exception as err:
        print(err)
        time.sleep(5)
else:
    print(Fore.RED+"Invalid option")
    print(Fore.RESET)
while True:
    print("Type c to close")
    e=input(" >> ")
    if e=="c":
        break
