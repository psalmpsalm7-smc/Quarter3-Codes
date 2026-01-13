names = ["Me", "Marvoun", "Stefanno"]

steps = [
    [4500, 5200, 4800, 5000, 5300],  
    [4000, 4100, 3900, 4200, 4600],  
    [6000, 5800, 5900, 6100, 6200]  
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

daily_totals = []


for col in range(len(steps[0])):
    total = 0
    for row in range(len(steps)):
        total += steps[row][col]
    daily_totals.append(total)
    print(f"Total steps on {days[col]}: {total}")


most_active_total = max(daily_totals)
most_active_index = daily_totals.index(most_active_total)

print(f"\nMost active day overall: {days[most_active_index]}")
print(f"Steps on that day: {most_active_total}")
