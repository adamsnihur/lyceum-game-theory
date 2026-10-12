# Part 3: Chapters 7, 8, 9 for Lyceum Game Theory
# Zero em-dashes strictly enforced.

def get_chapter_7():
    return """
      <!-- ROZDZIAŁ 7: WIEDZA I WSPÓLNA WIEDZA AUMANNA -->
      <section id="rozdzial-7" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Część III &bull; Rozdział 7</span>
          <span class="text-xs font-mono text-slate-400">Epistemic Game Theory &bull; Strony 253-288</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdział 7: Wiedza Indywidualna i Wspólna Wiedza Roberta Aumanna</h3>

        <!-- 7.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            7.1. Modele Kripkego i Aksjomaty Logiki Modalnej S5
          </h4>
          <p>
            W teorii epistemologicznej stan świata $\\omega \\in \\Omega$ reprezentuje pełny, wyczerpujący opis rzeczywistości.
            Każdy gracz $i \\in I$ posiada <strong>partycję informacyjną $\\mathcal{I}_i$</strong> zbioru $\\Omega$.
            Dla dowolnego stanu $\\omega$, komórka $\\mathcal{I}_i(\\omega) \\subseteq \\Omega$ to zbiór stanów, których gracz $i$ nie potrafi odróżnić od $\\omega$.
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 7.1 &bull; Operator Wiedzy Kripkego</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              Dla dowolnego zdarzenia $E \\subseteq \\Omega$, gracz $i$ <strong>wie, że $E$ zaszło</strong> w stanie $\\omega$, wtedy i tylko wtedy, gdy wszystkie stany uważane przez niego za możliwe należą do $E$:
              $$K_i(E) = \\{ \\omega \\in \\Omega : \\mathcal{I}_i(\\omega) \\subseteq E \\}$$
            </p>
          </div>
          <p>
            Ponieważ $\\mathcal{I}_i$ jest relacją równoważności (partycją), operator wiedzy $K_i$ spełnia pięć fundamentalnych własności <strong>systemu logiki modalnej S5</strong>:
          </p>
          <ul class="text-xs text-slate-600 space-y-1.5 list-disc list-inside">
            <li><strong>Aksjomat Prawdy (Truth Axiom / Aksjomat T):</strong> $K_i(E) \\subseteq E$ (nie można wiedzieć czegoś, co jest fałszem).</li>
            <li><strong>Aksjomat Spójności:</strong> $K_i(E) \\cap K_i(\\neg E) = \\emptyset$ (gracz nie może jednocześnie wiedzieć $E$ i wiedzieć $\\neg E$).</li>
            <li><strong>Pozytywna Introspekcja (Aksjomat 4):</strong> $K_i(E) \\subseteq K_i(K_i(E))$ (jeśli gracz wie $E$, to wie, że wie $E$).</li>
            <li><strong>Negatywna Introspekcja (Aksjomat 5):</strong> $\\neg K_i(E) \\subseteq K_i(\\neg K_i(E))$ (jeśli gracz nie wie $E$, to jest świadomy własnej niewiedzy!).</li>
            <li><strong>Monotoniczność:</strong> $E \\subseteq F \\implies K_i(E) \\subseteq K_i(F)$.</li>
          </ul>
        </div>

        <!-- 7.2 & 7.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            7.2 - 7.3. Wiedza Wzajemna a Wspólna Wiedza (Twierdzenie Aumanna)
          </h4>
          <p>
            Zdarzenie $E$ jest <strong>wiedzą wzajemną (Mutual Knowledge)</strong> pierwszego rzędu, gdy każdy z graczy wie, że $E$:
            $$K(E) = \\bigcap_{i=1}^n K_i(E)$$
            Wiedza wyższego rzędu to $K^2(E) = K(K(E))$ ("każdy wie, że każdy wie"), $K^3(E)$ itd.
            <strong>Wspólna wiedza (Common Knowledge)</strong> to nieskończony iloczyn:
          </p>
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 font-mono text-xs overflow-x-auto">
            $$CK(E) = \\bigcap_{m=1}^\\infty K^m(E)$$
          </div>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Twierdzenie 7.1 (Robert Aumann, 1976) &bull; Charakteryzacja Wspólnej Wiedzy</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              Niech $\\mathcal{M} = \\mathcal{I}_1 \\wedge \\mathcal{I}_2 \\wedge \\dots \\wedge \\mathcal{I}_n$ oznacza <strong>spojenie (Meet)</strong> partycji informacyjnych, czyli najdrobniejsze wspólne zgrubienie wszystkich partycji $\\mathcal{I}_i$.
              Wtedy dla dowolnego zdarzenia $E$ i stanu $\\omega$:
              $$\\omega \\in CK(E) \\iff \\mathcal{M}(\\omega) \\subseteq E$$
              Zdarzenie $E$ jest wspólną wiedzą w stanie $\\omega$ wtedy i tylko wtedy, gdy cała składowa spójności w grafie osiągalności zawiera się w $E$!
            </p>
          </div>
          <p>
            <strong>Zagadka Trzech Kapeluszy i Brudnych Dzieci:</strong>
            Trzech studentów siedzi w kole, każdy ma czerwony kapelusz. Każdy widzi dwa czerwone kapelusze u innych.
            Profesor pyta: <em>"Kto wie, jakiego koloru ma kapelusz?"</em>. Nikt się nie odzywa.
            Następnie profesor ogłasza publicznie: <em>"Co najmniej jeden kapelusz jest czerwony"</em>.
            Dlaczego to oświadczenie zmienia stan wiedzy, skoro każdy ze studentów już to widział na własne oczy?
            Przed oświadczeniem fakt ten był wiedzą wzajemną $K(E)$, lecz <strong>nie był wspólną wiedzą</strong>!
            Student 1 dopuszczał, że ma biały kapelusz; wtedy Student 2 widziałby 1 czerwony i dopuszczałby, że Student 3 widzi 2 białe kapelusze i uważa, że żadnego czerwonego nie ma!
            Publiczne ogłoszenie niszczy ten łańcuch kontrfaktyczny, tworząc $CKE$ i uruchamiając kaskadę eliminacji.
          </p>
        </div>

        <!-- ZADANIE 7.14 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyróżnione Zadanie 7.14 (Trzy Córki Pete'a i Koperty z Liczbami)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 7.E &bull; s. 277</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Treść Zadania:</strong> Pete wkłada do trzech kopert liczby całkowite dodatnie $x, y, z$ takie, że jedna jest sumą dwóch pozostałych (np. $z = x + y$).
            Każda z trzech córek widzi własną liczbę, lecz nie zna pozostałych.
            Pete pyta po kolei każdą córkę, czy wie, jakie są pozostałe liczby. Pierwsza mówi "Nie", druga mówi "Nie", a trzecia mówi "Tak, wiem!".
            Zadanie wymaga skonstruowania przestrzeni stanów Kripkego i pokazania, w jaki sposób sekwencja negatywnych deklaracji eliminuje komórki partycji, doprowadzając do natychmiastowej dedukcji.
          </p>
        </div>
      </section>
    """

