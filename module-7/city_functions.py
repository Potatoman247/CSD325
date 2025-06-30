def cityCountry(City, Country, Language = '', Population = ''):

    LocationString = City + ', ' + Country
    if(Population != ''):
        LocationString = LocationString + ' - population ' + Population
    if(Language != ''):
        LocationString = LocationString + ', ' + Language
    return LocationString

def main():
    print(cityCountry('Santiago', 'Chile'))
    print(cityCountry('Anaheim', 'USA', '350000'))
    print(cityCountry('Baltimore', 'USA', '800000', 'English'))
    
main()
