import tkinter
import tkinter.messagebox

nW = tkinter.Tk()
nW.title("Python窗体")
nW.geometry("600x600")


def HelloWorld():
    tkinter.messagebox.showinfo("hello", tl.get())


bl = tkinter.Button(nW, text="按钮", command=HelloWorld)
bl.grid(row=2, column=8)
tl=tkinter.Entry(nW)
tl.grid(row=0,column=0)
nW.mainloop()