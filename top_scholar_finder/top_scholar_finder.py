class TopScholarFinder:
    def __init__(self, student_records_file):
        self.student_records_file = student_records_file

    def get_highest_scholar(self):
        top_scholar_name = "None"
        best_grade = 5.0  

        with open(self.student_records_file, 'r') as file:
            for line in file:
                data_parts = line.strip().rsplit(' ', 1)
                
                if len(data_parts) == 2:
                    student_name = data_parts[0]
                    current_grade = float(data_parts[1])
                    
                    if current_grade < best_grade:
                        best_grade = current_grade
                        top_scholar_name = student_name