def get_chapter_8():
    return """
      <!-- ROZDZIAŁ 8: DODAWANIE PRZEKONAŃ, BAYES I TEORIA AGM -->
      <section id="rozdzial-8" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Część III &bull; Rozdział 8</span>
          <span class="text-xs font-mono text-slate-400">Przekonania i Bayes &bull; Strony 289-331</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdział 8: Przekonania Probabilistyczne, Bayes i Teoria AGM</h3>

        <!-- 8.1 - 8.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            8.1 - 8.3. Rewizja Przekonań AGM i Porządki Wiarygodności (Plausibility Orders)
          </h4>
          <p>
            W modelach probabilistycznych każdemu stanowi $\\omega$ przypisujemy rozkład $P_i(\\cdot | \\omega)$.
            Gdy nadejdzie informacja $E \\subseteq \\Omega$ z $P(E) > 0$, nowa ocena wynika wprost z reguły Bayesa: $P(A|E) = \\frac{P(A \\cap E)}{P(E)}$.
            <strong>Kluczowy Problem Teoretyczny:</strong> Co zrobić, gdy nastąpi zdarzenie $E$, któremu decydent przypisywał wcześniej prawdopodobieństwo zerowe ($P(E) = 0$)?
            Dzielenie przez zero w formule Bayesa uniemożliwia aktualizację!
          </p>
          <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-blue-800 text-xs block uppercase">Twierdzenie 8.1 (Adam Grove 1988 / Giacomo Bonanno 2009) &bull; Racjonalizacja AGM</span>
            <p class="text-xs text-blue-950 leading-relaxed">
              Funkcja rewizji przekonań spełnia aksjomaty <strong>AGM (Alchourron, Gardenfors, Makinson, 1985)</strong> wtedy i tylko wtedy, gdy jest generowana przez
              <strong>porządek wiarygodności (Plausibility Preorder)</strong> $\\precsim$ na zbiorze stanów $\\Omega$ (kompletną i przechodnią relację z warunkiem, że stany uważane za możliwe są ściśle najbardziej wiarygodne).
              Po zaobserwowaniu dowolnego zdarzenia $E \\ne \\emptyset$ (nawet z $P(E) = 0$), agent uznaje za możliwe wyłącznie stany będące <strong>minimami relacji $\\precsim$ wewnątrz $E$</strong>!
            </p>
          </div>
        </div>

        <!-- 8.4 - 8.5 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            8.4 - 8.5. Twierdzenie Aumanna o Braku Zgody na Niezgodę (Agreeing to Disagree) i No-Trade Theorem
          </h4>
          <p>
            Założenie <strong>Wspólnego Rozkładu Początkowego (Common Prior Assumption / Harsanyi Consistency)</strong> zakłada, że gracze przed uzyskaniem prywatnych sygnałów posiadali identyczny obiektywny rozkład prawdopodobieństwa $P$ na $\\Omega$.
          </p>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Twierdzenie 8.1 (Agreement Theorem &bull; Robert Aumann, 1976)</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              Niech dwóch graczy dzieli ten sam rozkład początkowy $P$ ($P(\\omega) > 0 \\; \\forall \\omega$).
              Jeśli w pewnym stanie $\\omega^*$ jest <strong>wspólną wiedzą</strong>, że Gracz 1 przypisuje zdarzeniu $E$ prawdopodobieństwo a posteriori $p = P(E | \\mathcal{I}_1(\\omega^*))$,
              a Gracz 2 przypisuje zdarzeniu $E$ prawdopodobieństwo $q = P(E | \\mathcal{I}_2(\\omega^*))$, to:
              $$p = q$$
              Dwaj racjonalni decydenci posiadający wspólne przekonania początkowe <strong>nie mogą zgodzić się na niezgodę</strong>!
            </p>
            <details class="text-xs bg-white p-3 rounded-lg border border-emerald-100 cursor-pointer">
              <summary class="font-bold text-emerald-700 select-none">Rozwiń Ścisły Dowód Twierdzenia Aumanna (Appendix 8.A Bonanno)</summary>
              <div class="mt-2 text-slate-700 space-y-2 leading-relaxed">
                <p>
                  Niech $M = \\mathcal{M}(\\omega^*)$ będzie komórką spojenia (Meet) zawierającą stan $\\omega^*$.
                  Z Twierdzenia 7.1 o wspólnej wiedzy, fakt, że $P(E | \\mathcal{I}_1) = p$ jest wspólną wiedzą w $\\omega^*$ oznacza, że dla <em>każdego</em> stanu $\\omega \\in M$ zachodzi $P(E | \\mathcal{I}_1(\\omega)) = p$.
                </p>
                <p>
                  Komórka $M$ jest sumą rozłącznych komórek partycji Gracza 1: $M = \\bigcup_{k=1}^r I_{1,k}$.
                  Dla każdej komórki $I_{1,k}$ mamy z definicji prawdopodobieństwa warunkowego:
                  $$\\frac{P(E \\cap I_{1,k})}{P(I_{1,k})} = p \\implies P(E \\cap I_{1,k}) = p \\cdot P(I_{1,k})$$
                  Sumując po wszystkich $k$:
                  $$P(E \\cap M) = \\sum_{k=1}^r P(E \\cap I_{1,k}) = p \\sum_{k=1}^r P(I_{1,k}) = p \\cdot P(M)$$
                  Wobec tego $p = \\frac{P(E \\cap M)}{P(M)}$.
                </p>
                <p>
                  Postępując identycznie dla Gracza 2 (ponieważ $M$ jest także sumą rozłącznych komórek partycji Gracza 2):
                  $$P(E \\cap M) = q \\cdot P(M) \\implies q = \\frac{P(E \\cap M)}{P(M)}$$
                  Z porównania obu równości wynika bezpośrednio: $p = q$. $\\blacksquare$
                </p>
              </div>
            </details>
          </div>
          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-1 text-xs">
            <strong class="text-blue-700 block font-mono">Twierdzenie o Braku Handlu (No-Trade Theorem &bull; Milgrom & Stokey 1982):</strong>
            Jeśli alokacja początkowa jest efektywna w sensie Pareto, gracze mają wspólny rozkład a priori i handlują czysto spekulacyjnie w oparciu o informacje prywatne, to fakt chęci zawarcia transakcji staje się wspólną wiedzą, zdradzając informacje rywalowi.
            W rezultacie <strong>żadna spekulacyjna transakcja nie dochodzi do skutku</strong>! Czysta spekulacja w racjonalnym rynku finansowym jest niemożliwa bez podmiotów handlujących z przyczyn płynnościowych (noise traders).
          </div>
        </div>

        <!-- ZADANIE 8.12 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyróżnione Zadanie 8.12 (Dwóch Lekarzy Diagnozujących Pacjenta z Common Prior)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 8.E &bull; s. 320</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Treść Zadania:</strong> Dwóch lekarzy bada pacjenta. Początkowo obaj oceniają ryzyko rzadkiej choroby $C$ na $10\\%$.
            Lekarz A wykonuje test krwi, a Lekarz B tomografię. Otrzymują prywatne wyniki.
            Zadanie dowodzi, że jeśli lekarze zaczną ogłaszać swoje bieżące subiektywne prawdopodobieństwa, to po kilku rundach ich oceny muszą zbiec się do dokładnie tej samej wartości, co stanowi empiryczną ilustrację twierdzenia o braku zgody na niezgodę!
          </p>
        </div>
      </section>
    """

