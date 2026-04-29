from even_odd_separator import EvenOddSeparator

def main():
    separator_instance = EvenOddSeparator('numbers.txt', 'even.txt', 'odd.txt')
    separator_instance.process_and_separate()

if __name__ == "__main__":
    main()