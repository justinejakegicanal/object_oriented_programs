class NumberSeparator:
    def __init__(self, source_file, even_file, odd_file):
        self.source_file = source_file
        self.even_file = even_file
        self.odd_file = odd_file

    def process_and_separate(self):
        try:
            with open(self.source_file, 'r') as file:
                numbers = [int(line.strip()) for line in file if line.strip()]

            even_nums = [str(n) for n in numbers if n % 2 == 0]
            odd_nums = [str(n) for n in numbers if n % 2 != 0]

            with open(self.even_file, 'w') as evens:
                evens.write('\n'.join(even_nums))

            with open(self.odd_file, 'w') as odds:
                odds.write('\n'.join(odd_nums))

            print(f"Success: Separated {len(even_nums)} even and {len(odd_nums)} odd numbers.")
        except FileNotFoundError:
            print(f"Error: The file '{self.source_file}' was not found.")