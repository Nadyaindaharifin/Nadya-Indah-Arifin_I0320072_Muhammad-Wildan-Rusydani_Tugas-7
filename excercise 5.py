def panggil(func):
    return func
def helloworld():
    return "Hello World"
def main():
    daftarnama = ["Adi, Cahyo, budi, Dedi"]
    print("Keadaan awal")
    print(daftarnama)

    print("\n Menggunakan sorted(): ")
    print(sorted(daftarnama))

    daftarnama.sort(key=lambda n: n.lower())

    print("\nKeadaan akhir: ")
    print(print(daftarnama))
if __name__ == '__main__':
    main()
