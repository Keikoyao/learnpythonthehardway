cities = {'CA':'San Francisco','MI':'Detroit','FL':'Jacksonville'}

cities['NY']='New York'
cities['OR']='Portland'

#A function is also a variable
def find_city(themap,state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

#ok pay attention!
cities['_find'] = find_city

while True:
    print("State?(ENTER to quit)",)
    state = input(">>>")
    if not state:break

    #this line is the most important ever! Study!
    city_found = cities['_find'](cities,state)
    print(city_found)
    
#we put a function find_city into a dict with a key '_find'
cities['_find'] = find_city
#create another variable coty_found, cities is a dict, with a key '_find' 
#find the value--find_city,which is a function. 
#2 parameters cities, state will be passed on to the function find_city
city_found = cities['_find'](cities,state)
#function find_city will try to find states(key) from cities and return the value
#if there is no match, return "Not found"
#find_city gives the value returned to the variable city_found

        
