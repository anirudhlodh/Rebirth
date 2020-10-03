# import os


# # def countdown(t): 
    
# #     while t: 
# #         mins, secs = divmod(t, 60) 
# #         timer = '{:02d}:{:02d}'.format(mins, secs) 
# #         print(timer, end="\r") 
# #         time.sleep(1) 
# #         t -= 1

# # def scriptchange():
# # 	os.system('python3.8 /home/anirudh/Desktop/2nd_year_project/ai_progect_face_recognition.py')
# # 	sys.exit("NO MASK FACE DETECTED!!")







# # 	t=5
# # 	if withoutMask:
# # 		countdown(int(t))
# # 		scriptchange()
# # 	else:
# # 		continue





# # 	tuple = ((1,2),(2.3))


# os.execv("usr/bin/python3", "/home/anirudh/Desktop/2nd_year_project/detect_mask_video.py")


# import time

# t_end = time.time() + 5 * 1
# while time.time() < t_end:
#     print("Anirudh is Great")


# def goto(linenum):
#     global line
#     line = linenum

# # line = 1
# # while True:
# #     if line == 1:
# #         response = raw_input("yes or no? ")
# #         if response == "yes":
# #             goto(2)
# #         elif response == "no":
# #             goto(3)
# #         else:
# #             goto(100)
# #     elif line == 2:
# #         print "Thank you for the yes!"
# #         goto(20)
# #     elif line == 3:
# #         print "Thank you for the no!"
# #         goto(20)
# #     elif line == 20:
# #         break
# #     elif line == 100:
# #         print "You're annoying me - answer the question!"
# #         goto(1)


# from tkinter import *
# from PIL import ImageTk, Image
# import cv2
# import imutils
# from imutils.video import VideoStream


# root = Tk()
# # Create a frame
# app = Frame(root, bg="white")
# app.grid()
# # Create a label in the frame
# lmain = Label(app)
# lmain.grid()

# # Capture from camera
# #cap = cv2.VideoCapture(0)
# cap = VideoStream(src=0).start()

# # function for video streaming
# def video_stream():
#     frame = cap.read()
#     #_, frame = cap.read()
#     cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
#     img = Image.fromarray(cv2image)
#     imgtk = ImageTk.PhotoImage(image=img)
#     lmain.imgtk = imgtk
#     lmain.configure(image=imgtk)
#     lmain.after(1, video_stream) 

# video_stream()
# root.mainloop()

#starter code
# import time
# import sqlite3
# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# win = tk.Tk()
# win.title(&quot;GUI&quot;)
# win.geometry(&quot;1680x1050&quot;)
# canvas = tk.Canvas(win, width = 1680, height = 1050)
# #Top lines
# canvas.create_line(0,30,1680,30 , fill = &quot;#000000&quot; , width = 100)
# canvas.create_line(0,90,1680,90 , fill = &quot;#000066&quot; , width = 3)
# #Login line
# canvas.create_line(0,565,1680,565 , fill = &quot;#000000&quot; , width = 2)
# #Bottom corner lines
# canvas.create_line(1390,1050,1680,790 , fill = &quot;#000000&quot; , width = 3)
# canvas.create_line(1400,1050,1680,800 , fill = &quot;#000066&quot; , width = 3)
# canvas.create_line(1470,1050,1700,840 , fill = &quot;#b35900&quot; , width = 60)
# canvas.create_line(1570,1050,1700,930 , fill = &quot;#669900&quot; , width = 60)
# canvas.place(anchor = &quot;nw&quot;, relx = 0 , rely = 0)
# title = tk.Label(win , text = &quot;Register!!!&quot; , font = &quot;Times 40 &quot; , fg = &quot;#ffffff&quot; , bg = &quot;#000000&quot;)
# title.place(anchor = &quot;n&quot; , relx = 0.5 , rely = 0.005)
# #create labels-can use pack(places in the centre) and grid(places according to arguments)
# title = tk.Label(win , text = &quot;Enter Your Credentials&quot; , font = &quot;Times 52 &quot;)
# title.place(anchor = &quot;n&quot; , relx = 0.5 , rely = 0.5)
# lbl1 = ttk.Label(win, text=&quot;Enter your name:&quot;)
# lbl1.place( relx = 0.41 , rely = 0.6 )
# lbl2 = ttk.Label(win, text=&quot;Enter your Email:&quot;)
# lbl2.place( relx = 0.41 , rely = 0.65 )
# lbl3 = ttk.Label(win, text=&quot;Enter your age:&quot;)
# lbl3.place( relx = 0.41 , rely = 0.70)
# lbl4 = ttk.Label(win, text=&quot;Select your gender:&quot;)
# lbl4.place( relx = 0.41 , rely = 0.75)
# lbl5 = ttk.Label(win, text=&quot;Create a Password:&quot;)
# lbl5.place( relx = 0.41 , rely = 0.80)
# #creating entry boxes
# txt1var = tk.StringVar()
# txt1 = ttk.Entry(win , width=16, textvariable=txt1var)
# txt1.place( anchor = &quot;n&quot; , width = 300 , relx = 0.5 , rely = 0.625)
# txt1.focus()
#     
# txt2var = tk.StringVar()
# txt2 = ttk.Entry(win , width=16, textvariable=txt2var)
# txt2.place( anchor = &quot;n&quot; , width = 300 , relx = 0.5 , rely = 0.675)
# txt3var = tk.StringVar()
# txt3 = ttk.Entry(win , width=16, textvariable=txt3var)
# txt3.place( anchor= &quot;n&quot; , width = 300 , relx = 0.5 , rely = 0.725)
# txt4var = tk.StringVar()
# txt4 = ttk.Entry(win, width=16, textvariable=txt4var, show=&quot;*&quot;)

