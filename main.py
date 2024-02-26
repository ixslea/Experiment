from customtkinter import *
import subprocess, os, sys
from fibRecursion import fibRecursion

set_appearance_mode("System")
set_default_color_theme("blue")


class tabView(CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        

        self.configure(width=1000, height=600)
        """self.add("About")
        self.add("Fibonacci")
        self.add("Harmonic")
        self.pack(padx = 0, pady = 0)"""
        

        self.add("Fibonacci")
        self.add("Harmonic")
        self.pack(expand=True, fill="both")


        currentTab = self.get()
        currentTabIndex =self.index(currentTab)
        print(currentTab)
        """ Choosing algorithm to execute """
        algoValues = [["Choose algorithm","fibRecursion", "Iterative algorithm", "Memoization"], ["Choose algorithm","fibRecursion", "Iterative algorithm"]]

        self.algoChoise = CTkComboBox(self.tab(f"{currentTab}"), values=algoValues[currentTabIndex-1], width=180, 
                                        command=self.algoChange)
        self.algoChoise.place(relx=0.8, rely=0.1)

        """ Checkbox for showing or not results online """
        self.showResults = CTkCheckBox(self.tab(f"{currentTab}"), text="Show results", fg_color="#C850C0", checkbox_height=30,
                        checkbox_width=30, corner_radius=36)
        self.showResults.place(relx=0.8, rely=0.18)
        
        """ Slider for choosing number of steps """
        self.sliderSteps = CTkSlider(self.tab(f"{currentTab}"), from_=0, to=100, number_of_steps=10, button_color="#C850C0", 
                                        progress_color="#C850C0", width=180, command=self.numberSteps)
        self.sliderSteps.place(relx=0.8, rely=0.305)

        """ Entry for inputing number of steps """
        self.entrySteps = CTkEntry(self.tab(f"{currentTab}"), placeholder_text="Number of steps", width=180)
        self.entrySteps.place(relx=0.8, rely=0.25)
        self.entrySteps.focus()

        """ Button for submiting number of steps """ 
        self.btnSteps = CTkButton(self.tab(f"{currentTab}"), text="Submit number of steps", corner_radius=32, fg_color="#3114F2",
                                    hover_color="#6D13FF", width=180, command=self.clickedEntrySteps)
        self.btnSteps.place(relx=0.8, rely=0.34)

        """ Entry for inputing number of rounds of algorithm's execution """
        self.entryRounds=CTkEntry(self.tab(f"{currentTab}"), placeholder_text="Number of rounds", width=180)
        self.entryRounds.place(relx=0.8, rely=0.45)
        self.entryRounds.focus()

        """ Slider for choosing number of rounds of algorithm's execution """
        self.sliderRounds = CTkSlider(self.tab(f"{currentTab}"), from_=0, to=100, number_of_steps=10, button_color="#C850C0", 
                                        progress_color="#C850C0", width=180, command=self.numberRounds)
        self.sliderRounds.place(relx=0.8, rely=0.505)

        """ Button for submiting number of rounds of algorithm's execution """ 
        self.btnRounds = CTkButton(self.tab(f"{currentTab}"), text="Submit number of rounds", corner_radius=32, fg_color="#3114F2",
                                    hover_color="#6D13FF", width=180, command=self.clickedEntryRounds)
        self.btnRounds.place(relx=0.8, rely=0.54)

        """ RUN button runs algorithm """     
        self.btnRun = CTkButton(self.tab(f"{currentTab}"), text="Run", corner_radius=32, fg_color="#3114F2",
                hover_color="#6D13FF", width=180, command=self.clickedRun)
        self.btnRun.place(relx=0.8, rely=0.65)

        """ About RUN button """
        self.labelRun = CTkLabel(self.tab(f"{currentTab}"), text="Run algorithms")
        self.labelRun.place(relx=0.85,rely=0.7)

        """ Frame for showing code to be executed """
        self.frame = CTkFrame(self.tab(f"{currentTab}"), border_width=2, border_color="#FFCC70")
        self.frame.pack(expand=True)

        """ Start label for frame for showing code to be executed """
        self.frlabel = CTkLabel(master=self.frame, text="Choose algorithm")
        self.frlabel.pack(anchor="sw", expand=True)

   
    """ Show code to execute after choosing algorithm """
    def algoChange(self, value):
        file =  open(f"{value}.py", "r")
        code = file.read()
        file.close()
        self.frlabel.configure(text=code, pady = 0, padx = 0, justify="left")

    """ Inputing number of steps """
    def numberSteps(self, value):
            value = int(value)
            self.entrySteps.delete(0, 5)
            self.entrySteps.insert(0, f"{value}")
            
    """ Submiting number of steps """
    def clickedEntrySteps(self):
        num = int(self.entrySteps.get())
        self.sliderSteps.set(num)

    """ Inputing rounds of rounds """
    def numberRounds(self, value):
            value = int(value)
            self.entryRounds.delete(0, 5)
            self.entryRounds.insert(0, f"{value}")
            
    """ Submiting number of rounds """
    def clickedEntryRounds(self):
        num = int(self.entryRounds.get())
        self.sliderRounds.set(num)
            
    """ Running algorithm """
    def clickedRun(self):
        alg = self.algoChoise.get()
        steps = int(self.entrySteps.get())
        rounds = int(self.entryRounds.get())
        command = f"{alg}.py"
        for _ in range (rounds):
            result = subprocess.run(["python", command, str(steps)], capture_output=True, text=True)
            print(result.stdout)

    def tabViewTabChangeClick():
        print(f"Click event once on new clicked tab. You Click:")

class App(CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x600")
        self.title("lol")

        self.tabview = tabView(master=self,command=tabView.tabViewTabChangeClick)
        
        

        

app = App()
app.mainloop()