# SZCZEGÓŁOWY SZKIC KURSU E-LEARNINGOWEGO: TEORIA GIER
## Na podstawie podręcznika akademickiego: *Game Theory: An open access textbook with 165 solved exercises* autorstwa Giacomo Bonanno (University of California, Davis)

---

### CZĘŚĆ WPROWADZAJĄCA

#### Rozdział 0: Geneza, Zakres i Filozofia Teorii Gier
- **0.1. Rys historyczny i pionierzy dyscypliny**
  - Prace Ernsta Zermelo (1913) - analiza szachów i determinizm skończonych gier dwuosobowych
  - John von Neumann (1928) - twierdzenie o minimaksie
  - Przełomowa monografia: John von Neumann & Oskar Morgenstern (*Theory of Games and Economic Behavior*, 1944)
  - Przełom Johna Nasha (1950-1951) - pojęcie równowagi dla gier niekooperacyjnych
  - Wkład Lloyda Shapleya (1953) - wartość Shapleya i gry stochastyczne
  - Nagrody Nobla z ekonomii dla teoretyków gier: 1994 (Nash, Harsanyi, Selten), 2005 (Aumann, Schelling), 2007 (Hurwicz, Maskin, Myerson), 2012 (Roth, Shapley)
  - Zastosowania praktyczne: aukcja pasma radiowego FCC (1994, 7 mld USD), organizacja rynków, teoria przetargów, biologia ewolucyjna (John Maynard Smith), medycyna (dynamika komórek nowotworowych)
- **0.2. Podstawowe pojęcia i aparat pojęciowy**
  - Definicja sytuacji interaktywnej: gracze podejmujący decyzje wzajemnie wpływające na ich rezultaty
  - Paradygmat *Homo rationalis* (Robert Aumann, 1985): istota celowa, logiczna, o ściśle określonych celach i nieograniczonej zdolności kalkulacyjnej
  - Granice racjonalności: ludzie w ekonomii behawioralnej (Colin Camerer), agenci programistyczni w informatyce (Shoham & Leyton-Brown), organizmy biologiczne w teorii ewolucyjnej
- **0.3. Dwa główne nurty teorii gier**
  - Teoria gier kooperacyjnych: komunikacja, koalicje, wiążące umowy (binding agreements)
  - Teoria gier niekooperacyjnych (przedmiot niniejszego kompendium): brak komunikacji lub brak możliwości egzekwowania prawnie wiążących umów (np. prawo antymonopolowe)
- **0.4. Architektura programu kształcenia**
  - Część I: Gry o wypłatach porządkowych (Rozdziały 1-3)
  - Część II: Gry o wypłatach kardynalnych (Rozdziały 4-6)
  - Część III: Zaawansowane zagadnienia I - Wiedza, wspólna wiedza i przekonania (Rozdziały 7-9)
  - Część IV: Zaawansowane zagadnienia II - Uszczegółowienia równowagi doskonałej w podgrach (Rozdziały 10-12)
  - Część V: Zaawansowane zagadnienia III - Gry o niepełnej informacji (Rozdziały 13-15)

---

### CZĘŚĆ I: GRY O WYPŁATACH PORZĄDKOWYCH (ORDINAL PAYOFFS)

#### Rozdział 1: Gry Porządkowe w Postaci Strategicznej (Normalnej)
- **1.1. Ramki gry a gry (Game frames and games)**
  - Definicja ramki gry w postaci strategicznej: czwórka $\langle I, (S_1, \dots, S_n), O, f \rangle$
    - Zbiór graczy $I = \{1, 2, \dots, n\}$, $n \ge 2$
    - Profile strategii: $S = S_1 \times S_2 \times \dots \times S_n$, wektory $s = (s_1, \dots, s_n)$
    - Zbiór rezultatów $O$
    - Funkcja wynikowa $f: S \to O$
  - Różnica między rezultatem a wypłatą: przypadek teleturnieju *Golden Balls* (Split or Steal)
  - Preferencje egoistyczne i chciwe vs preferencje altruistyczne, prospołeczne i oparte na sprawiedliwości (Fairness / Frans de Waal)
  - Relacje preferencji porządkowych: $\succ_i$ (ścisła preferencja), $\sim_i$ (obojętność), $\succsim_i$ (słaba preferencja - "co najmniej tak dobry jak")
  - Aksjomaty preferencji porządkowych: zupełność (completeness) i przechodniość (transitivity)
  - Porządkowa funkcja użyteczności $U_i: O \to \mathbb{R}$
  - Zredukowana postać gry: trójka $\langle I, (S_1, \dots, S_n), (\pi_1, \dots, \pi_n) \rangle$, gdzie $\pi_i(s) = U_i(f(s))$
