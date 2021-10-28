import tkinter as tk
from tkinter import *

root = tk.Tk()

root.geometry('300x300')
root.title('tkinterApp')

entry = tk.Entry(justify='center')

btn = tk.Button(bg='#fff', command=lambda:btN(),justify='center',width=20)

def btN():
	from tkinter import colorchooser
	s = colorchooser.askcolor()
	print(s[1])
	print(s)
	entry.delete(1,tk.END)
	entry.insert(1,s[1])
	color = tk.Label(root, text=s[1], bg = s[1], width = 20)
	color.pack()
entry.pack()
btn.pack()

root.mainloop()

#tkColorChooser.askcolor()