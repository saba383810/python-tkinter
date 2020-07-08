import tkinter as tk
root = tk.Tk()
def func(i):
    def x():
        print(i)
    return x

for i in range(3):
    tk.Button(root, text=i, command = func(i)).pack()
root.mainloop()