- **1.2. Dominacja ścisła i słaba (Strict and weak dominance)**
  - Notacja podprofilu strategii pozostałych graczy: $s_{-i} \in S_{-i}$
  - Definicja ścisłej dominacji: $a$ ściśle dominuje $b$, gdy $\pi_i(a, s_{-i}) > \pi_i(b, s_{-i})$ dla każdego $s_{-i}$
  - Definicja słabej dominacji: $a$ słabo dominuje $b$, gdy $\pi_i(a, s_{-i}) \ge \pi_i(b, s_{-i})$ dla wszystkich $s_{-i}$ oraz $\pi_i(a, \bar{s}_{-i}) > \pi_i(b, \bar{s}_{-i})$ dla co najmniej jednego $\bar{s}_{-i}$
  - Strategia równoważna: $\pi_i(a, s_{-i}) = \pi_i(b, s_{-i})$ dla wszystkich $s_{-i}$
  - Strategia ściśle dominująca vs słabo dominująca
  - Równowaga w strategiach dominujących (ścisła vs słaba)
  - Dylemat Więźnia (Prisoner's Dilemma) i konflikt racjonalności indywidualnej z racjonalnością kolektywną
  - Dominacja w sensie Pareto: rezultaty ściśle i słabo Pareto-lepsze
- **1.3. Aukcja drugiej ceny Vickreya (Second-Price Sealed-Bid Auction)**
  - Mechanizm aukcji: najwyższa oferta wygrywa, płaci drugą w kolejności najwyższą cenę
  - Reguły rozstrzygania remisów (tie-breaking rules)
  - Formalny model ramki gry dla $n$ oferentów
  - **Twierdzenie 1.1 (William Vickrey, 1961):** Przy preferencjach egoistycznych i chciwych, licytowanie własnej prawdziwej wyceny ($b_i = v_i$) jest strategią słabo dominującą
  - Dowód twierdzenia Vickreya: analiza przypadków $b_j \le v_i$ oraz $b_j > v_i$
  - Warunki załamania twierdzenia: motywacje złośliwe (spiteful) i altruistyczne
- **1.4. Mechanizm pivotowy Clarke'a (The Pivotal / Clarke Mechanism)**
  - Problem finansowania dóbr publicznych i zafałszowywania deklaracji podatkowych
  - Efektywność społeczna: realizacja projektu wtedy i tylko wtedy, gdy $\sum_{i=1}^n v_i > C$
  - Definicja gracza decydującego (pivotal player)
  - Reguła podatku Clarke'a: $t_i = |\sum_{j \ne i} w_j - \sum_{j \ne i} c_j|$
  - **Twierdzenie 1.2 (Edward Clarke, 1971):** W mechanizmie pivotowym prawdziwe ujawnienie wyceny ($w_i = v_i$) jest strategią słabo dominującą dla każdego uczestnika
  - Dowód analityczny twierdzenia Clarke'a (4 przypadki relacji sum wycen do kosztów)
- **1.5. Procedury eliminacji iteracyjnej (Iterated deletion procedures)**
  - 1.5.1. IDSDS (Iterated Deletion of Strictly Dominated Strategies):
    - Definicja rekurencyjna: $G^0 = G$, $G^{k+1}$ powstaje przez wycięcie strategii ściśle zdominowanych w $G^k$
    - Równowaga po iteracyjnej eliminacji strategii ściśle zdominowanych
    - Niezależność wyniku IDSDS od kolejności eliminacji w grach skończonych (Remark 1.5)
    - Epistemiczne uzasadnienie: wspólna wiedza o racjonalności
  - 1.5.2. IDWDS (Iterated Deletion of Weakly Dominated Strategies):
    - Zależność wyniku od kolejności eliminacji
    - Ścisła definicja synchroniczna: jednoczesne usunięcie wszystkich strategii słabo zdominowanych w danym kroku
    - Problemy z interpretacją ostrożnościową (caution vs deletion)
- **1.6. Równowaga Nasha (Nash Equilibrium)**
  - Definicja formalna dla 2 graczy i $n$ graczy
  - Cztery równoważne interpretacje:
    1. Brak żalu (*No regret*)
    2. Samoegzekwująca się umowa (*Self-enforcing agreement*)
    3. Wykonalna rekomendacja arbitra (*Viable recommendation*)
    4. Przejrzystość rozumowania (*Transparency of reason*)
  - Funkcja najlepszej odpowiedzi (Best reply / response)
  - Algorytm podkreślania komórek w tabeli (underlining method) dla 2 i 3 graczy
  - Problem istnienia równowag w grach porządkowych: gra w dopasowywanie monet (Matching Pennies)
- **1.7. Gry z nieskończonym zbiorem strategii (Infinite strategy sets)**
  - Ciągłe zbiory strategii: przykład gry liczbowej na przedziale $[1, \infty)$
  - Paradoks równowagi opartej na strategiach słabo zdominowanych
  - Klasyczny model konkurencji oligopolistycznej Augustin Cournota (1838):
    - Funkcja popytu $P(Q) = a - b(q_1 + q_2)$
    - Funkcje zysku i warunki pierwszego rzędu (FOC)
    - Wyprowadzenie analityczne równowagi Cournota: $q_1^* = q_2^* = \frac{a-c}{3b}$

#### Rozdział 2: Dynamiczne Gry o Doskonałej Informacji
- **2.1. Drzewa decyzyjne, ramki i gry (Trees, frames and games)**
  - Ukorzenione drzewa skierowane: węzeł początkowy (root), węzły decyzyjne $D$, węzły terminalne $Z$
  - Jednoznaczność ścieżki od korzenia do węzła
  - Przypisanie graczy do węzłów $\iota: D \to I$ i akcji do krawędzi $A$
  - Przykład rozwiązania spółki partnerskiej (Amy i Beth)
- **2.2. Indukcja wsteczna (Backward Induction)**
  - Algorytm indukcji wstecznej: oznaczanie węzłów przedostatnich (penultimate nodes) i propagacja wsteczna wektora wypłat
  - Niejednoznaczność rozwiązań przy remisach w wypłatach
- **2.3. Pojęcie strategii w grach o doskonałej informacji**
  - Definicja 2.4: Strategia jako kompletny, kontyngentny plan działania obejmujący decyzję w każdym węźle gracza
  - Problem nadmiarowości (redundancy) w definicji strategii i jej epistemiczne uzasadnienie (błędy wykonawcze, instrukcja dla pełnomocnika, przekonania rywala)
  - Transformacja gry z postaci ekstensywnej do postaci strategicznej
- **2.4. Relacja indukcji wstecznej do równowagi Nasha**
  - **Twierdzenie 2.1:** Każde rozwiązanie indukcji wstecznej jest równowagą Nasha powiązanej postaci strategicznej
  - Równowagi Nasha niebędące rozwiązaniami indukcji wstecznej i problem niewiarygodnych gróźb (incredible threats)
  - Gra w odstraszanie wejścia na rynek (Market Entry Game)
  - Gra w sieć sklepów Reinharda Seltena (Selten's Chain Store Paradox): indukcja wsteczna vs budowanie reputacji w horyzoncie skończonym
- **2.5. Gry dwuosobowe o doskonałej informacji**
  - Gry typu wygrana-przegrana (win-lose games): wyścigi liczbowe (Race to 100 / gra z odejmowaniem)
  - Koncepcja pozycji przegrywających (losing positions) i wsteczna identyfikacja strategii wygrywającej
  - **Twierdzenie 2.2:** W każdej skończonej dwuosobowej grze o doskonałej informacji typu wygrana-przegrana jeden z graczy posiada strategię wygrywającą
  - Gry z trzema wynikami (Wygrana 1, Wygrana 2, Remis): **Twierdzenie 2.3 (Uogólnienie twierdzenia Zermelo, 1913)**
  - Zastosowanie do kółka i krzyżyk (Tic-Tac-Toe), warcabów (Draughts) i szachów (Chess)

#### Rozdział 3: Ogólne Gry Dynamiczne i Informacja Niedoskonała
- **3.1. Zbiory informacyjne i niedoskonała informacja**
  - Motywacja: ściąganie na egzaminie z dwoma kolorami kartek
  - Definicja zbioru informacyjnego: partycja zbioru węzłów decyzyjnych danego gracza
  - Definicja 3.1: Postać ekstensywna z doskonałą pamięcią (Perfect Recall):
    - Równość zbiorów akcji we wszystkich węzłach danego zbioru informacyjnego
    - Zakaz relacji poprzednik-następnik wewnątrz tego samego zbioru informacyjnego
    - Formalny warunek pamiętania własnych przeszłych wyborów i informacji
  - Przykłady naruszenia doskonałej pamięci
- **3.2. Strategie w grach z niedoskonałą informacją**
  - Strategia jako funkcja przypisująca wybór każdemu zbiorowi informacyjnemu
  - Budowa macierzy wypłat postaci strategicznej
- **3.3. Podgry (Subgames)**
  - Definicja 3.3: Podgra właściwa (Proper subgame)
    - Początek w węźle pojedynczym (singleton) różnym od korzenia
    - Zakaz rozcinania zbiorów informacyjnych
  - Definicja 3.4: Podgra minimalna (Minimal proper subgame)
- **3.4. Równowaga doskonała w podgrach (Subgame-Perfect Equilibrium - SPE)**
  - Definicja 3.5: Profil strategii tworzący równowagę Nasha w całej grze i w każdej jej właściwej podgrze
  - Definicja 3.6: Algorytm rozwiązywania gier przez zwijanie podgier minimalnych
  - Koincydencja SPE z indukcją wsteczną w grach o doskonałej informacji
- **3.5. Gry z ruchami losowymi (Chance / Nature moves)**
  - Fikcyjny gracz Natura, rozkłady prawdopodobieństwa na gałęziach
  - Loterie monetarne i wartość oczekiwana
  - Założenie neutralności wobec ryzyka
  - Gry w blefowanie kartami i gra z wymianą kopert

---

### CZĘŚĆ II: GRY O WYPŁATACH KARDYNALNYCH (CARDINAL PAYOFFS)

#### Rozdział 4: Teoria Oczekiwanej Użyteczności (Expected Utility Theory)
- **4.1. Loterie pieniężne i postawy wobec ryzyka**
  - Definicja skończonej loterii pieniężnej: $L = \begin{pmatrix} \$x_1 & \dots & \$x_n \\ p_1 & \dots & p_n \end{pmatrix}$
  - Wartość oczekiwana $\mathbb{E}[L]$
  - Klasyfikacja postaw wobec ryzyka względem zdegenerowanej loterii wypłacającej $\mathbb{E}[L]$:
    - Awersja do ryzyka (Risk aversion): preferencja pewnej kwoty ponad loterię
    - Neutralność wobec ryzyka (Risk neutrality): obojętność
    - Zamiłowanie do ryzyka (Risk loving): preferencja loterii ponad pewną kwotę
  - Zasada *De gustibus non est disputandum* w teorii racjonalności
- **4.2. Twierdzenia o reprezentacji oczekiwanej użyteczności**
  - **Twierdzenie 4.1 (John von Neumann & Oskar Morgenstern, 1944):** Istnienie funkcji użyteczności $U: O \to \mathbb{R}$ takiej, że $L \succ L' \iff \mathbb{E}[U(L)] > \mathbb{E}[U(L')]$
  - **Twierdzenie 4.2:** Jednoznaczność funkcji użyteczności vNM z dokładnością do dodatniej transformacji afinicznej ($V(o) = a U(o) + b$, $a > 0$)
  - Funkcja użyteczności znormalizowana: $U(o_{\text{worst}}) = 0$, $U(o_{\text{best}}) = 1$
  - Procedura kalibracji funkcji użyteczności metodą pytań o prawdopodobieństwo obojętności
