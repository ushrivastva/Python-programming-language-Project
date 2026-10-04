from user_input import ask_unit, ask_number, ask_unit_hgt
from design import box, small
from calcutaion import  to_kg, to_meter

def bmi_category(bmi):
    if bmi < 18.5:
        return small("Underweight")
    elif bmi < 25:
        return small("Normal")
    elif bmi < 30:
        return small("Overweight")
    return small("Obesity")


def bmi_calculator():
    box("BMI Calculator")
    weight = ask_number("Enter weight: ")
    unit = ask_unit()
    height = ask_number("Enter height: ")
    unit_hgt = ask_unit_hgt()

    kg = to_kg(weight, unit)
    height_m = to_meter(height, unit_hgt)
    bmi = kg / (height_m ** 2)

    print(f"\nYour BMI is '{bmi:.1f}.'")
    bmi_category(bmi)
