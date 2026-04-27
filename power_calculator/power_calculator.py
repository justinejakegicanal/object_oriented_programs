class PowerCalculator:
    def __init__(self, source_numbers, squares_file, cubes_file):
        self.source_numbers = source_numbers
        self.squares_file = squares_file
        self.cubes_file = cubes_file

    def apply_powers(self):
        try:
            with open(self.source_numbers, 'r') as file:
                all_numbers = [int(line.strip()) for line in file if line.strip()]

            squared_evens = [str(num**2) for num in all_numbers if num % 2 == 0]
            cubed_odds = [str(num**3) for num in all_numbers if num % 2 != 0]

            with open(self.squares_file, 'w') as squares:
                squares.write('\n'.join(squared_evens))

            with open(self.cubes_file, 'w') as cubes:
                cubes.write('\n'.join(cubed_odds))

            print(f"Success! Checked '{self.squares_file}' and '{self.cubes_file}'.")
        except FileNotFoundError:
            print(f"Error: The input file '{self.source_numbers}' does not exist.")