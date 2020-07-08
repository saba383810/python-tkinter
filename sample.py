from tkinter import *

#画面表示
root = Tk()

#ウィンドウの名前を設定
root.title("calculator")

expression = StringVar()

#Cの機能
def clear():
    expression.set("")

#ACの機能
def all_clear():
    expression.set("")

#数字ボタン
def digit(number):
    def func():
        expression.set(expression.get() + str(number))
    return func

#演算ボタン
def op(label):
    def func():
        expression.set(expression.get() + label)
    return func

#=の機能
def calculate():
    try:
        expression.set(eval(expression.get()))
    except SyntaxError:
        expression.set("SyntaxError")
    except ZeroDivisionError:
        expression.set("ZeroDivisionError")
    except NameError:
        expression.set("NameError")

buttons = (
    (("C", clear   ), ("AC", all_clear), ("%", op("%") ), ("+", op("+"))),
    (("7", digit(7)), ("8",  digit(8) ), ("9", digit(9)), ("/", op("/"))),
    (("4", digit(4)), ("5",  digit(5) ), ("6", digit(6)), ("*", op("*"))),
    (("1", digit(1)), ("2",  digit(2) ), ("3", digit(3)), ("-", op("-"))),
    (("0", digit(1)), (None, None     ), ('.', op('.') ), ("=", calculate)),
)

#表示画面
e = Label(root, textvariable=expression, fg="#ffffff", bg="#000000", anchor=E, height=2)
e.grid(row=0, column=0, columnspan=4, sticky="EW")

for row, btns in enumerate(buttons, 1):
    for col, (label, func) in enumerate(btns):
        if label:
            b = Button(root, text=label, command=func, width=5, height=2)
            b.grid(row=row, column=col)

#文章で言うところの句読点みたいなものなので忘れずに。
root.mainloop()