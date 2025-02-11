destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paula, Brazil", "Cairo, Egypt"]


attractions = [[] for destination in destinations]

def get_destination_index(destination):
  return destinations.index(destination) if destination in destinations else -1

def get_traveler_location(traveler):
  traveler_destiantion = test_traveler[1]
  traveler_destination_index = get_destination_index(traveler_destiantion)
  return traveler_destination_index

def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []

  for attraction in attractions_in_city:
    possible_attraction, attraction_tag = attraction

    for interest in interests:
      if interest in attraction_tag:
        attractions_with_interest.append(possible_attraction)

  return attractions_with_interest

test_traveler = ['Erin Wilkes', "Shanghai, China", ['historical site', 'art']]
def get_attractions_for_traveler(traveler):
  traveler_name, traveler_destination, traveler_interests = traveler
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = f"Hi {traveler_name}, we think you'll like these places around "
  
  for attraction in traveler_attractions:
    interests_string = interests_string + " " + attraction
  
  return interests_string






#Adding attractions
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

test_destination_index = get_traveler_location(test_traveler)
la_arts = find_attractions("Los Angeles, USA", ['art'])
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
#print(smills_france)


# String operations
def password_generator(username):
  password = username[-1]
  
  for letter in username:
    password = password + letter
  return password[:-1]
#print(password_generator("AbeSimp"))


#better performance version
def password_generator_performance(username):
  return username[-1] + username[:-1]
#print(password_generator_performance("AbeSimp"))


#Get last name from an array of strings
def get_last_name(names):
  return [name.split()[-1] for name in names]

#print(get_last_name(['Audre Lorde', 'Gabriela Mistral', 'Jean Toomer', 'An Qi', 'Walt Whitman', 'Shel Silverstein', 'Carmen Boullosa', 'Kamala Suraiyya', 'Langston Hughes', 'Adrienne Rich', 'Nikki Giovanni']))









