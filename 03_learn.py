import tkinter as tk
from tkinter import ttk

def button_func():
    #get the content of the entry 
    entry_text=entry.get()

    # update the label options..
    # label.config(text='some other text..:)')
    # label.configure(text='some other text..:)')
    label['text'] = entry_text
    entry['state'] = 'disabled'
    print(label.configure())



# Window
window=tk.Tk()
window.title('Getting and setting widgets')
window.geometry('400x300')

# widgets 
label=ttk.Label(master=window,text='Some text')
label.pack()

entry= ttk.Entry(master=window)
entry.pack()

button=ttk.Button(master=window,text='The button',command=button_func)
button.pack()

'''exercise
add another button that changes text back to "some text" and that enables entry '''

def enable_func():
    label['text']='some text'
    entry['state']='enable'

exercise_btn=ttk.Button(master=window,text='enable',command=enable_func)
exercise_btn.pack()


# run 
window.mainloop()
