rainfall_for_chicago_2017 = {
    "Jan": 2.87,
    "Feb": 1.52,
    "Mar": 4.01,
    "Apr": 6.43,
    "May": 3.28,
    "Jun": 3.44,
    "Jul": 7.68,
    "Aug": 2.51,
    "Sep": 0.32,
    "Oct": 8.70,
    "Nov": 1.75,
    "Dec": 0.59
}
rainfall_list = list(rainfall_for_chicago_2017.values())

if any(val < 0 or not val for val in rainfall_list):
    print("Invalid data: Rainfall cannot be negative or blank.")
else:
    highest = max(rainfall_list)
    lowest = min(rainfall_list)
    total = sum(rainfall_list)
    average = total / len(rainfall_list)

    print("Data list:")
    for month, value in rainfall_for_chicago_2017.items():
        print(f"{month}: {value}")
    print(f"Highest: March {highest:.2f}")
    print(f"Lowest: November {lowest:.2f}")
    print(f"Total: {total:.1f}")
    print(f"Average: {average:.1f}")
