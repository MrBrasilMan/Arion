from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox as msgbox
import parser
import sys
import requests

import tkinter as tk
from tkinter import ttk


#Warning, this is some pretty messy code right now
#Preset webtext to the home page
version = "1.5.0"
latest_info = requests.get("https://raw.github.com/MrBrasilMan/Arion/main/info.txt").text
webtext = "Welcome to Arion Version " + version + "\nBy Lucas Frias\n___________________________________________________\n" + latest_info
#This is the web library of 0.4.2, somewhat modified.
#This function gets the website and returns it in text
def get_website():
  try:
    #Get the users' query.
    #Automatically https if the user does not specify.
    if "https://" in str(search.get(1.0, "end-1c")):
      body = requests.get(search.get(1.0, "end-1c"))
    if "https://" not in str(search.get(1.0, "end-1c")):
      if "http://" not in str(search.get(1.0, "end-1c")):
       body = requests.get("https://" + search.get(1.0, "end-1c"))
    #This places the parsed html in the website text, plus an end of page, and list of links belowards.
    window.title(parser.get_title(search.get(1.0, "end-1c")) + " - Arion")
    website_text = parser.parse(body.text) + "\n\n\n\n__________________________________\nList of links (elements of a)\n__________________________________\n" + parser.link_list(body.text)
    #Delete all of the text from the previous website
    website_body_text.delete('1.0', END)
    #This is putting the text in the main textbox to view.
    webtext = website_text
    website_body_text.insert(tk.END, webtext)
  #Error handling
  except:
      window.title("Error - Arion")
      try:
          a = body
          website_body_text.delete('1.0', END)
          if body.status_code != 200:
                  website_body_text.insert(tk.END, "Error\nArion was able to establish a connection to the website.\n When talking to the website however, it sent a " + str(body.status_code) + " response\nMake sure the given website is not forbidden or broken")
          if body.status_code == 200:
              #If it sends a two hundred, but an error occurs, it is almost most likely that there is a software error.
            website_body_text.insert(tk.END, "Error\n A software error occured when trying to load this website.\nArion is trying its hardest to improve. Any issues or feedback is appriceated.")


      except:
          #No internet response
        if search.get(1.0, "end-1c") == "":
            website_body_text.delete('1.0', END)
            window.title("What??????? - Arion")
            website_body_text.insert(tk.END, "Unidentified Bored Pigeon Error\n\nAs all people know, poultery is what powers today's modern computers. \nThe CPU (Chicken Processing Unit) is the main power of your computer.\nThe main problem with today's modern computing is, unlike back then when code was written in chicken friendly Assembler, we write very complex programs.\nThe chicken was already stressed out enough running this and god knows how many other programs.\nSo when the chicken saw it did all of that work just to calculate nothing, it just gave up.\n\nI hope you're happy now.\n\nProgrammers are also legally required to have at least one weird easter egg in their code.")
        else:
            website_body_text.delete('1.0', END)
            website_body_text.insert(tk.END, "Error\nWhen connecting to the website, we got no response\n\nTrying checking the name and make sure you did not mispell something. You can use the full service name (https://www.example.com) and try again\n\nIf this problem persits, check your network firewall")

#Starting out dimension
window = Tk()
#window.resizable(False, False)
window.title("Home - Arion")
#Set icon
photo = PhotoImage(file = "horse.png")
icon = PhotoImage(file = "horse_small.png")
window.iconphoto(False, photo)
window.geometry('700x420')
#Centering code shamelessly and gleefully stolen from
#https://www.skotechlearn.com/2020/06/tkinter-window-position-size-center-screen-in-python.html
Tk_Width = 700
Tk_Height = 420 
x_Left = int(window.winfo_screenwidth()/2 - Tk_Width/2)
y_Top = int(window.winfo_screenheight()/2 - Tk_Height/2)
window.geometry("+{}+{}".format(x_Left, y_Top))
window.configure(bg="white")
#Bind enter to function submit
#window.bind('<Return>',get_website)
#Submit Button
gobutton = Button(window,
	text = "Go!",
	command = get_website,
  width = 3,
  height = 2,
  bg = "#79d240",
  fg = "white",
  activebackground="#7ddf3f",
  activeforeground="white",
)
canvas = Canvas(window, width=40, height=40, borderwidth=0)
canvas.create_image(1,1, image=icon)


exitbutton = Button(window,
                     text="Exit",
                     command=sys.exit,
                     width=3,
                     height=1,
                     )
#Search Button
search = tk.Text(window,
                   height = 2,
                   width = 45)

#Website Text
website_body_text = ScrolledText(
  window,
  height=20,
  width=85,
  borderwidth=0,
  highlightthickness=0,
  )
def copy():
    try:
        window.clipboard_append(website_body_text.selection_get())
    except:
        window.clipboard_append("")
m = Menu(window, tearoff=0)
m.add_command(label="Copy", command=copy)
m.add_command(label="Reload", command=get_website)
m.add_separator()
m.add_command(label="Pass")
def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()
website_body_text.bind("<Button-3>", do_popup)

def paste():
    try:
        print(window.clipboard_get())
        search.insert(tk.END, str(window.clipboard_get()))
    except:
        window.clipboard_append("")
n = Menu(window, tearoff=0)
n.add_command(label="Paste", command=paste)
n.add_separator()
n.add_command(label="Pass")
def do_popupn(event):
    try:
        n.tk_popup(event.x_root, event.y_root)
    finally:
        pass
        #n.grab_release()
search.bind("<Button-3>", do_popupn)

#Pack all parts of the application
#gobutton.grid(column=1, row=0)
#exitbutton.grid(column=1, row=1)
#search.grid(column=0, row=0)
#website_body_text.grid(column=0, row=7)
gobutton.place(x=490, y=0)
canvas.place(x=10, y=10)
search.place(x=120, y=5)
website_body_text.place(x=0, y=50)
website_body_text.insert(tk.END, webtext)
search.insert(tk.END, "Type in a URl")
window.mainloop()
