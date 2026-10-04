from user_input import KG_PER, M_PER_HEIGHT

def to_kg(weight, unit):
    return weight * KG_PER[unit]

def from_kg(kg, unit):
    return kg / KG_PER[unit]

def to_meter(height, unit):
    if unit in M_PER_HEIGHT:
        return height * M_PER_HEIGHT[unit]

    if unit == "ft_in":
        feet = int(height)
        inches = round((height - feet) * 100)

        total_inches = feet * 12 + inches

        return total_inches * 0.0254

    raise ValueError("Invalid height unit")

def from_meter(meter, unit):

    if unit in M_PER_HEIGHT:
        return meter / M_PER_HEIGHT[unit]

    if unit == "ft_in":
        total_inches = meter / 0.0254

        feet = int(total_inches//12)

        inches = round(total_inches % 12)

        return feet + inches / 100

    raise ValueError("Invalid height unit")