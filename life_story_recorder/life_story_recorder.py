import datetime

class LifeStoryRecorder:
    def __init__(self, log_file="mylife.txt"):
        self.log_file = log_file

    def record_entries(self):
        with open(self.log_file, 'a') as file:
            while True:
                user_input = input("Enter line: ")
                
                # UPGRADE: Fetch current time and format it (e.g., [2026-04-28 10:00 AM])
                current_time = datetime.datetime.now().strftime("[%Y-%m-%d %I:%M %p]")
                formatted_entry = f"{current_time} {user_input}\n"
                
                file.write(formatted_entry)
                
                ask_continue = input("Are there more lines y/n? ").strip().lower()
                if ask_continue != 'y':
                    break
                    
        print(f"Life story entries successfully saved to {self.log_file}.")