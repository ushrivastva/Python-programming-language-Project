from design import wt_unit, hg_unit


KG_PER = {"kg": 1.0, "pound": 0.45359237, "stone": 6.35029318}
M_PER_HEIGHT = {"cm":0.01, "m":1, "in":0.0254, "ft":0.3048}

ALIASES = {
    "kg": "kg", "kgs": "kg", "kilogram": "kg",
    "pound": "pound", "pounds": "pound", "lb": "pound", "lbs": "pound",
    "stone": "stone", "st": "stone",
    "centimeter": "cm", "cm":"cm",
    "meter":"m", "m":"m",
    "inch":"in", "in":"in",
    "feet":"ft_in","ft":"ft_in",
    "feet+inch":"ft_in", "ftin":"ft_in", "ft_in":"ft_in" 
}


def ask_number(prompt):
    """Keep asking until the user enters a valid positive number."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
        except ValueError:
            print("That's not a number, try again.")

def ask_unit(prompt="Enter 'unit' of weight: "):
    """Show the unit menu and return a clean unit name."""
    wt_unit("KG", "POUND", "STONE")
    while True:
        unit = ALIASES.get(input(prompt).strip().lower())
        if unit:
            return unit
        print("Unknown unit, choose KG, POUND or STONE.")


def ask_unit_hgt(prompt="Enter 'unit' of height: "):
    """Show the unit menu and return a clean unit name."""
    hg_unit("Centimeter", "Inch(In)", "Meters","Feet(In + Ft)")
    while True:
        unit = ALIASES.get(input(prompt).strip().lower())
        if unit:
            return unit
        print("Unknown unit, choose cm., meter, inch, foot or feet.")