# txt4.place( anchor= &quot;n&quot; , width = 300 , relx = 0.5 , rely = 0.825)
# #combo boxes
# cmb1var = tk.StringVar()
# cmbgender=ttk.Combobox(win, width=14, textvariable=cmb1var, state=&quot;readonly&quot;)
# cmbgender[&quot;values&quot;]=(&quot;Male&quot;,&quot;Female&quot;,&quot;Other&quot;)
# cmbgender.current(0)
# cmbgender.place( anchor= &quot;n&quot; , width = 300 , relx = 0.5 , rely = 0.775)
# #radiobutton
# usertype = tk.StringVar()
# rad1=ttk.Radiobutton(win, text=&quot;student&quot;, value=&quot;student&quot;,variable=usertype)
# rad1.place( anchor= &quot;n&quot; , width = 300 , relx = 0.5 , rely = 0.875)
# rad2=ttk.Radiobutton(win, text=&quot;teacher&quot;, value=&quot;teacher&quot;,variable=usertype)
# rad2.place( anchor= &quot;n&quot; , width = 300 , relx = 0.6 , rely = 0.875)
# #checkbox
# chk=tk.IntVar()
# chk1 = ttk.Checkbutton(win, text=&quot;subscribe to our newsletter&quot;,variable=chk)
# chk1.place( anchor= &quot;n&quot; , width = 300 , relx = 0.5 , rely = 0.925)

# #buttonaction
# def action():
#         name = txt1.get()
#         email = txt2.get()
#         age = txt3.get()
#         gender = cmb1var.get()
#         typ = usertype.get()
#         psw = txt4.get()
#         if chk.get() == 0:
#             subscribed=&quot;NO&quot;
#         else:
#             subscribed=&quot;YES&quot;
#         print(f&#39;{name} is {age} years old and the email id is {email} {gender} {typ} {subscribed}&#39;)
#         with open(&quot;database.txt&quot;,&quot;a&quot;) as f:
#             f.write(f&#39;\n{name},{email},{age},{gender},{typ},{subscribed}\n&#39;)
#             
#         txt1.delete(0, tk.END)
#         txt2.delete(0, tk.END)
#         txt3.delete(0, tk.END)
#         lbl1.configure(foreground=&quot;Red&quot;)
#         lbl2.configure(foreground=&quot;Green&quot;)
#         lbl3.configure(foreground=&quot;Blue&quot;)
#         #creating a database, connecting to a database
#         try:
#             conn = sqlite3.connect(&#39;user.db&#39;)
#             c=conn.cursor()
#             c.execute(&quot;INSERT INTO users VALUES (:dname, :demail, :dpass, :dage, :dgender, :dsubs)&quot;,{&#39;dname&#39;:name, &#39;demail
# &#39;:email,&#39;dpass&#39;:psw, &#39;dage&#39;:age, &#39;dgender&#39;:gender, &#39;dsubs&#39;:subscribed})
#             conn.commit()
#             conn.close()
#             messagebox.showinfo(&quot;Success!!&quot;,&quot;Data Saved Successfully!!!&quot;)
#         except:
#             messagebox.showinfo(&quot;Error in DataType!!!&quot;,&quot;Error!!!&quot;)
#         finally:
#             win.destroy()
# #buttons if u want colour on button change ttk to tk
# btn1=ttk.Button(win, text=&quot;submit&quot;, command=action)
# btn1.place( anchor= &quot;n&quot; , relx = 0.5 , rely = 0.945)
# win.mainloop()




