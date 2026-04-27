import argparse
from power_calculator import PowerCalculator

def main():
    parser = argparse.ArgumentParser(description="Square even numbers and cube odd numbers from a text file.")
    
    parser.add_argument('--input', type=str, default='integers.txt')
    parser.add_argument('--evens', type=str, default='double.txt')
    parser.add_argument('--odds', type=str, default='triple.txt')

    args = parser.parse_args()

    calculator = PowerCalculator(args.input, args.evens, args.odds)
    calculator.apply_powers()

if __name__ == "__main__":
    main()