import psutil


def check_cpu(threshold):
    """Check CPU usage and print status."""
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        print("CPU Usage:", cpu_usage, "%")

        if cpu_usage > threshold:
            print("CPU ALERT")
        else:
            print("CPU OK")
    except Exception as e:
        print(f"Error checking CPU usage: {e}")


def check_memory(threshold):
    """Check memory usage and print status."""
    try:
        memory_usage = psutil.virtual_memory().percent
        print("Memory Usage:", memory_usage, "%")

        if memory_usage > threshold:
            print("MEMORY ALERT")
        else:
            print("MEMORY OK")
    except Exception as e:
        print(f"Error checking memory usage: {e}")


def check_disk(threshold):
    """Check disk usage and print status."""
    try:
        disk_usage = psutil.disk_usage('/').percent
        print("Disk Usage:", disk_usage, "%")

        if disk_usage > threshold:
            print("DISK ALERT")
        else:
            print("DISK OK")
    except Exception as e:
        print(f"Error checking disk usage: {e}")


def get_threshold_input(prompt):
    """Get an integer threshold from user with input validation."""
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 100:
                return value
            else:
                print("Please enter a percentage between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    print("System Health Check Threshold Setup")

    cpu_threshold = get_threshold_input("Enter CPU threshold (%): ")
    memory_threshold = get_threshold_input("Enter Memory threshold (%): ")
    disk_threshold = get_threshold_input("Enter Disk threshold (%): ")

    print("\n--- System Health Check ---")
    check_cpu(cpu_threshold)
    check_memory(memory_threshold)
    check_disk(disk_threshold)


if __name__ == "__main__":
    main()
