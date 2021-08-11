# Code part A, #2 here:
    
print((2 + 8 + 10) / 5)
print((8 + 2 * 10) / 5)

# Code part A, #3 here:
word = 'Hello'
print((word+" ")*4)

print(f"{word}{word}\n"*3)

print(f"{word}\t{word}\t{word}\n"*3)


# Part B

name_of_spaceship = 'Determination'

ship_speed = 17500

distance_to_mars = 225000000

miles_per_kilometer = .621

miles_to_mars = distance_to_mars * miles_per_kilometer

hours_to_mars = miles_to_mars / ship_speed

days_to_mars = hours_to_mars / 24

print(f"{name_of_spaceship} will take {days_to_mars} days to reach Mars.")

#Bonus

distance_to_moon = 384400

miles_to_moon = distance_to_moon * miles_per_kilometer

hours_to_moon = miles_to_moon / ship_speed

days_to_moon = hours_to_moon / 24

print(f"{name_of_spaceship} will take {days_to_moon} days to reach the Moon.")



#Part C

user_input = input("Enter a word: ")
print(f"The word '{user_input}' contains {len(user_input)} characters.")


rectangle_length = input("Enter the length of a rectangle: ")
rectangle_width = input("Enter the width of a rectangle: ")

print(f"The rectangle has an area of {int(rectangle_length) * int(rectangle_width)}.")


num_miles_driven = input("Enter number of miles driven: ")

num_gallons_used = input("Enter number of gallons used: ")

print(f"Your car got {int(num_miles_driven) / int(num_gallons_used)} miles per gallon.")


