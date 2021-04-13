# Zadanie 01 - generator wiadomość

Zbliża się koniec roku. Wyobraź sobie, że jesteś nauczycielem, który musi wysłać wiadomość do każdego ze swoich uczniów, przypominając im o brakujących zadaniach i ocenie końcowej.

Niby możesz napisać maile ręcznie, ale w tym roku masz do ocenienia 8 klas po 30 uczniów. Trochę za dużo roboty, by pisać do każdego osobno.

W arkuszu kalkulacyjnym przechowujesz informacje o klasie. Każdy uczeń ma imię, nazwisko, liczbę brakujących zadań oraz aktualną ocenę. Na szczęście masz Pythona i plan, że umieścisz dane w wiadomości, którą masz przygotowaną (plik message.txt). Dla ułatwienia klasa będzie anglojęzyczna co pozwoli uniknąć problemów z polską odmianą imion.

Zaplanuj jak powinen działać skrypt? Etap koncepcyjny jest bardzo ważny. Dalej możesz działać z własnym kodem lub skorzystać z poniższych podpowiedzi.

### Etap 1:

Zbuduj mały testowy kod, który pomoże Ci zrozumieć flow zadania. 

Stwórz skrypt w którym:
- Pobrane zostaną testowe dane od użytkownika 3 razy. Raz dla listy imion i nazwisk, raz dla listy brakujących zadań, a raz dla listy ocen.
- Utworzony zostanie szablon wiadomości tekstowej.
- Za pomocą pętli zostanie wyświetlona wiadomość dla każdego ucznia z poprawnymi wartościami. Potencjalna ocena to po prostu obecna + 1 (w dalszej części kodu warto zaproponować inny algorytm proponowanej oceny np. w zależności od ilości dostarczonych zadań).
- Ustal wspólną datę zaliczenia dla wszystkich uczniów

Podpowiedź rozwiązania etapu 1 znajduje się w folderze hints.

### Etap 2:

Kod z etapu 1 pozwolił zarysować koncepcję, ale nie pomoże, jeśli mamy kilka klas. Dlatego utwórz dowolny arkusz kalkulacyjny z uczniami wg wzoru `[klasa],[imię],[nazwisko],[brakujące zadania],[ocena]` 
np. `3A, Adam, Kowalski, 3, 4`.

Zapisz go jako `students.csv`.


### Etap 3: 
Wewnątrz skryptu stwórz funkcję, która będzie pobierać dane z pliku .csv. Zwróć uwagę, że plik csv używa znaku podziału.

Funkcja ma:
- Prawidłowo odczytać plik 
- Obsłużyć błąd w razie braku pliku w folderze
- Stworzy dowolną strukturę na podstawie danych z pliku - 3 listy (po odczycie wiersza doda dane do odpowiedniej grupy danych `imiona_nazwiska =[] zadania =[] ocena=[]` ) albo słownik (każdy użytkownik ma unikalny klucz i wartości - `{ klasa_imie_nazwisko : [imie, nazwisko, zadania, ocena]}`).

Struktura będzie przechowywać informację o uczniach i pozwoli w łatwy sposób dostać się do interesującego nas elementu.

### Etap 4:
- Zamień wstawioną na sztywno wiadomość na funkcje odczytującą wiadomość z pliku message.txt. Tekst wiadomości możesz dowolnie zmodyfikować.
- Zastosuj wyrażenie `if __name__ == '__main__'` do odzielenia wykonywanego kodu od definicji funkcji.

#### Rozszerzenie:
- Jeśli w pliku znajdzie się niespodziewana wartość np. zamiast oceny trafi się wartość nieliczbowa - wyrażenie 'nieobecny' nasz kod w jakiś sposób poradzi sobie z błędem (wstawinie oceny 0 jest jak najbardziej ok)

- Zapoznaj się z możliwościami biblioteki csv zamiast traktować plik jak zwykły plik tekstowy ;) Czy pozwoli Ci to na łatwiejszą obsługę pliku?
