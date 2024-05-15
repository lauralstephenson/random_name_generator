#This is from a custom tkinter tutorial from Turtle Code
#First some numpy to get the file of over 22 million sames sorted
#There are over a million names in this file, and about 19,000 surnames.
#The first three naames are female, the second three male, the last two agendered/nicknames/cool names

#Now for the user interface.
import tkinter
import customtkinter
import random

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title = "Name Generator"
app.geometry("400x450")

frame = customtkinter.CTkFrame(master=app,
                               width=350,
                               height=400,
                               corner_radius=10)
frame.pack(padx=5,pady=5)

# These are the names files
female_names = "female_names.csv"
male_names = "male_names.csv"
surnames = "sorted_surnames.csv" 
cool_names = "cool_names.csv"

def show_names():
    #print("Button pressed!") #Test to see if button is working                                                                                                          
    global female_names
    global male_names
    global surnames
    global cool_names
    
    with open(female_names) as f:
        names = f.read().split()
        my_pick_1 = random.choice(names)
        my_pick_2 = random.choice(names)
        my_pick_3 = random.choice(names)
        
        
    with open(male_names) as m:
        male = m.read().split()
        my_pick_4 = random.choice(male)
        my_pick_5 = random.choice(male)
        my_pick_6 = random.choice(male)
       
    
    with open(cool_names) as n:
        cool = n.read().split()
        my_pick_7 = random.choice(cool) 
        my_pick_8 = random.choice(cool)
    
    with open(surnames) as s:
        surname = s.read().split()
        my_pick_9 = random.choice(surname)
        my_pick_10 = random.choice(surname)
        my_pick_11 = random.choice(surname)
        my_pick_12 = random.choice(surname)
        my_pick_13 = random.choice(surname)
        my_pick_14 = random.choice(surname)
        my_pick_15 = random.choice(surname) 
        my_pick_16 = random.choice(surname)   
        
    name_label_1.configure(text=my_pick_1 + " " + my_pick_9)
    name_label_2.configure(text=my_pick_2 + " " + my_pick_10)
    name_label_3.configure(text=my_pick_3 + " " + my_pick_11)
    name_label_4.configure(text=my_pick_4 + " " + my_pick_12)
    name_label_5.configure(text=my_pick_5 + " " + my_pick_13)
    name_label_6.configure(text=my_pick_6 + " " + my_pick_14)
    name_label_7.configure(text=my_pick_7 + " " + my_pick_15)
    name_label_8.configure(text=my_pick_8 + " " + my_pick_16)
    
    
names_button = customtkinter.CTkButton(master=frame, 
                                  text="Generate Eight Names", 
                                  font=("Arial", 14),
                                  command=show_names)
names_button.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)


name_label_1 = customtkinter.CTkLabel(master=frame,
                                      text="", 
                                      font=("Arial", 16))
name_label_1.place(relx=0.29,rely=0.2) 

name_label_2 = customtkinter.CTkLabel(master=frame,
                                      text="", 
                                      font=("Arial", 16))
name_label_2.place(relx=0.29,rely=0.3) 

name_label_3 = customtkinter.CTkLabel(master=frame,
                                      text="", 
                                      font=("Arial", 16))
name_label_3.place(relx=0.29,rely=0.4) 

name_label_4 = customtkinter.CTkLabel(master=frame,
                                      text="", 
                                      font=("Arial", 16))
name_label_4.place(relx=0.29,rely=0.5) 

name_label_5 = customtkinter.CTkLabel(master=frame,
                                      text="", 
                                      font=("Arial", 16))
name_label_5.place(relx=0.29,rely=0.6) 

name_label_6 = customtkinter.CTkLabel(master=frame,
                                      text="", 
                                      font=("Arial", 16))
name_label_6.place(relx=0.29,rely=0.7) 

name_label_7 = customtkinter.CTkLabel(master=frame,
                                      text="", 
                                      font=("Arial", 16))
name_label_7.place(relx=0.29,rely=0.8) 

name_label_8 = customtkinter.CTkLabel(master=frame,
                                      text="", 
                                      font=("Arial", 16))
name_label_8.place(relx=0.29,rely=0.9) 

app.mainloop()