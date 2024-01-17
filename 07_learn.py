import tkinter as tk
from tkinter import ttk

#window 
window = tk.Tk()
window.geometry('600x500')
window.title('Event Binding')

#widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window,text = 'A button')
btn.pack()

#events
window.bind('<Alt-KeyPress-a>',lambda event: print(event))

#run
window.mainloop()
#edited..