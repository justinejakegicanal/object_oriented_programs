import datetime

class LifeStoryRecorder:
    def __init__(self, target_file_path="mylife.txt"):
        self.target_file_path = target_file_path
        self.current_session_year = 2026

    def record_entries(self):
        author_full_name = input("Enter author name: ")
        author_birth_year = int(input("Enter birth year: "))
        calculated_session_age = self.current_session_year - author_birth_year

        with open(self.target_file_path, 'a') as output_file:
            session_header = f"\n--- NEW ENTRY BY: {author_full_name} ({calculated_session_age} years old) ---\n"
            output_file.write(session_header)

            while True:
                entry_narrative = input("Enter line: ")
                current_timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %I:%M %p]")
                formatted_entry_line = f"{current_timestamp} {entry_narrative}\n"
                
                output_file.write(formatted_entry_line)
                
                continuation_prompt_response = input("Are there more lines y/n? ").strip().lower()
                if continuation_prompt_response != 'y':
                    break
                    
        print(f"\nLife story entries for {author_full_name} successfully saved to {self.target_file_path}.")