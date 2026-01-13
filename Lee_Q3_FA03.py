steps = [
    [5300, 6200, 7000, 6500, 7200],  
    [4500, 5800, 6000, 6100, 6900],  
    [7000, 7500, 8000, 7800, 8200]   
]


for i in range(len(steps)):
    total = sum(steps[i])
    average = total / len(steps[i])
    print(f"Friend {i+1} steps: {steps[i]}")
    print(f"Total steps: {total}")
    print(f"Average steps: {average}")
    print()

Using a 2d array made it easier to organize the steps day by day for each person. I could quickly calculate totals and averages for each friend since all I needed to do was enter the data and the code did it for me. The easiest part was calculating the total and average since i didn't even have to do it, the code already did it for me.
