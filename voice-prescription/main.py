from tkinter import *
import smtplib
import speech_recognition as sr
from gtts import gTTS
import os
import pandas as pd
import xlsxwriter


r=sr.Recognizer()
with sr.Microphone() as source:
    speech = gTTS("Tell me your name")
    speech.save("hello.mp3")
    os.system("start hello.mp3")
    print("Tell me your name")
    audio=r.listen(source)

    try:
        pname=r.recognize_google(audio)
        print("Your name is",pname)
    except:
        print("Sorry cann't recognize your voice")


    iage="Hii "+pname+".Please tell me your age and gender"
    speech = gTTS(iage)
    speech.save("age.mp3")
    os.system("start age.mp3")
    print("Hii" + pname + ".Please tell me your age and gender")
    ageaudio = r.listen(source)

    try:
        page = r.recognize_google(ageaudio)
        age=pname+"Your age is  "+page+"years .Thanks for sharing your age."
        print("Your age is", page)
    except:
        print("Sorry cann't recognize your voice")

    doc="hii doctor ramesh. Do you want to to suggest any medicines"
    speech = gTTS(doc)
    speech.save("doc.mp3")
    os.system("start doc.mp3")
    print("say yes")
    doc_ans = r.listen(source)

    try:
        ans = r.recognize_google(doc_ans)
        print(ans)
    except:
        print("Sorry cann't recognize your voice")
    if(ans=="yes" or ans=="Yes"or ans==None):
        doc = "tell me names medicines"
        speech = gTTS(doc)
        speech.save("doc.mp3")
        os.system("start doc.mp3")
        print("tell me names medicines")
        med = r.listen(source)

        try:
            mname = r.recognize_google(med)
            print(mname)
        except:
            print("Sorry cann't recognize your voice")
        doc2 = "Doctor please tell me time for consumption of medicines"
        speech = gTTS(doc2)
        speech.save("doc2.mp3")
        os.system("start doc2.mp3")
        print("Doctor please tell me time for consumption of medicines")
        medtime = r.listen(source)

        try:
            mtime = r.recognize_google(medtime)
            print(mtime)
        except:
            print("Sorry cann't recognize your voice")

#






root = Tk()
heading=Label(root,text="Medical Receipt",padx=300,pady=50,width=30,font=(None,30)).grid(row=1,column=2)
name=Label(root,text="Name of patient",font=(None,15),padx=20).grid(row=3,column=1)
iname=Entry( root ,width=50,bg="#f7f7f5",borderwidth=2)
iname.insert(0,pname)
iname.grid(row=3,column=2)


age=Label(root,text="Age and Gender of patient",font=(None,15),padx=20).grid(row=4,column=1)
iage=Entry( root ,width=50,bg="#f7f7f5",borderwidth=2)
iage.insert(0,page)
iage.grid(row=4,column=2)


medi=Label(root,text="1.Medicine name",font=(None,15),padx=20).grid(row=5,column=1)
imed=Entry( root ,width=50,bg="#f7f7f5",borderwidth=2)
imed.insert(0,mname)
imed.grid(row=5,column=2)
itime=Entry( root ,width=50,bg="#f7f7f5",borderwidth=2)
itime.insert(0,mtime)
itime.grid(row=6,column=2)


def printSomething():
    df = pd.DataFrame({
        'Name of patient': [pname],

        'Age and Gender': [page],
        'Medicine name': [mname],
        'Medicine time':[mtime]})


    writer = pd.ExcelWriter('hospital.xlsx', engine='xlsxwriter')


    df.to_excel(writer, sheet_name='Sheet1')


    writer.save()
    print("Don't forgot to fill email address:")
    sender_email = "Please enter your name here"
    rec_email = email.get()
    password = "Please enter your password of email"
    message = "Patient Name ="+pname+"\n"+"Age and gender="+page+"\n"+"medicine="+mname+"\n"+"Medicine Time="+mtime
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    print("login successfull")
    server.sendmail(sender_email, rec_email, message)
    print("email send successfully")



Patient_Email=Label(root,text="Email address of patient",font=(None,15),padx=20).grid(row=8,column=1)
email=Entry( root ,width=50,bg="#f7f7f5",borderwidth=2)
email.insert(0,"@gmail.com")
email.grid(row=8,column=2)




mybutton=Button(root,text="Send email",padx=20,pady=7,command=printSomething,fg="black",bg="blue").grid(row=11,column=2)

root.mainloop()



