from tkinter import  *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename , asksaveasfilename
import os


def newfile():
 global file
 root.title("Rajeev's - Notepad")
 file = None
 TextArea.delete(1.0 , END)
 

def openfile():
 global file
 file = askopenfilename(defaultextension=".txt" , filetypes=[("All Files" , "*.*") , ("Text Document" , "*.txt")])
 if file =="":
  file = None
 else:
  root.title(os.path.basename(file) + " - Notepad")
  TextArea.delete(1.0 , END)
  f = open(file , "r")
  TextArea.insert(1.0,f.read())
  f.close()



def savefile():
 global file
 if file == None:
  file = asksaveasfilename(initialfile='untitled.txt',  defaultextension=".txt" , filetypes=[("All Files" , "*.*") , ("Text Document" , "*.txt")])
  if file == "":
   file = None
  else:
   #SAVE AS A NEW FILE
   f = open(file , "w")
   f.write(TextArea.get(1.0 , END))
   f.close()

   root.title(os.path.basename(file) + "- Notepad")
   print("File Saved")

 else:
  #SAVE THE FILE
  f = open(file , "w")
  f.write(TextArea.get(1.0 , END))
  f.close()


def quitApp():
 root.destroy()

def cut():
 TextArea.event_generate(("<<Cut>>"))

def copy():
 TextArea.event_generate(("<<Copy>>"))

def paste():
 TextArea.event_generate(("<<Paste>>"))

def about():
 showinfo("Notepad Created by Rajeev Mishra as a college project .")







if __name__ == '__main__':
    
# BASIC TKINTER SETUP

 root = Tk()
 root.title("Rajeev's -  NOTEPAD")
 root.geometry("677x788")

    # ADD TEXT AREA

 TextArea = Text(root,font="lucida 13")
 file = None
 TextArea.pack(fill=BOTH , expand=True)

 #LETS CREATE A MENU BAR

 MenuBar = Menu(root)

 #LETS MENU STARTS
 FileMenu = Menu(MenuBar , tearoff=0)

 #To OPEN NEW FILE

 FileMenu.add_command(label="NEW" , command=newfile)

 #TO OPEN ALREADY EXISTING FILE

 FileMenu.add_command(label="OPEN" , command=openfile)

 #To SAVE THE CURRENT FILE

 FileMenu.add_command(label="SAVE" , command=savefile)
 FileMenu.add_separator()

 #TO EXIT FROM A FILE

 FileMenu.add_command(label="EXIT" , command=quitApp)

 MenuBar.add_cascade(label="FILE" , menu = FileMenu)

 #EDIT MENU STARTS 

 EditMenu = Menu(MenuBar , tearoff=0)

 #To ADD A FEATURE OF CUT , COPY AND PASTE

 EditMenu.add_command(label="CUT" , command=cut)
 EditMenu.add_command(label="COPY" , command=copy)
 EditMenu.add_command(label="PASTE" , command=paste)
 MenuBar.add_cascade(label="Edit" , menu=EditMenu)

 #EDIT MENU ENDS

 #HELP MENU STARTS

 HelpMenu = Menu(MenuBar , tearoff=0)

 #TO ADD ABOUT NOTEPAD IN HELP MENU

 HelpMenu.add_command(label="About" , command=about)
 MenuBar.add_cascade(label="Help" , menu=HelpMenu)





 #HELP MENU ENDS

 root.config(menu = MenuBar)


 #ADDING SCROLLBAR UAING RULES OF TKINTER

 Scroll = Scrollbar(TextArea)
 Scroll.pack(side=RIGHT , fill=Y)
 Scroll.config(command=TextArea.yview)
 TextArea.config(yscrollcommand=Scroll.set)





 root.mainloop()