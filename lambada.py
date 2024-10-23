import math

# function untuk luas lingkaran
def circle_area(radius):
    return math.pi * radius ** 2

# main function
def main():
    while True:
        user_input = input("Masukkan radius lingkaran (atau 'exit' untuk keluar): ")
        
        # cek pengguna
        if user_input.lower() == 'exit':
            print("Program dihentikan.")
            break
        
        try:
            # input + error handling
            radius = float(user_input)
            if radius < 0:
                print("Radius tidak boleh negatif. Silakan coba lagi.")
                continue
            
            # Hitung
            area = circle_area(radius)
            print(f"Luas lingkaran dengan radius {radius} adalah: {area:.2f}")
        
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

if __name__ == "__main__":
    main()