# Call Volume Estimator

This Python script is used to estimate the monthly inbound call volume for a call center based on the number of agents, average call duration, agent occupancy, and operating hours.

## Prerequisites

This script requires Python 3 to run. If you haven't installed Python 3 yet, you can download it from the official site: https://www.python.org/downloads/

## Usage

1. Clone the repository or download the Python script.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using the command `python call_volume_estimator.py`.
5. The script will prompt you to enter:
   - Average call duration (in minutes)
   - Open hours for each day of the week (in hours)
   - Number of working days in a month
   - Number of agents
   - Agent occupancy (as a decimal between 0 and 1)
6. After you've entered all the necessary information, the script will calculate and output the projected monthly inbound call volume, formatted to two decimal places.

## Sample Output

Projected monthly inbound call volume is: 12345.67 calls

This means that based on the input parameters, the call center is estimated to receive approximately 12345.67 calls over the course of a month.

## Note

The script assumes that all agents work all open hours every working day. If that's not the case in your situation, you would need to adjust the script accordingly.
