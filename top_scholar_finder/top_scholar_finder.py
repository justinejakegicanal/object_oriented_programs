class TopScholarFinder:
    def __init__(self, student_records_file):
        self.student_records_file = student_records_file

    def get_highest_scholar(self):
        top_scholar_name = "None"
        best_grade = 5.0 

        try:
            with open(self.student_records_file, 'r') as file:
                for line in file:
                    if not line.strip():
                        continue
                    
                    data_parts = line.strip().rsplit(' ', 1)
                    
                    if len(data_parts) == 2:
                        name = data_parts[0]
                        grade = float(data_parts[1])

                        if grade < best_grade:
                            best_grade = grade
                            top_scholar_name = name

            print(f"Top Scholar: {top_scholar_name} (GWA: {best_grade})")

        except FileNotFoundError:
            print(f"Error: '{self.student_records_file}' was not found.")
        except ValueError:
            print("Error: Could not read a grade. Ensure the file format is 'Name GWA'.")