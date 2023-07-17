import matplotlib.pyplot as plt

# 定义文件名列表
files = ['/Users/xs/PycharmProjects/math_lzy/111.txt',
         '/Users/xs/PycharmProjects/math_lzy/file_20230717_030011.txt',
         '/Users/xs/PycharmProjects/math_lzy/-1.txt',
         '/Users/xs/PycharmProjects/math_lzy/data.txt']

# 定义颜色列表
colors = ['r', 'g', 'b', 'y']

plt.figure()

for file_index in range(4):
    # Initialize x, y_min as empty lists
    x = []
    y_min = []

    # Read the first 1500 lines from the txt file
    with open(files[file_index], 'r') as f:
        line_count = 0
        for line in f:
            # Break the loop if line_count reaches 1500
            if line_count >= 150:
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

    # Add the minimum value line
    plt.plot(x, y_min, label=f'K {(file_index + 1) * 0.25} ', color=colors[file_index])

# Add the Y-axis title
plt.ylabel('Max Time',fontsize=15)

# Add the X-axis label
plt.xlabel(' ', fontsize=15)

# Add the legend
plt.legend()

# Show the plot
plt.show()
