def is_whole_number(text):
    """Return True when text is a valid whole number string."""
    if len(text) == 0:
        return False

    if text[0] in "+-":
        text = text[1:]
        if len(text) == 0:
            return False

    return text.isdigit()


def get_initial_readings():
    """Return the starting temperature readings for the monitoring system."""
    return [25, 28, 32, 36, 29]


def display_readings(readings):
    """Display each temperature reading with its position number."""
    print("\nCURRENT READINGS")
    print("----------------")
    for index in range(len(readings)):
        print(f"Reading {index + 1}: {readings[index]} °C")


def add_reading(readings, lowest, highest):
    """Validate one new reading and add it only when it is valid."""
    text = input("Enter new reading: ")

    if len(text) == 0:
        print("Invalid input. The reading cannot be empty.")
    elif not is_whole_number(text):
        print("Invalid input. Enter a whole number only.")
    else:
        reading = int(text)
        if reading < lowest or reading > highest:
            print(f"\nInvalid reading. Enter a value from {lowest} to {highest}.")
        else:
            readings.append(reading)
            print("\nReading added successfully.")


def classify_reading(reading, warning_limit, critical_limit):
    """Return the category label for a single temperature reading."""
    if reading >= critical_limit:
        return "CRITICAL"
    if reading >= warning_limit:
        return "WARNING"
    return "NORMAL"


def display_classifications(readings, warning_limit, critical_limit):
    """Display the classification of every stored reading."""
    print("\nREADING CLASSIFICATION")
    print("----------------------")
    category_monitor = Category(warning_limit, critical_limit)
    for reading in readings:
        category = category_monitor.classify_reading(reading)
        print(f"{reading} °C -> {category}")


def compute_total(readings):
    """Return the total of all readings using a loop."""
    total = 0
    for reading in readings:
        total = total + reading
    return total


def compute_average(readings):
    """Return the average of the readings."""
    return compute_total(readings) / len(readings)


def find_minimum(readings):
    """Return the smallest reading using a loop."""
    minimum = readings[0]
    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum


def find_maximum(readings):
    """Return the largest reading using a loop."""
    maximum = readings[0]
    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum

def count_category(readings, warning_limit, critical_limit, category):
    """Return how many readings belong to the requested category."""
    count = 0
    for reading in readings:
        if classify_reading(reading, warning_limit, critical_limit) == category:
            count = count + 1
    return count


def determine_overall_status(warning_count, critical_count):
    """Return the overall monitoring status using the required priority."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_summary(readings, warning_limit, critical_limit):
    """Calculate and display the numerical and classification summary."""
    number_of_readings = len(readings)
    total = compute_total(readings)
    average = total / number_of_readings
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)

    category_monitor = Category(warning_limit, critical_limit)
    normal_count = category_monitor.count_category(readings, "NORMAL")
    warning_count = category_monitor.count_category(readings, "WARNING")
    critical_count = category_monitor.count_category(readings, "CRITICAL")

    normal_percentage = normal_count / number_of_readings * 100
    warning_percentage = warning_count / number_of_readings * 100
    critical_percentage = critical_count / number_of_readings * 100
    overall_status = category_monitor.determine_overall_status(warning_count, critical_count)

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings : {number_of_readings}")
    print(f"Total of readings : {total}")
    print(f"Average temperature : {average:.2f} °C")
    print(f"Minimum temperature : {minimum} °C")
    print(f"Maximum temperature : {maximum} °C")
    print()
    print(f"NORMAL : {normal_count} ({normal_percentage:.2f}%)")
    print(f"WARNING : {warning_count} ({warning_percentage:.2f}%)")
    print(f"CRITICAL : {critical_count} ({critical_percentage:.2f}%)")
    print()
    print(f"Overall Status: {overall_status}")


def display_menu():
    """Display the main menu options."""
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


class Category:
    """Represent a temperature category with status thresholds."""

    def __init__(self, warning_limit, critical_limit):
        self.warning_limit = warning_limit
        self.critical_limit = critical_limit

    def classify_reading(self, reading):
        """Return a category label for the supplied reading."""
        if reading >= self.critical_limit:
            return "CRITICAL"
        if reading >= self.warning_limit:
            return "WARNING"
        return "NORMAL"

    def count_category(self, readings, category):
        """Return how many stored readings match the requested category."""
        count = 0
        for reading in readings:
            if self.classify_reading(reading) == category:
                count += 1
        return count

    def determine_overall_status(self, warning_count, critical_count):
        """Return the monitoring status using the required priority."""
        if critical_count >= 1:
            return "ATTENTION REQUIRED"
        if warning_count >= 1:
            return "MONITOR"
        return "NORMAL"


def main():
    """Run the device monitoring menu until the user chooses Exit."""
    readings = get_initial_readings()
    warning_limit = 30
    critical_limit = 35

    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            add_reading(readings, 0, 100)
        elif choice == "3":
            display_classifications(readings, warning_limit, critical_limit)
        elif choice == "4":
            display_summary(readings, warning_limit, critical_limit)
        elif choice == "5":
            print("\nThank you for using the Device Monitoring System.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")


main()