# Author: harundemir918
# Spectate mode of Counter-Strike

# Import random and time libraries
import random
import time

# Teams
teams = ["Terorist", "Counter-Terrorist"]

# Terrorists
terrorists = ["Guerilla", "Elite", "Avenger", "Krew"]

# Counter-Terrorists
counter_terrorists = ["CIA", "FBI", "MI6", "SAS"]

# Guns that terrorists used
terrorist_guns = ["M249", "AK-47", "SG-552", "Dual Elite", "Ingram", "Galil", "AWP", "XM1014", "Desert Eagle", "Glock-18"]

# Guns that counter-terrorists used
counter_terrorist_guns = ["M249", "M4A1", "AUG", "TMP", "AWP", "USP", "Five-Seven", "Desert Eagle", "MP5", "Famas"]

# Dead players
dead = []


while True:                                                     # Run until break

    # If all terrorists dead
    if len(terrorists)==0:
        print("--> Counter-Terrorists Win <--\n")               # Print the result
        print("Dead Players:\n")                                # Print dead players
        for i in dead:
            print(i)
        break                                                   # Exit from the while loop

    # If all counter-terrorists dead
    elif len(counter_terrorists)==0:
        print("--> Terrorists Win <--\n")                       # Print the result
        print("Dead Players:\n")                                # Print dead players
        for i in dead:
            print(i)
        break                                                   # Exit from the while loop

    # If the players are still alive
    else:
        counter_terrorist = random.choice(counter_terrorists)   # Select a player randomly from counter_terrorists list
        terrorist = random.choice(terrorists)                   # Select a player randomly from terrorists list
    for i in range(len(dead)):

        # If a counter-terrorist dead
        if counter_terrorist == dead[i]:
            counter_terrorists.remove(counter_terrorist)        # Remove dead counter-terrorist from the counter_terrorists list 
            break

        # If a terrorist dead
        elif terrorist == dead[i]:
            terrorists.remove(terrorist)                        # Remove dead terrorist from the terrorists list 
            break
    else:

        # If the team which is randomly selected is Counter-Terrorist
        if random.choice(teams) == "Counter-Terrorist":
            print("%s killed %s with %s" 
                %(  counter_terrorist, 
                    terrorist, 
                    random.choice(counter_terrorist_guns)))     # Print which CT killed T with CT guns
            dead.append(terrorist)                              # Append the dead terrorist to dead list
            time.sleep(random.randint(1,10))                    # Wait between 1 - 10 seconds
        
        # If the team which is randomly selected is Terrorist
        else:
            print("%s killed %s with %s" 
                %(  terrorist, 
                    counter_terrorist, 
                    random.choice(terrorist_guns)))             # Print which T killed CT with T guns
            dead.append(counter_terrorist)                      # Append the dead counter-terrorist to dead list
            time.sleep(random.randint(1,10))                    # Wait between 1 - 10 seconds
