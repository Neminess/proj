import tkinter as tk
from PIL import ImageTk, Image
import calendar
import datetime
import json

class StartPage(tk.Tk):
     def __init__(self):
          tk.Tk.__init__(self)
          container= tk.Frame(self)
          container.pack(side="top", fill="both", expand=True)
          container.grid_rowconfigure(0, weight=1)
          container.grid_columnconfigure(0, weight=1)
          
          self.frames= {}
          for F in (Fire, Refir):
               frame= F(container, self)
               self.frames[F]=frame
               frame.grid(row=0, column=0, sticky="nsew")
          self.show_frame(Fire)     
     
     def show_frame(self, cont):
          frame= self.frames[cont]
          frame.tkraise()
          
class Fire(tk.Frame):
     def __init__(self, parent, controller):
          tk.Frame.__init__(self, parent)
          self.filab=tk.Label(self, text="Welcome!")
          self.filab.pack()
          self.img=ImageTk.PhotoImage(Image.open("magics.png"))  
          self.welcome=tk.Canvas(self)
          self.welcome.create_image(1,1, anchor="nw", image=self.img)
          self.welcome.image=self.img
          self.welcome.pack()
          self.name=tk.Entry(self,text="Please enter name for reservation")
          self.name.insert(1, "Enter name")
          self.name.pack()
          self.nexpa=tk.Button(self, text="Continue to booking", command= self.cale)
          self.nexpa.pack()
          #name and reserv dates 
     def cale(self):
          self.nameval=self.name.get()
          self.name.destroy()
          self.lbl=tk.Label(self, text="Hello {}".format(self.nameval))
          self.lbl.pack()
          self.welcome.destroy()
          self.imuge=ImageTk.PhotoImage(Image.open("nex.png"))
          self.resers=tk.Canvas(self)
          self.resers.create_image(1,1, anchor="nw", image= self.imuge)
     
          self.resers.pack()
          self.nexpa.destroy()
          starda=datetime.date.today()
          stary=starda.year
          stam=starda.month
          self.now=calendar.month(stary,stam)
          self.lbl=tk.Label(self, text=self.now)
          self.lbl.pack()
 #starting date
          self.starday=tk.Entry(self)
          self.starday.focus_set()
          self.starday.pack()
          self.labl=tk.Label(self, text="Enter the date you wish to start your reservation")
          self.labl.pack()
          self.ender=tk.Entry(self)
          self.ender.pack()
          self.end_day=tk.Label(self, text="Enter the desired ending date")
          self.end_day.pack()
          self.reser=tk.Button(self, text="Availability", command=self.checker)
          self.reser.pack()
          
     def checker(self):
          taken=False
          wished=self.starday.get()
          end_res=self.ender.get()
          takenstart=["5.7.2020"]
          reservations={self.nameval:(wished, end_res)}
          if wished in takenstart:
               taken=True
               self.labl.configure(text="Please select a different starting date.")
          elif end_res in takenstart:
               taken=True
               self.end_day.configure(text="Please select a different end-date")
          elif taken!=True and len(wished)>0:
               self.tex=tk.Text(height=5, fg="green")
               self.tex.insert(1.0, "Reservation date: {} - {}".format(wished, end_res))
               self.tex.pack()
               with open("reserv.txt", "a") as f:
                    f.write(json.dumps(reservations))
                    f.close()
               self.confirm=tk.Button(self, text="Confirm reservation", command=lambda:StartPage.show_frame(Refir))
               self.confirm.pack(side="bottom")        
          elif len(wished)==0 or len(end_res)==0:
               self.labl.configure(text="Please enter valid dates")
             
         
class Refir(tk.Frame):
     def __init__(self, parent, controller):
          tk.Frame.__init__(self, parent)
          self.lbl=tk.Label(self, text="Hello people")
          self.lbl.pack()
     def infos(self):
          self.infex=tk.Text(self)
          self.infex.pack()
          with open("reserv.txt","r") as f:
               infos=f.read(json.loads(reservations))
          self.infex.insert(1, text=infos)
if __name__=="__main__":
     root=StartPage()
     root.geometry("700x700")
    
     root.mainloop()
