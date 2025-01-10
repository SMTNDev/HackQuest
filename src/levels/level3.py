from src.core.utils import read_file

def level3():
    """
    Level 3: Log File Analysis
    The player must analyze a simulated log file and find the hidden keyword.
    """
    print("Level 3: Log File Analysis")
    print("Analyze the log file for suspicious activity or hidden keywords.")

    # Path to the simulated log file
    log_file_path = "assets/levels/level3_logs.txt"

    # Read the log file content
    try:
        logs = read_file(log_file_path)
        print("Log File Content:")
        print(logs)
    except FileNotFoundError:
        print("Error: Log file not found!")
        return False

    # Prompt the player for the hidden keyword
    hidden_keyword = "ACCESS_GRANTED"
    print("\nHint: Look for unusual patterns or repeated sequences in the logs.")

    # Allow the player to guess
    while True:
        guess = input("Enter the hidden keyword: ").strip()
        if guess == hidden_keyword:
            print("Correct! You've successfully analyzed the logs.")
            return True
        else:
            print("Incorrect. Try again!")

