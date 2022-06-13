#
# Example Python program structure

from square import square

def main():
    
    # Get user input
    value = int(input("Enter a number: "))
    
    # Run the program
    result = square(value)
    
    # Print the result
    print(f"The square of the number is: {result}")
                

if __name__ == "__main__":
    main()