- **4.3. Aksjomaty teorii oczekiwanej użyteczności i paradoksy behawioralne**
  - Aksjomat 1: Zupełność i przechodniość (Completeness & Transitivity)
  - Aksjomat 2: Monotoniczność (Monotonicity)
  - Aksjomat 3: Ciągłość (Continuity)
  - Aksjomat 4: Niezależność / Zastępowalność (Independence / Substitutability)
  - Loterie złożone (compound lotteries) i redukcja do loterii prostych
  - Kompletny dowód twierdzenia von Neumanna-Morgensterna
  - Odchylenia behawioralne od teorii oczekiwanej użyteczności:
    - Paradoks Maurice'a Allais (1953) - naruszenie aksjomatu niezależności
    - Paradoks Daniela Ellsberga (1961) - awersja do niejednoznaczności (Ambiguity Aversion)

#### Rozdział 5: Strategie Mieszane w Grach w Postaci Strategicznej
- **5.1. Gry w postaci strategicznej o wypłatach kardynalnych**
  - Definicje 5.1 i 5.2: Ramki z loteriami i funkcje wypłat von Neumanna-Morgensterna
- **5.2. Strategie mieszane**
  - Definicja 5.3: Strategia mieszana jako rozkład prawdopodobieństwa $\sigma_i \in \Delta(S_i)$
  - Interpretacja randomizacyjna vs interpretacja epistemiczna (przekonania rywali)
  - Wypłata oczekiwana profilu strategii mieszanych $\Pi_i(\sigma)$
  - **Twierdzenie 5.1 (John Nash, 1951):** Każda skończona gra w postaci strategicznej o wypłatach kardynalnych posiada co najmniej jedną równowagę Nasha w strategiach mieszanych
