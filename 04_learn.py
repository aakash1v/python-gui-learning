import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')


# create a window 
window = tk.Tk()
window.title('Tkinter variables')

# tkinter variables
string_var = tk.StringVar()

#widgets
label = ttk.Label(master=window,text='label',textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window,textvariable=string_var)
entry.pack()

entry2= ttk.Entry(master=window,textvariable=string_var)
entry2.pack()

button =ttk.Button(master=window,text='button',command=button_func)
button.pack()

'''exercise
create 2 entry fields and 1 labels, they should all be connected via a StringVAr
set a start value of "test" '''

exercise_var = tk.StringVar(value = 'test')
ex_label= ttk.Label(master=window,text='test',textvariable=exercise_var)
ex_label.pack()
ex_entry1 = ttk.Entry(master=window,textvariable=exercise_var)
ex_entry1.pack()
ex_entry2 = ttk.Entry(master=window,textvariable=exercise_var)
ex_entry2.pack()

# run 
window.mainloop()
