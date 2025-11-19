import customtkinter as ctk

padXMain = 20
padYMain = 10

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Speed')

        self.main_frame = ctk.CTkFrame(self, width=250, height=250)
        self.main_frame.grid(row=0, column=0, padx=25, pady=25)

        self.mainText = ctk.CTkLabel(self.main_frame, text='Speed Converter')
        self.mainText.grid(row=0, column=0, columnspan=3, padx=padXMain, pady=padYMain)

        self.to_var = ctk.StringVar(value='Km/h')
        self.for_var = ctk.StringVar(value='Km/h')

        # 'To' radio buttons
        self.toKilometersPerHour = ctk.CTkRadioButton(self.main_frame, variable=self.to_var, value='Km/h', text='Km/h')
        self.toKilometersPerHour.grid(row=1, column=0, padx=padXMain, pady=padYMain)

        self.toMetersPerSecond = ctk.CTkRadioButton(self.main_frame, variable=self.to_var, value='m/s', text='m/s')
        self.toMetersPerSecond.grid(row=2, column=0, padx=padXMain, pady=padYMain)

        self.toMilesPerHour = ctk.CTkRadioButton(self.main_frame, variable=self.to_var, value='mph', text='mph')
        self.toMilesPerHour.grid(row=3, column=0, padx=padXMain, pady=padYMain)

        self.toFeetPerSecond = ctk.CTkRadioButton(self.main_frame, variable=self.to_var, value='feet/s', text='feet/s')
        self.toFeetPerSecond.grid(row=4, column=0, padx=padXMain, pady=padYMain)

        self.toKnot = ctk.CTkRadioButton(self.main_frame, variable=self.to_var, value='Knot', text='Knot')
        self.toKnot.grid(row=5, column=0, padx=padXMain, pady=padYMain)

        # 'For' radio buttons
        self.forText = ctk.CTkLabel(self.main_frame, text='For')
        self.forText.grid(row=1, rowspan=5, column=1, padx=padXMain, pady=padYMain)
        
        self.forKilometersPerHour = ctk.CTkRadioButton(self.main_frame, variable=self.for_var, value='Km/h', text='Km/h')
        self.forKilometersPerHour.grid(row=1, column=2, padx=padXMain, pady=padYMain)

        self.forMetersPerSecond = ctk.CTkRadioButton(self.main_frame, variable=self.for_var, value='m/s', text='m/s')
        self.forMetersPerSecond.grid(row=2, column=2, padx=padXMain, pady=padYMain)

        self.forMilesPerHour = ctk.CTkRadioButton(self.main_frame, variable=self.for_var, value='mph', text='mph')
        self.forMilesPerHour.grid(row=3, column=2, padx=padXMain, pady=padYMain)

        self.forFeetPerSecond = ctk.CTkRadioButton(self.main_frame, variable=self.for_var, value='feet/s', text='feet/s')
        self.forFeetPerSecond.grid(row=4, column=2, padx=padXMain, pady=padYMain)

        self.forKnot = ctk.CTkRadioButton(self.main_frame, variable=self.for_var, value='Knot', text='Knot')
        self.forKnot.grid(row=5, column=2, padx=padXMain, pady=padYMain)

        self.submitButton = ctk.CTkButton(self.main_frame, text='Submit', command=self.submit)
        self.submitButton.grid(row=6, column=1, padx=padXMain, pady=padYMain)

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

        speed_dialog = ctk.CTkInputDialog(text='Type the speed', title='Input Speed')
        try:
            input_speed = speed_dialog.get_input()
            conversion = float(input_speed)
        except Exception:
            self.printError = ctk.CTkLabel(self.printArea, text='ERROR! Invalid input.')
            self.printError.grid(row=0, column=0, padx=padXMain, pady=padYMain)
            return

        result_text = ''
        if to == 'Km/h':
            if fr == 'm/s':
                result = conversion / 3.6
                result_text = f'{conversion} Km/h = {result:.2f} m/s'
            elif fr == 'mph':
                result = conversion / 1.609
                result_text = f'{conversion} Km/h = {result:.2f} mph'
            elif fr == 'feet/s':
                result = conversion * 0.911344
                result_text = f'{conversion} Km/h = {result:.2f} feet/s'
            elif fr == 'Knot':
                result = conversion / 1.852
                result_text = f'{conversion} Km/h = {result:.2f} Knot'
        elif to == 'm/s':
            if fr == 'Km/h':
                result = conversion * 3.6
                result_text = f'{conversion} m/s = {result:.2f} Km/h'
            elif fr == 'mph':
                result = conversion * 2.237
                result_text = f'{conversion} m/s = {result:.2f} mph'
            elif fr == 'feet/s':
                result = conversion * 3.281
                result_text = f'{conversion} m/s = {result:.2f} feet/s'
            elif fr == 'Knot':
                result = conversion * 1.944
                result_text = f'{conversion} m/s = {result:.2f} Knot'
        elif to == 'mph':
            if fr == 'Km/h':
                result = conversion * 1.609
                result_text = f'{conversion} mph = {result:.2f} Km/h'
            elif fr == 'm/s':
                result = conversion / 2.237
                result_text = f'{conversion} mph = {result:.2f} m/s'
            elif fr == 'feet/s':
                result = conversion * 1.467
                result_text = f'{conversion} mph = {result:.2f} feet/s'
            elif fr == 'Knot':
                result = conversion / 1.151
                result_text = f'{conversion} mph = {result:.2f} Knot'
        elif to == 'feet/s':
            if fr == 'Km/h':
                result = conversion * 1.097
                result_text = f'{conversion} feet/s = {result:.2f} Km/h'
            elif fr == 'm/s':
                result = conversion / 3.281
                result_text = f'{conversion} feet/s = {result:.2f} m/s'
            elif fr == 'mph':
                result = conversion / 1.467
                result_text = f'{conversion} feet/s = {result:.2f} mph'
            elif fr == 'Knot':
                result = conversion / 1.688
                result_text = f'{conversion} feet/s = {result:.2f} Knot'
        elif to == 'Knot':
            if fr == 'Km/h':
                result = conversion * 1.852
                result_text = f'{conversion} Knot = {result:.2f} Km/h'
            elif fr == 'm/s':
                result = conversion / 1.944
                result_text = f'{conversion} Knot = {result:.2f} m/s'
            elif fr == 'mph':
                result = conversion * 1.151
                result_text = f'{conversion} Knot = {result:.2f} mph'
            elif fr == 'feet/s':
                result = conversion * 1.688
                result_text = f'{conversion} Knot = {result:.2f} feet/s'

        self.speedCard = ctk.CTkLabel(self.printArea, text=result_text)
        self.speedCard.grid(row=0, column=0, padx=padXMain, pady=padYMain)

app = App()
app.mainloop()