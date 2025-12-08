from rich.console import Console

console = Console(highlight=True)

import day1.solution
import day2.solution
import day3.solution
import day4.solution
import day5.solution
import day6.solution
import day7.solution

def print_available_days():
    console.print("What solution do you want to run?")
    console.print("0. Exit")
    console.print("1. Day 1")
    console.print("2. Day 2")
    console.print("3. Day 3")
    console.print("4. Day 4")
    console.print("5. Day 5")
    console.print("6. Day 6")
    console.print("7. Day 7")

def run_day(day):
    match day:
        case "0":
            print("Exiting...")
            return
        case 1:
            day1.solution.main()
        case 2:
            day2.solution.main()
        case 3:
            day3.solution.main()
        case 4:
            day4.solution.main()
        case 5:
            day5.solution.main()
        case 6:
            day6.solution.main()
        case 7:
            day7.solution.main()
        case _:
            print("Invalid day")

def main():
    print_available_days()
    day = int(input("Enter the day: "))
    run_day(day)


if __name__ == "__main__":
    main()
