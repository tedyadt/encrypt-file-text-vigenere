def shift_cipher(text, shift):
    result = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for char in text:
        if alph.count(char) == 1:
            result += alph[(alph.index(char) + shift) % 26]
        elif alph.count(char.lower()) == 1:
            result += alph[(alph.index(char.lower()) + shift) % 26].upper()
        else:
            result += char
    return result

def shift_decipher(text, shift):
    result = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for char in text:
        if alph.count(char) == 1:
            result += alph[(alph.index(char) - shift) % 26]
        elif alph.count(char.lower()) == 1:
            result += alph[(alph.index(char.lower()) - shift) % 26].upper()
        else:
            result += char
    return result

def new_alph(ch):
    ch = ch.lower()
    alph = 'abcdefghijklmnopqrstuvwxyz'
    new_alph = alph[alph.index(ch):] + alph[:alph.index(ch)]
    return new_alph

def encrypt(text, big_key, shift):
    vigenere_result = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'

    for i, char in enumerate(text):
        if alph.count(char) == 1:
            key_char = big_key[i % len(big_key)].lower()
            new = new_alph(key_char)
            vigenere_result += new[alph.index(char)]
        elif alph.count(char.lower()) == 1:
            key_char = big_key[i % len(big_key)].lower()
            new = new_alph(key_char)
            vigenere_result += new[alph.index(char.lower())].upper()
        else:
            vigenere_result += char

    shifted_cipher = shift_cipher(vigenere_result, shift)

    # Menyimpan hasil enkripsi ke dalam file
    with open('encrypted_text.txt', 'w', encoding='utf-8') as file:
        file.write(shifted_cipher)

    return vigenere_result, shifted_cipher

def decrypt(text, big_key, shift):
    vigenere_cipher = shift_decipher(text, shift)
    result = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for i, char in enumerate(vigenere_cipher):
        if alph.count(char) == 1:
            key_char = big_key[i % len(big_key)].lower()
            new = new_alph(key_char)
            result += alph[new.index(char)]
        elif alph.count(char.lower()) == 1:
            key_char = big_key[i % len(big_key)].lower()
            new = new_alph(key_char)
            result += alph[new.index(char.lower())].upper()
        else:
            result += char

    return result

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return None
        
#enkrip dan dekrip dari file
def read_encrypted_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            encrypted_text = file.read()
        return encrypted_text
    except FileNotFoundError:
        print("File enkripsi tidak ditemukan.")
        return None

def decrypt_from_file(file_path, big_key, shift):
    encrypted_text = read_encrypted_text_from_file(file_path)

    if encrypted_text:
        decrypted_result = decrypt(encrypted_text, big_key, shift)
        return decrypted_result
    else:
        return None

# Contoh penggunaan dengan switch case
file_path = 'plaintext.txt'
text = read_text_from_file(file_path)

if text:
    big_key = 'kayu'
    shift = int(input("Masukkan nilai shift: "))

    # Menampilkan menu
    print("Pilih operasi:")
    print("1. Enkripsi")
    print("2. Dekripsi dari file enkripsi")

    # Input pilihan pengguna
    option = int(input("Masukkan nomor operasi yang diinginkan (1/2): "))

    # Melakukan operasi sesuai pilihan pengguna
    if option == 1:  # Enkripsi
        vigenere_result, shifted_result = encrypt(text, big_key, shift)
        print("Vigenere Cipher:", vigenere_result)
        print("Shifted Cipher:", shifted_result)
        print("Hasil enkripsi disimpan dalam 'encrypted_text.txt'")
    elif option == 2:  # Dekripsi dari file enkripsi
        decrypted_result = decrypt_from_file(file_path, big_key, shift)
        if decrypted_result is not None:
            print("Hasil dekripsi:", decrypted_result)
        else:
            print("Gagal melakukan dekripsi. Pastikan file enkripsi ditemukan.")
    else:
        print("Opsi tidak valid")