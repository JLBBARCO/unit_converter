import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Unit Converter')

        self.main_frame = ctk.CTkFrame(self, width=250, height=250)
        self.main_frame.grid(row=0, column=0, padx=25, pady=25)

        self.text = ctk.CTkLabel(self.main_frame, text='Converts This Unities')
        self.text.grid(row=0, column=0, padx=100, pady=10)

        self.temperature = ctk.CTkButton(self.main_frame, text='Temperature', command=self.temperatureButton)
        self.temperature.grid(row=1, column=0, padx=100, pady=10)

        self.height = ctk.CTkButton(self.main_frame, text='Height', command=self.heightButton)
        self.height.grid(row=2, column=0, padx=100, pady=10)

        self.speed = ctk.CTkButton(self.main_frame, text='Speed', command=self.speedButton)
        self.speed.grid(row=3, column=0, padx=100, pady=10)

    def temperatureButton(self):
        from lib import temperature

    def heightButton(self):
        from lib import height

    def speedButton(self):
        from lib import speed

app = App()
app.mainloop()