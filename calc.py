from tkinter import *

def select(event):
    global scvalue
    text=event.widget.cget("text")
    
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(scvalue.get())
        scvalue.set(value)
        screen.update()        
        
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
    pass
root=Tk()


root.title('calculator')
root.geometry("800x800")
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font=("lucidia",40))
screen.pack(fill=Y,ipadx=5,pady=22,padx=17)
f=Frame(root,bg="black")
b=Button(f,text='9',padx=12,pady=13,font=('ariel',40))
b.pack(side="left",padx=16,pady=12)
b.bind("<Button-1>",select)

b=Button(f,text='8',padx=12,pady=13,font=('ariel',40))
b.pack(side="left",padx=16,pady=12)
b.bind("<Button-1>",select)

b=Button(f,text='7',padx=12,pady=13,font=('ariel',40))
b.pack(side="left",padx=16,pady=12)
b.bind("<Button-1>",select)

f.pack()

f=Frame(root,bg="black")
b=Button(f,text='6',padx=12,pady=13,font=('ariel',40))
b.pack(side="left",padx=16,pady=12)
b.bind("<Button-1>",select)

b=Button(f,text='5',padx=12,pady=13,font=('ariel',40))
b.pack(side="left",padx=16,pady=12)
b.bind("<Button-1>",select)

b=Button(f,text="4",padx=12,pady=13,font=('ariel',40))
b.pack(side="left",padx=16,pady=12)
b.bind("<Button-1>",select)

f.pack()

f=Frame(root,bg="black")
b=Button(f,text='3',padx=12,pady=13,font=('ariel',40))
b.pack(side="left",padx=16,pady=12)
b.bind("<Button-1>",select)

b=Button(f,text='2',padx=12,pady=13,font=('ariel',40))
b.pack(side="left",padx=16,pady=12)
b.bind("<Button-1>",select)

b=Button(f,text='1',padx=12,pady=13,font=('ariel',40))
b.pack(side="left",padx=16,pady=12)
b.bind("<Button-1>",select)

f.pack()

f=Frame(root,bg="black")
b=Button(f,text='0',padx=12,pady=13,font=('ariel',40))
b.pack(side="left",padx=16,pady=12)
b.bind("<Button-1>",select)

b=Button(f,text='-',padx=12,pady=13,font=('ariel',40))
b.pack(side="left",padx=16,pady=12)
b.bind("<Button-1>",select)

b=Button(f,text='+',padx=12,pady=13,font=('ariel',40))
b.pack(side="left",padx=16,pady=12)
b.bind("<Button-1>",select)

f.pack()

f=Frame(root,bg="black")
b=Button(f,text='/',padx=12,pady=13,font=('ariel',40))
b.pack(side="left",padx=16,pady=12)
b.bind("<Button-1>",select)

b=Button(f,text='%',padx=12,pady=13,font=('ariel',40))
b.pack(side="left",padx=16,pady=12)
b.bind("<Button-1>",select)

b=Button(f,text='=',padx=12,pady=13,font=('ariel',40))
b.pack(side="left",padx=16,pady=12)
b.bind("<Button-1>",select)

f.pack()

f=Frame(root,bg="black")
b=Button(f,text='*',padx=12,pady=13,font=('ariel',40))
b.pack(side="left",padx=16,pady=12)
b.bind("<Button-1>",select)

b=Button(f,text='C',padx=12,pady=13,font=('ariel',40))
b.pack(side="left",padx=16,pady=12)

b=Button(f,text='^',padx=12,pady=13,font=('ariel',40))
b.pack(side="left",padx=16,pady=12)

f.pack()
root.mainloop()