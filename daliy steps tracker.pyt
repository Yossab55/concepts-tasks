def daily_steps_tracker():
    steps = input("Enter the number of steps taken each day separated by spaces: ").split()
    
    steps = list(map(int, steps))
    
    highest_steps = max(steps)
    lowest_steps = min(steps)
    
    average_steps = sum(steps) / len(steps)
    
    sorted_steps = sorted(steps, reverse=True) #in descending order
    
    print("\nResults:")
    print(f"Highest Step Count: {highest_steps}")
    print(f"Lowest Step Count: {lowest_steps}")
    print(f"Average Step Count: {average_steps:.2f}")
    print(f"Step Counts in Descending Order: {sorted_steps}")

daily_steps_tracker()
