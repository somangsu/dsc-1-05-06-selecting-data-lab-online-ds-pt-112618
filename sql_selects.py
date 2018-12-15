def select_all_columns_and_rows():
    return "Select * from planets;"

def select_name_and_color_of_all_planets():
    return "Select name, color from planets;"

def select_all_planets_with_mass_greater_than_one():
    return "Select * from planets where mass > 1.00;"

def select_name_and_mass_of_planets_with_mass_less_than_equal_to_one():
    return "Select name, mass from planets where mass <= 1.00;"

def select_name_and_color_of_planets_with_more_than_10_moons():
    return "Select name, color from planets where num_of_moons > 10;"

def select_all_planets_with_moons_and_mass_less_than_one():
    return "Select * from planets where mass < 1.00 and moons < 1;"

def select_name_and_color_of_all_blue_planets():
    return "Select name, color from planets where color in ('blue','light blue','dark blue');"
