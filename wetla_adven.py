#Change the pic and other-names for this and nim
from tkinter import*
from PIL import Image, ImageTk
class noot(Tk):
     def __init__(self):
          Tk.__init__(self)
          self.btn=Button(self,text="Bye", command=self.byebye)
          self.advut= Button(self, text="Start off", command=self.Wetla_desc)
          self.btn.pack()
          self.advut.pack()
          
          self.img=ImageTk.PhotoImage(Image.open("Drakartest/volca.png"))
          self.canv= Canvas(self)
          self.canv.create_image(1,1, anchor=NW, image=self.img)
          self.image=self.img
          self.canv.pack(fill=BOTH, expand=True)
          self.tex=Text(self, wrap=WORD)
          self.tex.pack(side=BOTTOM)
     def slow_in(self,widget, string):
          if len(string)>0:
               widget.insert("end", string[0])
          if len(string)>1:
               widget.after(90, self.slow_in, widget, string[1:])
     def byebye(self):
          woot.destroy()
     def Wetla_desc(self):
          #time.sleep(2)
          self.slow_in(self.tex,"The portal to this land is underwater. As your group dives in to it, you feel the currents taking a hold of you and carrying you on swiftly.")
          #time.sleep(4)
          self.slow_in(self.tex,"Suddenly you see a dark and murky swirl ahead of you. The current rushes you to it and for a moment you can only see muddy green around you. When the water clears, you and your group are floating towards the surface.")
          #time.sleep(4)
          self.slow_in(self.tex,"When you reach the surface, you are enveloped in light fog, which lets you see around you. All you see is swamp, swamp everywhere. You've arrived in the Wetlands.")

woot=noot()
woot.mainloop()
'''
def adventure():
     print("Your group slowly makes its way to the driest spot you see. All your equipment is wet and you decide to make camp for the fast approaching night.\nWhile your companions start setting up a shelter, you are tasked with finding some reasonably dry wood for a campfire so you grab your axe and get to it.")
     #time.sleep(4)
     print("Once your shelter's set up and you have campfire going, it's time to rest. Or it would be, if one your groupmembers hadn't disappeared. Soma is nowhere to be seen. Everyone is calling out to him, but there is no answer. Slightly beginning to panic, you decide to search the area.")

     time.sleep(6)
     suunta=input("Do you want to search the forest or would the open, but slightly overgrown, marsh be the best place to look?")
     if suunta=="forest":
          clear()
          print("You start making your way to the forest, Mirka on the lead and the rest following close. You're carrying Nuppu, as she doesn't like the wetness of the area and due to her short fur, she get cold easily.")
     if suunta=="marsh":
          clear()
          print("Your companions don't seem to like the idea of getting wet again, but they all know Soma won't make it alone in this environment. Your group makes its way towards the marshlands.")
'''
