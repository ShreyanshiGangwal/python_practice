# Function using *args and **kwargs....

def display_info(*args, **kwargs):
    print("Positional arguments:", args)  # This will print the tuple of positional arguments
    print("Keyword arguments:", kwargs)   # This will print the dictionary of keyword arguments

# Example usage:
display_info("Alice", "Bob", age=25, city="New York")