def get_chapter_9():
    return """
      <!-- ROZDZIAŁ 9: WSPÓLNA WIEDZA O RACJONALNOŚCI -->
      <section id="rozdzial-9" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Część III &bull; Rozdział 9</span>
          <span class="text-xs font-mono text-slate-400">CKR & Epistemic Foundations &bull; Strony 332-352</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdział 9: Wspólna Wiedza o Racjonalności (CKR)</h3>

        <!-- 9.1 - 9.2 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            9.1 - 9.2. Epistemiczne Modele Gier i Twierdzenie Brandenburgera-Dekela / Tan-Werlanga
          </h4>
          <p>
            W epistemicznym modelu gry strategicznej (Definicja 9.1), każdy stan $\\omega \\in \\Omega$ określa nie tylko wybór strategii każdego gracza $s_i(\\omega)$, lecz także partycję informacyjną i przekonania probabilistyczne.
            Gracz $i$ jest <strong>racjonalny w stanie $\\omega$ (Definicja 9.2)</strong>, gdy jego wybór $s_i(\\omega)$ maksymalizuje oczekiwaną użyteczność względem jego przekonań w stanie $\\omega$.
            Niech $R_i \\subseteq \\Omega$ oznacza zdarzenie "Gracz $i$ jest racjonalny", a $R = \\bigcap R_i$ oznacza "Wszyscy są racjonalni".
          </p>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Twierdzenie 9.1 & 9.2 (Brandenburger & Dekel 1987 / Tan & Werlang 1988)</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              1. Jeśli w stanie $\\omega^*$ zachodzi <strong>Wspólna Wiedza o Racjonalności</strong> ($\\omega^* \\in CK(R)$), to zagrany w tym stanie profil strategii $s(\\omega^*)$ musi <strong>przetrwać procedurę IDSDS</strong> (iterowaną eliminację strategii ściśle zdominowanych)!<br>
              2. Odwrotnie: każdy profil strategii, który przetrwa IDSDS, może być zrealizowany w pewnym modelu epistemicznym w stanie, w którym zachodzi $CK(R)$.
            </p>
          </div>
          <p class="text-xs text-slate-600">
            Wniosek metodologiczny: Wspólna wiedza o racjonalności <em>nie implikuje</em> równowagi Nasha! Uzasadnia ona wyłącznie zbiory strategii racjonalizowalnych. Do uzyskania równowagi Nasha konieczne jest dodatkowo założenie o wspólnym rozkładzie pierwotnym lub prawidłowych oczekiwaniach.
          </p>
        </div>

        <!-- 9.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            9.3. CKR w Grach Ekstensywnych i Debata Aumann vs Stalnaker
          </h4>
          <p>
            W słynnej publikacji z 1995 roku Robert Aumann udowodnił, że w grach o doskonałej informacji ze ściśle unikalnymi wypłatami, <strong>CKR implikuje rozwiązanie indukcji wstecznej</strong>.
            Twierdzenie to wywołało jednak głęboką debatę filozoficzną (Stalnaker 1998, Ben-Porath 1997):
          </p>
          <div class="p-3 sm:p-4 bg-amber-50/70 border border-amber-200 rounded-xl text-xs text-amber-950 leading-relaxed">
            <strong>Krytyka Roberta Stalnakera (1998):</strong>
            Co ma pomyśleć Gracz 2, gdy znajdzie się w węźle, do którego racjonalny Gracz 1 nigdy nie powinien był dojść?
            Jeśli Gracz 1 właśnie popełnił rażący błąd, to w co Gracz 2 powinien wierzyć na temat racjonalności Gracza 1 w kolejnych krokach?
            Klasyczny dowód Aumanna zakłada "początkową" wspólną wiedzę, która nie musi przetrwać po zaobserwowaniu nieracjonalnego ruchu rywala.
          </div>
        </div>
      </section>
    """
