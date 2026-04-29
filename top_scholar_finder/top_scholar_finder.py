class TopScholarFinder:
    def __init__(self, student_records_file_path):
        self.student_records_file_path = student_records_file_path

    def get_highest_scholar(self):
        collection_of_top_achievers = []
        highest_recorded_gwa_score = 5.0

        try:
            with open(self.student_records_file_path, 'r') as student_data_source:
                for record_line in student_data_source:
                    if not record_line.strip():
                        continue

                    full_student_name, numerical_grade_string = record_line.strip().rsplit(' ', 1)
                    current_student_gwa = float(numerical_grade_string)

                    if current_student_gwa < highest_recorded_gwa_score:
                        highest_recorded_gwa_score = current_student_gwa
                        collection_of_top_achievers = [full_student_name]
                    elif current_student_gwa == highest_recorded_gwa_score:
                        collection_of_top_achievers.append(full_student_name)

            if collection_of_top_achievers:
                print(f"\nTop Scholar(s): {', '.join(collection_of_top_achievers)}")
                print(f"Achieved GWA: {highest_recorded_gwa_score}")
            else:
                print("No valid student records were found.")

        except FileNotFoundError:
            print(f"Error: Ang file na '{self.student_records_file_path}' ay hindi mahanap.")