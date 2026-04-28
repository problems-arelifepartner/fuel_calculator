from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Set background to black to make colors pop
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class FuelCalculatorApp(App):
    def build(self):
        # Create the main layout container
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        
        # Title
        title = Label(text='Trip Fuel Cost Calculator', font_size='24sp', bold=True, size_hint=(1, 0.2))
        
        # Input Fields
        self.mileage_input = TextInput(hint_text='Enter Mileage (km/l)', input_filter='float', multiline=False, font_size='18sp')
        self.distance_input = TextInput(hint_text='One-way Distance (km)', input_filter='float', multiline=False, font_size='18sp')
        self.fuel_rate_input = TextInput(hint_text='Fuel Rate (₹/l)', input_filter='float', multiline=False, font_size='18sp')
        
        # Calculate Button
        self.calc_button = Button(text='Calculate Trip', font_size='20sp', size_hint=(1, 0.8), background_color=(0.2, 0.6, 0.8, 1))
        self.calc_button.bind(on_press=self.calculate)
        
        # Output Labels (markup=True enables the hex color codes)
        self.distance_label = Label(markup=True, text="Total Round-Trip Distance : ", font_size='18sp')
        self.fuel_label = Label(markup=True, text="Total Fuel Required : ", font_size='18sp')
        self.cost_label = Label(markup=True, text="Total Estimated Cost : ", font_size='18sp')
        
        # Add all widgets to the screen
        self.layout.add_widget(title)
        self.layout.add_widget(self.mileage_input)
        self.layout.add_widget(self.distance_input)
        self.layout.add_widget(self.fuel_rate_input)
        self.layout.add_widget(self.calc_button)
        self.layout.add_widget(self.distance_label)
        self.layout.add_widget(self.fuel_label)
        self.layout.add_widget(self.cost_label)
        
        return self.layout

    def calculate(self, instance):
        try:
            # Get values from input boxes
            mileage = float(self.mileage_input.text)
            distance = float(self.distance_input.text)
            fuel_rate = float(self.fuel_rate_input.text)
            
            if mileage <= 0:
                self.distance_label.text = "[color=ff0000]Error: Mileage must be greater than zero.[/color]"
                return
                
            # Calculations
            total_distance = distance * 2
            fuel_needed = total_distance / mileage
            total_cost = fuel_needed * fuel_rate
            
            # Update labels with specific hex colors (Red, Yellow, Green)
            self.distance_label.text = f"Total Round-Trip Distance : [color=ff4444]{total_distance:.2f} km[/color]"
            self.fuel_label.text = f"Total Fuel Required : [color=ffeb3b]{fuel_needed:.2f} litres[/color]"
            self.cost_label.text = f"Total Estimated Cost : [color=00c851]₹{total_cost:.2f}[/color]"
            
        except ValueError:
            self.distance_label.text = "[color=ff4444]Error: Please fill all fields with valid numbers.[/color]"
            self.fuel_label.text = "Total Fuel Required : "
            self.cost_label.text = "Total Estimated Cost : "

if __name__ == '__main__':
    FuelCalculatorApp().run()
