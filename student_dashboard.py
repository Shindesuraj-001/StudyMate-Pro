from tkinter import *
import tkinter as tk
from tkinter.ttk import Progressbar
import datetime
from tkinter import messagebox


root = tk.Tk()
root.title("StudyMate Pro")
seconds = 0
root.config(bg = "orange")

date = datetime.date.today()

def update_time():
    t1 = datetime.datetime.now().time()
    time = str(t1).split('.')[0]
    clock.config(text=time)
    clock.after(1000,update_time)


t1 = datetime.datetime.now().time()
time = str(t1).split('.')[0]




def update_timer():
    
    global seconds

    if running:
        seconds += 1

        mins = seconds // 60
        secs = seconds % 60

        time_label.config(text=f"{mins:02d}:{secs:02d}")
        time_label.after(1000,update_timer)

def start_timer():
    global running,top,time_label
    
    running = True
    top = Toplevel()
    top.geometry("70x70")
    top.title("Timer")
    time_label = Label(top,text="00:00",font=("Arial",20,"bold"))
    time_label.grid(row=1,column=0,pady=10)

    update_timer()

def stop_timer():
    global running,top,time_label
    running = False
    top.destroy()

def add_task():
    task = task_entry.get()

    if task == "":
        messagebox.showwarning("Warning","Please enter a task")
    else:
        task_listbox.insert(END,task)
        messagebox.showinfo("Success","Task added successfully")
        task_entry.delete(0,END)
        update_progress()


def delete_task():
    selected_task = task_listbox.curselection()

    if selected_task == ():
        messagebox.showwarning("Warning","Please select a task")
    else:
        task_listbox.delete(selected_task)
        update_progress()
        messagebox.showinfo("Success","Task deleted successfully")


def save_notes():
    notes = notes_text.get(1.0,END)

    if notes == "":
        messagebox.showwarning("Warning","Please enter some notes")
    else:
        f =  open("notes.txt","a")
        f.write(notes)
        f.write("\n")
        f.close()
        messagebox.showinfo("Success","Notes saved successfully")
        notes_text.delete(1.0,END)

def light_theme():
    root.config(bg="white")

def dark_theme():
    root.config(bg="black")

def orange_theme():
    root.config(bg="orange")

def pink_theme():    
    root.config(bg="pink")  

def green_theme():
    root.config(bg="green")

def skyblue_theme():
    root.config(bg="skyblue")


def calculate():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    op = op_entry.get()

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2

    result_entry.delete(0,END)
    result_entry.insert(0,str(result))

def open_calculator():

    global num1_entry,num2_entry,op_entry,result_entry

    cal = Toplevel()
    cal.geometry("300x200")
    cal.title("Calculator")
    # cal.config(bg="skyblue")

    Label(cal,text="Calculator",font=("Arial",20,"bold"),fg="Orange",padx=50,pady=10).grid(row=0,column=0,columnspan=2)

    num1 = Label(cal,text="Enter first number :")
    num1.grid(row=1,column=0)

    num2 = Label(cal,text="Enter second number :")
    num2.grid(row=2,column=0)

    num1_entry = Entry(cal)
    num1_entry.grid(row=1,column=1)

    num2_entry = Entry(cal)
    num2_entry.grid(row=2,column=1)

    op = Label(cal,text="Enter operator:")
    op.grid(row=3,column=0)

    op_entry = Entry(cal)
    op_entry.grid(row=3,column=1)

    result_label = Label(cal,text="Result:")
    result_label.grid(row=4,column=0)

    result_entry = Entry(cal)
    result_entry.grid(row=4,column=1)

    calculate_button = Button(cal,text="Calculate",command=calculate)
    calculate_button.grid(row=5,column=1)


def update_progress():
    total = task_listbox.size()

    if total == 0:
        progress['value'] = 0
        return

    completed = 0

    for i in range(total):
        task = task_listbox.get(i)
        if "(Completed)  " in task:
            completed += 1

    percent = (completed / total) * 100
    progress['value'] = percent
    
def mark_completed():
    selected = task_listbox.curselection()

    if selected == ():
        messagebox.showwarning("Warning","Select a task")
    else:
        task = task_listbox.get(selected)
        new_task = "(Completed)  " + task
        task_listbox.delete(selected)
        task_listbox.insert(selected,new_task)
        update_progress()

def new_dashboard():
    
    task_listbox.delete(0, END)
    notes_text.delete(1.0, END)
    progress['value'] = 0

    global seconds
    seconds = 0
    messagebox.showinfo("New Dashboard","New dashboard started")

