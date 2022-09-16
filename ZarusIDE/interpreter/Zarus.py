import sys,clr,os,ctypes,threading,keyboard,time,pyfiglet,pip
from colorama import init,Fore,Back,Style
init(convert=True)
clr.AddReference("lib/ZarusBase")
clr.AddReference("lib/SystemNotifications")
from SystemNotifications import Main
from ZarusBase import SocketConnectionHandler
Notif=Main()
Socket=SocketConnectionHandler()

class Vars:
    Closed=False
    class TerminalVars:
        Contained=""
class SystemX:
    class SocketConnections:
        def BindRoute(a1,a2):
            Socket.BindAddressAndPort(a1,a2)
        class ServerSide:
            def ReceiveData(a1,a2):
                return Socket.RecieveDataServer(a1,a2)
            def AwaitConnection(a1):
                return Socket.WaitForConnection(a1)
            def BeginServer():
                return Socket.CreateServer()
            def StopServer(a1):
                return Socket.StopServer(a1)
            def GetClientAddress(a1):
                return Socket.GetClientAddress(a1)
            def CloseConnectionToClient(a1):
                return Socket.CloseConnectionToClient(a1)
        class ClientSide:
            def CloseConnection(a1):
                Socket.CloseConnectionToServer(a1)
            def Connect():
                return Socket.EstablishConnection()
            def SendData(a1,a2):
                Socket.SendDataClient(a1,a2)

    class Notifications:
        class Buttons:
            class ReturnButtons:
                Yes=6
                No=7
            YesNo=Notif.GetButtons("YesNo")
        def InfoMessageWithButtons(a1,a2,a3):
            return Notif.ShowWithButtons(a1,a2,a3);
        def InfoMessage(a1,a2):
            return Notif.Show(a1,a2)
class Zarus:
    def EndOfScript():
        Vars.Closed=True
    class PythonModuleManipulater:
        def Install(a1):
            pip.main(["install",a1])
    class ErrorCodes:
        DoesNotExist="$$556633944110102"
    class Shell:
        def ToShell(a1):
            os.system(a1)
    class InputManipluate:
        def PressRelease(key,delay):
            keyboard.press(key)
            time.sleep(delay)
            keyboard.release(key)
    class Input:
        Current=None
        def InputInitThread():
            while True:
                Zarus.Input.Current=keyboard.read_key()

        def Init():
            threading.Thread(target=Zarus.Input.InputInitThread).start()
        def Pressed(key):
            if keyboard.is_pressed(key):
                return True
            else:
                return False
        def TillPressed(key):
            while True:
                if keyboard.is_pressed(key):
                    break

        def CurrentNil():
            Zarus.Input.Current=None
        def TillReleased(key):
            while True:
                if keyboard.is_pressed(key):
                    pass
                else:
                    break

    class Terminal:
        Font=""
        class ASCIIArt:
            def Banner3D(a1):
                return pyfiglet.figlet_format(a1,"banner3-D")
            def Block3D(a1):
                return pyfiglet.figlet_format(a1,"3-D")
            def Alligator(a1):
                return pyfiglet.figlet_format(a1,"alligator")
            def Alligator2(a1):
                return pyfiglet.figlet_format(a1,"alligator2")
            def Banner3(a1):
                return pyfiglet.figlet_format(a1,"banner3")
            def Banner4(a1):
                return pyfiglet.figlet_format(a1,"banner4")
            def Colossal(a1):
                return pyfiglet.figlet_format(a1,"colossal")
            def CatWalk(a1):
                return pyfiglet.figlet_format(a1,"catwalk")
            def Contrast(a1):
                return pyfiglet.figlet_format(a1,"contrast")
            def Cosmic(a1):
                return pyfiglet.figlet_format(a1,"cosmic")
            def Cosmike(a1):
                return pyfiglet.figlet_format(a1,"cosmike")
            def Hollywood(a1):
                return pyfiglet.figlet_format(a1,"hollywood")
            def Poison(a1):
                return pyfiglet.figlet_format(a1,"poison")
        class Colorama:
            Foreground=Fore
            Background=Back

        def UpdateWindow(a1):
            os.system(f"title {a1}")
        def Open():
            ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 1 )
        def Close():
             ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
        def Inside():
            return Vars.TerminalVars.Contained
        def Out(text):
            Vars.TerminalVars.Contained+=(Zarus.Terminal.Font+str(text))
            sys.stdout.write(Zarus.Terminal.Font+str(text))
