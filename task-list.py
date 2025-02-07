"""
START
1. Funkcja menu():
    - Wyświetl dostępne operacje:
        1. Dodaj zadanie
        2. Wyświetl listę zadań
        3. Usuń zadanie
        4. Wyjście

2. Funkcja dodaj_zadanie():
    - Pobierz treść zadania od użytkownika.
    - Otwórz plik w trybie dopisywania (`a`).
    - Zapisz zadanie do pliku.
    - Potwierdź dodanie zadania.

3. Funkcja wyswietl_zadania():
    - Sprawdź, czy plik istnieje.
    - Otwórz plik w trybie odczytu (`r`).
    - Jeśli plik jest pusty, wyświetl komunikat "Brak zadań".
    - W przeciwnym razie wyświetl wszystkie linie.

4. Funkcja usun_zadanie():
    - Otwórz plik w trybie odczytu (`r`).
    - Wczytaj wszystkie linie i wyświetl numerowane zadania.
    - Pobierz numer zadania do usunięcia.
    - Usuń wybrane zadanie z listy.
    - Nadpisz plik nową listą zadań (`w`).
    - Potwierdź usunięcie.

5. Funkcja todo_app():
    - Powtarzaj w pętli:
        - Wyświetl menu.
        - Pobierz wybór użytkownika.
        - Jeśli wybór to:
            - 1 → Wywołaj `dodaj_zadanie()`
            - 2 → Wywołaj `wyswietl_zadania()`
            - 3 → Wywołaj `usun_zadanie()`
            - 4 → Zakończ program.
        - W przeciwnym razie wyświetl komunikat "Nieprawidłowy wybór".
END

"""
import os

def menu():
    print("""
          1. Dodaj zadanie
          2. Wyswietl liste zadan
          3. Usun zadanie
          4. Wyjscie
          """)

def add_task():
    if not os.path.exists("task-list.txt"):
        tasks = []
    else:
        with open("task-list.txt" , "r") as f:
            tasks = f.readlines()

    new_task = input("Podaj nowe zadanie: ").strip()
    if new_task:
        task_number = len(tasks) + 1
        with open("task-list.txt", "a") as f:
            f.write(f"{task_number}. {new_task}\n")
        print("Dodano zadanie")
    else:
        print("Zadanie nie moze byc puste")


def show_task():
    try:
        with open("task-list.txt", "r") as f:
            print(f.read())
    except:
        print("Plik jest pusty")

def delete_task():
    show_task()

    with open("task-list.txt", "r") as f:
        tasks = f.readlines()
    if not tasks:
        print("Brak zadan do usuniecia")
        return
    
    try:
        choice = int(input("Prosze podac numer zadania do usuniecia: "))
    except ValueError:
        print("To nie jest liczba")

    if 1 <= choice <= len(tasks):
        del tasks[choice - 1]
    else:
        print("Podales zly numer zadania")        
        return
    
    with open("task-list.txt", "w") as f:
        f.writelines(tasks)
    
    print("Zadanie usuniete")

operations = {
    1: add_task,
    2: show_task,
    3: delete_task
}

def todo_app():
    while True:
        menu()
        try:
            choice = int(input("Prosze wybrac co chcesz zrobic: "))
        except ValueError:
            print("Podaj odpowiednia wartosc")
            continue
        if choice == 4:
            print("Do zobaczenia")
            break

        action = operations.get(choice)
        if action:
            action()
        else:
            print("Niepoprawny wybor")

if __name__ == "__main__":
    todo_app()
        
        
           
# 1. jak numerowac w for przed wstawieniem tekstu
# 2. read zmienic na readlines
# 3. przeczytac dokladniej jak dzialaja petle i kiedy je stosowac, petla w petli