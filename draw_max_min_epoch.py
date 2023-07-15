import matplotlib.pyplot as plt

# Initialize x, y_min, y_avg as empty lists
x = []
y_min = []
y_avg = []

# Read the first 1500 lines from the txt file
with open('/Users/xs/PycharmProjects/math_lzy/data.txt', 'r') as f:
    line_count = 0
    for line in f:
        # Break the loop if line_count reaches 1500
        if line_count >= 1500:
            break

        # Increment line_count
        line_count += 1

        columns = line.strip().split(':')

        # Add x coordinate
        x.append(int(columns[0]))

        # Convert the string to a list
        y_data = list(map(int, columns[2].strip('[]').split(',')))

        # Calculate the minimum value
        y_min.append(min(y_data))

        # Calculate the average value
        y_avg.append(sum(y_data) / len(y_data))

# Create the plot
plt.figure()

# Add the minimum value line
plt.plot(x, y_min, label='Min')

# Add the average value line
plt.plot(x, y_avg, label='Avg')

# Add the Y-axis title
plt.ylabel('Processing Time',fontsize=15)

# Add the X-axis label
plt.xlabel('Genetic Generation', fontsize=15)

# Add the legend
plt.legend()

# Annotate the current values at every 400 generations
for i in range(0, len(x), 450):
    plt.annotate(f'Min: {y_min[i]}', (x[i], y_min[i]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=15)
    plt.annotate(f'Avg: {y_avg[i]}', (x[i], y_avg[i]), textcoords="offset points", xytext=(0, 20), ha='center', fontsize=15)

# Show the plot
plt.show()
