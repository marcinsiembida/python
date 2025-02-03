# START
# 1. Wyświetl komunikat: "Witaj w kalkulatorze!"
# 2. Powtarzaj, dopóki użytkownik nie zakończy pracy:
#    2.1. Wyświetl listę operacji do wyboru:
#         a. "1 - Dodawanie"
#         b. "2 - Odejmowanie"
#         c. "3 - Mnożenie"
#         d. "4 - Dzielenie"
#         e. "5 - Wyjście"
#    2.2. Pobierz wybór użytkownika.
#    2.3. Jeśli wybór to "5", zakończ program.
#    2.4. Jeśli wybór jest inny niż oczekiwany, wyświetl błąd i wróć do początku pętli.
#    2.5. Pobierz pierwszą liczbę od użytkownika.
#    2.6. Pobierz drugą liczbę od użytkownika.
#    2.7. Na podstawie wyboru wykonaj odpowiednią operację:
#         a. Jeśli "1", dodaj liczby.
#         b. Jeśli "2", odejmij liczby.
#         c. Jeśli "3", pomnóż liczby.
#         d. Jeśli "4", sprawdź, czy druga liczba nie jest zerem:
#              - Jeśli zero, wyświetl błąd.
#              - W przeciwnym razie wykonaj dzielenie.
#    2.8. Wyświetl wynik.
# 3. Wyświetl komunikat: "Do widzenia!"
# END

print("Witaj w kalkulatorze!")

while True:
    print("1 - Dodawanie")
    print("2 - Odejmowanie")
    print("3 - Mnozenie")
    print("4 - Dzielenie")
    print("5 - Wyjscie")
    
    choice = int(input("Podaj liczbe: "))

    if choice == 5:
        break
    elif choice > 5:
        print("Wybrales zla liczbe, wybierz jeszcze raz")
        choice = 0
        continue
    else:
        user_input1 = int(input("Prosze podac pierwsza liczbe: "))
        user_input2 = int(input("Prosze podac druga liczbe: "))
        if choice == 1:
            print(user_input1 + user_input2)
            break
    print("Do widzenia")

        



