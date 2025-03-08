from nicegui import ui

ui.colors(
      primary='#c28888',
      secondary='#b0abad',
      accent='#ff7da6',
      positive='#a2e0b0',
      negative='#f26676',
      info='#91c2cc',
      warning='#F2C037'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4")

with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl"):
    # w-100: Set element width to be fixed at 100
    # p-6:
    # shadow-xl:
    # mx-auto:
    # mt-10:
    # rounded-xl:
    ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4")
    # text-2xl: 
    # font-bold:
    # text-accent:
    # mb-4: 
    input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded")
    # w-full:
    # border:
    # rounded:
    conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
    convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded")
    # text-white:
    # py-2:
    # px-4:
    result_label = ui.label("").classes("text-lg mt-4")

ui.run()