def clear_task():
    task_listbox.delete(0,END)
    update_progress()

def clear_notes():
    notes_text.delete(1.0,END)

def about_project():
    messagebox.showinfo("About Project","This is a student dashboard project")

def developer_info():
    messagebox.showinfo("About Developer","This project is created by Suraj Shinde")

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Dashboard",command=new_dashboard)
filemenu.add_command(label="Save Notes",command=save_notes)
filemenu.add_command(label="Clear Task",command=clear_task)
filemenu.add_command(label="Exit",command = root.destroy)
menubar.add_cascade(label="File", menu=filemenu)

taskmenu = Menu(menubar, tearoff=0)
taskmenu.add_command(label="Add Task",command=add_task)
taskmenu.add_command(label="Delete Task",command=delete_task)
taskmenu.add_command(label="Marks task Completed",command=mark_completed)
taskmenu.add_command(label="Delete all Tasks",command = clear_task)
menubar.add_cascade(label="Task", menu=taskmenu)


toolmenu = Menu(menubar, tearoff=0)
toolmenu.add_command(label="Calculator",command=open_calculator)
toolmenu.add_command(label="Study Timer",command=start_timer)
toolmenu.add_command(label="Clear Notes",command=clear_notes)
toolmenu.add_command(label="Start Study Mode",command = skyblue_theme)
menubar.add_cascade(label="Tools", menu=toolmenu)

thememenu = Menu(menubar, tearoff=0)
thememenu.add_command(label="Light Theme",command=light_theme)
thememenu.add_command(label="Dark Theme",command=dark_theme)
thememenu.add_command(label="Orange Theme",command=orange_theme)
thememenu.add_command(label="pink Theme",command=pink_theme)
thememenu.add_command(label="Green Theme",command=green_theme)
thememenu.add_command(label="Sky blue Theme",command = skyblue_theme)
menubar.add_cascade(label="Theme", menu=thememenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About Project",command=about_project)
helpmenu.add_command(label="Developer Info",command=developer_info)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)



left_frame = Frame(root, bd=2,padx=10, pady=10)
left_frame.grid(row=0, column=0, padx=10, pady=10)

Label(left_frame, text="Clock & Date", font=("Arial",16, "bold")).grid(row=0, column=0, pady=5)
Label(left_frame, text="Date: " + str(date), font=("Arial", 10)).grid(row=1, column=0 )
clock = Label(left_frame, text="", font=("Arial", 12))
clock.grid(row=2, column=0)
update_time()


Label(left_frame, text="Study Timer", font=("Arial",16, "bold")).grid(row=3, column=0, pady=12)
start_btn = Button(left_frame, text="Start", width =16,command= start_timer)
start_btn.grid(row=4, column=0, pady=3)
stop_btn = Button(left_frame, text="Stop", width = 16,command= stop_timer)
stop_btn.grid(row=5, column=0, pady=3)

Label(left_frame, text="To-Do List", font=("Arial",16, "bold")).grid(row=6, column=0, pady=12)
task_entry = Entry(left_frame, width=50)
task_entry.grid(row=7, column=0)
add_btn = Button(left_frame, text="Add Task",width = 16 ,command = add_task)
add_btn.grid(row=8, column=0, pady=3)
delete_btn = Button(left_frame, text="Delete Task",width = 16, command = delete_task)
delete_btn.grid(row=9, column=0, pady=3)

task_listbox = Listbox(left_frame, width=30, height=6)
task_listbox.grid(row=10, column=0, pady=5)




right_frame = Frame(root, bd=2, relief=RIDGE, padx=10, pady=10)
right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

Label(right_frame, text="Notes Section", font=("Arial", 14, "bold")).grid(row=0, column=0, pady=5)
notes_text = Text(right_frame, width=40, height=8)
notes_text.grid(row=1, column=0)
save_notes_btn = Button(right_frame, text="Save Notes",command=save_notes)
save_notes_btn.grid(row=2, column=0, pady=5)


Label(right_frame, text="Calculator", font=("Arial", 18, "bold")).grid(row=3, column=0, pady=10)
calc_btn = Button(right_frame, text="Open Calculator",command = open_calculator)
calc_btn.grid(row=5, column=0, pady=5)

Label(right_frame, text="Progress of Task", font=("Arial", 14, "bold")).grid(row=6, column=0, pady=10)

progress = Progressbar(right_frame, orient=HORIZONTAL, length=250, mode='determinate')
progress.grid(row=7, column=0, pady=10)



root.mainloop()
