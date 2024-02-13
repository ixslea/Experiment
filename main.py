from customtkinter import *
import subprocess, os, sys

set_appearance_mode("System")
set_default_color_theme("blue")

class App(CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x600")
        self.title("lol")

        def choose_algorithm(value):
            file =  open(f"{value}.py", "r")
            msg = file.read()
            file.close()
            frlabel.configure(text=msg, pady = 0, padx = 0, justify="left")

        

        self.btn = CTkButton(self, text="Run", corner_radius=32, fg_color="#3114F2",
                 hover_color="#6D13FF", width=180, command=self.clickedRun)
        self.btn.place(relx=0.8, rely=0.38)
        
        self.label = CTkLabel(self, text="Run algorithms")
        self.label.place(relx=0.85,rely=0.43)

        self.combobox =CTkComboBox(self, values=["Choose algorithm","recursive_algorithm", "Iterative algorithm"], width=180, command=choose_algorithm)
        self.combobox.place(relx=0.8, rely=0.1)

        self.checkbox =CTkCheckBox(self, text="Show results", fg_color="#C850C0", checkbox_height=30,
                            checkbox_width=30, corner_radius=36)
        self.checkbox.place(relx=0.8, rely=0.18)

        self.entry=CTkEntry(self, placeholder_text="Number of steps", width=180)
        self.entry.place(relx=0.8, rely=0.25)
        self.entry.focus()

        self.btnEntry = CTkButton(self, text="Enter", corner_radius=32, fg_color="#3114F2",
                 hover_color="#6D13FF", command=self.clickedEntry)
        self.btnEntry.place(relx=0.6, rely=0.3)

        self.slider = CTkSlider(self, from_=0, to=100, number_of_steps=10, button_color="#C850C0", progress_color="#C850C0", width=180, command=self.number_event)
        self.slider.place(relx=0.8, rely=0.3)

        self.frame = CTkFrame(self, border_width=2, border_color="#FFCC70")
        self.frame.pack(expand=True)
        
        frlabel = CTkLabel(master=self.frame, text="Choose algorithm")
        frlabel.pack(anchor="sw", expand=True)

        
        
    def number_event(self, value):
            value = int(value)
            self.entry.delete(0, 5)
            self.entry.insert(0, f"{value}")
            
    def clickedEntry(self):
        num = int(self.entry.get())
        self.slider.set(num)
            
    def clickedRun(self):
        alg = self.combobox.get()
        num = int(self.entry.get())
        command = f"python {alg}.py"
        print(command)
        process = os.execvp(f"{alg}.py", num)
        output, error = process.communicate()
        print(output, error)



app = App()
app.mainloop()