- **5.3. Metody obliczania równowag w strategiach mieszanych**
  - Eliminacja strategii ściśle zdominowanych jako krok wstępny
  - **Twierdzenie 5.2 (Zasada obojętności / Indifference Principle):** Jeśli $\sigma^*$ jest równowagą w strategiach mieszanych, to gracz $i$ osiąga identyczną oczekiwaną wypłatę ze wszystkich czystych strategii w nośniku $\text{supp}(\sigma_i^*)$
  - Cel randomizacji: uczynienie rywala obojętnym, a nie maksymalizacja własnej wypłaty wprost
  - Metoda analityczna rozwiązywania układów równań obojętności dla gier $2 \times 2$
  - Graficzna analiza obwiedni najlepszych odpowiedzi (Best reply envelopes) dla gier $2 \times 3$
- **5.4. Ścisła dominacja przez strategie mieszane i racjonalizowalność**
  - Przypadek czystej strategii zdominowanej przez mieszaninę innych strategii (mimo braku dominacji przez jakąkolwiek pojedynczą strategię czystą)
  - **Twierdzenie 5.3 (David Pearce, 1984 / Douglas Bernheim):** W grach 2-osobowych czysta strategia nie jest najlepszą odpowiedzią na żadną strategię rywala wtedy i tylko wtedy, gdy jest ściśle zdominowana przez pewną strategię mieszaną
  - Definicja 5.6: Kardynalna procedura IDSDS i pojęcie strategii racjonalizowalnych
  - Rozróżnienie gier 2-osobowych i gier $n$-osobowych ($n \ge 3$): korelacja przekonań rywali a niezależność produktowa rozkładów

#### Rozdział 6: Dynamiczne Gry o Wypłatach Kardynalnych
- **6.1. Strategie behawioralne w grach dynamicznych**
  - Strategia mieszana (rozkład nad globalnymi planami) vs strategia behawioralna (niezależne rozkłady w każdym zbiorze informacyjnym)
  - Liczba parametrów opisujących strategię mieszaną vs behawioralną
  - **Twierdzenie 6.1 (Harold W. Kuhn, 1953):** W grach ekstensywnych z doskonałą pamięcią (perfect recall) strategie mieszane i strategie behawioralne generują identyczne rozkłady prawdopodobieństwa na węzłach terminalnych (są równoważne)
  - Załamanie twierdzenia Kuhna przy braku doskonałej pamięci
- **6.2. Ponowna analiza równowagi doskonałej w podgrach**
  - **Twierdzenie 6.2:** Każda skończona gra ekstensywna o kardynalnych wypłatach posiada co najmniej jedno SPE
  - Algorytm rozwiązywania podgier z wykorzystaniem równowag mieszanych
