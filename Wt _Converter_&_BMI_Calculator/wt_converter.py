from design import box
from user_input import ask_number, ask_unit
from calcutaion import from_kg,to_kg

def weight_converter():

    box("Wt. Converter")
    
    weight = ask_number("Enter weight: ")
    from_unit = ask_unit("Convert FROM which unit?: ")
    to_unit = ask_unit("Convert TO which unit?: ")

    result = from_kg(to_kg(weight, from_unit), to_unit)
    print(f"\n{weight} {from_unit} = {result:.2f} {to_unit}")
