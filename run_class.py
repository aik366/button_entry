import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class NewAccount(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("300x510+720+250")
        self.title("New Account")

        self.img = ctk.CTkImage(Image.open("images/login.png"), size=(220, 220))
        self.label = ctk.CTkLabel(self, text="", image=self.img)
        self.label.pack()

        self.entry_1 = ctk.CTkEntry(self, width=220, height=50, corner_radius=25, border_width=2,
                                    fg_color="transparent",
                                    font=("Roboto", 18), placeholder_text="Username", )
        self.entry_1.pack(padx=20, pady=10)

        self.entry_2 = ctk.CTkEntry(self, width=220, height=50, corner_radius=25, border_width=2,
                                    fg_color="transparent",
                                    font=("Roboto", 18), placeholder_text="Password", show="*")
        self.entry_2.pack(padx=20, pady=10)

        self.entry_3 = ctk.CTkEntry(self, width=220, height=50, corner_radius=25, border_width=2,
                                    fg_color="transparent",
                                    font=("Roboto", 18), placeholder_text="Confirm Password", show="*")
        self.entry_3.pack(padx=20, pady=10)

        self.button = ctk.CTkButton(self, text="Register", width=220, height=50, corner_radius=25, font=("Roboto", 18),
                                    border_width=2, fg_color="transparent", hover_color='#565B5E',
                                    command=self.register_func)
        self.button.pack(padx=20, pady=10)

    def register_func(self):
        print(f"{self.entry_1.get()}\n{self.entry_1.cget('border_color')}\n{self.button.cget('border_color')}")


if __name__ == "__main__":
    app = NewAccount()
    app.mainloop()
