import tkinter as tk

root = tk.Tk()
root.geometry("555x330")
root.title("Safelock")
root.resizable(False, False)
root.anchor('center')

password = '1111'
passtry = ''
open = False
doorOpen = False

backDef = tk.PhotoImage(file='Safe.png')
backUnl = tk.PhotoImage(file='SafeUnl.png')
backOp = tk.PhotoImage(file='SafeOp.png')

canvas = tk.Canvas(root, width = 600, height = 360)
canvas.pack()

#region Digits Funcs
def d1Pressed(event):
    global passtry
    passtry += '1'
def d2Pressed(event):
    global passtry
    passtry += '2'
def d3Pressed(event):
    global passtry
    passtry += '3'
def d4Pressed(event):
    global passtry
    passtry += '4'
def d5Pressed(event):
    global passtry
    passtry += '5'
def d6Pressed(event):
    global passtry
    passtry += '6'
def d7Pressed(event):
    global passtry
    passtry += '7'
def d8Pressed(event):
    global passtry
    passtry += '8'
def d9Pressed(event):
    global passtry
    passtry += '9'
def d0Pressed(event):
    global passtry
    passtry += '0'
#endregion


def tryPass(event):
    global open
    global passtry
    global password

    if passtry == password:
        open = True
        UpdateVisual(backUnl)
    else:
        open = False

    passtry = ''


def changePass(event):
    global password
    global passtry

    if doorOpen:
        password = passtry
        print('New password: ', password)
    else:
        print('Vall closed')

def openDoor(event):
    global doorOpen
    if not(open): return

    doorOpen = True
    UpdateVisual(backOp)
    print('Door opened')


def closeDoor(event):
    global passtry
    global doorOpen
    global open
    if not(doorOpen): return

    print('Door closed')
    doorOpen = False
    open = False
    UpdateVisual(backDef)
    passtry = ''


def UpdateVisual(bIm):
    canvas.delete('all')
    canvas.create_image(0, 0, anchor='nw', image=bIm)
    #region Buttons Place
    b1 = tk.PhotoImage(file='bd.png')
    bi1 = canvas.create_image(30, 50, image=b1, anchor='nw')
    canvas.tag_bind(bi1, "<Button-1>", d1Pressed)

    b2 = tk.PhotoImage(file='bd.png')
    bi2 = canvas.create_image(90, 50, image=b2, anchor='nw')
    canvas.tag_bind(bi2, "<Button-1>", d2Pressed)

    b3 = tk.PhotoImage(file='bd.png')
    bi3 = canvas.create_image(150, 50, image=b3, anchor='nw')
    canvas.tag_bind(bi3, "<Button-1>", d3Pressed)

    b4 = tk.PhotoImage(file='bd.png')
    bi4 = canvas.create_image(30, 110, image=b4, anchor='nw')
    canvas.tag_bind(bi4, "<Button-1>", d4Pressed)

    b5 = tk.PhotoImage(file='bd.png')
    bi5 = canvas.create_image(90, 110, image=b5, anchor='nw')
    canvas.tag_bind(bi5, "<Button-1>", d5Pressed)

    b6 = tk.PhotoImage(file='bd.png')
    bi6 = canvas.create_image(150, 110, image=b6, anchor='nw')
    canvas.tag_bind(bi6, "<Button-1>", d6Pressed)

    b7 = tk.PhotoImage(file='bd.png')
    bi7 = canvas.create_image(30, 170, image=b7, anchor='nw')
    canvas.tag_bind(bi7, "<Button-1>", d7Pressed)

    b8 = tk.PhotoImage(file='bd.png')
    bi8 = canvas.create_image(90, 170, image=b8, anchor='nw')
    canvas.tag_bind(bi8, "<Button-1>", d8Pressed)

    b9 = tk.PhotoImage(file='bd.png')
    bi9 = canvas.create_image(150, 170, image=b9, anchor='nw')
    canvas.tag_bind(bi9, "<Button-1>", d9Pressed)

    b0 = tk.PhotoImage(file='bd.png')
    bi0 = canvas.create_image(30, 230, image=b0, anchor='nw')
    canvas.tag_bind(bi0, "<Button-1>", d0Pressed)

    bt = tk.PhotoImage(file='bd.png')
    bit = canvas.create_image(90, 230, image=bt, anchor='nw')
    canvas.tag_bind(bit, "<Button-1>", tryPass)

    bc = tk.PhotoImage(file='bd.png')
    bic = canvas.create_image(150, 230, image=bc, anchor='nw')
    canvas.tag_bind(bic, "<Button-1>", changePass)

    bOp = tk.PhotoImage(file='bOp.png')
    bdOp = canvas.create_image(210, 50, image=bOp, anchor='nw')
    canvas.tag_bind(bdOp, "<Button-1>", openDoor)

    bCl = tk.PhotoImage(file='bCl.png')
    bdCl = canvas.create_image(430, 50, image=bCl, anchor='nw')
    canvas.tag_bind(bdCl, "<Button-1>", closeDoor)
    #endregion


UpdateVisual(backDef)
root.mainloop()