import customtkinter as ctk

# create main window, size 500x400px and 20,20 px margin from top left corner
app = ctk.CTk()
app.geometry("500x400+20+20")

# tabView tabs names
tab1Name = "Tab1Name"
tab2Name = "Tab2Name"

def tabViewTabChangeClick():
    print(f"Click event once on new clicked tab. You Click: {tabView.get()}")

def tabViewTab1Click(event):
    print(f"Every click on tab1 body. You Click: {event}")

tabView = ctk.CTkTabview(master=app, width=200, height=70, command=tabViewTabChangeClick)
tabView.pack(expand=True, fill="both")

tab1 = tabView.add(tab1Name)
tab2 = tabView.add(tab2Name)

#tab1.bind("<Button-1>", command=tabViewTab1Click)

app.mainloop()