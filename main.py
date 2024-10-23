def convert_temperature(temp_value, temp_unit):
    if temp_unit.upper() == 'C':
        # Convert Celsius to Fahrenheit
        return temp_value * 9/5 + 32
    elif temp_unit.upper() == 'F':
        # Convert Fahrenheit to Celsius
        return (temp_value - 32) * 5/9
    else:
        raise ValueError("'C' or 'F'")

def main():
    while True:
        try:
            temp_value = float(input("input: "))
            temp_unit = input("use ('C' or'F'): ")
            result = convert_temperature(temp_value, temp_unit)
            print(f"output: {result:.2f} {'F' if temp_unit.upper() == 'C' else 'C'}")
            break  # Keluar dari loop jika konversi berhasil
        except ValueError as e:
            print(f"Terjadi kesalahan: {e}. Silakan coba lagi.")

if __name__ == "__main__":
    main()