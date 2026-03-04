    [5300, 6200, 7000, 6500, 7200],  
    [4500, 5800, 6000, 6100, 6900],  
    [7000, 7500, 8000, 7800, 8200]   

print("Daily Steps for Each Friend (Mon–Fri):")
for i in range(len(steps)):
    print(f"Friend {i+1}: {steps[i]}")

print()


print("Totals and Averages:")
for i in range(len(steps)):
    total = sum(steps[i])
    average = total / len(steps[i])
    print(f"Friend {i+1} → Total: {total}, Average: {average:.2f}")

print()

# Using the array honestly made it way easier to look at all the step data because everything was already organized in rows and columns. I didn’t have to keep checking each number one by one since the loops handled most of it. The totals and averages were pretty simple to do, but finding the max value took me a bit longer since I had to check every number in the dataset. Overall it helped me understand the data better and it wasn’t as hard as I thought.
