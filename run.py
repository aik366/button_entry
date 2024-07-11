import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


def button_callback():
    print(f'button clicked\n{entry_1.get()}\n{entry_1.cget("border_color")}\n{button.cget("border_color")}')


app = ctk.CTk()
app.geometry("300x510+720+250")
app.title("New Account")

img = ctk.CTkImage(Image.open("images/login.png"), size=(220, 220))
label = ctk.CTkLabel(app, text="", image=img)
label.pack()

entry_1 = ctk.CTkEntry(app, width=220, height=50, corner_radius=25, border_width=2, fg_color="transparent",
                       font=("Roboto", 18), placeholder_text="Username", )
entry_1.pack(padx=20, pady=10)

entry_2 = ctk.CTkEntry(app, width=220, height=50, corner_radius=25, border_width=2, fg_color="transparent",
                       font=("Roboto", 18), placeholder_text="Password", show="*")
entry_2.pack(padx=20, pady=10)

entry_3 = ctk.CTkEntry(app, width=220, height=50, corner_radius=25, border_width=2, fg_color="transparent",
                       font=("Roboto", 18), placeholder_text="Confirm Password", show="*")
entry_3.pack(padx=20, pady=10)

button = ctk.CTkButton(app, text="Register", width=220, height=50, corner_radius=25, command=button_callback,
                       border_width=2, fg_color="transparent", hover_color='#565B5E', font=("Roboto", 18))
button.pack(padx=20, pady=10)

app.mainloop()
