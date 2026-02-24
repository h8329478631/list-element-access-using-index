# 🏏 IPL Teams Analysis Using Python Lists

## 📌 Project Description

This project demonstrates how to use **Python Lists**, **Indexing**, and **Loops** using IPL team data.

The program:

- Creates 4 IPL team player lists
- Selects best batsmen using indexing
- Selects best bowlers using indexing
- Finds common players (All-Rounders) using nested loops

---

## 🏆 IPL Teams Included

- Royal Challengers Bengaluru (RCB)
- Punjab Kings (PBKS)
- Mumbai Indians (MI)
- Gujarat Titans (GT)

Each team contains 4 players stored in a Python list.

---

## 💻 Python Code

```python
# Create List of 4 IPL teams of your choice.

print("\n List of IPL Teams: \n")

rcb = ["Virat Kohli", "Rajat Patidar", "Faf du Plessis", "Mohammed Siraj"]
pbks = ["Shikhar Dhawan", "Liam Livingstone", "Kagiso Rabada", "Sam Curran"]
mi = ["Rohit Sharma", "Jasprit Bumrah", "Suryakumar Yadav", "Hardik Pandya"]
gt = ["Shubman Gill", "David Miller", "Rashid Khan", "Mohammed Shami"]

print(" List Of RCB Players = ",rcb,"\n",
      "List Of PBKS Players = ",pbks,"\n",
      "List Of MI Players = ",mi,"\n",
      "List Of GT Players = ",gt,"\n")


print("\n Here are some of the best batsmen from each team: \n")

best_batsmen_of_rcb = rcb[0]
best_batsmen_of_pbks = pbks[2]
best_batsmen_of_gt = gt[2]
best_batsmen_of_mi = mi[1]

ListOfBestBatsmen = [
    best_batsmen_of_gt,
    best_batsmen_of_mi,
    best_batsmen_of_pbks,
    best_batsmen_of_rcb
]

print("List Of Best Batsmen = ", ListOfBestBatsmen)


print("\n Here are some of the best bowlers from each team: \n")

best_bowlers_of_rcb = rcb[3]
best_bowlers_of_pbks = pbks[2]
best_bowlers_of_gt = gt[2]
best_bowlers_of_mi = mi[1]

ListOfBestBowlers = [
    best_bowlers_of_rcb,
    best_bowlers_of_pbks,
    best_bowlers_of_gt,
    best_bowlers_of_mi
]

print("List Of Best Bowlers = ",ListOfBestBowlers)


print("\n Here are some of the best all rounder player from each team: \n")

ListOfAllRounderPlayer = []

for plyr in ListOfBestBatsmen:
    for plyr2 in ListOfBestBowlers:
        if plyr == plyr2:
            ListOfAllRounderPlayer.append(plyr)

print("List Of All Rounder Player = ",ListOfAllRounderPlayer)
```

---

## 🧠 Logic Explanation

### 🔹 Step 1: Create Team Lists
Each IPL team is stored inside a Python list.

### 🔹 Step 2: Select Best Batsmen
Using list indexing:
```
rcb[0]
```

### 🔹 Step 3: Select Best Bowlers
Using list indexing:
```
rcb[3]
```

### 🔹 Step 4: Find All-Rounders
Nested loops compare:
- Best Batsmen List
- Best Bowlers List  

If a player exists in both → added to All-Rounder list.

---

## 📚 Concepts Used

- Python Lists
- List Indexing
- Nested For Loop
- Conditional Statements
- List Append Method

---

## 🎯 Learning Outcome

After completing this project, you will understand:

✔ How to create and print lists  
✔ How to access elements using index  
✔ How nested loops work  
✔ How to compare two lists  
✔ How to find common elements  

---

## 🚀 Possible Improvements

- Use Dictionary instead of multiple lists
- Use Set intersection for better performance
- Convert into function-based program
- Take user input dynamically

---

## 👨‍💻 Author

**Harshal Warke**  
Python Learner 🚀  