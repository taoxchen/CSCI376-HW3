from nicegui import ui

ui.colors(
      primary='#31ccec',
      secondary='#789491',
      accent='#c10015',
      positive='#21ba45',
      negative='#cf0018',
      info='#31ccec',
      warning='#c10015'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: applies positive color defined in ui.colors()
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4")
        # text-negative: applies negative color defined in ui.colors()

def convertSlider(value):
    temp = float(value)
    if conversion2_type.value == "Celsius to Fahrenheit":
        result2_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
    else:
        result2_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
    result2_label.classes("text-lg font-semibold text-positive mt-4")


with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl"):
    # w-100: Set element width to be fixed at 100
    # p-6: Adds padding of 1.5 rem inside the card for spacing 
    # shadow-xl: applies an extra large shadow effect to the card  
    # mx-auto: centers the card horizotally in its container 
    # mt-10: adds a top margin of 2.5rem to space it from elements above
    # rounded-xl: rounds the corners of the card 
    ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4")
    # text-2xl: sets the font size to be extra-large 
    # font-bold: makes the text bold 
    # text-accent: applies the accent color defined in the theme
    # mb-4: adds a bottom margin of 1rem to create spacing between elements
    input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded")
    # w-full: make the row take up the full width of the card
    # border: adds a border around the input field 
    # rounded: rounds the input field corner slightly 
    conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("justify-center w-full mb-4")
    convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded justify-center w-full")
    # text-white: makes the text color white
    # py-2: adds vertical padding of 2 units inside the button
    # px-4: adds horizontal padding of 4 units inside the button 
    result_label = ui.label("").classes("text-xl font-semibold text-info mt-4 border border-info p-2 rounded-lg")

with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl"):
    ui.label("Slider Temperature Converter").classes("text-3xl font-bold text-accent mb-4")
    slider = ui.slider(min=-150, max=150, value=0, step=1, on_change= (lambda e: convertSlider(e.value))).classes("w-100 mb-5")
    ui.label().bind_text_from(slider, 'value').classes("mx-auto")
    conversion2_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("justify-center w-fullmb-4")
    result2_label = ui.label("").classes("text-xl font-semibold text-info mt-4 border border-info p-2 rounded-lg justify-center")

ui.run(port=8081)

