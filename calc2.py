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
    print("""
          1 - Dodawanie
          2 - Odejmowanie
          3 - Mnozenie
          4 - Dzielenie
          5 - Wyjscie
          """)

def get_choice_from_user():
    while True:
        try:
            choice = int(input("Wybierz operacje: "))
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
    while True:
        try:
            x = float(input("Podaj pierwsza liczbe: "))
            y = float(input("Podaj druga liczbe: "))
            return x,y
        except ValueError:
            print("Podaj liczbe, nie tekst")

def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return ("Nie dziel przez zero") if y == 0 else x/y

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
            print("Do zobaczenia")
            break
        x, y = get_numbers_from_user()
        result = operations[choice](x,y)
        print(f"Wynik: {result}")

if __name__ == "__main__":
    calculate()