- **6.3. Wady i ograniczenia pojęcia równowagi doskonałej w podgrach**
  - Niewydolność SPE w eliminacji nieracjonalnych zachowań w nieosiąganych zbiorach informacyjnych
  - Przykłady gier bez podgier właściwych, gdzie SPE dopuszcza ściśle zdominowane wybory poza ścieżką gry

---

### CZĘŚĆ III: ZAAWANSOWANE ZAGADNIENIA I - WIEDZA, WSPÓLNA WIEDZA I PRZEKONANIA

#### Rozdział 7: Wiedza i Wspólna Wiedza (Knowledge and Common Knowledge)
- **7.1. Modelowanie wiedzy indywidualnej**
  - Przestrzeń stanów świata $W$ (stany jako kompletne opisy rzeczywistości)
  - Zdarzenia jako podzbiory $E \subseteq W$
  - Partycja informacyjna $\mathcal{I}$ i komórki $\mathcal{I}(w)$
  - Definicja wiedzy: w stanie $w$ agent wie, że zaszło $E \iff \mathcal{I}(w) \subseteq E$
  - Operator wiedzy $K: 2^W \to 2^W$, gdzie $KE = \{w \in W : \mathcal{I}(w) \subseteq E\}$
  - Aksjomatyka logiki modalnej wiedzy (system S5):
    - Aksjomat Prawdy (Truth / Axiom T): $KE \subseteq E$ (można wiedzieć tylko to, co prawdziwe)
    - Spójność (Consistency / Axiom D): $KE \cap K(\neg E) = \emptyset$
    - Pozytywna Introspekcja (Positive Introspection / Axiom 4): $KE \subseteq KKE$
    - Negatywna Introspekcja (Negative Introspection / Axiom 5): $\neg KE \subseteq K(\neg KE)$
    - Monotoniczność (Monotonicity): $E \subseteq F \implies KE \subseteq KF$
    - Koniunkcja (Conjunction): $K(E \cap F) = KE \cap KF$
- **7.2. Wiedza interaktywna wielu agentów**
  - Modele Kripkego dla $n$ agentów: partycje $\mathcal{I}_1, \dots, \mathcal{I}_n$ i operatory $K_1, \dots, K_n$
  - Wiedza wyższych rzędów: $K_i K_j E$ ("$i$ wie, że $j$ wie, że $E$")
  - Zagadka trzech kapeluszy (Three Hats Puzzle / Muddy Children):
    - Formalna analiza eliminacji stanów krok po kroku
    - Dlaczego publiczne ogłoszenie faktu, o którym każdy już wie prywatnie, drastycznie zmienia stan wiedzy interaktywnej
- **7.3. Wspólna wiedza (Common Knowledge)**
  - Definicja formalna wspólnej wiedzy: nieskończony iloczyn operatorów wiedzy $CKE = \bigcap_{m=1}^\infty K^m E$
  - Relacja osiągalności w grafie stanów (1-krokowa, 2-krokowa, $m$-krokowa)
  - Definicja 7.5: Partycja wspólnej wiedzy $\mathcal{I}_{CK}$ jako najdrobniejsze wspólne zgrubienie (finest common coarsening)
  - **Twierdzenie 7.1 (Robert Aumann, 1976):** Zdarzenie $E$ jest wspólną wiedzą w stanie $w$ wtedy i tylko wtedy, gdy $\mathcal{I}_{CK}(w) \subseteq E$
  - Zastosowanie: gra koordynacyjna Abby, Bruno i Caroline - dlaczego brak wspólnej wiedzy uniemożliwia koordynację

#### Rozdział 8: Dodawanie Przekonań do Wiedzy (Adding Beliefs to Knowledge)
- **8.1. Przekonania probabilistyczne**
  - Rozkłady prawdopodobieństwa na komórkach partycji informacyjnej
  - Różnica między wiedzą a pewnością (Certainty vs Knowledge):
    - Pewność: $P(E) = 1$
    - Możliwość bycia w błędzie: $P(E) = 1$ przy stanie rzeczywistym $w \notin E$
- **8.2. Prawdopodobieństwo warunkowe i aktualizacja Bayesa**
  - Definicja $P(w|E) = \frac{P(w)}{P(E)}$ dla $P(E) > 0$
  - Reguła Bayesa dla hipotez i obserwacji
  - Zastosowania diagnostyczne (bóle pleców a zapalenie nerek)
- **8.3. Rewizja przekonań i teoria AGM (Belief Revision)**
  - Problem aktualizacji w obliczu informacji zaskakującej ($P(E) = 0$)
  - Aksjomatyka teorii AGM (Carlos Alchourrón, Peter Gärdenfors, David Makinson, 1985)
  - Aksjomat Kennetha Arrowa dla rewizji przekonań
  - Porządek wiarygodności $\precsim$ (total preorder na stanach)
  - **Twierdzenie 8.1 (Adam Grove 1988, Giacomo Bonanno 2009):** Funkcja rewizji przekonań spełnia aksjomaty AGM wtedy i tylko wtedy, gdy jest racjonalizowana przez porządek wiarygodności
  - Probabilistyczna wersja AGM i rozkłady $P_E$
- **8.4. Spójność przekonań Harsanyiego (Like-mindedness & Common Prior)**
  - Czy dwaj racjonalni agenci mogą mieć różne przekonania? Rola asymetrii informacyjnej
  - Definicja 8.10: Założenie wspólnego rozkładu a priori (Common Prior Assumption - CPA)
  - Sprawdzanie istnienia wspólnego rozkładu a priori za pomocą układów równań liniowych
