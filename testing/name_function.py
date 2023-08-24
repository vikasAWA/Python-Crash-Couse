def get_formatted_name(first, last, middle=''):
    """Get neatly formstted full name"""
    if middle:
        return f"{first} {middle} {last}".title()
    else:
        return f"{first} {last}".title()

