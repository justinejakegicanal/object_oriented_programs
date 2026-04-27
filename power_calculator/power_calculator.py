class PowerCalculator:
    def __init__(self, source_numbers, squares_file, cubes_file):
        self.source_numbers = source_numbers
        self.squares_file = squares_file
        self.cubes_file = cubes_file

    def apply_powers(self):
        with open(self.source_numbers, 'r') as file:
            all_numbers = [int(line.strip()) for line in file if line.strip()]

        squared_evens = [str(num**2) for num in all_numbers if num % 2 == 0]
        cubed_odds = [str(num**3) for num in all_numbers if num % 2 != 0]