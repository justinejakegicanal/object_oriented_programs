class NumberSeparator:
    def __init__(self, source_file, even_file, odd_file):
        self.source_file = source_file
        self.even_file = even_file
        self.odd_file = odd_file

    def process_and_separate(self):
        with open(self.source_file, 'r') as file:
            numbers = [int(line.strip()) for line in file if line.strip()]

