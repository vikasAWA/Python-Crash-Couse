def get_city_country(city, country, population=''):
    """Returning in the form of City, Country"""
    if population:
        return f"{city}, {country}".title() + f" - population {population}"
    else:
        return f"{city}, {country}".title()
        

print(get_city_country('delhi', 'india', 400000))