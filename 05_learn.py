import tkinter as tk
from tkinter import ttk

# setup
window=tk.Tk()
window.title('buttons')
window.geometry('600x400')

# buttons 
def button_func():
    print('a basic button')

button_string = tk.StringVar(value='A button with string var')
button = ttk.Button(window,text='A simple button',command=button_func,textvariable=button_string)
button.pack()

# checkbutton
check_var = tk.BooleanVar()
check = ttk.Checkbutton(window,text='checkbox 1',command= lambda: print(check_var.get()),variable=check_var,onvalue=True,offvalue=False)    
check.pack()
check2= ttk.Checkbutton(window,text='checkbox 2',command= lambda: check_var.set(5))    
check2.pack()

# radio buttons 
radio_var =tk.StringVar()
radio1 = ttk.Radiobutton(window,text='Radio button 1',value = 'radio 1'
                 ,variable=radio_var,command = lambda : print(radio_var.get()))
radio1.pack()

radio2= ttk.Radiobutton(window,text='Radio button 2',value =2,variable=radio_var,command = lambda : print(radio_var.get()))
radio2.pack()

'''create another checkbutton and 2 radiobuttons
radio button:
    values for the buttons are A and B
    ticking either prints the value of the checkbutton
    ticking the radio button unchecks the checkbutton
check button:
    ticking the checkbutton prints the value of the radio button value
    use tkinter var for Booleans!'''
def radio_func():
    check_bool.set(False)

# data 
radio_string= tk.StringVar()
check_bool = tk.BooleanVar()

# widgets
ex_radio1 = ttk.Radiobutton(window,text='Radio A',value ='A',variable=radio_string,command=radio_func)
ex_radio2 = ttk.Radiobutton(window,text='Radio B',value='B',variable=radio_string,command=radio_func)
ex_check = ttk.Checkbutton(window,text='exercise check',variable=check_bool,command= lambda : print(radio_string.get()))

# layout 
ex_radio1.pack()
ex_radio2.pack()
ex_check.pack()


# run 
window.mainloop()