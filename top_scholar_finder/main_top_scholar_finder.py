from top_scholar_finder import TopScholarFinder

def main():
    scholar_search_engine = TopScholarFinder('students.txt')
    scholar_search_engine.get_highest_scholar()

if __name__ == "__main__":
    main()