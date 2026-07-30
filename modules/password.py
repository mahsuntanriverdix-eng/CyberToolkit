import secrets
import string


def ask_yes_no(question):
    """Kullanıcıdan E/H cevabı alır."""
    while True:
        answer = input(question).strip().lower()

        if answer in ("e", "evet"):
            return True

        if answer in ("h", "hayır", "hayir"):
            return False

        print("Lütfen sadece E veya H giriniz.\n")


def password_strength(password):
    """Parola gücünü değerlendirir."""

    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Zayıf"

    elif score <= 4:
        return "Orta"

    elif score == 5:
        return "Güçlü"

    return "Çok Güçlü"


def generate_password():

    print("\n========== PASSWORD GENERATOR ==========\n")

    while True:
        try:
            length = int(input("Parola uzunluğu (min 8): "))

            if length < 8:
                print("Parola en az 8 karakter olmalıdır.\n")
                continue

            break

        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.\n")

    use_upper = ask_yes_no("Büyük harf kullanılsın mı? (E/H): ")
    use_lower = ask_yes_no("Küçük harf kullanılsın mı? (E/H): ")
    use_digits = ask_yes_no("Rakam kullanılsın mı? (E/H): ")
    use_symbols = ask_yes_no("Özel karakter kullanılsın mı? (E/H): ")

    if not any([use_upper, use_lower, use_digits, use_symbols]):
        print("\nEn az bir karakter grubu seçmelisiniz!")
        return

    pool = ""
    password = []

    if use_upper:
        pool += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))

    if use_lower:
        pool += string.ascii_lowercase
        password.append(secrets.choice(string.ascii_lowercase))

    if use_digits:
        pool += string.digits
        password.append(secrets.choice(string.digits))

    if use_symbols:
        pool += string.punctuation
        password.append(secrets.choice(string.punctuation))

    while len(password) < length:
        password.append(secrets.choice(pool))

    secrets.SystemRandom().shuffle(password)

    password = "".join(password)

    print("\n==============================")
    print("Oluşturulan Parola")
    print("==============================")
    print(password)
    print("------------------------------")
    print(f"Uzunluk : {len(password)}")
    print(f"Güç     : {password_strength(password)}")
    print("==============================")

    save = ask_yes_no("\nParola data/passwords.txt dosyasına kaydedilsin mi? (E/H): ")

    if save:
        try:
            import os

            os.makedirs("data", exist_ok=True)

            with open("data/passwords.txt", "a", encoding="utf-8") as file:
                file.write(password + "\n")

            print("Parola başarıyla kaydedildi.")

        except Exception as error:
            print(f"Hata: {error}")


if __name__ == "__main__":
    generate_password()