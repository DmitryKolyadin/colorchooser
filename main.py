import tkinter as tk
from tkinter import *

root = tk.Tk()

root.geometry('300x300')
root.title('tkinterApp')

lbl = tk.Label(text='HEX', justify='center')

entry = tk.Entry(justify='center')

btn = tk.Button(text = 'Выберите цвет', bg='#fff', command=lambda:btN(),justify='center',width=20)

lbl1 = tk.Label(text='Цвет который получился', justify='center')

color = tk.Label(width = 20, justify='center')

def btN():
	entry.delete(1,tk.END)

	from tkinter import colorchooser

	s = colorchooser.askcolor()
	
	print(s[1])

	if s[1][0] in '#':
		entry.delete(0)

	color.configure(bg=s[1])
	entry.delete(1,tk.END)
	entry.insert(1,s[1])

lbl.pack()
entry.pack()
btn.pack(pady=10)
lbl1.pack()
color.pack(pady=10)

root.mainloop()