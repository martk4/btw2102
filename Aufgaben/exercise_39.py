# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

def lines():
    print('-'*10)

# add some more cities
cities['NY']= 'New York'
cities['OR']= 'Portland'

#print out some cities
print('-'* 10)
print("NY State has: ", cities['NY'])
print("OR State has. ", cities['OR'])

#print some states
print('-' * 10)
print(" Michigans abbreviation is: ", states['Michigan'])
print(" Floridas abbreviation is: ", states['Florida'])

#do it by using the state then cities dict
lines()
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state abbreviation
lines()
for state,abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in the state
lines()
for abbrev,city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
lines()
for state,abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"and has the city {cities[abbrev]}")

lines()
#safely get a abbreviation by state that might not be there 
state = state.get('Texas')

if not state:
    print('Sorry,no Texas.')

#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is : {city} ")
