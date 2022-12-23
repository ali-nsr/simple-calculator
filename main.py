from tkinter import *
import tkinter.messagebox

# ===================== settings =====================
root = Tk()
root.title('Calculator')
root.geometry('400x200')
root.resizable(width=False, height=False)
color = 'gray'
root.config(bg=color)

# ===================== variables =====================
num_1 = StringVar()
num_2 = StringVar()
res_value = StringVar()
# ===================== frames =====================
top_first = Frame(root, width=400, height=50, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=50, bg=color)
top_forth.pack(side=TOP)


# ===================== functions =====================
def error_msg(msg):
    if msg == 'error':
        tkinter.messagebox.showerror('Error', 'Something Went Wrong')
    elif msg == 'division zero error':
        tkinter.messagebox.showerror('Division Error', 'Can Not Divide By 0')


def plus():
    try:
        value = float(num_1.get()) + float(num_2.get())
        res_value.set(value)
    except:
        error_msg('error')


def minus():
    try:
        value = float(num_1.get()) - float(num_2.get())
        res_value.set(value)
    except:
        error_msg('error')


def mul():
    try:
        value = float(num_1.get()) * float(num_2.get())
        res_value.set(value)
    except:
        error_msg('error')


def div():
    if num_2.get() == '0':
        error_msg('division zero error')
    elif num_2.get() != '0':
        try:
            value = float(num_1.get()) / float(num_2.get())
            res_value.set(value)
        except:
            error_msg('error')


# ===================== buttons =====================
btn_plus = Button(top_third, text='+', width=10, highlightbackground=color, command=lambda: plus())
btn_plus.pack(side=LEFT, padx=10, pady=10)

btn_minus = Button(top_third, text='-', width=10, highlightbackground=color, command=lambda: minus())
btn_minus.pack(side=LEFT, padx=10, pady=10)

btn_mul = Button(top_third, text='*', width=10, highlightbackground=color, command=lambda: mul())
btn_mul.pack(side=LEFT, padx=10, pady=10)

btn_div = Button(top_third, text='/', width=10, highlightbackground=color, command=lambda: div())
btn_div.pack(side=LEFT, padx=10, pady=10)
# ===================== entries and labels =====================
first_label_num = Label(top_first, text='Please Enter First Number 1 : ', bg=color)
first_label_num.pack(side=LEFT, padx=10, pady=10)

first_entry_num = Entry(top_first, highlightbackground=color, textvariable=num_1)
first_entry_num.pack(side=LEFT)

second_label_num = Label(top_second, text='Please Enter First Number 2 : ', bg=color)
second_label_num.pack(side=LEFT, padx=10, pady=10)

second_entry_num = Entry(top_second, highlightbackground=color, textvariable=num_2)
second_entry_num.pack(side=LEFT)

res_label = Label(top_forth, text='Result : ', bg=color)
res_label.pack(side=LEFT, padx=10, pady=10)

res_num = Entry(top_forth, highlightbackground=color, textvariable=res_value)
res_num.pack(side=LEFT)

root.mainloop()
