import subprocess
import os
import tkinter
import customtkinter
import psutil

ver = "B2.3"

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("328x318")
app.resizable(False, False)
app.title("EasyActions " + ver)
app.iconbitmap("Dependencies/EasyActions.ico")

#Thanks geeksforgeeks.org
if not os.path.isdir("Custom"):
    os.mkdir("Custom")


def restart_explorer():
   os.system("TASKKILL /f /im explorer.exe")
   subprocess.Popen("explorer")


def optimpize_ram():
    subprocess.run("Dependencies\Optimize.bat")

def custom_module():
    if not switch_2:
        if switch_1.get():
            os.system("start /MIN Custom\\" + entry_1.get() + ".bat")
        else:
            os.system("start Custom\\" + entry_1.get() + ".bat")
    else:
        os.system("py Custom\\" + entry_1.get() + ".py")

def mcheck():
    progressbar.set(psutil.virtual_memory()[2] / 100)
    progressbar2.set(float(psutil.cpu_percent()) / 100)
    app.after(100, mcheck)

frame_1 = customtkinter.CTkFrame(master=app, corner_radius=0)
frame_1.place(relheight=1.0, relwidth=0.6)
# frame_1.pack(pady=20, padx=40, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(text="EasyActions    ", font=customtkinter.CTkFont(size=20, weight="bold"), master=frame_1, justify=tkinter.LEFT)
label_1.pack(pady=10, padx=10)

tinylabel_1 = customtkinter.CTkLabel(text=ver, master=frame_1, text_color="gray", font=customtkinter.CTkFont(size=15))
tinylabel_1.place(x=150, y=11)

button_1 = customtkinter.CTkButton(text="Restart Explorer", master=frame_1, command=restart_explorer)
button_1.pack(pady=10, padx=10)

button_2 = customtkinter.CTkButton(text="Optimize Ram", master=frame_1, command=optimpize_ram)
button_2.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Custom Module")
entry_1.pack(pady=10, padx=10)

button_3 = customtkinter.CTkButton(text="Run Custom Module", master=frame_1, command=custom_module, bg_color="#262626")
button_3.pack(pady=10, padx=10)

switch_2 = customtkinter.CTkCheckBox(text="Custom Modules use py", master=frame_1)
switch_2.pack(pady=5, padx=10)

switch_1 = customtkinter.CTkCheckBox(text="Run Modules Minimized", master=frame_1)
switch_1.pack(pady=5, padx=10)

label_3 = customtkinter.CTkLabel(text="RAM", master=None, justify=tkinter.LEFT)
label_3.place(x=230, y=65)
progressbar = customtkinter.CTkProgressBar(master=None, orientation="vertical", progress_color=("#f54242"))
progressbar.place(x=240, y=90)

label_4 = customtkinter.CTkLabel(text="CPU", master=None, justify=tkinter.LEFT)
label_4.place(x=270, y=65)
progressbar2 = customtkinter.CTkProgressBar(master=None, orientation="vertical", progress_color=("#f5a442"))
progressbar2.place(x=280, y=90)

label_5 = customtkinter.CTkLabel(text="System Stats", master=None, justify=tkinter.LEFT, font=customtkinter.CTkFont(weight="bold"))
label_5.place(x=218, y=20)

app.after(100, mcheck())
app.mainloop()