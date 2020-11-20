from tkinter import*
import time
root=Tk()
root.title("DIGITAL CLOCK")
root.geometry("1350x700+0+0")
root.config(bg="#081923")

def clock():
    h=str(time.strftime("%H"))
    m=str(time.strftime("%M"))
    s=str(time.strftime("%S"))
    #print(h,m,s)
    if int(h)>12:
        h=str((int(h)-12))
    if int(h)>=12 and int(m)>0:
        lbl_noon.config(text="PM")


    lbl_hr.config(text=h)
    lbl_min.config(text=m)
    lbl_sec.config(text=s)

    lbl_hr.after(200,clock)
    
lbl_hr=Label(root,text="12",font=("times new romam",50,"bold"),bg="white",fg="#0875B7")
lbl_hr.place(x=250,y=200,width=200,height=200)

lbl_hr2=Label(root,text="Hour",font=("EB Garamond",35,"bold"),bg="white",fg="#0875B7")
lbl_hr2.place(x=250,y=420,width=200,height=80)

lbl_min=Label(root,text="12",font=("times new romam",50,"bold"),bg="#f5c32f",fg="white")
lbl_min.place(x=450,y=200,width=200,height=200)

lbl_min2=Label(root,text="Min",font=("EB Garamond",35,"bold"),bg="#f5c32f",fg="white")
lbl_min2.place(x=450,y=420,width=200,height=80)

lbl_sec=Label(root,text="12",font=("times new romam",50,"bold"),bg="#ff0000",fg="white")
lbl_sec.place(x=650,y=200,width=200,height=200)

lbl_sec2=Label(root,text="Secs",font=("EB Garamond",35,"bold"),bg="#ff0000",fg="white")
lbl_sec2.place(x=650,y=420,width=200,height=80)

lbl_noon=Label(root,text="AM",font=("times new romam",50,"bold"),bg="#59ff00",fg="white")
lbl_noon.place(x=850,y=200,width=200,height=200)

lbl_noon2=Label(root,text="Noon",font=("EB Garamond",35,"bold"),bg="#59ff00",fg="white")
lbl_noon2.place(x=850,y=420,width=200,height=80)
clock()
root.mainloop()

