import tkinter as tk
import customtkinter as ctk
import json
import math

# Set the appearance mode and color theme for customtkinter
ctk.set_appearance_mode("dark")  # Options: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Options: "blue" (default), "green", "dark-blue"
root = ctk.CTk()

class ConverterApp:
    def __init__(self, root):
        # Initialize the ConverterApp class
        self.root = root
        self.root.title("Converter App")  # Set the title of the window
        self.root.geometry("500x700")  # Set the window size

        self.history = []  # Initialize an empty list for history
        self.load_history()  # Load history from file if available

        self.favorites = []  # Initialize an empty list for favorites
        self.load_favorites()  # Load favorites from file if available

        self.current_theme = "default"  # Set the initial theme to default

        self.create_home_page()  # Create the home page

    def create_home_page(self):
        # Create the home page layout
        self.clear_frame()  # Clear any existing content in the window

        home_frame = ctk.CTkFrame(self.root)  # Create a frame for the home page
        home_frame.pack(padx=10, pady=10, fill="both", expand=True)  # Pack the frame with padding

        # Add a title label to the home page
        ctk.CTkLabel(home_frame, text="CONVERTOCALC", font=("Arial", 32, "bold")).pack(pady=20)
    
        # Add the illustrative line below the title
        ctk.CTkLabel(home_frame, text="Your Ultimate Toolkit for Quick, Accurate Calculations!", font=("Arial", 16, "bold")).pack(pady=10)

        # Add a "Get Started" button to the home page
        ctk.CTkButton(home_frame, text="Get Started", font=("Arial", 20), command=self.create_main_menu).pack(pady=20)

        # Add a frame for theme selection
        theme_frame = ctk.CTkFrame(home_frame)
        theme_frame.pack(pady=10)

        # Add labels and buttons for selecting color themes
        ctk.CTkLabel(theme_frame, text="Choose Color Theme:", font=("Arial", 16)).pack(pady=10)
        ctk.CTkButton(theme_frame, text="Default", command=self.set_default_theme).pack(pady=5)
        ctk.CTkButton(theme_frame, text="Black-Orange", command=self.set_black_orange_theme).pack(pady=5)
        ctk.CTkButton(theme_frame, text="Black-Yellow", command=self.set_black_yellow_theme).pack(pady=5)

    def set_default_theme(self):
        # Set the theme to default
        self.current_theme = "default"
        self.apply_theme()  # Apply the selected theme

    def set_black_orange_theme(self):
        # Set the theme to black-orange
        self.current_theme = "black-orange"
        self.apply_theme()  # Apply the selected theme

    def set_black_yellow_theme(self):
        # Set the theme to black-yellow
        self.current_theme = "black-yellow"
        self.apply_theme()  # Apply the selected theme

    def apply_theme(self):
        # Apply the selected theme to the entire application
        if self.current_theme == "default":
            ctk.set_default_color_theme("blue")
            self.root.configure(bg=ctk.ThemeManager.theme['CTk']['fg_color'])  # Set default background color
        elif self.current_theme == "black-orange":
            self.root.configure(bg="black")  # Set background to black for black-orange theme
        elif self.current_theme == "black-yellow":
            self.root.configure(bg="black")  # Set background to black for black-yellow theme

        self.update_theme(self.root)  # Update the theme for all widgets

    def update_theme(self, widget):
        # Recursively update the theme for each child widget
        for child in widget.winfo_children():
            if isinstance(child, ctk.CTkButton):
                # Set button colors based on the current theme
                if self.current_theme == "black-orange":
                    child.configure(fg_color="darkorange", hover_color="orange")
                elif self.current_theme == "black-yellow":
                    child.configure(fg_color="darkgoldenrod", hover_color="goldenrod")
                else:
                    child.configure(fg_color=None, hover_color=None)
            elif isinstance(child, (ctk.CTkFrame, ctk.CTkLabel, ctk.CTkEntry, ctk.CTkComboBox)):
                # Continue updating the theme for child widgets
                self.update_theme(child)

    def create_main_menu(self):
        # Create the main menu layout
        self.clear_frame()  # Clear any existing content in the window

        main_frame = ctk.CTkFrame(self.root)  # Create a frame for the main menu
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)  # Pack the frame with padding

        # Add a label and buttons for each menu option
        ctk.CTkLabel(main_frame, text="CONVERTOCALC APP", font=("Arial", 24)).pack(pady=20)
        ctk.CTkButton(main_frame, text="Converters", command=self.create_converter_menu).pack(pady=10)
        ctk.CTkButton(main_frame, text="Calculators", command=self.create_calculator_menu).pack(pady=10)
        ctk.CTkButton(main_frame, text="View Favorites", command=self.view_favorites).pack(pady=10)
        ctk.CTkButton(main_frame, text="View History", command=self.view_history).pack(pady=10)
        ctk.CTkButton(main_frame, text="Clear Favorites", command=self.clear_favorites).pack(pady=10)
        ctk.CTkButton(main_frame, text="Clear History", command=self.clear_history).pack(pady=10)

        # Add a home button to return to the home page
        ctk.CTkButton(main_frame, text="Home", command=self.create_home_page).pack(pady=10)

        self.apply_theme()  # Apply the selected theme

    def create_converter_menu(self):
        # Create the converters menu layout
        self.clear_frame()  # Clear any existing content in the window

        converter_frame = ctk.CTkFrame(self.root)  # Create a frame for the converters menu
        converter_frame.pack(padx=10, pady=10, fill="both", expand=True)  # Pack the frame with padding

        # Add a label and buttons for each converter option
        ctk.CTkLabel(converter_frame, text="CONVERTORS", font=("Arial", 20)).pack(pady=20)
        ctk.CTkButton(converter_frame, text="Length", command=self.create_length_converter).pack(pady=10)
        ctk.CTkButton(converter_frame, text="Temperature", command=self.create_temperature_converter).pack(pady=10)
        ctk.CTkButton(converter_frame, text="Currency", command=self.create_currency_converter).pack(pady=10)
        ctk.CTkButton(converter_frame, text="Back", command=self.create_main_menu).pack(pady=10)
        ctk.CTkButton(converter_frame, text="Home", command=self.create_home_page).pack(pady=10)

        self.apply_theme()  # Apply the selected theme

    def create_calculator_menu(self):
        # Create the calculators menu layout
        self.clear_frame()  # Clear any existing content in the window

        calc_frame = ctk.CTkFrame(self.root)  # Create a frame for the calculators menu
        calc_frame.pack(padx=10, pady=10, fill="both", expand=True)  # Pack the frame with padding

        # Add a label and buttons for each calculator option
        ctk.CTkLabel(calc_frame, text="CALCULATORS", font=("Arial", 20)).pack(pady=20)
        ctk.CTkButton(calc_frame, text="Simple Calculator", command=self.create_simple_calculator).pack(pady=10)
        ctk.CTkButton(calc_frame, text="Scientific Calculator", command=self.create_scientific_calculator).pack(pady=10)
        ctk.CTkButton(calc_frame, text="BMI Calculator", command=self.create_bmi_calculator).pack(pady=10)
        ctk.CTkButton(calc_frame, text="Back", command=self.create_main_menu).pack(pady=10)
        ctk.CTkButton(calc_frame, text="Home", command=self.create_home_page).pack(pady=10)

        self.apply_theme()  # Apply the selected theme

    def create_length_converter(self):
        # Create the length converter layout
        self.clear_frame()  # Clear any existing content in the window

        length_frame = ctk.CTkFrame(self.root)  # Create a frame for the length converter
        length_frame.pack(padx=10, pady=10, fill="both", expand=True)  # Pack the frame with padding

        # Add labels, entry fields, and buttons for length conversion
        ctk.CTkLabel(length_frame, text="LENGTH CONVERTOR", font=("Arial", 20)).pack(pady=20)
        self.from_unit = ctk.CTkComboBox(length_frame, values=["Meters", "Kilometers", "Miles"])
        self.from_unit.pack(padx=5, pady=5)
        self.to_unit = ctk.CTkComboBox(length_frame, values=["Meters", "Kilometers", "Miles"])
        self.to_unit.pack(padx=5, pady=5)
        self.unit_value = ctk.CTkEntry(length_frame)
        self.unit_value.pack(padx=5, pady=5)
        self.convert_button = ctk.CTkButton(length_frame, text="Convert", command=self.convert_length)
        self.convert_button.pack(padx=5, pady=5)
        self.length_result = ctk.CTkLabel(length_frame, text="Result", font=("Arial", 16))
        self.length_result.pack(padx=5, pady=5)
        self.favorite_button = ctk.CTkButton(length_frame, text="Add to Favorites", command=self.add_unit_favorite)
        self.favorite_button.pack(padx=5, pady=5)
        ctk.CTkButton(length_frame, text="Back", command=self.create_converter_menu).pack(padx=5, pady=5)
        ctk.CTkButton(length_frame, text="Home", command=self.create_home_page).pack(padx=5, pady=5)

        self.apply_theme()  # Apply the selected theme

    def convert_length(self):
        # Perform length conversion and display the result
        try:
            value = float(self.unit_value.get())  # Get the input value from the user
        
            if value < 0:  # Check if the input value is negative
                raise ValueError("Length cannot be negative!")  # Raise an error for negative values
        
            from_unit = self.from_unit.get()  # Get the source unit
            to_unit = self.to_unit.get()  # Get the target unit
            conversion_factors = {"Meters": 1, "Kilometers": 1000, "Miles": 1609.34}  # Define conversion factors
            result = value * conversion_factors[from_unit] / conversion_factors[to_unit]  # Perform conversion
            self.length_result.configure(text=f"Result: {result:.2f} {to_unit}")  # Display the result
            self.add_to_history(f"{value} {from_unit} to {result:.2f} {to_unit}")  # Add conversion to history
        except ValueError as ve:
            self.length_result.configure(text=f"Error: {ve}")  # Display validation error for negative values
        except Exception as e:
            self.length_result.configure(text=f"Error: {e}")  # Handle other errors

    def create_temperature_converter(self):
        # Create the temperature converter layout
        self.clear_frame()  # Clear any existing content in the window

        temp_frame = ctk.CTkFrame(self.root)  # Create a frame for the temperature converter
        temp_frame.pack(padx=10, pady=10, fill="both", expand=True)  # Pack the frame with padding

        # Add labels, entry fields, and buttons for temperature conversion
        ctk.CTkLabel(temp_frame, text="TEMPERATURE CONVERTOR", font=("Arial", 20)).pack(pady=20)
        self.temp_type = ctk.CTkComboBox(temp_frame, values=["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
        self.temp_type.pack(padx=5, pady=5)
        self.temp_value = ctk.CTkEntry(temp_frame)
        self.temp_value.pack(padx=5, pady=5)
        self.temp_convert_button = ctk.CTkButton(temp_frame, text="Convert", command=self.convert_temperature)
        self.temp_convert_button.pack(padx=5, pady=5)
        self.temp_result = ctk.CTkLabel(temp_frame, text="Result", font=("Arial", 16))
        self.temp_result.pack(padx=5, pady=5)
        self.temp_favorite_button = ctk.CTkButton(temp_frame, text="Add to Favorites", command=self.add_temp_favorite)
        self.temp_favorite_button.pack(padx=5, pady=5)
        ctk.CTkButton(temp_frame, text="Back", command=self.create_converter_menu).pack(padx=5, pady=5)
        ctk.CTkButton(temp_frame, text="Home", command=self.create_home_page).pack(padx=5, pady=5)

        self.apply_theme()  # Apply the selected theme

    def convert_temperature(self):
        # Perform temperature conversion and display the result
        try:
            value = float(self.temp_value.get())  # Get the input value from the user
            temp_type = self.temp_type.get()  # Get the conversion type (Celsius to Fahrenheit or vice versa)
            if (value < -273.15 and "Celsius" in temp_type) or (value < -459.67 and "Fahrenheit" in temp_type):
                raise ValueError("Temperature below absolute zero!")  # Handle absolute zero cases
            if temp_type == "Celsius to Fahrenheit":
                result = (value * 9/5) + 32  # Convert Celsius to Fahrenheit
            elif temp_type == "Fahrenheit to Celsius":
                result = (value - 32) * 5/9  # Convert Fahrenheit to Celsius
            self.temp_result.configure(text=f"Result: {result:.2f}")  # Display the result
            self.add_to_history(f"{value} {temp_type} to {result:.2f}")  # Add conversion to history
        except Exception as e:
            self.temp_result.configure(text=f"Error: {e}")  # Handle errors

    def create_currency_converter(self):
        # Create the currency converter layout
        self.clear_frame()  # Clear any existing content in the window

        currency_frame = ctk.CTkFrame(self.root)  # Create a frame for the currency converter
        currency_frame.pack(padx=10, pady=10, fill="both", expand=True)  # Pack the frame with padding

        # Add labels, entry fields, and buttons for currency conversion
        ctk.CTkLabel(currency_frame, text="CURRENCY CONVERTOR", font=("Arial", 20)).pack(pady=20)
        self.from_currency = ctk.CTkComboBox(currency_frame, values=["USD", "EUR", "GBP", "PKR"])
        self.from_currency.pack(padx=5, pady=5)
        self.to_currency = ctk.CTkComboBox(currency_frame, values=["USD", "EUR", "GBP", "PKR"])
        self.to_currency.pack(padx=5, pady=5)
        self.currency_value = ctk.CTkEntry(currency_frame)
        self.currency_value.pack(padx=5, pady=5)
        self.currency_convert_button = ctk.CTkButton(currency_frame, text="Convert", command=self.convert_currency)
        self.currency_convert_button.pack(padx=5, pady=5)
        self.currency_result = ctk.CTkLabel(currency_frame, text="Result", font=("Arial", 16))
        self.currency_result.pack(padx=5, pady=5)
        self.currency_favorite_button = ctk.CTkButton(currency_frame, text="Add to Favorites", command=self.add_currency_favorite)
        self.currency_favorite_button.pack(padx=5, pady=5)
        ctk.CTkButton(currency_frame, text="Back", command=self.create_converter_menu).pack(padx=5, pady=5)
        ctk.CTkButton(currency_frame, text="Home", command=self.create_home_page).pack(padx=5, pady=5)

        self.apply_theme()  # Apply the selected theme

    def convert_currency(self):
        # Perform currency conversion and display the result
        try:
            value = float(self.currency_value.get())  # Get the input value from the user
        
            if value < 0:  # Check if the input value is negative
                raise ValueError("Amount cannot be negative!")  # Raise an error for negative values
        
            from_currency = self.from_currency.get()  # Get the source currency
            to_currency = self.to_currency.get()  # Get the target currency

            # Define exchange rates relative to USD (1 USD as the base)
            exchange_rates = {
                "USD": 1,
                "EUR": 0.85,  # 1 USD = 0.85 EUR
                "GBP": 0.75,  # 1 USD = 0.75 GBP
                "PKR": 276.58  # 1 USD = 276.58 PKR
            }

            # Convert from the base currency (USD) to the target currency
            if from_currency != "USD":
                value_in_usd = value / exchange_rates[from_currency]  # Convert to USD first
            else:
                value_in_usd = value

            result = value_in_usd * exchange_rates[to_currency]  # Convert from USD to target currency

            self.currency_result.configure(text=f"Result: {result:.2f} {to_currency}")  # Display the result
            self.add_to_history(f"{value} {from_currency} to {result:.2f} {to_currency}")  # Add conversion to history

        except ValueError as ve:
            self.currency_result.configure(text=f"Error: {ve}")  # Handle validation errors (like negative values)
        except Exception as e:
            self.currency_result.configure(text=f"Error: {e}")  # Handle other errors

    def create_simple_calculator(self):
        # Create the simple calculator layout
        self.clear_frame()  # Clear any existing content in the window

        calc_frame = ctk.CTkFrame(self.root)  # Create a frame for the simple calculator
        calc_frame.pack(padx=10, pady=10, fill="both", expand=True)  # Pack the frame with padding

        # Add an entry field and buttons for basic calculator operations
        ctk.CTkLabel(calc_frame, text="SIMPLE CALCULATOR", font=("Arial", 20)).pack(pady=20)
        self.calc_entry = ctk.CTkEntry(calc_frame, justify='right', font=("Arial", 18))
        self.calc_entry.pack(padx=5, pady=5, fill='x')

        button_frame = ctk.CTkFrame(calc_frame)  # Create a frame for the calculator buttons
        button_frame.pack(pady=10, padx=10)

        # Define the text for each button
        button_texts = [
            '1', '2', '3', '+',
            '4', '5', '6', '-',
            '7', '8', '9', 'x',
            '0', 'C', '=', '/'
        ]

        buttons = []
        # Create buttons and set their commands
        for text in button_texts:
            button = ctk.CTkButton(button_frame, text=text, width=80, height=60, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            buttons.append(button)

        # Arrange buttons in a grid layout
        for i in range(4):
            for j in range(4):
                buttons[i * 4 + j].grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

        for i in range(4):
            button_frame.grid_rowconfigure(i, weight=1)
            button_frame.grid_columnconfigure(i, weight=1)

        # Add back and home buttons
        ctk.CTkButton(calc_frame, text="Back", command=self.create_calculator_menu).pack(pady=10)
        ctk.CTkButton(calc_frame, text="Home", command=self.create_home_page).pack(pady=10)

        self.apply_theme()  # Apply the selected theme

    def on_button_click(self, char):
        # Handle button click events for the simple calculator
        if char == "=":
            self.calculate()  # Calculate the result
        elif char == "C":
            self.calc_entry.delete(0, tk.END)  # Clear the entry field
        else:
            self.calc_entry.insert(tk.END, char)  # Insert the clicked button character into the entry field

    def calculate(self):
        # Perform the calculation and display the result
        try:
            expression = self.calc_entry.get()  # Get the expression from the entry field
            expression = expression.replace('x', '*')  # Replace 'x' with '*' for multiplication
            result = eval(expression)  # Evaluate the expression
            self.calc_entry.delete(0, tk.END)  # Clear the entry field
            self.calc_entry.insert(tk.END, str(result))  # Display the result
            self.add_to_history(f"{expression} = {result}")  # Add the calculation to history
        except Exception as e:
            self.calc_entry.delete(0, tk.END)  # Clear the entry field
            self.calc_entry.insert(tk.END, f"Error: {e}")  # Display the error message

    def create_scientific_calculator(self):
        # Create the scientific calculator layout
        self.clear_frame()  # Clear any existing content in the window

        sci_calc_frame = ctk.CTkFrame(self.root)  # Create a frame for the scientific calculator
        sci_calc_frame.pack(padx=10, pady=10, fill="both", expand=True)  # Pack the frame with padding

        # Add an entry field and buttons for scientific calculator operations
        ctk.CTkLabel(sci_calc_frame, text="SCIENTIFIC CALCULATOR", font=("Arial", 20)).pack(pady=20)
        self.calc_entry = ctk.CTkEntry(sci_calc_frame, justify='right', font=("Arial", 18))
        self.calc_entry.pack(padx=5, pady=5, fill='x')

        button_frame = ctk.CTkFrame(sci_calc_frame)  # Create a frame for the calculator buttons
        button_frame.pack(pady=10, padx=10)

        # Define the text for scientific functions on top
        sci_function_texts = [
            'sin', 'cos', 'tan', 'log',
            '√', '^', '(', ')',
            'pi', 'e', 'C', 'exp'
        ]

        # Define the text for number buttons on bottom
        number_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        sci_buttons = []
        num_buttons = []

        # Create scientific function buttons
        for text in sci_function_texts:
            button = ctk.CTkButton(button_frame, text=text, width=80, height=60, font=("Arial", 18), command=lambda t=text: self.on_sci_button_click(t))
            sci_buttons.append(button)

        # Create number buttons
        for text in number_texts:
            button = ctk.CTkButton(button_frame, text=text, width=80, height=60, font=("Arial", 18), command=lambda t=text: self.on_sci_button_click(t))
            num_buttons.append(button)

        # Arrange scientific function buttons on the top (3 rows, 4 columns)
        for i in range(3):
            for j in range(4):
                if i * 4 + j < len(sci_buttons):
                    sci_buttons[i * 4 + j].grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

        # Arrange number buttons on the bottom (4 rows, 4 columns)
        for i in range(4):
            for j in range(4):
                if i * 4 + j < len(num_buttons):
                    num_buttons[i * 4 + j].grid(row=i + 3, column=j, padx=5, pady=5, sticky="nsew")  # Adjusted row index

        for i in range(7):  # Set row configuration for all 7 rows
            button_frame.grid_rowconfigure(i, weight=1)
            button_frame.grid_columnconfigure(i % 4, weight=1)  # Only 4 columns

        # Add back and home buttons
        ctk.CTkButton(sci_calc_frame, text="Back", command=self.create_calculator_menu).pack(pady=10)
        ctk.CTkButton(sci_calc_frame, text="Home", command=self.create_home_page).pack(pady=10)

        self.apply_theme()  # Apply the selected theme

    def on_sci_button_click(self, char):
        # Handle button click events for the scientific calculator
        if char == "=":
            self.calculate_scientific()  # Calculate the result
        elif char == "C":
            self.calc_entry.delete(0, tk.END)  # Clear the entry field
        elif char == "√":
            self.calc_entry.insert(tk.END, "math.sqrt(")  # Insert square root function
        elif char == "pi":
            self.calc_entry.insert(tk.END, str(math.pi))  # Insert the value of pi
        elif char == "e":
            self.calc_entry.insert(tk.END, str(math.e))  # Insert the value of e
        elif char in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'sinh', 'cosh', 'tanh', 'log', 'ln', 'log10', 'exp']:
            # Insert the appropriate math function
            if char == 'log':
                self.calc_entry.insert(tk.END, "math.log10(")
            elif char == 'ln':
                self.calc_entry.insert(tk.END, "math.log(")
            elif char == 'exp':
                self.calc_entry.insert(tk.END, "math.exp(")
            else:
                self.calc_entry.insert(tk.END, f"math.{char}(")
        elif char == "^":
            self.calc_entry.insert(tk.END, "**")  # Insert exponentiation operator
        else:
            self.calc_entry.insert(tk.END, char)  # Insert the clicked button character into the entry field

    def calculate_scientific(self):
        # Perform the scientific calculation and display the result
        try:
            expression = self.calc_entry.get()  # Get the expression from the entry field
            expression = expression.replace('x', '*')  # Replace 'x' with '*' for multiplication
            result = eval(expression)  # Evaluate the expression
            self.calc_entry.delete(0, tk.END)  # Clear the entry field
            self.calc_entry.insert(tk.END, str(result))  # Display the result
            self.add_to_history(f"{expression} = {result}")  # Add the calculation to history
        except Exception as e:
            self.calc_entry.delete(0, tk.END)  # Clear the entry field
            self.calc_entry.insert(tk.END, f"Error: {e}")  # Display the error message

    def create_bmi_calculator(self):
        # Create the BMI calculator layout
        self.clear_frame()  # Clear any existing content in the window

        bmi_frame = ctk.CTkFrame(self.root)  # Create a frame for the BMI calculator
        bmi_frame.pack(padx=10, pady=10, fill="both", expand=True)  # Pack the frame with padding

        # Add labels, entry fields, and buttons for BMI calculation
        ctk.CTkLabel(bmi_frame, text="BMI CALCULATOR", font=("Arial", 20)).pack(pady=20)
        ctk.CTkLabel(bmi_frame, text="Weight (kg)").pack()
        self.bmi_weight = ctk.CTkEntry(bmi_frame)
        self.bmi_weight.pack(padx=5, pady=5)
        ctk.CTkLabel(bmi_frame, text="Height (cm)").pack()
        self.bmi_height = ctk.CTkEntry(bmi_frame)
        self.bmi_height.pack(padx=5, pady=5)
        self.bmi_result = ctk.CTkLabel(bmi_frame, text="BMI", font=("Arial", 16))
        self.bmi_result.pack(padx=5, pady=5)
        ctk.CTkButton(bmi_frame, text="Calculate", command=self.calculate_bmi).pack(padx=5, pady=5)
        ctk.CTkButton(bmi_frame, text="Back", command=self.create_calculator_menu).pack(padx=5, pady=5)
        ctk.CTkButton(bmi_frame, text="Home", command=self.create_home_page).pack(padx=5, pady=5)

        self.apply_theme()  # Apply the selected theme

    def calculate_bmi(self):
        # Perform BMI calculation and display the result with status
        try:
            weight = float(self.bmi_weight.get())  # Get the weight from the user
            height = float(self.bmi_height.get()) / 100  # Get the height from the user and convert to meters
            bmi = weight / (height * height)  # Calculate BMI

            # Determine the BMI status
            if bmi < 18.5:
                status = "Underweight"
            elif 18.5 <= bmi < 24.9:
                status = "Normal weight"
            elif 25 <= bmi < 29.9:
                status = "Overweight"
            else:
                status = "Obese"

            self.bmi_result.configure(text=f"BMI: {bmi:.2f} ({status})")  # Display the BMI result with status
            self.add_to_history(f"Weight: {weight}kg, Height: {height*100}cm, BMI: {bmi:.2f} ({status})")  # Add calculation to history
        except Exception as e:
            self.bmi_result.configure(text=f"Error: {e}")  # Handle errors

    def view_favorites(self):
        # Display the list of favorite conversions
        self.clear_frame()  # Clear any existing content in the window

        favorites_frame = ctk.CTkFrame(self.root)  # Create a frame for the favorites list
        favorites_frame.pack(padx=10, pady=10, fill="both", expand=True)  # Pack the frame with padding

        ctk.CTkLabel(favorites_frame, text="Favorites", font=("Arial", 20)).pack(pady=20)  # Add a label for favorites

        # Display each favorite entry
        for fav in self.favorites:
            ctk.CTkLabel(favorites_frame, text=fav).pack(padx=5, pady=5)

        # Add back and home buttons
        ctk.CTkButton(favorites_frame, text="Back", command=self.create_main_menu).pack(pady=10)
        ctk.CTkButton(favorites_frame, text="Home", command=self.create_home_page).pack(pady=10)

        self.apply_theme()  # Apply the selected theme

    def view_history(self):
        # Display the list of conversion history
        self.clear_frame()  # Clear any existing content in the window

        history_frame = ctk.CTkFrame(self.root)  # Create a frame for the history list
        history_frame.pack(padx=10, pady=10, fill="both", expand=True)  # Pack the frame with padding

        ctk.CTkLabel(history_frame, text="History", font=("Arial", 20)).pack(pady=20)  # Add a label for history

        # Display each history entry
        for entry in self.history:
            ctk.CTkLabel(history_frame, text=entry).pack(padx=5, pady=5)

        # Add back and home buttons
        ctk.CTkButton(history_frame, text="Back", command=self.create_main_menu).pack(pady=10)
        ctk.CTkButton(history_frame, text="Home", command=self.create_home_page).pack(pady=10)

        self.apply_theme()  # Apply the selected theme

    def clear_favorites(self):
        # Clear the list of favorite conversions
        self.favorites = []  # Empty the favorites list
        self.save_favorites()  # Save the empty list to file

    def clear_history(self):
        # Clear the conversion history
        self.history = []  # Empty the history list
        self.save_history()  # Save the empty list to file

    def add_unit_favorite(self):
        # Add the current length conversion to favorites
        from_unit = self.from_unit.get()  # Get the source unit
        to_unit = self.to_unit.get()  # Get the target unit
        value = self.unit_value.get()  # Get the value
        self.favorites.append(f"{value} {from_unit} to {to_unit}")  # Add the conversion to the favorites list
        self.save_favorites()  # Save the updated favorites list to file

    def add_temp_favorite(self):
        # Add the current temperature conversion to favorites
        temp_type = self.temp_type.get()  # Get the conversion type
        value = self.temp_value.get()  # Get the value
        self.favorites.append(f"{value} {temp_type}")  # Add the conversion to the favorites list
        self.save_favorites()  # Save the updated favorites list to file

    def add_currency_favorite(self):
        # Add the current currency conversion to favorites
        from_currency = self.from_currency.get()  # Get the source currency
        to_currency = self.to_currency.get()  # Get the target currency
        value = self.currency_value.get()  # Get the value
        self.favorites.append(f"{value} {from_currency} to {to_currency}")  # Add the conversion to the favorites list
        self.save_favorites()  # Save the updated favorites list to file

    def add_to_history(self, entry):
        # Add a new entry to the history list
        self.history.append(entry)  # Append the entry to the history list
        self.save_history()  # Save the updated history list to file

    def save_favorites(self):
        # Save the favorites list to a file
        with open("favorites.json", "w") as f:
            json.dump(self.favorites, f)  # Write the favorites list to the JSON file

    def load_favorites(self):
        # Load the favorites list from a file
        try:
            with open("favorites.json", "r") as f:
                self.favorites = json.load(f)  # Load the favorites list from the JSON file
        except FileNotFoundError:
            self.favorites = []  # Initialize an empty list if the file is not found

    def save_history(self):
        # Save the history list to a file
        with open("history.json", "w") as f:
            json.dump(self.history, f)  # Write the history list to the JSON file

    def load_history(self):
        # Load the history list from a file
        try:
            with open("history.json", "r") as f:
                self.history = json.load(f)  # Load the history list from the JSON file
        except FileNotFoundError:
            self.history = []  # Initialize an empty list if the file is not found

    def clear_frame(self):
        # Clear all widgets from the current window
        for widget in self.root.winfo_children():
            widget.destroy()  # Destroy each widget in the window

# Create an instance of the ConverterApp class and start the main loop
app = ConverterApp(root)
root.mainloop()


