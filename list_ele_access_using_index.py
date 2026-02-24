# Create List of 4 IPL teams of your choice.

print("\n List of IPL Teams: \n")

rcb = ["Virat Kohli", "Rajat Patidar", "Faf du Plessis", "Mohammed Siraj"]  # Players Of Royal Challengers Bengaluru

pbks = ["Shikhar Dhawan", "Liam Livingstone", "Kagiso Rabada", "Sam Curran"]   # Punjab Kings

mi = ["Rohit Sharma", "Jasprit Bumrah", "Suryakumar Yadav", "Hardik Pandya"]   # Mumbai Indians

gt = ["Shubman Gill", "David Miller", "Rashid Khan", "Mohammed Shami"]      # Gujarat Titans


print(" List Of RCB Players = ",rcb,"\n","List Of PBKS Players = ",pbks,"\n","List Of MI Players = ",mi,"\n","List Of GT Players = ",gt,"\n")

print("\n Here are some of the best batsmen from each team: \n")

# Here are some of the best batsmen from each team:

best_batsmen_of_rcb = rcb[0]  # Virat Kohli
best_batsmen_of_pbks = pbks[2]   # Kagiso Rabada
best_batsmen_of_gt = gt[2]   # Rashid Khan
best_batsmen_of_mi = mi[1]  # Jasprit Bumrah

ListOfBestBatsmen = [best_batsmen_of_gt,best_batsmen_of_mi,best_batsmen_of_pbks,best_batsmen_of_rcb]

print("List Of Best Batsmen = ", ListOfBestBatsmen)



print("\n Here are some of the best bowlers from each team: \n")

#  Here are some of the best bowlers from each team:

best_bowlers_of_rcb = rcb[3]
best_bowlers_of_pbks = pbks[2]
best_bowlers_of_gt = gt[2]
best_bowlers_of_mi = mi[1]

ListOfBestBowlers = [best_bowlers_of_rcb,best_bowlers_of_pbks,best_bowlers_of_gt,best_bowlers_of_mi]

print("List Of Best Bowlers = ",ListOfBestBowlers)


print("\n Here are some of the best all rounder player from each team: \n")
#  Here are some of the best all rounder player from each team:

ListOfAllRounderPlayer = []

for plyr in ListOfBestBatsmen:
    for plyr2 in ListOfBestBowlers:
        if plyr == plyr2:
            ListOfAllRounderPlayer.append(plyr)

print("List Of All Rounder Player = ",ListOfAllRounderPlayer)



