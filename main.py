import customtkinter as ctk
from customtkinter import *
import qrcode
app = ctk.CTk()
app.geometry("500x500")

#TitleLabel
Title_label = ctk.CTkLabel(app,text="Qr Code Generator",font=("Inter",48,"bold"),text_color="gray")
Title_label.pack(pady=25)

#filename label and textbox
filename_label = ctk.CTkLabel(app,text="Enter Filename", font=("Inter",20,"bold"))
filename_label.pack()

filename_textbox = ctk.CTkTextbox(app,fg_color="white",height=0,width=400,text_color="black")
filename_textbox.pack(pady=10)

#link label and textbox
link_label = ctk.CTkLabel(app,text="Enter Link", font=("Inter",20,"bold"))
link_label.pack()

link_textbox = ctk.CTkTextbox(app,fg_color="white",height=0,width=400,text_color="black")
link_textbox.pack(pady=10)

sucessvar= ctk.StringVar(app,"")
Success_Generation = CTkLabel(app,textvariable=sucessvar,font=("Inter",20,"bold"))
Success_Generation.pack()


data = ""
QR = qrcode.make(data)

def generate_code():
    #if not empty
    global sucessvar
    global QR
    global filename_textbox
    global link_textbox
    global data
    if filename_textbox and link_textbox:
        new_name = str(filename_textbox.get("1.0","end-1c"))
        new_format = str(link_textbox.get("1.0","end-1c"))
        data = new_format
        QR = qrcode.make(data)
        QR.save(new_name)
        sucessvar.set("Sucessfully Generated QR Code!")
    
        
        
        
        
        
        
#button
button_gen = ctk.CTkButton(app,hover=True,text="Generate Qr Code", font=("Inter",14),command=generate_code)
button_gen.pack(pady=10)


app.mainloop()