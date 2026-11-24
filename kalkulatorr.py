
import math

print("===== KALKULATOR LENGKAP =====")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")
print("5. Modulus (%)")
print("6. Pangkat (**)")
print("7. Akar Kuadrat (sqrt)")
print("8. Sinus (sin)")
print("9. Cosinus (cos)")
print("10. Tangen (tan)")
print("11. Persentase (persen)")
print("12. Logaritma (log)")
print("13. Konstanta Pi (pi)")

opr = input("Pilih operator: ")

if opr == "sqrt":
    bil1 = float(input("Masukkan bilangan: "))

    if bil1 >= 0:
        print("Hasil akar =", math.sqrt(bil1))
    else:
        print("Error: Bilangan tidak boleh negatif")

elif opr == "sin":
    bil1 = float(input("Masukkan sudut: "))
    print("Sin", bil1, "=", math.sin(math.radians(bil1)))

elif opr == "cos":
    bil1 = float(input("Masukkan sudut: "))
    print("Cos", bil1, "=", math.cos(math.radians(bil1)))

elif opr == "tan":
    bil1 = float(input("Masukkan sudut: "))
    sudut = math.radians(bil1)

    if math.isclose(math.cos(sudut), 0, abs_tol=1e-12):
        print("Error: Tangen tidak terdefinisi")
    else:
        print("Tan", bil1, "=", math.tan(sudut))

elif opr == "log":
    bil1 = float(input("Masukkan bilangan: "))

    if bil1 > 0:
        print("Log", bil1, "=", math.log10(bil1))
    else:
        print("Error: Bilangan harus positif")

elif opr == "ln":
    bil1 = float(input("Masukkan bilangan: "))

    if bil1 > 0:
        print("Ln", bil1, "=", math.log(bil1))
    else:
        print("Error: Bilangan harus positif")




elif opr == "pi":
    print("Nilai Pi =", math.pi)

else:
    bil1 = float(input("Bilangan 1 = "))
    bil2 = float(input("Bilangan 2 = "))

    if opr == "+":
        print(bil1, "+", bil2, "=", bil1 + bil2)

    elif opr == "-":
        print(bil1, "-", bil2, "=", bil1 - bil2)

    elif opr == "*":
        print(bil1, "x", bil2, "=", bil1 * bil2)

    elif opr == "/":
        if bil2 != 0:
            print(bil1, ":", bil2, "=", bil1 / bil2)
        else:
            print("Error: Tidak bisa dibagi nol")

    elif opr == "%":
        if bil2 != 0:
            print(bil1, "%", bil2, "=", bil1 % bil2)
        else:
            print("Error: Tidak bisa dibagi nol")

    elif opr == "**":
        print(bil1, "pangkat", bil2, "=", bil1 ** bil2)

    elif opr == "persen":
        print(bil1, "% dari", bil2, "=", bil1 * bil2 / 100)

    else:
        print("Error: Operator tidak tersedia")
