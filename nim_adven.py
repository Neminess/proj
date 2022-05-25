from tkinter import*
from PIL import Image, ImageTk
class noot(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.btn=Button(self,text="Bye", command=self.byebye)
		self.advut= Button(self, text="Start off", command=self.Nim_desc)
		self.btn.pack()
		self.advut.pack()
		self.configure(bg="#3227CD")
		self.img=ImageTk.PhotoImage(Image.open("Drakartest/volca.png"))
		self.canv= Canvas(self)
		self.canv.create_image(1,1, anchor=NW, image=self.img)
		self.image=self.img
		self.canv.pack(fill=BOTH, expand=True)
		self.tex=Text(self, wrap=WORD, bg="#4E42EB")
		self.tex.pack(side=BOTTOM)
		
		self.slow_in(self.tex, "You have chosen to venture into the darkness of Nimeria")
	def slow_in(self,widget, string):
		if len(string)>0:
			widget.insert("end", string[0])
		if len(string)>1:
			widget.after(90, self.slow_in, widget, string[1:])
	def byebye(self):
		root.destroy()
	def Nim_desc(self):
		self.tex.delete(1.0, "end")
		self.slow_in(self.tex,"You step in a portal and pass through the twisting nether into a land that is dark with eternal night, the moon being the only lightsource here. Looking around you, you see a faint outline of a temple. Its walls shimmer slightly in the distance. \n")
		#print("Near the temple shadows, barely visible but definitely there, can be seen. They seem to belong to some horselike-creatures. When the moon reveals what they are, you see magnificent beings with shining and sleek fur eating a dead deer.\n These are hellhorses. Hope that they don't see you, and welcome to Nimeria.")

def adventure(): 
	print("Soma and Nuppu seem to be in their element, Soma climbing on trees and Nuppu searching for prey in the bushes nearby.")
	print("The air feels cool on your skin. You wonder how the cats are so comfortable, taken their fur is almost non-existent.")
	print("Just as this thought passes through your mind, Soma lets out a loud meow and jumps on your shoulders. He is trying to burrow himself inside your cloak for warmth")
root=noot()
root.mainloop()