- **8.5. Twierdzenie Aumanna o uzgadnianiu przekonań (Agreeing to Disagree)**
  - **Twierdzenie 8.1 (Agreement Theorem; Robert Aumann, 1976):** Dwaj racjonalni agenci o wspólnych przekonaniach pierwotnych nie mogą mieć wspólnej wiedzy o tym, że różnią się w oszacowaniu prawdopodobieństwa zdarzenia ($p = q$)
  - Dowód lematu o partycjach i twierdzenia Aumanna
  - Dynamiczny proces wymiany opinii między badaczami i zbieżność do wspólnej wiedzy

#### Rozdział 9: Wspólna Wiedza o Racjonalności (Common Knowledge of Rationality - CKR)
- **9.1. Modele epistemiczne gier w postaci strategicznej**
  - Program epistemicznych podstaw teorii gier
  - Definicja 9.1: Model epistemiczny gry $G$: stany, partycje, rozkłady przekonań oraz odwzorowanie $\sigma_i: W \to S_i$
  - Definicja 9.2: Racjonalność gracza w stanie $w$: wybór maksymalizujący oczekiwaną wypłatę względem subiektywnych przekonań
  - Zdarzenie racjonalności $R_i$ oraz zdarzenie powszechnej racjonalności $R = \bigcap R_i$
- **9.2. Wspólna wiedza o racjonalności w grach strategicznych**
  - Zdarzenie $CKR$ (Common Knowledge of Rationality)
  - **Twierdzenie 9.1:** W każdym modelu gry $G$, jeśli w stanie $w$ zachodzi $w \in CKR$, to wektor strategii $\sigma(w)$ przetrwa procedurę IDSDS
  - **Twierdzenie 9.2:** Każdy profil strategii przetrwający procedurę IDSDS może być zrealizowany w pewnym modelu w stanie, w którym zachodzi $CKR$
  - Fundamentalny wniosek: $CKR$ nie implikuje równowagi Nasha! Równowaga Nasha wymaga dodatkowo zgodności przekonań
- **9.3. Wspólna wiedza o racjonalności w grach ekstensywnych**
  - Paradoksy modelowania zachowań w węzłach kontrfaktycznych
  - Krytyka przypisywania strategii do stanów w grach dynamicznych
  - Modele doksastyczno-behawioralne i uszczegółowienia pojęciowe

---

### CZĘŚĆ IV: ZAAWANSOWANE ZAGADNIENIA II - USZCZEGÓŁOWIENIA RÓWNOWAGI DOSKONAŁEJ W PODGRACH

#### Rozdział 10: Pierwsza Próba: Słaba Równowaga Sekwencyjna (Weak Sequential Equilibrium)
- **10.1. Oceny i racjonalność sekwencyjna**
  - Definicja 10.1: Ocena $(\sigma, \mu)$ złożona z profilu strategii behawioralnych $\sigma$ oraz systemu przekonań $\mu$ na węzłach zbiorów informacyjnych
  - Oczekiwana wypłata warunkowa $\pi_i(H | \sigma, \mu)$
  - Definicja 10.2: Racjonalność sekwencyjna (brak opłacalności jednostronnych odchyleń we wszystkich zbiorach informacyjnych)
- **10.2. Aktualizacja Bayesa w osiąganych zbiorach informacyjnych**
  - Definicja 10.3: Zbiór informacyjny osiągany z dodatnim prawdopodobieństwem
  - Definicja 10.4: Wymóg zgodności przekonań $\mu(x) = \frac{\mathbb{P}_{root,\sigma}(x)}{\mathbb{P}_{root,\sigma}(H)}$
  - Dowolność przekonań w zbiorach informacyjnych o zerowym prawdopodobieństwie
- **10.3. Słaba równowaga sekwencyjna (Weak Sequential Equilibrium - WSE)**
  - Definicja 10.5: Ocena spełniająca racjonalność sekwencyjną i regułę Bayesa w osiąganych zbiorach informacyjnych
  - **Twierdzenie 10.1:** Każda słaba równowaga sekwencyjna indukuje równowagę Nasha
  - Porażka WSE jako uszczegółowienia SPE: WSE może nie być SPE w nieosiąganych podgrach!
  - Relacje zawierania: diagram Venna dla równowag Nasha, SPE i WSE

#### Rozdział 11: Równowaga Sekwencyjna Krepsa-Wilsona (Sequential Equilibrium)
- **11.1. Oceny spójne (Consistent Assessments)**
  - Kryterium Davida Krepsa i Roberta Wilsona (1982)
  - Definicja 11.1: Spójność KW jako granica ciągu strategii całkowicie mieszanych $\sigma_n \to \sigma$ i indukowanych przekonań $\mu_n \to \mu$
  - Rygor analityczny dowodzenia spójności i metody dowodzenia niespójności
- **11.2. Definicja i własności równowagi sekwencyjnej**
  - Definicja 11.2: Ocena będąca spójną w sensie KW i sekwencyjnie racjonalną
  - **Twierdzenie 11.1 (Kreps & Wilson, 1982):** Każda równowaga sekwencyjna jest równowagą doskonałą w podgrach (SPE)!
  - **Twierdzenie 11.2:** Każda skończona gra w postaci ekstensywnej posiada co najmniej jedną równowagę sekwencyjną
  - Hierarchia uszczegółowień: Równowaga Sekwencyjna $\subset (SPE \cap WSE) \subset Nash$
