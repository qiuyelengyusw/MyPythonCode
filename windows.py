import tkinter
import tkinter.messagebox

nW = tkinter.Tk()
nW.title("Python窗体")
nW.geometry("600x600")


def hello():
    tkinter.messagebox.showinfo("hello", tl.get())
    la["fg"] = "red"


bl = tkinter.Button(nW, text="确认", command=hello)
bl.grid(row=0, column=1, padx=10)
la = tkinter.Label(nW, text="Hello Python", font=16, fg="blue")
la.grid(row=2, column=2, padx=10)
tl = tkinter.Entry(nW)
tl.grid(row=0, column=0)
nW.mainloop()
