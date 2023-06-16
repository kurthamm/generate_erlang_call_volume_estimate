def get_input(prompt, err_msg="Invalid input. Please enter a valid number."):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Please enter a positive value.")
            return value
        except ValueError as e:
            print(e)


def get_hours_per_day():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    total_hours = 0

    for day in days:
        hours = get_input(f"Enter the open hours for {day}: ")
        total_hours += hours

    return total_hours / len(days)


def calculate_call_volume():
    # Get necessary inputs
    average_call_duration = get_input("Enter average call duration (in minutes): ")
    average_open_hours_per_day = get_hours_per_day()
    days_per_month = get_input("Enter number of working days in a month: ")
    number_of_agents = get_input("Enter the number of agents: ")
    agent_occupancy = get_input("Enter the agent occupancy (as a decimal between 0 and 1): ")

    # Convert call duration from minutes to hours
    average_call_duration_hours = average_call_duration / 60.0

    # Convert working hours to working minutes
    working_minutes_per_day = average_open_hours_per_day * 60.0

    # Calculate total working minutes in a month
    total_working_minutes_per_month = working_minutes_per_day * days_per_month

    # Calculate total agent working minutes in a month
    total_agent_working_minutes_per_month = total_working_minutes_per_month * number_of_agents

    # Calculate inbound call volume based on agent occupancy
    inbound_call_volume = (total_agent_working_minutes_per_month * agent_occupancy) / average_call_duration

    print(f"Projected monthly inbound call volume is: {format(inbound_call_volume, '.2f')} calls")


# Execute the function
calculate_call_volume()