- **11.3. Ograniczenia i krytyka spójności Krepsa-Wilsona**
  - Zarzuty Krepsa, Wilsona, Osborne'a i Rubinsteina: nieintuicyjny, czysto techniczny charakter granic zaburzeń
  - Problem strategii słabo zdominowanych: dlaczego równowaga sekwencyjna dopuszcza słabo zdominowane wybory (konieczność wprowadzenia równowagi doskonałej drżącej ręki Seltena, Trembling-Hand Perfection 1975)

#### Rozdział 12: Doskonała Równowaga Bayesowska i Zamknięcie Luki (Perfect Bayesian Equilibrium)
- **12.1. Rewizja przekonań i spójność AGM na historiach gry**
  - Podejście oparte na historiach (History-based extensive forms, Appendix 12.A)
  - Definicja 12.1: Porządek wiarygodności $\precsim$ na zbiorze historii $H$ (warunki PL1, PL2, PL3)
  - Definicja 12.2: Spójność AGM oceny $(\sigma, \mu)$
- **12.2. Spójność bayesowska (Bayesian Consistency)**
  - Zasada "aktualizacji bayesowskiej tak długo, jak to możliwe"
  - Definicja 12.3: Spójność bayesowska oceny względem porządku wiarygodności (warunki B1, B2, B3)
- **12.3. Doskonała równowaga bayesowska (PBE)**
  - Definicja 12.4: Ocena sekwencyjnie racjonalna, spójna w sensie AGM i spójna bayesowsko
  - **Twierdzenie 12.1 (Giacomo Bonanno, 2013):** Każde PBE jest SPE i WSE
  - **Twierdzenie 12.2:** Każda równowaga sekwencyjna jest PBE, lecz nie każde PBE jest równowagą sekwencyjną!
- **12.4. Dodanie warunków niezależności (Independent PBE)**
  - Zjawisko odwracania przekonań (belief reversal) po ruchach niezależnych graczy
  - Aksjomaty niezależności: $IND_1$, $IND_2$, $IND_3$
  - Definicja 12.5: Niezależne PBE (Independent Perfect Bayesian Equilibrium)
  - **Twierdzenie 12.4:** Równowaga sekwencyjna $\subset$ Niezależne PBE $\subset$ PBE
- **12.5. Zamknięcie luki między PBE a równowagą sekwencyjną Krepsa-Wilsona**
  - Definicja 12.7: Mierzalność wyborów (Choice Measurability - CM) porządku wiarygodności
  - Definicja 12.8: Jednorodna spójność bayesowska (Uniformly Bayesian consistency)
  - **Twierdzenie 12.5 (Giacomo Bonanno, 2015):** Ocena $(\sigma, \mu)$ jest Równowagą Sekwencyjną Krepsa-Wilsona wtedy i tylko wtedy, gdy jest Doskonałą Równowagą Bayesowską racjonalizowaną przez mierzalny porządek wiarygodności i jednorodnie bayesowską!
  - Całkowite wyeliminowanie granic ciągów i topologii na rzecz czystej algebry przekonań

---

### CZĘŚĆ V: ZAAWANSOWANE ZAGADNIENIA III - INFORMACJA NIEPEŁNA (INCOMPLETE INFORMATION)

#### Rozdział 13: Informacja Niepełna w Grach Statycznych
- **13.1. Pojęcie informacji niepełnej a transformacja Harsanyiego**
  - Różnica między informacją niepełną (brak wiedzy o regułach/wypłatach) a niedoskonałą (brak wiedzy o przeszłych ruchach)
  - Metoda Johna Harsanyiego (1967-1968): redukcja gry o niepełnej informacji do gry ekstensywnej o niedoskonałej informacji z ruchem Natury
  - Definicja Bayesowskiej Równowagi Nasha (Bayesian Nash Equilibrium - BNE)
- **13.2. Informacja niepełna jednostronna (One-sided incomplete information)**
  - Model epistemiczny: stany rzeczywiste i kontrfaktyczne
  - Pojęcie typu gracza
  - Równowaga zlewająca (Pooling equilibrium) vs równowaga rozdzielająca (Separating equilibrium)
  - Ciągły model duopolu Cournota z niepewnością co do kosztu krańcowego rywala
- **13.3. Informacja niepełna obustronna (Two-sided incomplete information)**
  - Asymetria informacyjna po obu stronach interakcji
  - Kluczowa rola istnienia wspólnego rozkładu a priori (Common Prior) w transformacji Harsanyiego
  - Skutki braku wspólnego rozkładu a priori
- **13.4. Informacja niepełna wielostronna (Multi-sided incomplete information)**
  - Gry z 3 i więcej graczami o wielopoziomowej asymetrii informacyjnej

