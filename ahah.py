from customtkinter import *

app = CTk()
app.geometry("1000x600")
app.title("lol")

set_appearance_mode("dark")

def choose_algorithm(value):
    if value == "recursive algorithm":
        file =  open("fib_rec.txt", "r")
        alg = file.read()
        frlabel.configure(text=alg, pady = 0, padx = 0, justify="left")
        file.close()

frame = CTkFrame(master=app, border_width=2, border_color="#FFCC70")
frame.pack(expand=True)

frlabel = CTkLabel(master=frame, text="Choose algorithm")
frlabel.pack(anchor="sw", expand=True)



btn = CTkButton(master=app, text="Run", corner_radius=32, fg_color="#3114F2",
                 hover_color="#6D13FF", width=180)
btn.place(relx=0.8, rely=0.35)

label = CTkLabel(master=app, text="Run algorithms")
label.place(relx=0.85,rely=0.4)

combobox =CTkComboBox(master=app, values=["Choose algorithm","recursive algorithm", "linear algorithm"], width=180, command=choose_algorithm)
combobox.place(relx=0.8, rely=0.1)

checkbox =CTkCheckBox(master=app, text="Show results", fg_color="#C850C0", checkbox_height=30,
                      checkbox_width=30, corner_radius=36)
checkbox.place(relx=0.8, rely=0.18)

entry=CTkEntry(master=app, placeholder_text="Number of steps", width=180)
entry.place(relx=0.8, rely=0.25)

slider = CTkSlider(master=app, from_=0, to=100, number_of_steps=10, button_color="#C850C0", progress_color="#C850C0", width=180)
slider.place(relx=0.8, rely=0.3)

app.mainloop()

def lowpriority():
    """ Set the priority of the process to below-normal."""

    import sys
    try:
        sys.getwindowsversion()
    except AttributeError:
        isWindows = False
    else:
        isWindows = True

    if isWindows:
        # Based on:
        #   "Recipe 496767: Set Process Priority In Windows" on ActiveState
        #   http://code.activestate.com/recipes/496767/
        import win32api,win32process,win32con

        pid = win32api.GetCurrentProcessId()
        handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, True, pid)
        win32process.SetPriorityClass(handle, win32process.BELOW_NORMAL_PRIORITY_CLASS)
    else:
        import os

        os.nice(1)