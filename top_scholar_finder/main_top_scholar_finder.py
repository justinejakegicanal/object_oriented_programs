from top_scholar_finder import TopScholarFinder

def main():
    scholar_finder = TopScholarFinder('students.txt')
    scholar_finder.get_highest_scholar()

if __name__ == "__main__":
    main()