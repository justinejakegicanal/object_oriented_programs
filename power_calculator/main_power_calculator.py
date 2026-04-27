import argparse
from power_calculator import PowerCalculator

def main():
    parser = argparse.ArgumentParser(description="Square even numbers and cube odd numbers from a text file.")
    
    parser.add_argument('--input', type=str, default='integers.txt', help='The source text file containing integers.')
    parser.add_argument('--evens', type=str, default='double.txt', help='The output file for squared even numbers.')
    parser.add_argument('--odds', type=str, default='triple.txt', help='The output file for cubed odd numbers.')
    
    args = parser.parse_args()

    # Pass the dynamic terminal arguments to the class
    calculator = PowerCalculator(args.input, args.evens, args.odds)
    calculator.apply_powers()

if __name__ == "__main__":
    main()