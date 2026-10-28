def celsius_to_fahrenheit(celsius):
    
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        print("\n=== Temperature Converter ===")
        print("1. Convert Celsius to Fahrenheit (Push 1)")
        print("2. Convert Fahrenheit to Celsius (Push 2)")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
            except ValueError:
                print("Invalid input.")
                
        elif choice == '2':
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
            except ValueError:
                print("Invalid input! ")
                
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
            
        else:
            print("Invalid choice! Please select an option between 1 and 3.")

if __name__ == "__main__":
    main()
