'''
Authors:
Date: July 30, 2020
ID Numbers: 
Purpose:

'''
from tkinter import*
from tkinter import messagebox
from tkinter import Tk, Label, PhotoImage
 


#Creating Login Window#


window=Tk()
window.title ("Pokeman Battle Login System")
window.resizable (False,False)
window['background'] = 'light blue'
headingLabel= Label(window,text="Pokeman Battle Login", font= "Cambria 15 bold", fg='red', bg= 'black').grid(row=0,column=(1),pady=10,padx=10,rowspan=1,sticky=E)



#Giving Function to Login Process#


def Login ():

    if window.username.get()=="" or window.password.get()=="":
        messagebox.showerror("Error","All fields are required")


    elif window.username.get()== "Group8" and window.password.get()== "12345":
        messagebox.showinfo("Information","Welcome Lets Begin !")


    else:
          
       messagebox.showerror("Error","Invalid Username or Password, Try Again")
   

#Creating Profile Image#

window.profilelogo=PhotoImage(file="Profile Icon2.png")
Label(window, bg = "#bd4b53", image=window.profilelogo).grid (row=1,column=1,pady=5,padx=5, rowspan=2, sticky=W)


#Defining Username & Password Variables#

window.username=StringVar()
window.password=StringVar()
entryusername= StringVar()
entrypassword= StringVar()


#Creating Username Entry Box#
Label(window,text="Username", bg= "black", fg= 'red', font = 'Cambria 10 bold').grid(row=20,column=0,padx=5,pady=10)
entryusername=Entry(window,width=25,textvariable=window.username)
entryusername.grid(row=20,column=1,sticky=W)

#Creating Password Entry Box#
Label(window,text="Password",bg= 'black', font= 'Cambria 10 bold', fg= 'red').grid(row=24,column=0)
entrypassword=Entry(window,width=25,textvariable=window.password)
entrypassword.grid(row=24,column=1,sticky=W)

    
#Creating Login Button#
buttonLogin=Button(text="Login",width=10,command = Login, bg="red", font= ' Cambria 12 bold').grid(row=25,column=0,padx=20,pady=30,columnspan=2)

mainloop()


#Creating RPS Application#

def doNothing():
    print("ok ok i wont...")


win=Tk()
win.geometry("350x250")
win.title("Pokemon Battle RPS Style")


menu = Menu(win)
win.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project...",command=doNothing)
subMenu.add_command(label="New...",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit...",command=doNothing)

editMenu=Menu(menu)
menu.add_cascade(label="Rules",menu=subMenu)
editMenu.add_command(label="New Game",command=doNothing)

subMenu = Menu(menu)
menu.add_cascade(label="Restart",menu=subMenu)
subMenu.add_command(label="Redo",command=doNothing)
subMenu.add_command(label="Edit",command=doNothing)

lblChoice = Label(win,text="Choice").grid(row=20,column=0)
v = StringVar(win,"1")

values={"Chartzard  1" : "1",
        "Blastoise  2" : "2",
        "Venusaur   3" : "3"}
for (text,value) in values.items():
    Radiobutton(win,text=text,variable=v,
                value = value).grid(padx=4,pady=20,column=0)

lblScore=Label(win,text="Score").grid(row=80,column=0)
lblHealth=Label(win,text="Health:").grid(row=100,column=0,pady=75)
btnButton=Button(win,text="Attack").grid(row=105,column=12,padx=400)
lblEnemy=Label(win,text="Enemy").grid(row=150,column=0,pady=90)


mainloop()


