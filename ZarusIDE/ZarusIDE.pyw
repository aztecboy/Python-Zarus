import PySimpleGUI as sg
import threading,time,ctypes,os,random,keyboard
class vars:
    loadingdone=False
sg.theme("black")

idelayout=[
[sg.Button("Compile",key="cd")],
[sg.Multiline(key="s",size=(200,200),font=("Arial",15))],
]
newprojectlayout=[
[sg.T("New Project",font=("Arial",15))],
[sg.FileBrowse("Compile Script",key="ccs",enable_events=True)]
]
loadinglayout=[
[sg.Image("LoadingImage.png",size=(700,400))],
[sg.ProgressBar(size=(64,10),max_value=64,key="lb")],

]

def misc1(win):
    win["s"].print("#",text_color="black")
def misc2(win):
    win["s"].print("-include .net exampledll;")
    win["s"].print("From ExampleNameSpace import Exampleclass;")

    print(values)
win=sg.Window("ZarusIDE",loadinglayout,icon="Icon.ico",finalize=True)
def mainloop1():
    for i in range(65):
        win["lb"].update(i)
        #time.sleep(0.1)
    vars.loadingdone=True
threading.Thread(target=mainloop1).start()
while True:

    event, values = win.read(timeout=100)

    if event == sg.WINDOW_CLOSED:
        break
    if vars.loadingdone==True:
        win.close()
        break
win=sg.Window("ZarusIDE",newprojectlayout,icon="Icon.ico",finalize=True,size=(200,250))
while True:
    event, values = win.read(timeout=100)
    if event == sg.WINDOW_CLOSED:
        break
    elif event=="ccs":
        
