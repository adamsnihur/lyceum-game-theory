# Part 3: Chapters 7, 8, 9 for Lyceum Game Theory
# Zero em-dashes strictly enforced.

def get_chapter_7():
    return """
      <!-- ROZDZIAL 7: WIEDZA I WSPOLNA WIEDZA AUMANNA -->
      <section id="rozdzial-7" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Czesc III &bull; Rozdzial 7</span>
          <span class="text-xs font-mono text-slate-400">Epistemic Game Theory &bull; Strony 253-288</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdzial 7: Wiedza Indywidualna i Wspolna Wiedza Roberta Aumanna</h3>

        <!-- 7.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            7.1. Modele Kripkego i Aksjomaty Logiki Modalnej S5
          </h4>
          <p>
            W teorii epistemologicznej stan swiata $\\omega \\in \\Omega$ reprezentuje pelny, wyczerpujacy opis rzeczywistosci.
            Kazdy gracz $i \\in I$ posiada <strong>partycje informacyjna $\\mathcal{I}_i$</strong> zbioru $\\Omega$.
            Dla dowolnego stanu $\\omega$, komorka $\\mathcal{I}_i(\\omega) \\subseteq \\Omega$ to zbior stanow, ktorych gracz $i$ nie potrafi odroznic od $\\omega$.
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 7.1 &bull; Operator Wiedzy Kripkego</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              Dla dowolnego zdarzenia $E \\subseteq \\Omega$, gracz $i$ <strong>wie, ze $E$ zaszlo</strong> w stanie $\\omega$, wtedy i tylko wtedy, gdy wszystkie stany uwazane przez niego za mozliwe naleza do $E$:
              $$K_i(E) = \\{ \\omega \\in \\Omega : \\mathcal{I}_i(\\omega) \\subseteq E \\}$$
            </p>
          </div>
          <p>
            Poniewaz $\\mathcal{I}_i$ jest relacja rownowaznosci (partycja), operator wiedzy $K_i$ spelnia piec fundamentalnych wlasnosci <strong>systemu logiki modalnej S5</strong>:
          </p>
          <ul class="text-xs text-slate-600 space-y-1.5 list-disc list-inside">
            <li><strong>Aksjomat Prawdy (Truth Axiom / Aksjomat T):</strong> $K_i(E) \\subseteq E$ (nie mozna wiedziec czegos, co jest falszem).</li>
            <li><strong>Aksjomat Spojnosci:</strong> $K_i(E) \\cap K_i(\\neg E) = \\emptyset$ (gracz nie moze jednoczesnie wiedziec $E$ i wiedziec $\\neg E$).</li>
            <li><strong>Pozytywna Introspekcja (Aksjomat 4):</strong> $K_i(E) \\subseteq K_i(K_i(E))$ (jesli gracz wie $E$, to wie, ze wie $E$).</li>
            <li><strong>Negatywna Introspekcja (Aksjomat 5):</strong> $\\neg K_i(E) \\subseteq K_i(\\neg K_i(E))$ (jesli gracz nie wie $E$, to jest swiadomy wlasnej niewiedzy!).</li>
            <li><strong>Monotonicznosc:</strong> $E \\subseteq F \\implies K_i(E) \\subseteq K_i(F)$.</li>
          </ul>
        </div>

        <!-- 7.2 & 7.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            7.2 - 7.3. Wiedza Wzajemna a Wspolna Wiedza (Twierdzenie Aumanna)
          </h4>
          <p>
            Zdarzenie $E$ jest <strong>wiedza wzajemna (Mutual Knowledge)</strong> pierwszego rzedu, gdy kazdy z graczy wie, ze $E$:
            $$K(E) = \\bigcap_{i=1}^n K_i(E)$$
            Wiedza wyzszego rzedu to $K^2(E) = K(K(E))$ ("kazdy wie, ze kazdy wie"), $K^3(E)$ itd.
            <strong>Wspolna wiedza (Common Knowledge)</strong> to nieskonczony iloczyn:
          </p>
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 font-mono text-xs overflow-x-auto">
            $$CK(E) = \\bigcap_{m=1}^\\infty K^m(E)$$
          </div>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Twierdzenie 7.1 (Robert Aumann, 1976) &bull; Charakteryzacja Wspolnej Wiedzy</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              Niech $\\mathcal{M} = \\mathcal{I}_1 \\wedge \\mathcal{I}_2 \\wedge \\dots \\wedge \\mathcal{I}_n$ oznacza <strong>spojenie (Meet)</strong> partycji informacyjnych, czyli najdrobniejsze wspolne zgrubienie wszystkich partycji $\\mathcal{I}_i$.
              Wtedy dla dowolnego zdarzenia $E$ i stanu $\\omega$:
              $$\\omega \\in CK(E) \\iff \\mathcal{M}(\\omega) \\subseteq E$$
              Zdarzenie $E$ jest wspolna wiedza w stanie $\\omega$ wtedy i tylko wtedy, gdy cala skladowa spojnosci w grafie osiagalnosci zawiera sie w $E$!
            </p>
          </div>
          <p>
            <strong>Zagadka Trzech Kapeluszy i Brudnych Dzieci:</strong>
            Trzech studentow siedzi w kole, kazdy ma czerwony kapelusz. Kazdy widzi dwa czerwone kapelusze u innych.
            Profesor pyta: <em>"Kto wie, jakiego koloru ma kapelusz?"</em>. Nikt sie nie odzywa.
            Nastepnie profesor oglasza publicznie: <em>"Co najmniej jeden kapelusz jest czerwony"</em>.
            Dlaczego to oswiadczenie zmienia stan wiedzy, skoro kazdy ze studentow juz to widzial na wlasne oczy?
            Przed oswiadczeniem fakt ten byl wiedza wzajemna $K(E)$, lecz <strong>nie byl wspolna wiedza</strong>!
            Student 1 dopuszczal, ze ma bialy kapelusz; wtedy Student 2 widzialby 1 czerwony i dopuszczalby, ze Student 3 widzi 2 biale kapelusze i uważa, ze zadnego czerwonego nie ma!
            Publiczne ogłoszenie niszczy ten łańcuch kontrfaktyczny, tworząc $CKE$ i uruchamiając kaskadę eliminacji.
          </p>
        </div>

        <!-- ZADANIE 7.14 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyrznione Zadanie 7.14 (Trzy Corki Pete'a i Koperty z Liczbami)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 7.E &bull; s. 277</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Tresc Zadania:</strong> Pete wklada do trzech kopert liczby calkowite dodatnie $x, y, z$ takie, ze jedna jest suma dwoch pozostalych (np. $z = x + y$).
            Kazda z trzech corek widzi wlasna liczbe, lecz nie zna pozostalych.
            Pete pyta po kolei kazda corke, czy wie, jakie sa pozostale liczby. Pierwsza mowi "Nie", druga mowi "Nie", a trzecia mowi "Tak, wiem!".
            Zadanie wymaga skonstruowania przestrzeni stanow Kripkego i pokazania, w jaki sposob sekwencja negatywnych deklaracji eliminuje komorki partycji, doprowadzajac do natychmiastowej dedukcji.
          </p>
        </div>
      </section>
    """

