class EvenOddSeparator:
    def __init__(self, input_file_path, even_output_path, odd_output_path):
        self.input_file_path = input_file_path
        self.even_output_path = even_output_path
        self.odd_output_path = odd_output_path

    def process_and_separate(self):
        try:
            with open(self.input_file_path, 'r') as source_file:
                all_integers = [int(line.strip()) for line in source_file if line.strip()]

            even_numbers_list = [num for num in all_integers if num % 2 == 0]
            odd_numbers_list = [num for num in all_integers if num % 2 != 0]

            total_sum_of_all = sum(all_integers)
            average_value = total_sum_of_all / len(all_integers) if all_integers else 0

            with open(self.even_output_path, 'w') as even_file:
                even_file.write('\n'.join(map(str, even_numbers_list)))
            with open(self.odd_output_path, 'w') as odd_file:
                odd_file.write('\n'.join(map(str, odd_numbers_list)))

            print(f"\n--- Statistics for {self.input_file_path} ---")
            print(f"Total: {len(all_integers)} | Sum: {total_sum_of_all} | Avg: {average_value:.2f}")
            print(f"Success! Data saved to {self.even_output_path} and {self.odd_output_path}.")

        except FileNotFoundError:
            print(f"Error: Hindi mahanap ang '{self.input_file_path}'. Siguraduhing tama ang folder location.")