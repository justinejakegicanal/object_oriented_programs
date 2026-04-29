class PowerCalculator:
    def __init__(self, source_data_path, square_file_path, cube_file_path):
        self.source_data_path = source_data_path
        self.square_file_path = square_file_path
        self.cube_file_path = cube_file_path

    def apply_powers(self, is_verbose_enabled=False):
        try:
            with open(self.source_data_path, 'r') as source_file:
                raw_integers = [int(line.strip()) for line in source_file if line.strip()]

            even_squares, odd_cubes = [], []

            for current_number in raw_integers:
                if current_number % 2 == 0:
                    calculated_result = current_number ** 2
                    even_squares.append(str(calculated_result))
                    if is_verbose_enabled:
                        print(f"[DEBUG] Even {current_number}² = {calculated_result}")
                else:
                    calculated_result = current_number ** 3
                    odd_cubes.append(str(calculated_result))
                    if is_verbose_enabled:
                        print(f"[DEBUG] Odd {current_number}³ = {calculated_result}")

            with open(self.square_file_path, 'w') as output_f:
                output_f.write('\n'.join(even_squares))
            with open(self.cube_file_path, 'w') as output_f:
                output_f.write('\n'.join(odd_cubes))

            print("\nCalculation complete. Files updated successfully.")

        except Exception as error_msg:
            print(f"Critical System Error: {error_msg}")