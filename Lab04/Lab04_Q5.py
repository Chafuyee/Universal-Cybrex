

def get_country_alpha3(country_dictionary, name):
    try:
        country_code = country_dictionary[name]
        return country_code
    except KeyError:
        country_name = "'" + str(name) + "'" 
        print("ERROR: " + country_name + " is not available.")