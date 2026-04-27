from even_odd_separator import EvenOddSeparator

def main():
    separator = EvenOddSeparator('numbers.txt', 'even.txt', 'odd.txt')
    separator.process_and_separate()

if __name__ == "__main__":
    main()