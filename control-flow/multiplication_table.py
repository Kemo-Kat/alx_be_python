# multiplication_table.py
# Multiplication Table Generator

def main():
    # Prompt user for a number
    number = float(input("Enter a number to see its multiplication table: "))
    
    # Generate and print the multiplication table using a for loop
    print(f"\nMultiplication table for {number}:")
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

# Run the program
if __name__ == "__main__":
    main()