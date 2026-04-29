import datetime
import time

class LifeStoryRecorder:
    def __init__(self, target_file_path="mylife.txt"):
        self.target_file_path = target_file_path
        self.current_session_year = 2026

    def get_time_based_greeting(self):
        current_hour = datetime.datetime.now().hour
        if current_hour < 12:
            return "Good morning"
        elif 12 <= current_hour < 18:
            return "Good afternoon"
        else:
            return "Good evening"

    def record_entries(self):
        greeting_prefix = self.get_time_based_greeting()
        author_full_name = input(f"{greeting_prefix}! Enter author name: ")
        author_birth_year = int(input("Enter birth year: "))
        session_topic_category = input("What is the main topic of today's entry? (e.g., Career, Family, Dreams): ")
        current_mood_indicator = input("Current mood: ")
        
        calculated_session_age = self.current_session_year - author_birth_year
        session_start_timestamp = time.time()
        session_entry_count = 0
        total_word_count_in_session = 0

        with open(self.target_file_path, 'a') as output_data_file:
            entry_header_divider = "=" * 40
            session_metadata_header = (
                f"\n{entry_header_divider}\n"
                f"JOURNAL ENTRY: {datetime.datetime.now().strftime('%B %d, %Y')}\n"
                f"AUTHOR: {author_full_name} ({calculated_session_age} years old)\n"
                f"TOPIC: {session_topic_category.upper()}\n"
                f"MOOD: {current_mood_indicator}\n"
                f"{entry_header_divider}\n"
            )
            output_data_file.write(session_metadata_header)

            while True:
                entry_narrative_content = input("Enter line: ")
                timestamp_prefix = datetime.datetime.now().strftime("[%I:%M %p]")
                
                session_entry_count += 1
                total_word_count_in_session += len(entry_narrative_content.split())
                
                formatted_narrative_line = f"{timestamp_prefix} {entry_narrative_content}\n"
                output_data_file.write(formatted_narrative_line)
                
                user_continuation_choice = input("Add another line? (y/n): ").strip().lower()
                if user_continuation_choice != 'y':
                    break
            
            session_end_timestamp = time.time()
            elapsed_session_time_minutes = round((session_end_timestamp - session_start_timestamp) / 60, 2)
            
            session_summary_footer = (
                f"{'-'*40}\n"
                f"SUMMARY: {session_entry_count} entries | {total_word_count_in_session} words\n"
                f"TIME SPENT: {elapsed_session_time_minutes} minutes\n"
                f"{'-'*40}\n"
            )
            output_data_file.write(session_summary_footer)
                    
        print(f"\nJournaling session for '{session_topic_category}' has been successfully archived.")