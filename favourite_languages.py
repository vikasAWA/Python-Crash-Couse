from collections import OrderedDict

favourite_languages = OrderedDict()

favourite_languages['jen'] = "python"
favourite_languages['sarah']  = 'c'
favourite_languages['john'] = 'c#'
favourite_languages['phil'] = 'ruby'

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}")