#Movie dictionary 
movie_list = {
    1: "Civil War",
    2: "Kung Fu Panda",
    3: "Godzilla X Kong",
}
#Screen Dictionary
screen_list = {
    1: "Screen 1",
    2: "Screen 2",
    3: "Screen 3",
}
#Theatre Dictionary
theaters = {
    1: "Inox",
    2: "Icon",
    3: "PVP",
}
#Cities Dictionary
cities = {
    1: "London",
    2: "Manchester",
    3: "Bristol",
}
#Time Slots Dictionary 
time_slots = {
    1: {"1": "10.00-1.00", "2": "1.10-4.10", "3": "4.20-7.20", "4": "7.30-10.30"},
    2: {"1": "10.15-1.15", "2": "1.25-4.25", "3": "4.35-7.35", "4": "7.45-10.45"},
    3: {"1": "10.30-1.30", "2": "1.40-4.40", "3": "4.50-7.50", "4": "8.00-10.45"},
}

#Select City 
def select_city():
    print("Welcome to the movie ticket booking system!")
    print("Where do you want to watch the movie?")
    for key, value in cities.items():
        print(f"{key}: {value}")
    print("0: Exit")
    city_choice = int(input("Choose your option: "))
    if city_choice in cities:
        select_theater()
    elif city_choice == 0:
      exit()
    else:
        print("Invalid choice!")
        select_city()

#Select Theatre 
def select_theater():
    print("Which theater do you wish to see the movie?")
    for key, value in theaters.items():
        print(f"{key}: {value}")
    print("0: Return")
    theater_choice = int(input("Choose your option: "))
    if theater_choice in theaters:
        select_movie()
    elif theater_choice == 0:
            select_city()
    else:
        print("Invalid choice!")
        select_theater()

#Select Movie 
def select_movie():
    print("Which movie do you want to watch?")
    for key, value in movie_list.items():
        print(f"{key}: {value}")
    print("0: Return")
    movie_choice = int(input("Choose your movie: "))
    if movie_choice == 0:
        select_theater()
    elif movie_choice in movie_list:
        select_screen()
        return movie_list[movie_choice]
    else:
        print("Invalid choice! Please select one of the available options.")
        return select_movie()

#Select Screen
def select_screen():
    print("Which screen do you want to watch the movie on?")
    for key, value in screen_list.items():
        print(f"{key}: {value}")
    print("0: Return")
    screen_choice = int(input("Choose your screen: "))
    if screen_choice in screen_list:
        select_timing(screen_choice)
    elif screen_choice == 0:
        select_movie()
    else:
        print("Invalid choice! Please select one of the available options.")

#Select Timing
def select_timing(screen):
    print("Choose your preferred timing:")
    for key, value in time_slots[screen].items():
        print(f"{key}: {value}")
    print("0: Return")
    timing_choice = input("Select your timing: ")
    if timing_choice in time_slots[screen]:
        print(f"Successful! Enjoy the movie on {screen_list[screen]} at {time_slots[screen][timing_choice]}")
    elif timing_choice == "0":
        select_screen()
    else:
        print("Invalid choice! Please select one of the available options.")
        select_timing(screen)
select_city()