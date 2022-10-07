import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import environ
from select import select
import smtplib
from typing_extensions import Self
from source import email
from dotenv import load_dotenv
from tkinter import END, Button, Entry, Label, StringVar, Text, Tk, messagebox, ttk

load_dotenv()

ventana = Tk()
ventana.title("BIENVENIDO A GMAIL ATRAVEZ DE PYTHON:")
ventana.geometry("650x500")
ventana.resizable(False,False)
ventana.configure(background="#058f8e")


#------------------------------Funciones------------------------------
def enviar():
    emisor = correo.get()
    password = passw.get()
    destinatario = email.get()
    asunto = subject.get()
    mensaje = message.get(1.0, END)
    print(destinatario)
    print(mensaje)
    ventana.destroy()
    try:
        #-------------Fecha y hora-------------------
        """"
        hoy = datetime.now()
        dia = hoy.strftime("%d")
        mes = hoy.strftime("%m")
        año = hoy.strftime("%y")
        hora = hoy.strftime("%H")
        minuto = hoy.strftime("%M")
        segundo = hoy.strftime("%S")
        fecha = dia + "/" + mes + "/" + año
        #-------------Fecha y hora-------------------
"""
        msg = MIMEMultipart()
        msg['From'] = emisor
        msg['To'] = destinatario
        msg['Subject'] = asunto


        cuerpo = """
       
           <!DOCYPE html>
            <html>
            <body>
            <h1><FONT FACE="courier">Saludos desde python </FONT> 
            <img src="gmail.png" style="width:300px heigth:300px;">   </h1>
            <p></p>
          </body>
       </html>
           
        """
        msg.attach(MIMEText(cuerpo, 'html'))
        texto = msg.as_string()

        
        serverSMTP = smtplib.SMTP('smtp.gmail.com', 587)
        serverSMTP.ehlo()
        serverSMTP.starttls()
        serverSMTP.ehlo()
        serverSMTP.login(emisor, password)
        serverSMTP.sendmail(emisor, destinatario, texto)
        serverSMTP.close()
        messagebox.showinfo("Enviar correo", "Correo enviado exitosamente")
        
    except Exception as e:
        messagebox.showerror("Error", str(e))
#-----------------------------Funciones-------------------------------

#------------------------------Widgets------------------------------
lbl = Label(ventana, text="Correo: ")
lbl.place(x=20, y=30)
lbl.configure(foreground="white", background="#058f8e", font=("Arial Bold", 10))

correo = Entry(ventana)
correo.place(x=80, y=30)
correo.configure(background="white", font=("Arial", 10))

lbl = Label(ventana, text="Contraseña: ")
lbl.place(x=20, y=70)
lbl.configure(foreground="white", background="#058f8e", font=("Arial Bold", 10))

passw = Entry(ventana)
passw.place(x=100, y=70)
passw.configure(background="white", font=("Arial", 10))
passw.configure(show="*")

lbl = Label(ventana, text="Destinatario: ")
lbl.place(x=20, y=110)
lbl.configure(foreground="white", background="#058f8e", font=("Arial Bold", 10))

email = Entry(ventana)
email.place(x=115, y=110)
email.configure(background="white", font=("Arial", 10))

lbl = Label(ventana, text="Asunto: ")
lbl.place(x=20, y=150)
lbl.configure(foreground="white", background="#058f8e", font=("Arial Bold", 10))

subject = Entry(ventana)
subject.place(x=80, y=150)
subject.configure(background="white", font=("Arial", 10))

lbl = Label(ventana, text="Mensaje: ")
lbl.place(x=20, y=190)
lbl.configure(foreground="white", background="#058f8e", font=("Arial Bold", 10))

message = Text(ventana)
message.place(x=80, y=200, width=550, height=200)
message.configure(background="white", font=("Arial", 11))

btn = Button(ventana, text="Enviar", command=enviar)
btn.place(x=550, y=420)
btn.configure(background="#058f8e", font=("Arial", 11))


ventana.mainloop()

""""
mensaje_html=

<!DOCYPE html>
<html>
<body>
<img src="gmail.png" style="width:300px heigth:300px;">
<h1><FONT FACE="courier">Saludos desde python </FONT> {}</h1>
<p>{}</p>
</body>
</html>


origen=input("Desde donde se manda los correos: ")
environ["STMP_USER"]=origen
nombre=input("A quién quieres mandarle tu correo? ")
destinatario=input("Escribe el correo de la persona: ")
mensaje=""
Correo = email.Email()
Correo.mandar_email([destinatario],"Prueba Python", message_format=mensaje_html.format(nombre,mensaje), format="html")
 
"""

#ALFREDO JOSE ZELAYA LAINEZ 
#DAVID ISAAC FERNANDEZ CHICAS 