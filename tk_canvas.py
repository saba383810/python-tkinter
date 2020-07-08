import tkinter as tk
root = tk.Tk()


var1 = tk.StringVar()


def blueBtn():
    cv.create_oval(50,10,100,60,fill='blue')
    cv.create_oval(100,10,150,60,fill='black')
    cv.create_oval(150,10,200,60,fill='black')

def yellowBtn():
    cv.create_oval(50,10,100,60,fill='black')
    cv.create_oval(100,10,150,60,fill='yellow')
    cv.create_oval(150,10,200,60,fill='black')

def redBtn():
    cv.create_oval(50,10,100,60,fill='black')
    cv.create_oval(100,10,150,60,fill='black')
    cv.create_oval(150,10,200,60,fill='red')

    

cv = tk.Canvas( root, width = 250, height = 70 )
cv.pack()
cv.create_oval(50,10,100,60,fill='black')
cv.create_oval(100,10,150,60,fill='black')
cv.create_oval(150,10,200,60,fill='black')

btn1 = tk.Button(root, text='青', command=blueBtn)
btn1.pack()
btn2 = tk.Button(root, text='黄', command=yellowBtn)
btn2.pack()
btn3 = tk.Button(root, text='赤', command=redBtn)
btn3.pack()
root.mainloop()