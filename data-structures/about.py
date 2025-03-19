# Write code below 💖
friends = ['sarah', 'sian', 'kristina', 'alexis', 'geli']
tv_show = {
 'title':'Supernatural',
 'genre': 'Drama',
 'cast': ['Jensen Ackles', 'Jared Padalecki', 'Misha Collins', 'Jim Beaver', 'Mark Sheppard', 'Felicia Day', 'Rob Benedict', 'Richard Speight Jr.'],
 'released': 2005,
 'endyear': 2020
}
places = {'tokyo', 'seoul', 'kyoto'}
song = {
    'title': 'Carry On Wayward Son',
    'artist': 'Kansas',
    'year': 1976
}

#print information on my friends: 
print('My Friends:')
print(', '.join(friends))

#print information about my favorite tv show:
print('\nMy Favorite TV Show ')
print('Title: ', tv_show['title'])
print('Genre: ', tv_show['genre'])
print('Cast: ', end=' ')
print(', '.join(tv_show['cast']))
print('Favorite Actor: ', tv_show['cast'][0])
print('Release Year: ' , tv_show['released'])
print('End Year: ', tv_show['endyear'])

#print information about favorite song with format string and .items()
print('\nFavorite Song: ')
for key, value in song.items():
    print(f"{key}: {value}")
    
#print information about places I want to go:
print('\nPlaces I want to go: ')
print(', '.join(places))