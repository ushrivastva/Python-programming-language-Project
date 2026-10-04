from design import small_box, box
from wt_converter import weight_converter
from bmi_calculator import bmi_calculator


def main():

    small_box("Wt. Converter", "BMI Calculator")

    option = input("Enter what you want!: ").strip().lower()

    if option in ["wt.", "wt", "wt. converter", "wt converter", "weight converter", "weight"]:
        weight_converter()
    elif option in ["bmi", "bmi calculator", "bmicalculator", "body mass index"]:
        bmi_calculator()
    else:
        box("Error!")

if __name__ == "__main__":
    main()