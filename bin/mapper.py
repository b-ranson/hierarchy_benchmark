import matplotlib.pyplot as plt
import numpy as np

num_cpus = int(input())

throughput_matrix = np.zeros((num_cpus, num_cpus))

for cpu1 in range(num_cpus):

    input_line = input().split()

    for cpu2 in range(num_cpus):
        throughput_matrix[cpu1, cpu2] = input_line[cpu2]

png_name = "average_throughput_map.png"

# Generate and display the heatmap
plt.imshow(throughput_matrix, cmap='viridis', interpolation='nearest')
plt.colorbar(label='Throughput (increments/sec)')
plt.xlabel('Thread 1 Core')
plt.ylabel('Thread 2 Core')
plt.title('Throughput Heatmap')
#plt.show() # comment out when in ssh

plt.savefig(png_name)
plt.close()
