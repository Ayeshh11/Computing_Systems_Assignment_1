import time
import csv

workloads = [100000, 500000, 2000000]
results = []

for size in workloads:
    times = []

    for run in range(3):
        start = time.perf_counter()

        total = sum(i * i for i in range(size))

        end = time.perf_counter()
        duration = end - start
        times.append(duration)

        print(f"Size: {size}, Run {run + 1}: {duration:.4f} seconds")

    average = sum(times) / len(times)

    print(f"Average: {average:.4f} seconds")
    print("--------------------------")

    results.append([size, *times, average])

with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Workload",
        "Run 1 (s)",
        "Run 2 (s)",
        "Run 3 (s)",
        "Average (s)"
    ])
    writer.writerows(results)

print("Results saved to results.csv")



