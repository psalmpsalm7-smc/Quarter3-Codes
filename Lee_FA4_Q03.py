names = ["Me", "Marvoun", "Stefanno"]

steps = [
    [6700, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]


totals = []
for i in range(len(steps)):
    total = sum(steps[i])
    totals.append(total)
    print(f"{names[i]}'s total steps: {total}")
highest_total = max(totals)
lowest_total = min(totals)
highest_index = totals.index(highest_total)
lowest_index = totals.index(lowest_total)
print(f"\nPerson with the highest total steps: {names[highest_index]}")
print(f"Highest total steps: {highest_total}")
difference = highest_total - lowest_total
print(f"Difference between highest and lowest total steps: {difference}")