def get_chapter_8():
    return """
      <!-- ROZDZIAL 8: DODAWANIE PRZEKONAN, BAYES I TEORIA AGM -->
      <section id="rozdzial-8" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Czesc III &bull; Rozdzial 8</span>
          <span class="text-xs font-mono text-slate-400">Przekonania i Bayes &bull; Strony 289-331</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdzial 8: Przekonania Probabilistyczne, Bayes i Teoria AGM</h3>

        <!-- 8.1 - 8.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            8.1 - 8.3. Rewizja Przekonan AGM i Porzadki Wiarygodnosci (Plausibility Orders)
          </h4>
          <p>
            W modelach probabilistycznych kazdemu stanowi $\\omega$ przypisujemy rozklad $P_i(\\cdot | \\omega)$.
            Gdy nadejdzie informacja $E \\subseteq \\Omega$ z $P(E) > 0$, nowa ocena wynika wprost z reguly Bayesa: $P(A|E) = \\frac{P(A \\cap E)}{P(E)}$.
            <strong>Kluczowy Problem Teoretyczny:</strong> Co zrobic, gdy nastapi zdarzenie $E$, ktoremu decydent przypisywal wczesniej prawdopodobienstwo zerowe ($P(E) = 0$)?
            Dzielenie przez zero w formule Bayesa uniemozliwia aktualizacje!
          </p>
          <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-blue-800 text-xs block uppercase">Twierdzenie 8.1 (Adam Grove 1988 / Giacomo Bonanno 2009) &bull; Racjonalizacja AGM</span>
            <p class="text-xs text-blue-950 leading-relaxed">
              Funkcja rewizji przekonan spelnia aksjomaty <strong>AGM (Alchourron, Gardenfors, Makinson, 1985)</strong> wtedy i tylko wtedy, gdy jest generowana przez
              <strong>porzadek wiarygodnosci (Plausibility Preorder)</strong> $\\precsim$ na zbiorze stanow $\\Omega$ (kompletna i przechodnia relacje z warunkiem, ze stany uwazane za mozliwe sa scisle najbardziej wiarygodne).
              Po zaobserwowaniu dowolnego zdarzenia $E \\ne \\emptyset$ (nawet z $P(E) = 0$), agent uznaje za mozliwe wylacznie stany bedace <strong>minimami relacji $\\precsim$ wewnatrz $E$</strong>!
            </p>
          </div>
        </div>

        <!-- 8.4 - 8.5 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            8.4 - 8.5. Twierdzenie Aumanna o Braku Zgody na Niezgode (Agreeing to Disagree) i No-Trade Theorem
          </h4>
          <p>
            Zalozenie <strong>Wspolnego Rozkladu Poczatkowego (Common Prior Assumption / Harsanyi Consistency)</strong> zaklada, ze gracze przed uzyskaniem prywatnych sygnalow posiadali identyczny obiektywny rozklad prawdopodobienstwa $P$ na $\\Omega$.
          </p>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Twierdzenie 8.1 (Agreement Theorem &bull; Robert Aumann, 1976)</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              Niech dwoch graczy dzieli ten sam rozklad poczatkowy $P$ ($P(\\omega) > 0 \\; \\forall \\omega$).
              Jesli w pewnym stanie $\\omega^*$ jest <strong>wspolna wiedza</strong>, ze Gracz 1 przypisuje zdarzeniu $E$ prawdopodobienstwo a posteriori $p = P(E | \\mathcal{I}_1(\\omega^*))$,
              a Gracz 2 przypisuje zdarzeniu $E$ prawdopodobienstwo $q = P(E | \\mathcal{I}_2(\\omega^*))$, to:
              $$p = q$$
              Dwaj racjonalni decydenci posiadajacy wspolne przekonania poczatkowe <strong>nie moga zgodzic sie na niezgode</strong>!
            </p>
            <details class="text-xs bg-white p-3 rounded-lg border border-emerald-100 cursor-pointer">
              <summary class="font-bold text-emerald-700 select-none">Rozwin Scisly Dowod Twierdzenia Aumanna (Appendix 8.A Bonanno)</summary>
              <div class="mt-2 text-slate-700 space-y-2 leading-relaxed">
                <p>
                  Niech $M = \\mathcal{M}(\\omega^*)$ bedzie komorka spojenia (Meet) zawierajaca stan $\\omega^*$.
                  Z Twierdzenia 7.1 o wspolnej wiedzy, fakt ze $P(E | \\mathcal{I}_1) = p$ jest wspolna wiedza w $\\omega^*$ oznacza, ze dla <em>kazdego</em> stanu $\\omega \\in M$ zachodzi $P(E | \\mathcal{I}_1(\\omega)) = p$.
                </p>
                <p>
                  Komorka $M$ jest suma rozlacznych komorek partycji Gracza 1: $M = \\bigcup_{k=1}^r I_{1,k}$.
                  Dla kazdej komorki $I_{1,k}$ mamy z definicji prawdopodobienstwa warunkowego:
                  $$\\frac{P(E \\cap I_{1,k})}{P(I_{1,k})} = p \\implies P(E \\cap I_{1,k}) = p \\cdot P(I_{1,k})$$
                  Sumujac po wszystkich $k$:
                  $$P(E \\cap M) = \\sum_{k=1}^r P(E \\cap I_{1,k}) = p \\sum_{k=1}^r P(I_{1,k}) = p \\cdot P(M)$$
                  Wobec tego $p = \\frac{P(E \\cap M)}{P(M)}$.
                </p>
                <p>
                  Postepujac identycznie dla Gracza 2 (poniewaz $M$ jest takze suma rozlacznych komorek partycji Gracza 2):
                  $$P(E \\cap M) = q \\cdot P(M) \\implies q = \\frac{P(E \\cap M)}{P(M)}$$
                  Z porownania obu rownosci wynika bezposrednio: $p = q$. $\\blacksquare$
                </p>
              </div>
            </details>
          </div>
          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-1 text-xs">
            <strong class="text-blue-700 block font-mono">Twierdzenie o Braku Handlu (No-Trade Theorem &bull; Milgrom & Stokey 1982):</strong>
            Jesli alokacja poczatkowa jest efektywna w sensie Pareto, gracze maja wspolny rozklad a priori i handluja czysto spekulacyjnie w oparciu o informacje prywatne, to fakt checi zawarcia transakcji staje sie wspolna wiedza, zdradzajac informacje rywalowi.
            W rezultacie <strong>zadna spekulacyjna transakcja nie dochodzi do skutku</strong>! Czysta spekulacja w racjonalnym rynku finansowym jest niemozliwa bez podmiotow handlujacych z przyczyn plynnościowych (noise traders).
          </div>
        </div>

        <!-- ZADANIE 8.12 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyrznione Zadanie 8.12 (Dwóch Lekarzy Diagnozujących Pacjenta z Common Prior)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 8.E &bull; s. 320</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Tresc Zadania:</strong> Dwoch lekarzy bada pacjenta. Poczatkowo obaj oceniaja ryzyko rzadkiej choroby $C$ na $10\\%$.
            Lekarz A wykonuje test krwi, a Lekarz B tomografie. Otrzymuja prywatne wyniki.
            Zadanie dowodzi, ze jesli lekarze zaczna oglaszac swoje biezace subiektywne prawdopodobienstwa, to po kilku rundach ich oceny musza zbiec sie do dokladnie tej samej wartosci, co stanowi empiryczna ilustracje twierdzenia o braku zgody na niezgode!
          </p>
        </div>
      </section>
    """

