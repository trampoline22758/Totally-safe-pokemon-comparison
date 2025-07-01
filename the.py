import matplotlib.pyplot as plt
import os as os
import pandas as pd
print("if you want to see cool stuff type I when it shows my name in Ascii art but it has to be capitalized 'I'")
os.system('cls') # also found out how to clear terminal every time
csv_file = "https://raw.githubusercontent.com/lgreski/pokemonData/master/Pokemon.csv"
df = pd.read_csv(csv_file)
df['Type1'] = df['Type1'].str.capitalize()
print(df.head(1000))
print("\n")
print("Time to filter type of pokemon, if you dont want to filter type idk")
df_type = input("Enter the type of Pokémon you want to filter (e.g., Fire, Water): ").capitalize() # I found out that if you put .capitalize it capitilizes it
if df_type in df['Type1']:
    filtered_df = df[df['Type1'] == df_type]
    print(filtered_df[['Name', 'Type1', 'HP', 'Attack', 'Defense', 'Speed']])
else: #I finally get how to use if/else, it was hard 
    print("Doesnt exist")
    os.system('cls')
print("you choose what to compare (Attack, Defense, HP, Sp. Atk, Sp. Def), you have to put it exactly as it is typed here:")
firstpick = input("Enter the first attribute: ")
secondpick = input("Enter the second attribute: ")
os.system('cls')
print(f"{firstpick} vs {secondpick} type of pokemon {df_type}")
plt.scatter(df[firstpick], df[secondpick])
plt.title(f'{firstpick} vs {secondpick}')
plt.xlabel(firstpick)
plt.ylabel(secondpick)
plt.show()
print("pokemon with sp. def have average attack, pokemon with high attack have average sp. def")
print("I might put this on github because this version is cool \n -Anjney")
delay = input("        / /\                /\ \     _          /\ \     /\ \     _    /\ \ /\ \     /\_\ \n       / /  \              /  \ \   /\_\        \ \ \   /  \ \   /\_\ /  \ \\ \ \   / / / \n      / / /\ \            / /\ \ \_/ / /        /\ \_\ / /\ \ \_/ / // /\ \ \\ \ \_/ / / \n     / / /\ \ \          / / /\ \___/ /        / /\/_// / /\ \___/ // / /\ \_\\ \___/ / \n    / / /  \ \ \        / / /  \/____/_       / / /  / / /  \/____// /_/_ \/_/ \ \ \_/ \n   / / /___/ /\ \      / / /    / / //\ \    / / /  / / /    / / // /____/\     \ \ \ \n  / / /_____/ /\ \    / / /    / / / \ \_\  / / /  / / /    / / // /\____\/      \ \ \ \n / /_________/\ \ \  / / /    / / /  / / /_/ / /  / / /    / / // / /______       \ \ \ \n/ / /_       __\ \_\/ / /    / / /  / / /__\/ /  / / /    / / // / /_______\       \ \_\ \n\_\___\     /____/_/\/_/     \/_/   \/_______/   \/_/     \/_/ \/__________/        \/_/  ")
if delay == "":
    os.system('cls')
elif delay == "I":
    print("you have lost my friend")
    (lambda x: print("I\n" * x, end=""))(2000000000) 
else:
    print("no clear terminal") #idk



