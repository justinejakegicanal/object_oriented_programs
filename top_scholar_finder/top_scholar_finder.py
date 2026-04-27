class TopScholarFinder:
    def __init__(self, student_records_file):
        self.student_records_file = student_records_file

    def get_highest_scholar(self):
        top_scholar_name = "None"
        best_grade = 5.0  

        with open(self.student_records_file, 'r') as file:
            for line in file:
                pass 