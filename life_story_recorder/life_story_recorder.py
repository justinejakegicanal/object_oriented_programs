class LifeStoryRecorder:
    def __init__(self, log_file="mylife.txt"):
        self.log_file = log_file

    def record_entries(self):
        # UPGRADE: Changed 'w' to 'a' to prevent overwriting past entries
        with open(self.log_file, 'a') as file:
            while True:
                user_input = input("Enter line: ")
                file.write(user_input + '\n')
                
                ask_continue = input("Are there more lines y/n? ").strip().lower()
                if ask_continue != 'y':
                    break
                    
        print(f"Life story entries successfully saved to {self.log_file}.")