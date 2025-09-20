# pattern_drawing.py
# Drawing Patterns with Nested Loops

def main():
    # Prompt user for pattern size
    size = int(input("Enter the size of the pattern: "))
    
    # Input validation to ensure positive integer
    if size <= 0:
        print("Please enter a positive integer.")
        return
    
    # Draw the pattern using nested loops
    print(f"\nSquare pattern of size {size}:")
    
    # Initialize row counter for while loop
    row = 0
    
    # Outer while loop for rows
    while row < size:
        # Inner for loop for columns - prints asterisks in the current row
        for col in range(size):
            print("*", end="")
        
        # Move to the next line after completing a row
        print()
        
        # Increment row counter
        row += 1

# Run the program
if __name__ == "__main__":
    main()