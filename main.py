from customtkinter import *
import subprocess, psutil, platform, logging, drowPlots, markdown
from PIL import Image




class tabView(CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(width=1000, height=600, command=self.runExperiment)
        
        """ Adding tabs """
        self.add("About")
        self.add("Fibonacci")
        self.add("Harmonic")
        self.pack(expand=True, fill="both")
        self.set("About")
        
        """ 'About' tab setup """
        self.aboutLabel = CTkLabel(master=self.tab("About"), text="About", font=("Times New Roman", 20))
        self.aboutLabel.place(relx=0.48, rely=0.1)

        file =  open("about.txt", "r")
        aboutText = file.read()
        file.close()
        
        self.infoText = CTkTextbox(master=self.tab("About"), width=620, height=400,corner_radius=0, wrap="word", font=("Times New Roman", 20))
        self.infoText.place(relx=0.2, rely=0.2)
        self.infoText.insert("0.0", aboutText)
        
    """ Algorithms' tabs setup"""
    def runExperiment(self):
        currentTab = self.get()
        self.currentTabIndex =self.index(currentTab)

        logging.info(f"Chosen numbers: {currentTab}")

        if self.currentTabIndex in (1, 2):
            """ Choosing algorithm to execute """
            self.algoValues = [["Choose algorithm","Fibonacci recursive", "Fibonacci iterative"], ["Choose algorithm","Harmonic recursion", "Harmonic linear"]]
            
            self.algoChoise = CTkComboBox(self.tab(f"{currentTab}"), values=self.algoValues[self.currentTabIndex-1], width=180, 
                                            command=self.algoChange)
            self.algoChoise.place(relx=0.8, rely=0.1) 


            """ Checkbox for showing or not results online """
            self.showResults = CTkCheckBox(self.tab(f"{currentTab}"), text="Show graphs", fg_color="#C850C0", checkbox_height=30,
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
            self.btnSteps = CTkButton(self.tab(f"{currentTab}"), text="Submit number of steps", corner_radius=32, fg_color="#F31313",
                                        hover_color="#F31313", text_color = "#000000", width=180, command=self.clickedEntrySteps)
            self.btnSteps.place(relx=0.8, rely=0.34)


            """ Entry for inputing number of runs of algorithm's execution """
            self.entryRuns=CTkEntry(self.tab(f"{currentTab}"), placeholder_text="Number of runs", width=180)
            self.entryRuns.place(relx=0.8, rely=0.45)
            self.entryRuns.focus()


            """ Slider for choosing number of runs of algorithm's execution """
            self.sliderRuns = CTkSlider(self.tab(f"{currentTab}"), from_=0, to=100, number_of_steps=10, button_color="#C850C0", 
                                            progress_color="#C850C0", width=180, command=self.numberRuns)
            self.sliderRuns.place(relx=0.8, rely=0.505)


            """ Button for submiting number of runs of algorithm's execution """ 
            self.btnRuns = CTkButton(self.tab(f"{currentTab}"), text="Submit number of runs", corner_radius=32, fg_color="#F31313",
                                        hover_color="#F31313", text_color = "#000000", width=180, command=self.clickedEntryRuns)
            self.btnRuns.place(relx=0.8, rely=0.54)


            """ RUN button runs algorithm """     
            self.btnRun = CTkButton(self.tab(f"{currentTab}"), text="Run", corner_radius=32, fg_color="#3114F2",
                    hover_color="#6D13FF", width=180, command=self.clickedRun)
            self.btnRun.place(relx=0.8, rely=0.65)

            """ About RUN button """
            self.labelRun = CTkLabel(self.tab(f"{currentTab}"), text="Run algorithms")
            self.labelRun.place(relx=0.85,rely=0.71)

            """ Frame for showing code to be executed """
            self.frame = CTkScrollableFrame(self.tab(f"{currentTab}"), border_width=5, border_color="#FFCC70",
                    width=1000, height=600)
            self.frame.pack(expand=True, padx=275)

            """ Start label for frame for showing code to be executed """
            self.frlabel = CTkLabel(master=self.frame, text="")
            self.frlabel.pack(expand=True)

            """ Label for graphs """
            self.plotLabel = CTkLabel(master=self.frame, anchor='e', text='')
            self.plotScaledLabel = CTkLabel(master=self.frame,anchor='w', text='')
            self.plotLabel.pack(expand=True)
            self.plotScaledLabel.pack(expand=True)

            """ Results for plotting """
            self.resultTotal =[]
        

            

    """ Show code to execute after choosing algorithm """
    def algoChange(self, value):
        file =  open(f"codeLabels/{value}.txt", "r")
        code = file.read()
        file.close()
        logging.info(f"Chosen algorithm: {value}")
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
        self.btnSteps.configure(hover_color="#13F33F", fg_color="#13F33F")
        
    """ Inputing runs of runs """
    def numberRuns(self, value):
            value = int(value)
            self.entryRuns.delete(0, 5)
            self.entryRuns.insert(0, f"{value}")
            
    """ Submiting number of runs """
    def clickedEntryRuns(self):
        num = int(self.entryRuns.get())
        self.sliderRuns.set(num)
        self.btnRuns.configure(hover_color="#13F33F", fg_color="#13F33F")
            
    """ Running algorithm """
    def clickedRun(self):
        if self.showResults.get() == 1:
            self.cleanfrlabel()
        algName = self.algoChoise.get()
        alg = str(self.currentTabIndex-1) + str(self.algoValues[self.currentTabIndex-1].index(algName))
        steps = int(self.entrySteps.get())
        runs = int(self.entryRuns.get())
        command = f"algs/{alg}.py"
        self.resultTotal = [0] *steps
        
        logging.info(f"{algName} ran")

        for self.round in range(runs):  
            for self.step in range (steps):
                result = subprocess.Popen(["python", command, str(self.step)], stdout=subprocess.PIPE, universal_newlines=True)
                
                if platform.system() == 'Windows':
                    psutil.Process(result.pid).nice(psutil.REALTIME_PRIORITY_CLASS)
                else:
                    psutil.Process(result.pid).nice(-20)
                
                
                self.output = result.stdout.read()
                self.resultTotal[self.step] += (int(self.output.rstrip())/(int(self.entryRuns.get())))
                logging.info(f"result {algName} {self.step+1} step, {self.round+1} round: {self.output}")
    
        """ Condition to create graphs """
        if self.showResults.get() == 1:
            drowPlots.plotting(steps, self.resultTotal, algName)

            self.plotNormal = CTkImage(light_image=Image.open(f"resultPlots/{algName}_average.png"),size=(375, 300))
            self.plotLogScaled = CTkImage(light_image=Image.open(f"resultPlots/{algName}_average_log_scaled.png"),size=(375, 300))
            self.plotInput()

        """ Return unsubmitted color """
        self.btnSteps.configure(hover_color="#F31313", fg_color="#F31313")
        self.btnRuns.configure(hover_color="#F31313", fg_color="#F31313")

    """ Do not show algorithm if graphs were chosen to show """
    def cleanfrlabel(self):
        self.resultTotal = []
        self.frlabel.configure(text="")  
        self.plotLabel.configure(image="", text = "")
        self.plotScaledLabel.configure(image="", text ="") 
    
    """ Graphs paste """
    def plotInput(self):
        self.frlabel.configure(text="")  
        self.plotLabel.configure(image=self.plotNormal, text="")
        self.plotScaledLabel.configure(image=self.plotLogScaled, text="")

""" Initial class """
class App(CTk):
    def __init__(self):
        super().__init__()

        """Setting appearance and geometry"""
        set_appearance_mode("System")
        set_default_color_theme("blue") 

        self.geometry("1000x600+400x400")
        self.maxsize(1000, 600)
        self.title("Experiment")

        self.iconbitmap("icon.ico")

        self.tabview = tabView(master=self)
        

if __name__ == "__main__": 

    """Logger setup"""
    logging.basicConfig(level=logging.INFO, filename="experiment_log_info.log",filemode="w", format="%(asctime)s %(levelname)s %(message)s")

    app = App()
    app.mainloop()

    
