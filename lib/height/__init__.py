import customtkinter as ctk

padXMain = 20
padYMain = 10

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Height')

        self.main_frame = ctk.CTkFrame(self, width=250, height=250)
        self.main_frame.grid(row=0, column=0, padx=25, pady=25)

        self.mainText = ctk.CTkLabel(self.main_frame, text='Height Converter')
        self.mainText.grid(row=0, column=0, columnspan=3, padx=padXMain, pady=padYMain)

        self.to_var = ctk.StringVar(value='Meters')
        self.for_var = ctk.StringVar(value='Meters')

        # 'To' radio button
        self.toMeters = ctk.CTkRadioButton(self.main_frame, variable=self.to_var, value='Meters', text='Meters')
        self.toMeters.grid(row=1, column=0, padx=padXMain, pady=padYMain)
        
        self.toCentimeter = ctk.CTkRadioButton(self.main_frame, variable=self.to_var, value='Centimeters', text='Centimeters')
        self.toCentimeter.grid(row=2, column=0, padx=padXMain, pady=padYMain)

        self.toFeet = ctk.CTkRadioButton(self.main_frame, variable=self.to_var, value='Feet', text='Feet')
        self.toFeet.grid(row=3, column=0, padx=padXMain, pady=padYMain)

        self.toInches = ctk.CTkRadioButton(self.main_frame, variable=self.to_var, value='Inches', text='Inches')
        self.toInches.grid(row=4, column=0, padx=padXMain, pady=padYMain)

        # 'For' radio button
        self.forText = ctk.CTkLabel(self.main_frame, text='For')
        self.forText.grid(row=1, column=1, rowspan=4, padx=padXMain, pady=padYMain)

        self.forMeters = ctk.CTkRadioButton(self.main_frame, variable=self.for_var, value='Meters', text='Meters')
        self.forMeters.grid(row=1, column=2, padx=padXMain, pady=padYMain)
        
        self.forCentimeter = ctk.CTkRadioButton(self.main_frame, variable=self.for_var, value='Centimeters', text='Centimeters')
        self.forCentimeter.grid(row=2, column=2, padx=padXMain, pady=padYMain)

        self.forFeet = ctk.CTkRadioButton(self.main_frame, variable=self.for_var, value='Feet', text='Feet')
        self.forFeet.grid(row=3, column=2, padx=padXMain, pady=padYMain)

        self.forInches = ctk.CTkRadioButton(self.main_frame, variable=self.for_var, value='Inches', text='Inches')
        self.forInches.grid(row=4, column=2, padx=padXMain, pady=padYMain)

        self.submitButton = ctk.CTkButton(self.main_frame, text='Submit', command=self.submit)
        self.submitButton.grid(row=5, column=1, padx=padXMain, pady=padYMain)

        self.printArea = ctk.CTkLabel(self)

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

        height_dialog = ctk.CTkInputDialog(text='Type the height', title='Input Height')
        try:
            input_value = height_dialog.get_input()
            conversion = float(input_value)
        except Exception:
            self.printError = ctk.CTkLabel(self.printArea, text='ERROR! Invalid input.')
            self.printError.grid(row=0, column=0, padx=padXMain, pady=padYMain)
            return

        result_text = ''
        if to == 'Meters':
            if fr == 'Centimeters':
                result = conversion * 100
                result_text = f'{conversion}m results in {result}cm'
            elif fr == 'Feet':
                result = conversion * 3.281
                result_text = f'{conversion}m results in {result}feet'
            elif fr == 'Inches':
                result = conversion * 39.37
                result_text = f'{conversion}m results in {result}inches'
        elif to == 'Centimeters':
            if fr == 'Meters':
                result = conversion / 100
                result_text = f'{conversion}cm results in {result}m'
            elif fr == 'Feet':
                result = conversion / 30.48
                result_text = f'{conversion}cm results in {result}feet'
            elif fr == 'Inches':
                result = conversion / 2.54
                result_text = f'{conversion}cm results in {result}inches'
        elif to == 'Feet':
            if fr == 'Meters':
                result = conversion / 3.281
                result_text = f'{conversion}feet results in {result}m'
            elif fr == 'Centimeters':
                result = conversion * 30.48
                result_text = f'{conversion}feet results in {result}cm'
            elif fr == 'Inches':
                result = conversion * 12
                result_text = f'{conversion}feet results in {result}inches'
        elif to == 'Inches':
            if fr == 'Meters':
                result = conversion / 39.37
                result_text = f'{conversion}inches results in {result}m'
            elif fr == 'Centimeters':
                result = conversion * 2.54
                result_text = f'{conversion}inches results in {result}cm'
            elif fr == 'Feet':
                result = conversion / 12
                result_text = f'{conversion}inches results in {result}feet'

        self.heightCard = ctk.CTkLabel(self.printArea, text=result_text)
        self.heightCard.grid(row=0, column=0, padx=padXMain, pady=padYMain)

app = App()
app.mainloop()