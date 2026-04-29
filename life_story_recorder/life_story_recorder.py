import datetime

class LifeStoryRecorder:
    def __init__(self, target_file_path="mylife.txt"):
        self.target_file_path = target_file_path
        self.current_session_year = 2026

    def record_entries(self):
        author_full_name = input("Enter author name: ")
        author_birth_year = int(input("Enter birth year: "))
        current_mood_tag = input("How are you feeling today? (e.g., Happy, Tired): ")
        
        calculated_session_age = self.current_session_year - author_birth_year
        session_entry_count = 0
        total_session_word_count = 0

        with open(self.target_file_path, 'a') as output_file:
            session_header = (
                f"\n{'='*30}\n"
                f"SESSION: {author_full_name} ({calculated_session_age} yrs old)\n"
                f"MOOD: {current_mood_tag}\n"
                f"{'='*30}\n"
            )
            output_file.write(session_header)

            while True:
                entry_narrative = input("Enter line: ")
                current_timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %I:%M %p]")
                
                session_entry_count += 1
                total_session_word_count += len(entry_narrative.split())
                
                formatted_entry_line = f"{current_timestamp} {entry_narrative}\n"
                output_file.write(formatted_entry_line)
                
                continuation_prompt_response = input("Are there more lines y/n? ").strip().lower()
                if continuation_prompt_response != 'y':
                    break
            
            session_footer = f"--- End of Session | Entries: {session_entry_count} | Words: {total_session_word_count} ---\n"
            output_file.write(session_footer)
                    
        print(f"\nJournaling complete. {session_entry_count} entries saved for {author_full_name}.")