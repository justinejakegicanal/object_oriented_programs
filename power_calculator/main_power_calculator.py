import argparse
from power_calculator import PowerCalculator

def main():
    terminal_args_parser = argparse.ArgumentParser(description="Professional Power Calculator")
    terminal_args_parser.add_argument('--input', default='integers.txt')
    terminal_args_parser.add_argument('--verbose', action='store_true', help="Show live math process")

    cli_inputs = terminal_args_parser.parse_args()
    
    calculator_service = PowerCalculator(cli_inputs.input, 'double.txt', 'triple.txt')
    calculator_service.apply_powers(is_verbose_enabled=cli_inputs.verbose)

if __name__ == "__main__":
    main()