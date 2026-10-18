# Simulated Device Monitoring and Alert System
 
**Student Name:** Desiree D. Baron
**Student Number:** 2601349
**Section:** 1CPE-B
 
## Project Description
This program monitors simulated device-temperature readings using a list of numbers.
It classifies each reading as NORMAL, WARNING, or CRITICAL, and it provides a 
numerical summary and an overall monitoring status. The program is for classroom 
practice only and does not connect to a real device or sensor.
 
## Features
- View all current temperature readings and their position numbers.
- Add a new whole-number reading from 0 to 100.
- Reject empty, non-numeric, negative, and above-range readings.
- Classify all readings using the required temperature rules.
- Calculate the total, average, minimum, maximum, category counts, and percentages.
- Determine the overall monitoring status.
- Repeat the menu until the user chooses Exit.

## Requirements
- Python 3 (no external packages)
 
## How to Run
1. Open a terminal in the Week17 folder.
2. Run: python device_monitor.py
3. If your computer uses python3, run: python3 device_monitor.py.
 
## Sample Output
MONITORING SUMMARY
------------------
Number of readings : 5
Total of readings : 160
Average temperature : 32.00 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C

NORMAL : 2 (40.00%)
WARNING : 2 (40.00%)
CRITICAL : 1 (20.00%)

Overall Status: ATTENTION REQUIRED
 
## Test Cases
The program was run with automated input sequences for the listed checks. 
The actual results recorded in test_cases.md are based on those runs. Run 
the program yourself before submitting so you can confirm the results on 
your computer.
 
## Known Limitations
The readings are stored in memory only and are lost when the program closes.
The program uses simulated values and does not read an actual temperature sensor.
The classification limits are classroom rules, not real device-safety standards.
 
## Reflection
I learned how to combine lists, loops, selection statements, and functions in one 
program. The most important part was checking user input before converting it to 
an integer or adding it to the list. I also learned to calculate the total, minimum,
maximum, and category percentages using loops. Boundary values such as 30 °C and 
35 °C need careful conditions so they are both classified as WARNING. In the future,
I would improve the program by saving readings between runs and connecting it to 
a real sensor if that were part of the project requirements.