def get_chapter_9():
    return """
      <!-- ROZDZIAL 9: WSPOLNA WIEDZA O RACJONALNOSCI -->
      <section id="rozdzial-9" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Czesc III &bull; Rozdzial 9</span>
          <span class="text-xs font-mono text-slate-400">CKR & Epistemic Foundations &bull; Strony 332-352</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdzial 9: Wspolna Wiedza o Racjonalnosci (CKR)</h3>

        <!-- 9.1 - 9.2 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            9.1 - 9.2. Epistemiczne Modele Gier i Twierdzenie Brandenburgera-Dekela / Tan-Werlanga
          </h4>
          <p>
            W epistemicznym modelu gry strategicznej (Definicja 9.1), kazdy stan $\\omega \\in \\Omega$ okresla nie tylko wybor strategii kazdego gracza $s_i(\\omega)$, lecz takze partycje informacyjna i przekonania probabilistyczne.
            Gracz $i$ jest <strong>racjonalny w stanie $\\omega$ (Definicja 9.2)</strong>, gdy jego wybor $s_i(\\omega)$ maksymalizuje oczekiwana uzytecznosc wzgledem jego przekonan w stanie $\\omega$.
            Niech $R_i \\subseteq \\Omega$ oznacza zdarzenie "Gracz $i$ jest racjonalny", a $R = \\bigcap R_i$ oznacza "Wszyscy sa racjonalni".
          </p>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Twierdzenie 9.1 & 9.2 (Brandenburger & Dekel 1987 / Tan & Werlang 1988)</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              1. Jesli w stanie $\\omega^*$ zachodzi <strong>Wspolna Wiedza o Racjonalnosci</strong> ($\\omega^* \\in CK(R)$), to zagrany w tym stanie profil strategii $s(\\omega^*)$ musi <strong>przetrwac procedure IDSDS</strong> (iterowana eliminacje strategii scisle zdominowanych)!<br>
              2. Odwrotnie: kazdy profil strategii, ktory przetrwa IDSDS, moze byc zrealizowany w pewnym modelu epistemicznym w stanie, w ktorym zachodzi $CK(R)$.
            </p>
          </div>
          <p class="text-xs text-slate-600">
            Wniosek metodologiczny: Wspolna wiedza o racjonalnosci <em>nie implikuje</em> rownowagi Nasha! Uzasadnia ona wylacznie zbiory strategii racjonalizowalnych. Do uzyskania rownowagi Nasha konieczne jest dodatkowo zalozenie o wspolnym rozkladzie pierwotnym lub prawidlowych oczekiwaniach.
          </p>
        </div>

        <!-- 9.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            9.3. CKR w Grach Ekstensywnych i Debata Aumann vs Stalnaker
          </h4>
          <p>
            W slynnej publikacji z 1995 roku Robert Aumann udowodnil, ze w grach o doskonalej informacji ze scisle unikalnymi wyplatami, <strong>CKR implikuje rozwiazanie indukcji wstecznej</strong>.
            Twierdzenie to wywolalo jednak gleboka debate filozoficzna (Stalnaker 1998, Ben-Porath 1997):
          </p>
          <div class="p-3 sm:p-4 bg-amber-50/70 border border-amber-200 rounded-xl text-xs text-amber-950 leading-relaxed">
            <strong>Krytyka Roberta Stalnopera (1998):</strong>
            Co ma pomyslec Gracz 2, gdy znajdzie sie w wezle, do ktorego racjonalny Gracz 1 nigdy nie powinien byl dojsc?
            Jesli Gracz 1 wlasnie popelnil razacy blad, to w co Gracz 2 powinien wierzyc na temat racjonalnosci Gracza 1 w kolejnych krokach?
            Klasyczny dowod Aumanna zakłada "poczatkowa" wspolna wiedze, ktora nie musi przetrwac po zaobserwowaniu nieracjonalnego ruchu rywala.
          </div>
        </div>
      </section>
    """