# import sqlite3

# try:
#     conn = sqlite3.connect('DETECTIONS.sqlite')
#     c = conn.cursor()
#     c.execute("INSERT INTO detect VALUES (:did, :dname)",{'did':23, 'dname':"Anirudh"})
#     conn.commit()
#     conn.close()
#     print("Success!!!")
# except:
#     print("Failed!!!")



# import tkinter
# import time
# import sqlite3
# from tkinter import ttk
# from tkinter import messagebox

# root = tkinter.Tk()

# root.geometry("1680x1050")

# canvas = tkinter.Canvas(root, width = 1680, height = 1050)

# #Top lines
# canvas.create_line(0,30,1680,30 , fill = "#000000" , width = 100)
# canvas.create_line(0,90,1680,90 , fill = "#000066" , width = 3)

# #Login line
# canvas.create_line(0,565,1680,565 , fill = "#000000" , width = 2)

# #Bottom corner lines
# canvas.create_line(1390,1050,1680,790 , fill = "#000000" , width = 3)
# canvas.create_line(1400,1050,1680,800 , fill = "#000066" , width = 3)
# canvas.create_line(1470,1050,1700,840 , fill = "#b35900" , width = 60)
# canvas.create_line(1570,1050,1700,930 , fill = "#669900" , width = 60)

# canvas.place(anchor = "nw", relx = 0 , rely = 0)

# userText = tkinter.StringVar()
# passText = tkinter.StringVar()

# title = tkinter.Label(root , text = "Please Login" , font = "Times 40 " , fg = "#ffffff" , bg = "#000000")
# title.place(anchor = "n" , relx = 0.5 , rely = 0.005)

# title = tkinter.Label(root , text = "Login" , font = "Times 52 ")
# title.place(anchor = "n" , relx = 0.5 , rely = 0.5)

# userLabel = tkinter.Label(root, text = "Username")
# userLabel.place( relx = 0.41 , rely = 0.6 )

# userName = tkinter.Entry(root , textvariable = userText  )
# userName.place( anchor = "n" , width = 300 , relx = 0.5 , rely = 0.625)

# passLabel = tkinter.Label(root, text = "Password" , show="*")
# passLabel.place( relx = 0.41 , rely = 0.65 )

# passWord = tkinter.Entry(root , textvariable  = passText)
# passWord.place( anchor = "n" , width = 300 , relx = 0.5 , rely = 0.675)

# infoMessage = tkinter.Message(root , width = 300)


# def checkCred():

#         conn = sqlite3.connect('user.db')
#         c=conn.cursor()
#         c.execute("SELECT * FROM users WHERE email=:demail AND Password=:dpass",{'demail':userText.get(),'dpass':passText.get()})
#         results = c.fetchall()
#         conn.commit()
#         try:
#             if results:
#                 for i in results:
#                     messagebox.showinfo("Success!!!","Welcome "+i[0])
#             else:
#                 messagebox.showinfo("Invalid Credentials!!","Error!!!")
#         except:
#             messagebox.showinfo("Some Database Error!!!","Error!!!")
#         finally:
#             root.destroy()
#         
#         conn.close()

# loginBtn = tkinter.Button(root, text = "login" , activebackground = "#97cf9a" , command = checkCred)
# loginBtn.place(anchor = "n" , width = 300 , relx = 0.5, rely = 0.7)



# root.mainloop()



# import smtplib

# content = 'Hi just testing'

# mail = smtplib.SMTP('smtp.gmail.com',587)

# mail.ehlo()

# mail.starttls()

# mail.login('facemaskdetection@gmail.com','hihowareyou')

# mail.sendmail('facemaskdetection@gmail.com','anirudhlodh@gmail.com',content)

# mail.close()


