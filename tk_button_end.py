import tkinter as tk

root = tk.Tk()

def func():
    print("プログラムを終了します")
    root.quit()

label = tk.Label(root, text='サンプル')

label.pack()

button = tk.Button(root, text='終了', command=func)

button.pack()

root.mainloop()