# Computing_Systems_Assignment_1
Computing Systems — Mission 3: Workload and Performance
Investigation question
Does increasing the workload size affect the execution time of a Python program?

Prediction
Before testing, I predicted that larger workloads would take longer because the program would perform more arithmetic operations. I expected small differences between repeated trials because other programs and operating system activity can influence timing.

Project overview
This project measures the time Python takes to calculate the sum of squared integers at three workload sizes (100,000, 500,000, and 2,000,000). Each workload is measured three times with time.perf_counter(). The program prints the individual times and their averages and generates results.csv.

Device and environment
Primary device: Microsoft Surface Pro 8
Operating system: Windows 11 Home (64-bit)
Processor: 11th Gen Intel Core i5-1135G7 (4 cores, 8 logical processors)
RAM: 8 GB
Python version: Record the result of py --version on the computer used for the experiment (not visible in the supplied evidence).
Environment: Windows 11 computer using Python and Command Prompt. Confirm whether execution was local before publishing.
Project files
performance_test.py — code for the calculation, timing, repetition, and CSV output.
results.csv — add the original file generated on the tested computer for full-precision readings; it is not reconstructed here.
program_execution_evidence.png — screenshot of actual execution provided for this assignment.
README.md — setup instructions, measured results, and explanation.

How to run
Install Python 3 if necessary.

Download the project folder or clone its repository.

Open the folder in File Explorer and type cmd in the address bar.

Check the Python version:

py --version
Run the program:

py performance_test.py
Read the terminal results and open the newly generated results.csv in Excel or a text editor. Because workload timing is system-dependent, a fresh run will not necessarily match the original measurements.

The program uses only the standard Python time and csv modules; no external packages are required.

Experimental procedure
For each of the three input sizes, the program times sum(i * i for i in range(size)) using time.perf_counter(). It repeats the calculation three times and computes the arithmetic mean. Only the calculation is timed; displaying results and writing the CSV occur outside the timed interval.

Actual experimental results
The following times are actual values transcribed from the supplied execution screenshot. They are rounded to four decimal places, exactly as shown in the terminal; the original results.csv can retain greater precision.

Workload	Run 1 (s)	Run 2 (s)	Run 3 (s)	Average (s)
Small — 100,000	0.0078	0.0110	0.0068	0.0085
Medium — 500,000	0.0400	0.0453	0.0488	0.0447
Large — 2,000,000	0.1978	0.1737	0.1786	0.1834

Analysis and interpretation
The mean time increased as the workload increased. The medium workload processed five times as many integers as the small one and took approximately 5.3 times as long (0.0447 ÷ 0.0085). The large workload processed twenty times as many integers as the small one and took approximately 21.6 times as long (0.1834 ÷ 0.0085).

This supports the prediction that more arithmetic work increases elapsed execution time for this program. The growth was broadly proportional to input size, but not perfectly proportional. Trial-to-trial variation was visible: small-workload measurements ranged from 0.0068 to 0.0110 s, medium from 0.0400 to 0.0488 s, and large from 0.1737 to 0.1978 s.

The program repeatedly performs Python integer multiplication and addition, so more iterations create more work. Differences between repeats may be affected by Windows scheduling, other processes, changes in CPU operating speed, and measurement noise. time.perf_counter() measures elapsed time, not CPU utilization or CPU-only time.

Limitations
Tests were conducted using one device and one kind of Python computation; results should not be generalized to every program.
Each workload was repeated only three times.
Background activity and processor frequency were not experimentally controlled.
The displayed terminal values were rounded to four decimal places.
The original results.csv is needed for full-precision source data.
Conclusion
The actual mean execution times were 0.0085 s, 0.0447 s, and 0.1834 s for the small, medium, and large workloads, respectively. The evidence shows a clear increase in elapsed execution time with workload size for this Python calculation on the investigated Windows 11 device. The prediction was supported within the tested conditions.

Academic integrity and AI assistance
The numerical results above came from the my actual execution screenshot. AI was used to explain the assignment, help with Python code, and draft this README. AI has not been used for any other part of the assignment
