
import tkinter as tk
root = tk.Tk()

root.title("計算機")

expression = tk.StringVar()

def clear():
    expression.set("")

def digit(number):
    def func():
        expression.set(expression.get() + str(number))
    return func

def op(label):
    def func():
        expression.set(expression.get() + label)
    return func
#=の機能
def equal():
    try:
        expression.set(eval(expression.get()))
    except SyntaxError:
        expression.set("SyntaxError")
    except ZeroDivisionError:
        expression.set("ZeroDivisionError")
    except NameError:
        expression.set("NameError")

#数字ボタン配置
for i in range(1,4):
    for j in range(1,4):
        tk.Button(root,text=i*j,command=digit(i*j) ,width=4,height=3).grid(column=i, row=j)
tk.Button(root,text=0,command=digit(0) ,width=8,height=3).grid(column=1,row=4,columnspan=2)
#計算記号配置
tk.Button(root,text="+",command=op("+") ,width=4,height=3).grid(column=4, row=1)
tk.Button(root,text="-",command=op("-") ,width=4,height=3).grid(column=4, row=2)
tk.Button(root,text="*",command=op("*") ,width=4,height=3).grid(column=4, row=3)
tk.Button(root,text="/",command=op("/") ,width=4,height=3).grid(column=4, row=4)
tk.Button(root,text="C",command=clear ,width=4,height=3).grid(column=4, row=0)
tk.Button(root,text="=",command=equal ,width=4,height=3).grid(column=3, row=4)

#テキスト表示&デザイン
bg = tk.Label(root,bg="#000000",height=3)
bg.grid(row=0, column=0, columnspan=4, sticky="EW")
e = tk.Label(root, textvariable=expression,anchor=tk.E, height=2)
e.grid(row=0, column=0, columnspan=4, sticky="EW")
root.mainloop()