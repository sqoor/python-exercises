from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import *

# # Q.1
root1 = Tk()
root1.title('Resister')
root1.geometry('300x150+50+50')

name = Label(root1, text="Name").place(x=20, y=20)
password = Label(root1, text="Password").place(x=20, y=40)
e1value = StringVar()
e2value = StringVar()
e1 = Entry(root1, textvariable=e1value).place(x=80, y=20)
e2 = Entry(root1, textvariable=e2value).place(x=80, y=40)


def Pressed():
    print('pressed the button', e1value.get(), e2value.get())
    if e1value.get() == 'Orange' and e2value.get() == '1234':
        root1.destroy()
    else:
        messagebox.showinfo('Error', 'You have entered incorrect credentials')


button = Button(root1, text="Resister", command=Pressed).place(x=30, y=120)

root1.mainloop()


# Q.2
root2 = Tk()
root2.title('Parent')


# root.geometry('300x150+50+50')

def Pressed():
    dialog_title = 'Title'
    dialog_text = 'This is a message'
    messagebox.showinfo(dialog_title, dialog_text)


def open_child1():
    c = Toplevel(root2)
    c.title('Child window 1')
    # c.geometry('200x160+230+130')
    # Label(c, text="Child window 1").grid()

    name = Label(c, text="Emp Number").place(x=20, y=20)
    password = Label(c, text="Emp Name").place(x=20, y=40)
    e1value = StringVar()
    e2value = StringVar()
    e1 = Entry(c, textvariable=e1value).place(x=80, y=20)
    e2 = Entry(c, textvariable=e2value).place(x=80, y=40)

    button = Button(c, text="Exit", command=c.destroy).place(x=30, y=120)


def open_child2():
    c = Toplevel(root2)
    c.title('Child window 1')
    # c.geometry('200x160+230+130')

    lst = Listbox(c)

    for num in range(1, 20):
        lst.insert(num, f'The count is {num}')

    lst.pack()


msg = Button(root2, text='Message', command=Pressed).pack(pady=40, padx=40)
window1 = Button(root2, text='Open child window 1', command=open_child1).pack(pady=40, padx=40)
window2 = Button(root2, text='Open child window 2', command=open_child2).pack(pady=40, padx=40)
root2.mainloop()


# Q.3
root3 = Tk()
root3.title('Parent')


def selectColor():
    color = askcolor()
    root3.configure(background=color[1])


msg = Button(root3, text='Select Color', command=selectColor).pack(pady=40, padx=40)
root3.mainloop()
