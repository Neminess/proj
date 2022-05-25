from tkinter import*
from PIL import Image, ImageTk
class noot(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.btn=Button(self,text="Bye", command=self.byebye)
		self.advut= Button(self, text="Start off", command=self.desc)
		self.configure(bg="#901515")
		self.btn.pack()
		self.advut.pack()
		
		self.img=ImageTk.PhotoImage(Image.open("Drakartest/volca.png"))
		self.canv= Canvas(self)
		self.canv.create_image(1,1, anchor=NW, image=self.img)
		self.image=self.img
		self.canv.pack(fill=BOTH, expand=True)
		self.tex=Text(self, wrap=WORD, bg="#901515")
		self.tex.pack(side=BOTTOM)
		self.slow_in(self.tex,"You have chosen to venture to Grenda, the land of smoke, ash and brimstone.")
	def slow_in(self,widget, string):
		if len(string)>0:
			widget.insert("end", string[0])
		if len(string)>1:
			widget.after(90, self.slow_in, widget, string[1:])
	def byebye(self):
		boot.destroy()
	#Below works, but requires waaay too many funcs in order to work for the whole game
	def desc(self):	
		self.after(3000, self.intro)
	def intro(self):
		self.tex.delete(1.0, "end")
		self.slow_in(self.tex," To reach this volcanic land, you must set up a campfire, throw some rubies in it and draw the above symbols around it; the first on north, second on east, third on south, fourth on west. After this, the symbols will light up with red, lava-like substance before the campfire explodes and sends out burning pieces of wood everywhere. The earth quakes and you lose your balance. When you get up from the ground and look at the now nearly extinguished fire, a portal will've risen up before you from the ground. It is a smoking hot, made of ashen rocks and flaming veins of lava. You slowly step through the portal, from the dense forest to hot mountain air. The smell of fires, burning rock and excruciatingly dry wind hit you. Welcome to Grenda, land of fires and giants.")
	
boot=noot()
boot.geometry("500x500")
boot.mainloop()
'''	
def Gren_desc():
	print("\n")	
	print("As your eyes adjust to the bright light, your group starts to make out details in your surroundings. You appear to be in a valley, where the ground and walls are made of red rock.")
	print("On the otherside of the valley, gigantian creatures with grey skin and orange-red tattoos are building something in front of their huts which are built from black, obsidian looking substance.\nWelcome to Grenda.")	 
	print("What would you like to do?")
	#Options: Approach the creatures, look around the valley to satisfy your curiosity, search for water
	#Button to continue to be placed here
	#if approach:
	print("You decided to approach the strange creatures. Your companions seem wary of the beings")
'''
