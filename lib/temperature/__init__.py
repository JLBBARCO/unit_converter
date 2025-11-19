import customtkinter as ctk

padXMain = 20
padYMain = 10

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Temperature')

        self.main_frame = ctk.CTkFrame(self, width=250, height=250)
        self.main_frame.grid(row=0, column=0, padx=25, pady=25)

        self.mainText = ctk.CTkLabel(self.main_frame, text='Temperature Converter')
        self.mainText.grid(row=0, column=0, columnspan=3, padx=padXMain, pady=padYMain)

        self.to_var = ctk.StringVar(value='Celsius')
        self.for_var = ctk.StringVar(value='Celsius')

        # 'To' radio buttons
        self.toCelsius = ctk.CTkRadioButton(self.main_frame, variable=self.to_var, value='Celsius', text='Celsius')
        self.toCelsius.grid(row=2, column=0, padx=padXMain, pady=padYMain)

        self.toFahrenheit = ctk.CTkRadioButton(self.main_frame, variable=self.to_var, value='Fahrenheit', text='Fahrenheit')
        self.toFahrenheit.grid(row=3, column=0, padx=padXMain, pady=padYMain)

        self.toKelvin = ctk.CTkRadioButton(self.main_frame, variable=self.to_var, value='Kelvin', text='Kelvin')
        self.toKelvin.grid(row=4, column=0, padx=padXMain, pady=padYMain)

        self.forText = ctk.CTkLabel(self.main_frame, text='For')
        self.forText.grid(row=2, column=1, rowspan=3, padx=padXMain, pady=padYMain)

        # 'For' radio buttons
        self.forCelsius = ctk.CTkRadioButton(self.main_frame, variable=self.for_var, value='Celsius', text='Celsius')
        self.forCelsius.grid(row=2, column=2, padx=padXMain, pady=padYMain)

        self.forFahrenheit = ctk.CTkRadioButton(self.main_frame, variable=self.for_var, value='Fahrenheit', text='Fahrenheit')
        self.forFahrenheit.grid(row=3, column=2, padx=padXMain, pady=padYMain)

        self.forKelvin = ctk.CTkRadioButton(self.main_frame, variable=self.for_var, value='Kelvin', text='Kelvin')
        self.forKelvin.grid(row=4, column=2, padx=padXMain, pady=padYMain)

        self.submitButton = ctk.CTkButton(self.main_frame, text='Submit', command=self.submit)
        self.submitButton.grid(row=5, column=1, padx=padXMain, pady=padYMain)

        self.printArea = ctk.CTkFrame(self)

    def submit(self):
        self.printArea.destroy()
        self.printArea = ctk.CTkFrame(self)
        self.printArea.grid(row=1, column=0, padx=25, pady=25)
        
        to = self.to_var.get()
        fr = self.for_var.get()
        if to == fr:
            self.printError = ctk.CTkLabel(self.printArea, text='ERROR! The options cannot be the same')
            self.printError.grid(row=0, column=0, padx=padXMain, pady=padYMain)
            return

        temperature_dialog = ctk.CTkInputDialog(text='Type the temperature', title='Input Temperature')
        try:
            input_value = temperature_dialog.get_input()
            conversion = float(input_value)
        except Exception:
            self.printError = ctk.CTkLabel(self.printArea, text='ERROR! Invalid input.')
            self.printError.grid(row=0, column=0, padx=padXMain, pady=padYMain)
            return

        result_text = ""
        if to == 'Celsius' and fr == 'Fahrenheit':
            result = (conversion * 9 / 5) + 32
            result_text = f'{conversion}°C results in {result}°F'
        elif to == 'Celsius' and fr == 'Kelvin':
            result = conversion + 273.15
            result_text = f'{conversion}°C results in {result}K'
        elif to == 'Fahrenheit' and fr == 'Celsius':
            result = (conversion - 32) * 5 / 9
            result_text = f'{conversion}°F results in {result}°C'
        elif to == 'Fahrenheit' and fr == 'Kelvin':
            result = (conversion - 32) * 5 / 9 + 273.15
            result_text = f'{conversion}°F results in {result}K'
        elif to == 'Kelvin' and fr == 'Celsius':
            result = conversion - 273.15
            result_text = f'{conversion}K results in {result}°C'
        elif to == 'Kelvin' and fr == 'Fahrenheit':
            result = (conversion - 273.15) * 9 / 5 + 32
            result_text = f'{conversion}K results in {result}°F'
        else:
            result_text = "ERROR! Conversion not supported."

        self.temperatureCard = ctk.CTkLabel(self.printArea, text=result_text)
        self.temperatureCard.grid(row=0, column=0, padx=padXMain, pady=padYMain)

app = App()
app.mainloop()