countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def exists(country):
    if 'land' in country:
        return False
    return True

no_land = filter(exists, countries)
print(list(no_land))

