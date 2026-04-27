class EvenOddSeparator:
    def __init__(self, source_file, even_file, odd_file):
        """Initializes the file names for the source and the outputs."""
        self.source_file = source_file
        self.even_file = even_file
        self.odd_file = odd_file

    def process_and_separate(self):
        """Reads integers, separates them by parity, and writes to files."""
        try:
            with open(self.source_file, 'r') as file:
                # This line reads each line, strips whitespace, and converts to int
                # only if the line isn't empty.
                numbers = [int(line.strip()) for line in file if line.strip()]

            even_nums = [str(n) for n in numbers if n % 2 == 0]
            odd_nums = [str(n) for n in numbers if n % 2 != 0]

            with open(self.even_file, 'w') as evens:
                evens.write('\n'.join(even_nums))

            with open(self.odd_file, 'w') as odds:
                odds.write('\n'.join(odd_nums))

            print(f"Success! Processed {len(numbers)} total integers.")
            print(f"-> {len(even_nums)} even numbers saved to '{self.even_file}'")
            print(f"-> {len(odd_nums)} odd numbers saved to '{self.odd_file}'")

        except FileNotFoundError:
            print(f"Error: The file '{self.source_file}' was not found.")
            print("Tip: Make sure 'numbers.txt' is in the same folder as your scripts.")
        except ValueError:
            print(f"Error: '{self.source_file}' contains non-integer data.")