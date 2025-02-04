# START
# 1. Funkcja wyswietl_menu():
#     - Wyświetla listę dostępnych operacji.

# 2. Funkcja pobierz_wybor():
#     - Pobiera od użytkownika numer operacji.
#     - Sprawdza, czy liczba jest w zakresie 1-5.
#     - Jeśli nie, wyświetla błąd i ponownie prosi o wpisanie liczby.

# 3. Funkcja pobierz_liczbe(tekst):
#     - Pobiera od użytkownika liczbę.
#     - Jeśli użytkownik wpisze coś niepoprawnego, prosi o ponowne wprowadzenie.

# 4. Funkcje dodaj(a, b), odejmij(a, b), pomnoz(a, b), podziel(a, b):
#     - Przyjmują dwie liczby i zwracają wynik odpowiedniej operacji.
#     - W przypadku dzielenia sprawdzają, czy `b != 0`.

# 5. Funkcja kalkulator():
#     - Wywołuje wyswietl_menu().
#     - Powtarza w pętli:
#         - Pobiera wybór użytkownika.
#         - Jeśli wybór to 5, kończy działanie.
#         - Pobiera dwie liczby.
#         - Wywołuje odpowiednią funkcję (dodaj, odejmij, itd.).
#         - Wyświetla wynik.
#         - Powtarza proces, dopóki użytkownik nie wybierze wyjścia.

# 6. Uruchomienie kalkulator():
#     - `kalkulator()` wykonuje wszystkie operacje w pętli.
# END


def menu():
    print("Wybierz liczbe ktora odpowiada dzialaniu: ")
    print("1 - Dodawanie")
    print("2 - Odejmowanie")
    print("3 - Mnozenie")
    print("4 - Dzielenie")
    print("5 - Wyjscie")

def get_choice_from_user():
    while True:
        try:
            choice = float(input("Wybierz operacje: "))
        except ValueError:
            print("To nie jest liczba, podaj liczbe jeszcze raz ")
            continue            

        if choice == 5:
            return choice
        elif choice not in range(1,5):
            print("Wybierz liczbe z zakresu ")
            continue
        else:
            return choice
            
def get_numbers_from_user():
    try:
        x = float(input("Podaj pierwsza liczbe: "))
        y = float(input("Podaj druga liczbe: "))
    except ValueError:
        print("Podaj liczbe, nie tekst")
    return x, y

def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    if y == 0:
        print("Nie dziel przez zero ")
    else:
        return x/y

operations = {
    1: addition,
    2: subtraction,
    3: multiplication,
    4: division
}

def calculate():
    menu()
    while True:
        choice = get_choice_from_user()
        if choice == 5:
            break
        else:
            x, y = get_numbers_from_user()
            result = operations[choice](x,y)
            print(result)
            continue

if __name__ == "__main__":
    calculate()