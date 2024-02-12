def count_letters(input_string):
    # Mengubah string menjadi lowercase untuk konsistensi
    input_string = input_string.lower()
    letter_count = {}

    # Menghitung kemunculan setiap huruf
    for char in input_string:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    # Membuat string output
    output = ""
    for char, count in sorted(letter_count.items()):
        output += f"{char}={count}, "

    # Menghapus koma dan spasi ekstra di akhir
    output = output[:-2]
    
    return output

# Contoh penggunaan
input_str_1 = "We Always Mekar"
input_str_2 = "coding is fun"

print("Output 1:", count_letters(input_str_1))
print("Output 2:", count_letters(input_str_2))

def sort_letters(input_list):
    # Menggabungkan semua kata menjadi satu string
    input_string = "".join(input_list).lower()
    letter_count = {}

    # Menghitung kemunculan setiap huruf
    for char in input_string:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    # Mengurutkan huruf berdasarkan jumlah kemunculan (terbanyak ke terendah)
    sorted_letters = sorted(letter_count.items(), key=lambda x: (-x[1], x[0]))

    # Membuat string output
    output = ""
    for char, _ in sorted_letters:
        output += char

    return output

# Contoh penggunaan
input_list_1 = ["Abc", "bCd"]
input_list_2 = ["Oke", "One"]
input_list_3 = ["Pendanaan", "Terproteksi", "Untuk", "Dampak", "Berarti"]

print("Output 1:", sort_letters(input_list_1))
print("Output 2:", sort_letters(input_list_2))
print("Output 3:", sort_letters(input_list_3))