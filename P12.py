rainfall_data_file = open('rainfall.txt', 'r')
rainfall_lines = rainfall_data_file.readlines()
rainfall_data_file.close()

rainfall_data = [float(line.split(':')[1].strip()) for line in rainfall_lines]

print("Data list:")
months = [
    'January', 
    'February', 
    'March', 
    'April',
    'May', 
    'June', 
    'July', 
    'August',
    'September', 
    'October', 
    'November', 
    'December'
]
for month, rainfall in zip(months, rainfall_data):
    print(f"{month}: {rainfall}")

highest = max(rainfall_data)
lowest = min(rainfall_data)
total = sum(rainfall_data)
average = total / len(rainfall_data)

total_formatted = '{:.2f}'.format(total)
average_formatted = '{:.2f}'.format(average)

print(f"\nHighest: {months[rainfall_data.index(highest)]} {highest}")
print(f"Lowest: {months[rainfall_data.index(lowest)]} {lowest}")
print(f"Total: {total_formatted}")
print(f"Average: {average_formatted}")
