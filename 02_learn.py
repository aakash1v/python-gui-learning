import tkinter as tk
from tkinter import ttk
def button_func():
    print("button was pressed")

def print_hello():
    print("hello !")

# create a window 
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x600')

# ttk label
label = ttk.Label(master=window,text="This is a test")
label.pack()

# tk.Text
text=tk.Text(master=window)
text.pack()

# ttk entry
entry =ttk.Entry(master=window)
entry.pack()

exercise_label = ttk.Label(master=window,text="my label")
exercise_label.pack()


# ttk button
button = ttk.Button(master=window,text='A button',command=button_func)
button.pack()


#exercise 
'''Add one more text label and a button with a function that prints hello
the label should say "my label" and be between the entry widget and the button '''
# run



# exercise_btn = ttk.Button(master=window,text="click",command=print_hello)
exercise_btn = ttk.Button(master=window,text="click",command=lambda : print('hello'))
exercise_btn.pack()

window.mainloop()
