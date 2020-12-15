#Does not work
from tkinter import*
root=Tk()

def slow_in(widget, string):
	if len(string)>0:
		widget.insert("end", string[0])
	if len(string)>1:
		widget.after(500, slow_in, widget, string[1:])
		

red=0
green=0
blue=0

def fader():
	global red
	global green
	global blue
	
	red+=1
	green+=0
	blue+=1
	try:
		if red<100:
			colour='#{:02x}{:02x}{:02x}'.format(red, green, blue)
			t.configure(bg=colour)
			t.after(100,fader)
		if red ==100:
			red+=0
			green+=0
			blue+=1
			colour="#{:02x}{:02x}{:02x}".format(red, green, blue)
			t.configure(bg=colour)
			t.after(100, fader)
	finally:
		if t.compare("end-1c", "==", "1.0"):		
			slow_in(t,"Hello")
		else:
			pass
def plaque(event):
	fader()
	
t=Text(root, bg="black", fg="white")
t.bind("<Button-1>", plaque)
t.pack()

root.mainloop()
