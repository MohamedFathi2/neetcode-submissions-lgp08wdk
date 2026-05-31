class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, w_1 : str, w_2 : str = ""):
        if w_2:
            return w_1 + w_2
        return w_1.upper()



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