#### Rozdział 14: Informacja Niepełna w Grach Dynamicznych
- **14.1. Gry dynamiczne z jednostronną informacją niepełną**
  - Konieczność uszczegółowień dynamicznych (BNE może zawierać niewiarygodne groźby)
  - Zastosowanie 1: Rozwiązanie Paradoksu Sieci Sklepów Seltena (Chain Store Paradox):
    - Wprowadzenie typu irracjonalnego/furiata (hotheaded monopolist)
    - Wyprowadzenie równowagi, w której racjonalny monopolista walczy z pierwszym wejściem, aby zbudować reputację i odstraszyć drugiego pretendenta!
  - Zastosowanie 2: Negocjacje pracodawca-związki zawodowe i koszty strajków:
    - Informacja asymetryczna o zyskach przedsiębiorstwa
    - Strajk jako kosztowny mechanizm sygnalizacyjny (costly signaling) w równowadze rozdzielającej
  - Zastosowanie 3: Uczciwa reklama i prawo o ujawnianiu informacji (Milgrom & Roberts, 1986):
    - Sceptycyzm nabywcy i mechanizm *unraveling* wymuszający pełne ujawnienie jakości
- **14.2. Gry dynamiczne z wielostronną informacją niepełną**
  - Model przetargu dwustronnego (Bilateral bargaining) o prywatnych wycenach
  - Oferty, kontroferty i efekt urazy kupującego ($\varepsilon$)
  - Analiza dla $n=2$ oraz uogólnienie na $n=100$

#### Rozdział 15: Podejście Oparte na Przestrzeni Typów (The Type-Space Approach)
- **15.1. Typy graczy a struktury Kripkego**
  - Porównanie metody Harsanyiego z semantyką światów możliwych Saula Kripkego
- **15.2. Typy znające własne wypłaty**
  - Definicja 15.1: Statyczna gra bayesowska o niepełnej informacji z prywatną znajomością wypłat
  - Algorytm konwersji ze struktury stanów (state-space) do przestrzeni typów (type-space)
  - Algorytm konwersji z przestrzeni typów do struktury stanów
- **15.3. Przypadek ogólny: wartości współzależne (Interdependent values)**
  - Definicja 15.2: Użyteczność zależna od profilu typów wszystkich graczy $U_i(t, s)$
  - Dowód równoważności obu reprezentacji i unifikacja teorii gier o niepełnej informacji

---

### CZĘŚĆ VI: LABORATORIUM INTERAKTYWNE & TESTY WIEDZY

#### Moduł 16: Interaktywne Symulatory Poznawcze (Interactive Labs 60 FPS)
- **Laboratorium 1: Solver Macierzy Wypłat $2 \times 2$ i $3 \times 3$:**
  - Dynamiczna edycja macierzy w czasie rzeczywistym
  - Automatyczne wyznaczanie najlepszych odpowiedzi (podkreślanie)
  - Wykrywanie dominacji ścisłej i słabej
  - Kalkulator równowag w strategiach czystych i mieszanych (pary prawdopodobieństw $p, q$)
- **Laboratorium 2: Eksplorator Drzew Decyzyjnych & Indukcja Wsteczna:**
  - Interaktywna wizualizacja drzewa decyzyjnego
  - Krokowa propagacja indukcji wstecznej z eliminacją niewiarygodnych gróźb
- **Laboratorium 3: Symulator Bayesa & Paradoks Monty Halla:**
  - Dynamiczna wizualizacja 3 drzwi z podglądem prawdopodobieństw a priori i a posteriori
  - Eksperyment Monte Carlo demonstrujący wyższość strategii zmiany drzwi ($2/3$ vs $1/3$)
- **Laboratorium 4: Graf Wiedzy Aumanna & Zgoda na Niezgodę:**
  - Wizualizacja przestrzeni stanów, partycji informacyjnych i grafu osiągalności
  - Wyznaczanie partycji wspólnej wiedzy $\mathcal{I}_{CK}$ i weryfikacja Twierdzenia o Zgodzie

#### Moduł 17: Diagnostyczny Quiz Dydaktyczny (6 Zadań Rygoru Bonanno)
- 6 pytań diagnostycznych obejmujących kluczowe pułapki teoretyczne:
  1. Aukcja Vickreya i motywacje pozapieniężne
  2. Wspólna wiedza a wiedza powszechna pierwszego rzędu (zagadka kapeluszy)
  3. Twierdzenie o braku zgody na niezgodę Aumanna
  4. Równowaga w strategiach mieszanych a obojętność gracza
  5. Słaba równowaga sekwencyjna a uszczegółowienie SPE
  6. Charakteryzacja Bonanno (2015) dla równowagi sekwencyjnej Krepsa-Wilsona
- Natychmiastowa weryfikacja, dynamiczny KaTeX, wyjaśnienia dydaktyczne i licznik punktów na żywo.

#### Moduł 18: Praktyczna Implementacja Algorytmów w Pythonie
- Kompletny, minimalistyczny skrypt `game_theory_core.py` z implementacją:
  - Znajdowania równowag w strategiach czystych i mieszanych w grach $2 \times 2$
  - Algorytmu wstecznej indukcji w drzewie ekstensywnym
  - Aktualizacji bayesowskiej i filtru spójności
- Przycisk kopiowania do schowka

#### Moduł 19: Kanoniczna Bibliografia Naukowa & Odnośniki DOI
- Kompletny wykaz publikacji źródłowych (Nash, von Neumann & Morgenstern, Selten, Harsanyi, Aumann, Kreps & Wilson, Bonanno, Vickrey, Clarke, Pearce, Milgrom & Roberts) z bezpośrednimi linkami DOI.
