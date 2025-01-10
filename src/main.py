from config.settings import COLORS, GAME_NAME, VERSION
from src.core.commands import execute_command
from src.levels.level1 import level1
from src.levels.level2 import level2
from src.levels.level3 import level3

def display_help():
    """Display the list of available commands."""
    print(f"{COLORS['success']}Available Commands:{COLORS['reset']}")
    print("- help          : Show this help menu")
    print("- level1        : Start Level 1 (Password Retrieval)")
    print("- level2        : Start Level 2 (File Decryption)")
    print("- level3        : Start Level 3 (Log Analysis)")
    print("- exit          : Exit the game")
    print("- Other Commands: Simulate hacking tools (e.g., 'scan', 'decrypt')")

def main():
    """Main game loop."""
    print(f"{COLORS['success']}{GAME_NAME} - Version {VERSION}{COLORS['reset']}")
    print("Welcome to the ultimate hacking simulation experience!")
    print("Type 'help' to see available commands.")
    trace_level = 0  # Trace level starts at 0

    while True:
        try:
            command = input("\n>> ").strip().lower()

            if command == "exit":
                print("Exiting game. Goodbye!")
                break
            elif command == "help":
                display_help()
            elif command == "level1":
                print("Starting Level 1...")
                level1()
            elif command == "level2":
                print("Starting Level 2...")
                level2()
            elif command == "level3":
                print("Starting Level 3...")
                level3()
            else:
                # Simulate commands or return invalid command message
                result = execute_command(command)
                print(result)
        except KeyboardInterrupt:
            print("\nExiting game. Goodbye!")
            break
        except Exception as e:
            print(f"{COLORS['error']}An error occurred: {e}{COLORS['reset']}")

if __name__ == "__main__":
    main()
