# Write a program that prints popular computer games,
# each game name on a separate line. Use the while statement.
# Additionally, number the list (print the next number before each list item)
# and sort the list alphabetically
# (use one of a Python built-in functions for sorting)

computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

index = 0
number = 1

computer_games_sorted = sorted(computer_games)

while index < len(computer_games_sorted)-1:
    print(str(number)+ ".", computer_games_sorted[index])
    index += 1
    number += 1