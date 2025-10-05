import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Robust Division Calculator")
        print("Usage: python main.py <numerator> <denominator>")
        print("Examples:")
        print("  python main.py 10 5")
        print("  python main.py 7.5 2.5")
        print("  python main.py -15 3")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    
    # Format output nicely
    if isinstance(result, (int, float)):
        print(f"The result of {numerator} ÷ {denominator} is: {result}")
    else:
        print(result)

if __name__ == "__main__":
    main()