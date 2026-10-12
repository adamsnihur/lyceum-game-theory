# Teoria Gier - Giacomo Bonanno | Interaktywny Traktat i E-Learning Lyceum

Kompleksowa platforma edukacyjna oraz traktat pojęciowy z teorii gier, stworzony na podstawie podręcznika akademickiego:
**Giacomo Bonanno**, *Game Theory: An open access textbook with 165 solved exercises* (University of California, Davis, 2015).

Live Deployment: [https://adamsnihur.github.io/lyceum-game-theory/](https://adamsnihur.github.io/lyceum-game-theory/)

---

## Zakres i Struktura Kursu

Platforma pokrywa pełen program akademicki (wszystkie 15 rozdziałów + rozdział wprowadzający 0):

### Część I: Gry o Wypłatach Porządkowych
- **Rozdział 0:** Geneza, Zakres i Paradygmat *Homo rationalis* (Zermelo, von Neumann, Nash, Selten, Harsanyi, Aumann)
- **Rozdział 1:** Gry Porządkowe w Postaci Strategicznej (Ramki gry, dominacja, aukcja Vickreya, mechanizm Clarke'a, IDSDS, IDWDS, równowaga Nasha, duopol Cournota)
- **Rozdział 2:** Dynamiczne Gry o Doskonałej Informacji (Drzewa decyzyjne, indukcja wsteczna, strategie kontyngentne, paradoks sieci sklepów Seltena, uogólnione twierdzenie Zermelo dla gier z remisem)
- **Rozdział 3:** Ogólne Gry Dynamiczne i Niedoskonała Informacja (Zbiory informacyjne, doskonała pamięć / Perfect Recall, podgry właściwe, równowaga doskonała w podgrach - SPE, ruchy losowe Natury)

### Część II: Gry o Wypłatach Kardynalnych
- **Rozdział 4:** Teoria Oczekiwanej Użyteczności von Neumanna-Morgensterna (Loterie monetarne, postawy wobec ryzyka, twierdzenia o reprezentacji vNM, aksjomaty, paradoksy Allais i Ellsberga)
- **Rozdział 5:** Strategie Mieszane w Grach w Postaci Strategicznej (Twierdzenie Nasha z 1951 r., zasada obojętności, dominacja przez strategie mieszane, twierdzenie Pearce'a z 1984 r., racjonalizowalność)
- **Rozdział 6:** Gry Dynamiczne o Wypłatach Kardynalnych (Strategie behawioralne vs mieszane, twierdzenie Kuhna z 1953 r., SPE o wypłatach kardynalnych, wady SPE)

### Część III: Zaawansowane Zagadnienia I - Wiedza, Wspólna Wiedza i Przekonania
- **Rozdział 7:** Wiedza i Wspólna Wiedza (Przestrzenie stanów, operator wiedzy K, aksjomatyka S5, wiedza interaktywna, łamigłówka 3 kapeluszy, wspólna wiedza CKE, twierdzenie Aumanna o grafie osiągalności)
- **Rozdział 8:** Dodawanie Przekonań do Wiedzy (Przekonania probabilistyczne, pewność vs wiedza, aktualizacja Bayesa, teoria rewizji przekonań AGM 1985, porządki wiarygodności, Harsanyi consistency, Twierdzenie Aumanna o Zgodzie / Agreement Theorem)
- **Rozdział 9:** Wspólna Wiedza o Racjonalności - CKR (Modele epistemiczne, Twierdzenia 9.1 i 9.2: CKR vs IDSDS, dlaczego CKR nie implikuje równowagi Nasha, trudności w grach ekstensywnych)

### Część IV: Zaawansowane Zagadnienia II - Uszczegółowienia Równowagi Doskonałej w Podgrach
- **Rozdział 10:** Słaba Równowaga Sekwencyjna - WSE (Oceny, racjonalność sekwencyjna, reguła Bayesa w osiąganych zbiorach informacyjnych, diagram relacji WSE i SPE)
- **Rozdział 11:** Równowaga Sekwencyjna Krepsa-Wilsona - 1982 (Spójność KW jako granica zaburzeń, twierdzenia o uszczegółowieniu SPE, krytyka technicznej natury granic)
- **Rozdział 12:** Doskonała Równowaga Bayesowska - PBE (Podejście oparte na historiach, porządki wiarygodności, spójność AGM, Twierdzenie Bonanno z 2015 r. unifikujące PBE i Równowagę Sekwencyjną bez nieskończonych granic!)

### Część V: Zaawansowane Zagadnienia III - Informacja Niepełna
- **Rozdział 13:** Informacja Niepełna w Grach Statycznych (Transformacja Harsanyiego, Bayesowska Równowaga Nasha - BNE, pooling vs separating, duopol Cournota)
- **Rozdział 14:** Informacja Niepełna w Grach Dynamicznych (Rozwiązanie Paradoksu Sieci Sklepów Seltena przez typ furiata i budowanie reputacji, strajki jako kosztowna sygnalizacja, prawo o uczciwej reklamie Milgroma-Robertsa 1986)
- **Rozdział 15:** Podejście Oparte na Przestrzeni Typów (Przestrzenie typów Harsanyiego vs stany Kripkego, dwukierunkowy algorytm konwersji, wartości współzależne)

---

## 4 Interaktywne Symulatory (Moduł 16)
1. **Solver Macierzy Wypłat $2 \times 2$ i $3 \times 3$**: Wyznaczanie najlepszych odpowiedzi, równowag czystych i mieszanych, dominacji.
2. **Eksplorator Drzewa Ekstensywnego**: Indukcja wsteczna, parametry sprawiedliwości i koszty procesu sądowego.
3. **Silnik Monte Carlo Bayesa**: Symulacja paradoksu Monty Halla z aktualizacją przekonań a posteriori.
4. **Graf Wspólnej Wiedzy Aumanna**: Wyznaczanie partycji $\mathcal{I}_{CK}$ i weryfikacja Twierdzenia o Zgodzie.

---

## Uruchomienie Testów i Weryfikacja QA
```bash
./.venv312/bin/python verify_site.py
```
