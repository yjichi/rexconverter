#!/usr/bin/python3
import os, sys, glob, platform
import tkinter as tk
from tkinter import filedialog, ttk

class Application(tk.Frame):

    global masterfont, Mfamily, iDir
    masterfont = 12
    pf = platform.system()
    if pf == "Windows":
        Mfamily = "Times"
    elif pf == "Darwin":
        Mfamily = "Helvetica"
    elif pf == "Linux":
        Mfamily = "Ubuntu"
   
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.initUI()
        self.createMenu()


    def initUI(self):
        self.master.geometry("600x150")
        self.master.resizable(width=False,height=False)
        self.master.title("REX converter (alpha)")
	
    def createMenu(self):
        menu1 = tk.LabelFrame(self.master,text="Convert specified files",font=(Mfamily,masterfont,"bold"))
        menu1.configure(relief="ridge",padx=5,pady=5)
        menu1.columnconfigure(0,weight=1)
        menu1.columnconfigure(1,weight=1)
        menu1.columnconfigure(2,weight=1)
        menu1.columnconfigure(3,weight=1)
        menu1.columnconfigure(4,weight=1)
        menu1.pack(side="top",fill="x",expand=0)
        
        btn_ex3toEMu = tk.Button(menu1,text="\u03bct",font=(Mfamily,masterfont),width=7,command=self.ex3toEMu)
        btn_ex3toEMu.grid(row=0,column=0)
        btn_xantoENorm = tk.Button(menu1,text="Norm. \u03bct",font=(Mfamily,masterfont),width=7,command=self.xantoENorm)
        btn_xantoENorm.grid(row=0,column=1)
        btn_xantoPF = tk.Button(menu1,text="Patt. Fit",font=(Mfamily,masterfont),width=7,command=self.xantoPF)
        btn_xantoPF.grid(row=0,column=2)
        btn_rextokChi = tk.Button(menu1,text="\u03c7(k)",font=(Mfamily,masterfont),width=7,command=self.rextokChi)
        btn_rextokChi.grid(row=1,column=0)
        btn_rextoknChi = tk.Button(menu1,text="k^n\u03c7(k)",font=(Mfamily,masterfont),width=7,command=self.rextoknChi)
        btn_rextoknChi.grid(row=1,column=1)
        btn_rextorFT = tk.Button(menu1,text="FT",font=(Mfamily,masterfont),width=7,command=self.rextorFT)
        btn_rextorFT.grid(row=1,column=2)
        btn_rextokFit = tk.Button(menu1,text="Curve Fit",font=(Mfamily,masterfont),width=7,command=self.rextokFit)
        btn_rextokFit.grid(row=1,column=3)
        btn_rextorFT = tk.Button(menu1,text="AFT",font=(Mfamily,masterfont),width=7,command=self.rextoAFT)
        btn_rextorFT.grid(row=1,column=4)

        menu_sys = tk.Frame(self.master)
        menu_sys.pack(side="top")
        q_btn = tk.Button(menu_sys,text="Quit",font=(Mfamily,masterfont),width=7,command=self.master.destroy)
        q_btn.grid(row=0,column=0)
        
    def ex3toEMu(self):
        files = filedialog.askopenfilenames(filetype=[("ex3 file",".ex3"),("xan file",".xan"),("rex file",".rex")],initialdir="./",title="Open file")
        for file in files:
            filename = os.path.splitext(file)[0]
            with open(file,"r") as input ,open(str(filename) + "_EMu.txt","w",encoding="utf-8") as out:
                copy = False
                for line in input:
                    if line.strip() == "[EX_BEGIN]":
                        copy = True
                    elif line.strip() == "[EX_END]":
                        copy = False
                    elif copy:
                        out.write(line)

    def xantoENorm(self):
        files = filedialog.askopenfilenames(filetype=[("xan file",".xan")],initialdir="./",title="Open file")
        for file in files:
            filename = os.path.splitext(file)[0]
            with open(file,"r") as input ,open(str(filename) + "_Norm.txt","w",encoding="utf-8") as out:
                copy = False
                for line in input:
                    if line.strip() == "[BG_BEGIN]":
                        copy = True
                    elif line.strip() == "[BG_END]":
                        copy = False
                    elif copy:
                        out.write(line)

    def xantoPF(self):
        files = filedialog.askopenfilenames(filetype=[("xan file",".xan")],initialdir="./",title="Open file")
        for file in files:
            filename = os.path.splitext(file)[0]
            with open(file,"r") as input ,open(str(filename) + "_PatF.txt","w",encoding="utf-8") as out:
                copy = False
                for line in input:
                    if line.strip() == "[PF_BEGIN]":
                        copy = True
                    elif line.strip() == "[PF_END]":
                        copy = False
                    elif copy:
                        out.write(line)

    def rextokChi(self):
        files = filedialog.askopenfilenames(filetype=[("rex file",".rex")],initialdir="./",title="Open file")
        for file in files:
            filename = os.path.splitext(file)[0]
            with open(file,"r") as input ,open(str(filename) + "_kChi.txt","w",encoding="utf-8") as out:
                copy = False
                for line in input:
                    if line.strip() == "[XI_BEGIN]":
                        copy = True
                    elif line.strip() == "[XI_END]":
                        copy = False
                    elif copy:
                        out.write(line)

    def rextoknChi(self):
        files = filedialog.askopenfilenames(filetype=[("rex file",".rex")],initialdir="./",title="Open file")
        for file in files:
            filename = os.path.splitext(file)[0]
            with open(file,"r") as input ,open(str(filename) + "_knChi.txt","w",encoding="utf-8") as out:
                copy = False
                for line in input:
                    if line.strip() == "[ED_BEGIN]":
                        copy = True
                    elif line.strip() == "[ED_END]":
                        copy = False
                    elif copy:
                        out.write(line)

    def rextorFT(self):
        files = filedialog.askopenfilenames(filetype=[("rex file",".rex")],initialdir="./",title="Open file")
        for file in files:
            filename = os.path.splitext(file)[0]
            with open(file,"r") as input ,open(str(filename) + "_FT.txt","w",encoding="utf-8") as out:
                copy = False
                for line in input:
                    if line.strip() == "[FT_BEGIN]":
                        copy = True
                    elif line.strip() == "[FT_END]":
                        copy = False
                    elif copy:
                        out.write(line)

    def rextokFit(self):
        files = filedialog.askopenfilenames(filetype=[("rex file",".rex")],initialdir="./",title="Open file")
        for file in files:
            filename = os.path.splitext(file)[0]
            with open(file,"r") as input ,open(str(filename) + "_kCF.txt","w",encoding="utf-8") as out:
                copy = False
                for line in input:
                    if line.strip() == "[CF_BEGIN]":
                        copy = True
                    elif line.strip() == "[CF_END]":
                        copy = False
                    elif copy:
                        out.write(line)

    def rextoAFT(self):
        files = filedialog.askopenfilenames(filetype=[("rex file",".rex")],initialdir="./",title="Open file")
        for file in files:
            filename = os.path.splitext(file)[0]
            with open(file,"r") as input ,open(str(filename) + "_AFT.txt","w",encoding="utf-8") as out:
                copy = False
                for line in input:
                    if line.strip() == "[AFT_BEGIN]":
                        copy = True
                    elif line.strip() == "[AFT_END]":
                        copy = False
                    elif copy:
                        out.write(line)

def main():
    mainwindow = tk.Tk()
    app = Application(master=mainwindow)
    app.mainloop()

if __name__ == '__main__':
    main()