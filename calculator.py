from tkinter import *
window=Tk()

# add widgets here

window.title('Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightblue')

def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(i, 2)

    result_label.destroy()
    
    output_message = Label(result_frame, text = username+", your interest is "+interest, bg="lightblue", font=("Calibri", 12), width=42)
    output_message.place(x=20, y=40)
    output_message.pack()


app_label=Label(window, text="INTEREST CALCULATOR", fg = "black", bg = "lightblue", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightblue", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=170, y=92)

principle_label = Label(window, text="Enter your principle:", fg="black", bg="lightblue", font=("Calibri", 12))
principle_label.place(x=20, y=140)

principle = Entry(window, text="", bd=2, width=15)
principle.place(x=170, y=142)

rate_label = Label(window, text="Enter your rate:", fg="black", bg="lightblue", font=("Calibri", 12))
rate_label.place(x=20, y=185)

rate = Entry(window, text="", bd=2, width=15)
rate.place(x=170, y=187)

time_label = Label(window, text="Enter your time:", fg="black", bg="lightblue", font=("Calibri", 12))
time_label.place(x=20, y= 220)

time = Entry(window, text="", bd=2, width=15)
time.place(x=170, y=220)

calculate_button = Button(window, text="Calculate", fg="black", bg="pink", bd=4, command=calculate_interest)
calculate_button.place(x=20, y=260)

result_frame = LabelFrame(window,text="Result", bg = "lightblue", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightblue", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()