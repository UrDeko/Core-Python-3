movie_schedule = {"Frosty the snowman": "11:00am",
                 "Grinch": "3:00pm",
                 "Christmas Carol": "5:00pm"}

print("\n".join(movie_schedule.keys()))

movie = input("What movie would you like the showtime for?\n")

if movie_schedule.get(movie):
    print(movie_schedule.get(movie))
else:
    print("Requested showtime isn't playing")