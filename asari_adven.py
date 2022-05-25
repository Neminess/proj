from tkinter import*
from PIL import Image, ImageTk
class noot(Tk):
     def __init__(self):
          Tk.__init__(self)
          self.configure(bg="#234AE8")
          self.btn=Button(self,text="Bye", command=self.byebye)
          self.advut= Button(self, text="Start off", command=self.goon)
          self.btn.pack()
          self.advut.pack()
          
          self.img=ImageTk.PhotoImage(Image.open("Drakartest/2.png"))
          self.canv= Canvas(self)
          self.canv.create_image(1,1, anchor=NW, image=self.img)
          self.image=self.img
          self.canv.pack(fill=BOTH, expand=True)
          self.tex=Text(self, wrap=WORD, bg="#234AE8")
          self.tex.pack(side=BOTTOM)
          self.slow_in(self.tex,"You have chosen to venture to the lands above all. \nTo get there, you must climb to the highest mountain you see, throw some feathers with salt and powderer gingerroot from it and jump off.")
          #self.tex.after(15000, self.goon)
     def slow_in(self,widget, string):
          if len(string)>0:
               widget.insert("end", string[0])
          if len(string)>1:
               widget.after(90, self.slow_in, widget, string[1:])
     #Below works, but requires waaay too many funcs in order to work for the whole game
     #def desc(self):         
     
     def goon(self):
          self.tex.delete(1.0, "end")
          self.slow_in(self.tex, "Once you've gathered the feathers and gingerroot, it's almost noon. You climb on top of the mountain to your right with your group, throw the items from it and jump off.\nThe air hits you hard as you fall. Everything around you is a blur of grey and green, with the ground below approaching fast.\n The terrain grows closer as the feeling of impending doom crawls in your mind./n While you are swallowed by thoughts and visions of your body mangled from hitting the ground, the rocks turn to clouds and you land softly on the white surface.")
          self.img=ImageTk.PhotoImage(Image.open("volca.png"))
          self.canv.create_image(1,1,anchor=NW, image=self.img)
          self.image=self.img
          #this needs some work, crashes the gui if below is activated
          #self.tex.after(15000)
          #self.tex.delete(1.0, "end")
          #self.slow_in(self.tex, "After everyone's catched their breath, you look around you to see marvelous, white and silver buildings made from moonstone. The sunlight glistens off of them, making it seem as if they'd be covered in diamonds.\nYou gasp at the beauty of it all. Welcome to Asaria.")
     def desc(self):
          pass
          
     def byebye(self):
          boot.destroy()
boot=noot()
boot.geometry("500x500")
boot.mainloop()
'''
def Asa_desc():
     #time.sleep(2)
     
     print
     #time.sleep(4)
  
     print("")
     #time.sleep(5)
     print()
     #time.sleep(4)
'''
'''
def adventure():
          cont=input("Continue your adventure?")
          if cont== "y" or cont=="Y":
          #Clears screen if cont== y or Y
               clear()
               print("The air is cool around you, the wind is blowing softly and you can hear windbells.\nApart from the beautiful buildings ahead of you there are pale hills to your left and dark-silvery forest to your right.")
               suunta=input("Which way do you want to go? (forward/right/left)")
               if suunta=="forward":
                    print("Your group warily makes its way towards the buildings. At first none of you notice any living creatures anywhere, although Soma seems to be detecting some kind of movement in his peripheral vision as he turns his head swiftly to left and right at times, trying to find something.\nUnfortunately for you, he can't tell what he is seeing. In this world, cats do not talk.")
                    time.sleep(3)
               #Iiro to the buildings as a lord
               if suunta=="right":
                    print("Your group decides to venture in to the forest. Closing in on the woods, you start to hear a faint fluttering sound. The sound is similar to that of small wings, although there are no creatures in sight.")
                    time.sleep(5)
                    print("As you advance deeper, it's getting clear that this forest has something hidden in it.\nThe fluttering slowly fades, only to be replaced by a rustle here and there. You can see flashes of violet where the rustling is heard. It seems you may have company.")
                    time.sleep(6)
                    stay=input("Would you like to try and find out what the creature following you is? ")
                    if stay=="y" or stay=="Y":
                         print("Your group decides to catch the creature.")
                         time.sleep(3)
                         clear()
                         choice=input("Which approach would you like to take? \n(1.Lure the creature in with food. 2.Trap it with a box or 3.Catch it with a net.)")
                         if choice=="1":
                              print("Deciding to take the gentlest approach, you all sit down in a small clearing. Mirka places honeytreats and pieces of venisonjerky around the small area while the rest of your group makes a small campfire.\nThe cats are sleeping close to it on someones' coat." )
                              print("Once Mirka is happy with her work, she sits down next to Soma and Nuppu. Now we wait.")
                              time.sleep(5)
                    else:
                         print("You decide that it is best to let the creature be, after all this is a new place and there is no way to tell if the creature is deadly.")
                         time.sleep(3)
                         print("Going further in to the dim forest, the cats seem to be rather relaxed. You wonder how they can act so dog-like.")
                         print("Mirka sees you looking at the cats and smiles. In case you are wondering, these cats are not normal cats.")
'''
