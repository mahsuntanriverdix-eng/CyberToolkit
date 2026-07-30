from modules.password import generate_password


def show_menu():
    print("\n===================================")
    print("        CYBER TOOLKIT v0.2")
    print("===================================")
    print("1) Password Generator")
    print("2) Network Tools (Yakında)")
    print("3) Crypto Tools (Yakında)")
    print("4) File Tools (Yakında)")
    print("5) System Tools (Yakında)")
    print("0) Çıkış")
    print("===================================")


def main():
    while True:
        show_menu()

        choice = input("Seçiminiz: ").strip()

        if choice == "1":
            generate_password()

        elif choice == "2":
            print("\nBu modül henüz geliştirme aşamasında.")

        elif choice == "3":
            print("\nBu modül henüz geliştirme aşamasında.")

        elif choice == "4":
            print("\nBu modül henüz geliştirme aşamasında.")

        elif choice == "5":
            print("\nBu modül henüz geliştirme aşamasında.")

        elif choice == "0":
            print("\nCyberToolkit kapatılıyor...")
            break

        else:
            print("\nGeçersiz seçim!")


if __name__ == "__main__":
    main()