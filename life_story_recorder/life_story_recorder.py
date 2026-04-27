class LifeStoryRecorder:
    def __init__(self, log_file="mylife.txt"):
        self.log_file = log_file

    def record_entries(self):
        with open(self.log_file, 'w') as file:
            pass 