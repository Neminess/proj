from tkinter import*
from PIL import Image, ImageTk

class StarMenu(Tk):
     def __init__(self):
          Tk.__init__(self)
          self.img=ImageTk.PhotoImage(Image.open("Drakartest/0.png"))
          self.canv=Canvas(self)
          self.canv.create_image(1,1, anchor=NW, image=self.img)
          self.canv.image= self.img
          self.canv.pack()
          self.btn1=Button(self, text="Asaria", command= self.goasa)
          self.btn2=Button(self, text="Grenda", command= self.gogren)
          self.btn3=Button(self, text="Nimeria", command= self.gonim)
          self.btn4=Button(self, text="Wetlands", command= self.gowet)
          
          self.btn1.pack()
          self.btn2.pack()
          self.btn3.pack()
          self.btn4.pack()
          
          #self.lbl=Label(self, text="Hello")
          #self.lbl.pack()
          
     def goasa(self):
          #self.lbl.configure(text="Welcome to Asaria")
          root.destroy()
          import asari_adven
          
     def gogren(self):
          #self.lbl.configure(text="Welcome to Grenda")
          root.destroy()
          import grenda_adven
     def gonim(self):
          #self.lbl.configure(text="Welcome to Nimeria")
          root.destroy()
          import nim_adven
     def gowet(self):
          #self.lbl.configure(text="Welcome to Wetlands")
          root.destroy()
          import wetla_adven
if __name__=="__main__":
     root=StarMenu()
     root.mainloop()          
