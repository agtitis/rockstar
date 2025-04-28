from guizero import App, Box, Text, TextBox, Picture, PushButton, Window
from tkinter import Message
from PIL import ImageTk, Image

tx_colour = "#ffffff"
font_type = "Verdana"
  
app = App(bg="#b566ff", title="Ποιος Rockstar είσαι;")
question_window = Window(app, title="Questions", bg="#b566ff")
question_window.hide()

end_window = Window(app, title="End", bg="#000000")
end_window.hide()

def q_window():
  question_window.show(wait=True)

def e_window():
  question_window.hide()
  end_window.show(wait=True)



#Intro page

title_box = Box(app, width="fill", align="top", border=False,height=80)
Text(title_box, text="Ποιος rockstar είσαι;", font=font_type, size=25, color=tx_colour)

content_box = Box(app, layout = "grid",width="fill")

#guitarist_image=ImageTk.PhotoImage(Image.open("guitarist.png"))
guitarist_image = Picture(content_box, image="guitarist.png", grid=[0,0,1,2], height = 300, width = 200)
text_content_box = Box(content_box, grid=[1,0,2,1])
intro_text = Message(text_content_box.tk, text="Γεια σου. Θέλεις να μάθεις ποιο είναι το Rockstar όνομά σου;\n\nΚάνε κλικ στο κουμπί Έναρξη, απάντησε σε μερικές απλές ερωτήσεις και θα σου αποκαλύψω το Rockstar όνομά σου!!")
intro_text.config(bg='#b566ff', font=('Verana', 12),width=300, foreground="#ffffff")
intro_text.pack()
button = PushButton(content_box,text = "Έναρξη", command=q_window, grid=[2,1,2,1])

#Questions page
q_title_box = Box(question_window, width="fill", align="top", border=False,height=80)
Text(q_title_box, text="Ερωτήσεις", font=font_type, size=25, color=tx_colour)

questions_box = Box(question_window, layout = "grid",width="fill")

name_label = Text(questions_box, text="Όνομα", grid=[0,0], align="left", color = tx_colour,  font = font_type )
name = TextBox(questions_box, grid=[1,0])
band_label = Text(questions_box, text="Ποιος είναι ο αγαπημένος σου καλλιτέχνης;", grid=[0,1], align="left", color = tx_colour,  font = font_type)
band = TextBox(questions_box, grid=[1,1])
dob_label = Text(questions_box, text="Ποια είναι η ημερομηνία γένησης;", grid=[0,2], align="left", color = tx_colour,  font = font_type)
dob = TextBox(questions_box, grid=[1,2])
pet_label = Text(questions_box, text="Ποια είναι η αγαπημένη σου ομάδα;", grid=[0,3], align="left", color = tx_colour,  font = font_type)
pet = TextBox(questions_box, grid=[1,3])
maiden_label = Text(questions_box, text="Ποιο είναι το αγαπημένο σου χρώμα;", grid=[0,4], align="left", color = tx_colour,  font = font_type)
maiden = TextBox(questions_box, grid=[1,4])

finish_button = PushButton(questions_box,text = "Υποβολή", command=e_window, grid = [0,5,2,1], align="left")

#End page

e_title_box = Box(end_window, width="fill", align="top", border=False,height=80)
Text(e_title_box, text="STOP AND THINK", font=font_type, size=25, color=tx_colour)
guitarist_image = Picture(end_window, image="end_image.png", height = 100, width = 200)

end_text_content_box = Box(end_window, border=False, width="fill")
end_text = Message(end_text_content_box.tk,  text= "Κοινοποιήσατε ελεύθερα τα προσωπικά σας δεδομένα σε εμάς. Απλώς σκεφτείτε τι θα μπορούσε να κάνει ένας εγκληματίας του κυβερνοχώρου με αυτά τα δεδομένα!\n\nΔήλωση αποποίησης ευθύνης: Αυτό το πρόγραμμα στοχεύει να τονίσει τους κινδύνους της ελεύθερης υποβολής των προσωπικών σας δεδομένων. Κανένα από τα προσωπικά σας δεδομένα δεν έχει αποθηκευτεί από αυτό το πρόγραμμα.")
end_text.config(bg='#000000', font=('Verana', 12),width=300, foreground="#ffffff")
end_text.pack()

app.display()
















