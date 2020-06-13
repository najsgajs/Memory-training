from tkinter import *
from random import randint
from random import seed

seed()


def ilosc(event):
    
    c=int(int(e1.get())/10)
    a=0
    e=''
    for x in range(int(e1.get())):
       e=e+str(randint(0,9))
       a+=1
       if a ==10:
           e=e+' '
           a=0
    a=e.split()
    entry=[]
    for x in frame.winfo_children():
        x.destroy()
    d = Label(frame)
    for x in range(c):
        Label(frame, text=' '*12+a[x]+12*' ',font=("Helvetica", 25)).grid(row=x+2,column=20,sticky=E)
      
    def klik():
        ko= Label(frame)
        ko.after(12)
        for x in frame.winfo_children():
            x.destroy()
        for x in range(c):
            Label(frame, text='Rząd %s '%x,font=("Helvetica", 15)).grid(row=x,column=0)
            entry.append(Entry(frame,font=("Helvetica", 15),width=15))
            entry[x].grid(row=x,column=1)
        def spra():
            
            for x in range(c):
                h=entry[x].get().strip()
                k=0
                
                for f in h:
                    if str(f)==a[x][k].strip():
                        Label(frame, text=str(a[x][k].strip()),font=("Helvetica", 15),fg='green').grid(row=x,column=3+k)
                        k+=1
                    else:
                        Label(frame, text=str(a[x][k].strip()),font=("Helvetica", 15),fg='red').grid(row=x,column=3+k)
                        k+=1
                     
        but = Button(frame, text="Sprawdz",command=spra)
        but.grid(row=c+1,column =0)
    but = Button(frame, text='Klik', command=klik)
    but.grid(row = c+2, column=20)
    
root= Tk()
root.geometry('600x650')
#background_image=PhotoImage(file='martixd.gif')
#background_label = Label(root, image=background_image)
#background_label.photo=background_label
#background_label.place(x=0, y=0, relwidth=1, relheight=1)
frame = Frame(root)
frame.grid(row=0,column=0,rowspan=40,columnspan=20)
l2=Label(frame,text='Pamietaj by kliknąć przycisk zanim zaczniesz !!!')
l2.grid(row=0,column=0)
l=Label(frame, text ="Wprowadz ilość liczb: ")
l.grid(row=1,column=0)
e1 = Entry(frame)
e1.grid(row=1,column=1)

e1.bind("<Return>", ilosc)



root.mainloop()
