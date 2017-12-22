races = []

def get_races():
    cx_races = []
    for race in races:
        #print(race['name'])
        cx_races.append(race['name'].title())
    return cx_races

def add_race(name, type='cx'):
    race = {'name': name, 'type': type}
    races.append(race)
    #print('race added')

def save_file(race):
    try:
        file = open('races.txt', 'a')
        file.write(race + '\n')
        file.close()
    except Exception:
        print('cannot save the file')

def read_file():
    try:
        file = open('races.txt', 'r')
        for race in file.readlines():
            add_race(race)
        file.close()
    except Exception:
        print('something terrible happened')


read_file()
#print(races)
print(get_races())

#add_race('crossliget')
# add_race('kazincbarcika')
# add_race('kecskemet')

race_name = input('enter race name: ')
add_race(race_name)
save_file(race_name)

#add_race(race_name)
#     answer = input('want to add more race? (yes/no)')

#    print(get_races())


# race_name = input('enter race name: ')

#print(races)
#print(get_races())

