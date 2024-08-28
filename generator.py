import random
from text import choices_for_text

class Generate:
    def __init__(self, array):
        self.array = array
        self.last_text = None
    
    def randomText(self):
        if not self.array:
            raise ValueError("The array is empty.")
        
        # Avoid repeating the last text
        available_texts = [text for text in self.array if text != self.last_text]
        
        if not available_texts:
            raise ValueError("No unique texts available to display.")
        
        self.last_text = random.choice(available_texts)
        return self.last_text

    def get_choices(self, current_text):
        if not self.array:
            raise ValueError("The array is empty.")
        
        # Generate a dictionary of choices based on the current text
        choices = choices_for_text.get(current_text, {})
        return choices
