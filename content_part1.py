# Part 1: Chapters 0, 1, 2, 3 for Lyceum Game Theory
# Zero em-dashes strictly enforced.

def get_chapter_0():
    return """
      <!-- ROZDZIAL 0: WPROWADZENIE I GENEZA TEORII GIER -->
      <section id="rozdzial-0" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Wprowadzenie</span>
          <span class="text-xs font-mono text-slate-400">Giacomo Bonanno &bull; Rozdzial 0 &bull; Strony 1-5</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdzial 0: Geneza, Metodologia i Paradygmat Homo Rationalis</h3>

        <!-- 0.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            0.1. Rys Historyczny i Cztery Fale Nagrod Nobla
          </h4>
          <p>
            Teoria gier powstala jako scisly dzial matematyki badajacy interaktywne sytuacje decyzyjne, w ktorych wynik zalezy od jednoczesnych lub sekwencyjnych dzialan wielu niezaleznych podmiotow (zwanych graczami).
            Pionierami dyscypliny w pierwszej polowie XX wieku byli <strong>Ernst Zermelo (1913)</strong>, ktory sformulowal pierwsze twierdzenie o determinizmie w grach takich jak szachy, oraz <strong>John von Neumann (1928)</strong>, autor twierdzenia o minimaksie w grach dwuosobowych o sumie zerowej.
          </p>
          <p>
            Punktem zwrotnym stala sie fundamentalna monografia Johna von Neumanna i Oskara Morgensterna z 1944 roku pt. <em>Theory of Games and Economic Behavior</em>.
            Kolejna dekada przyniosla rewolucyjne odkrycia <strong>Johna Nasha (1950, 1951)</strong> (pojecie rownowagi w strategiach mieszanych), <strong>Lloyda Shapleya (1953)</strong> (wartosc Shapleya w grach kooperacyjnych) oraz <strong>Harolda Kuhna (1953)</strong> (postac ekstensywna i strategie behawioralne).
          </p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
            <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
              <span class="text-xs font-mono font-bold text-blue-700 block uppercase">Fale Nagrod Nobla w Dziedzinie Teorii Gier:</span>
              <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside">
                <li><strong>1994:</strong> John Nash, John Harsanyi, Reinhard Selten (za analize rownowag w teorii gier niekooperacyjnych).</li>
                <li><strong>2005:</strong> Robert Aumann, Thomas Schelling (za poglebienie rozumienia konfliktu i kooperacji).</li>
                <li><strong>2007:</strong> Leonid Hurwicz, Eric Maskin, Roger Myerson (za fundamenty teorii projektowania mechanizmow - Mechanism Design).</li>
                <li><strong>2012:</strong> Lloyd Shapley, Alvin Roth (za teorie stabilnych alokacji i projektowanie rynkow).</li>
              </ul>
            </div>
            <div class="p-4 bg-blue-50/60 border border-blue-200 rounded-xl space-y-2">
              <span class="text-xs font-mono font-bold text-blue-900 block uppercase">Praktyczny Triumf: Aukcje FCC (1994)</span>
              <p class="text-xs text-blue-950 leading-relaxed">
                W 1994 roku Federalna Komisja Lacznosci USA (FCC) uzyla zaawansowanej teorii gier do zaprojektowania rownoczesnej aukcji wielorundowej pasma radiowego o wartosci 7 miliardow dolarow.
                Aukcja ta zapobiegla spekulacjom, wyeliminowala zjawisko "klatwy zwyciezcy" (Winner's Curse) i stala sie swiatowym standardem alokacji czestotliwosci telekomunikacyjnych.
              </p>
            </div>
          </div>
        </div>

        <!-- 0.2 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            0.2. Aksjomat Homo Rationalis i Granice Racjonalnosci
          </h4>
          <p>
            Tradycyjna teoria gier opiera sie na precyzyjnie zdefiniowanym modelu decydenta. Jak zauwaza laureat Nagrody Nobla Robert Aumann:
          </p>
          <div class="p-4 bg-slate-50 border-l-4 border-blue-600 rounded-r-xl text-xs sm:text-sm text-slate-800 leading-relaxed italic">
            "Mowiac krotko, teoria gier i ekonomia zajmuja sie interaktywnym zachowaniem <em>Homo rationalis</em> - czlowieka racjonalnego.
            Homo rationalis to gatunek, ktory zawsze dziala zarowno celowo, jak i logicznie, posiada scisle okreslone cele, jest motywowany wylacznie pragnieniem
            zblizenia sie do tych celow tak bardzo, jak to mozliwe, i ma zdolnosci kalkulacyjne wymagane, aby to uczynic."
            <div class="text-right text-xs font-sans font-semibold text-slate-500 not-italic mt-1">- Robert Aumann (1985, s. 35)</div>
          </div>
          <p>
            W podreczniku Giacomo Bonanno przyjmuje ten klasyczny paradygmat: gracze sa w pelni inteligentni, zdolni do bezblednej dedukcji, a takze swiadomi, ze ich partnerzy i rywale sa rowniez racjonalni.
            Odrznia to tradycyjna teorie gier od biologii ewolucyjnej (gdzie "graczami" sa bezmyslne organizmy podlegajace doborowi naturalnemu) oraz behawioralnej teorii gier (analizujacej poznawcze ograniczenia i bledy heurystyczne ludzi).
          </p>
        </div>

        <!-- 0.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            0.3. Piec Fundamentalnych Dychotomii Podzialu Gier
          </h4>
          <p>
            Teoria gier dzieli interakcje decyzyjne wedlug pieciu fundamentalnych wymiarow formalnych:
          </p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
            <div class="p-3 bg-white border border-slate-200 rounded-xl space-y-1 shadow-sm">
              <strong class="text-blue-700 block font-mono">1. Gry Kooperacyjne vs Niekooperacyjne</strong>
              <p class="text-slate-600">
                W grach kooperacyjnych gracze moga zawierac wiazace prawnie porozumienia (binding agreements) egzekwowane przez sad lub arbitra.
                W grach niekooperacyjnych (ktorym poswiecony jest ten podrecznik) porozumienia musza byc <strong>samoegzekwujace sie (self-enforcing)</strong>.
              </p>
            </div>
            <div class="p-3 bg-white border border-slate-200 rounded-xl space-y-1 shadow-sm">
              <strong class="text-blue-700 block font-mono">2. Postac Strategiczna vs Postac Ekstensywna</strong>
              <p class="text-slate-600">
                Postac strategiczna (macierzowa) opisuje gry jednoczesne, gdzie gracze wybieraja strategie w izolacji.
                Postac ekstensywna (drzewo decyzyjne) uwzglednia uplyw czasu, kolejnosc posuniec i dynamiczna strukture informacji.
              </p>
            </div>
            <div class="p-3 bg-white border border-slate-200 rounded-xl space-y-1 shadow-sm">
              <strong class="text-blue-700 block font-mono">3. Informacja Doskonala vs Niedoskonalosc Informacji</strong>
              <p class="text-slate-600">
                Informacja jest doskonala, gdy w kazdym momencie gracz podejmujacy decyzje dokladnie zna cala przeszla historie ruchow.
                Informacja jest niedoskonala, gdy pewne wezly decyzyjne tworza nieodroznialne zbiory informacyjne (np. poker, ruchy rownoczesne).
              </p>
            </div>
            <div class="p-3 bg-white border border-slate-200 rounded-xl space-y-1 shadow-sm">
              <strong class="text-blue-700 block font-mono">4. Informacja Pelna vs Informacja Niepelna</strong>
              <p class="text-slate-600">
                Informacja jest pelna, gdy reguly gry i funkcje wyplat sa wspolna wiedza wszystkich graczy.
                Informacja jest niepelna, gdy gracze nie znaja funkcji wyplat rywali (modele Harsanyiego z typami graczy i ruchem Natury).
              </p>
            </div>
            <div class="p-3 bg-white border border-slate-200 rounded-xl space-y-1 shadow-sm md:col-span-2">
              <strong class="text-blue-700 block font-mono">5. Wyplaty Porzadkowe (Ordinal) vs Wyplaty Kardynalne (Cardinal)</strong>
              <p class="text-slate-600">
                Wyplaty porzadkowe (Czesc I) wymagaja wylacznie uszeregowania rezultatow (wystarczy wiedziec co gracz woli bardziej).
                Wyplaty kardynalne (Czesc II-V) opieraja sie na teorii oczekiwanej uzytecznosci von Neumanna-Morgensterna, umozliwiajac analize ryzyka, loterii i strategii mieszanych.
              </p>
            </div>
          </div>
        </div>

        <!-- 0.4 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            0.4. Epistemiczny Zwrot w Teorii Gier
          </h4>
          <p>
            Tradycyjna literatura pytala: <em>"Jaka jest rownowaga tej gry?"</em>.
            Nowoczesne podejście epistemiczne (rozwijane w Czesciach III i IV przez Aumanna, Brandenburgera, Dekela oraz Giacomo Bonanno) stawia glebsze pytanie:
            <strong>"Co gracze musza wiedziec i w co musza wierzyc na temat gry oraz na temat wzajemnej racjonalnosci, aby uzasadnic wybor konkretnej strategii?"</strong>.
            To wlasnie ten epistemologiczny rygor wyznacza unikalny charakter calego podrecznika Bonanno.
          </p>
        </div>
      </section>
    """

def get_chapter_1():
    return """
      <!-- ROZDZIAL 1: GRY PORZADKOWE W POSTACI STRATEGICZNEJ -->
      <section id="rozdzial-1" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Czesc I &bull; Rozdzial 1</span>
          <span class="text-xs font-mono text-slate-400">Gry w Postaci Strategicznej &bull; Strony 6-64</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdzial 1: Gry Porzadkowe w Postaci Strategicznej</h3>

        <!-- 1.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            1.1. Ramki Gry a Gry (Game Frames and Games)
          </h4>
          <p>
            W podreczniku Bonanno kluczowym rozroznieniem jest separacja fizycznej struktury decyzyjnej od psychologicznych motywacji decydentow.
            Formalnie sytuacje interaktywna bez przypisania preferencji okreslamy jako <strong>ramke gry w postaci strategicznej (Definicja 1.1)</strong>:
          </p>
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 font-mono text-xs overflow-x-auto">
            $$\\mathcal{F} = \\langle I, (S_1, S_2, \\dots, S_n), O, f \\rangle$$
          </div>
          <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside">
            <li>$I = \\{1, 2, \\dots, n\\}$ to skonczony zbior graczy ($n \\ge 2$).</li>
            <li>$S_i$ to zbior strategii dostepnych dla gracza $i$. Zbior profili strategii to iloczyn kartezjanski $S = S_1 \\times S_2 \\times \\dots \\times S_n$.</li>
            <li>$O$ to zbior mozliwych fizycznych rezultatow gry (outcomes).</li>
            <li>$f: S \\to O$ to funkcja rezultatu przyporzadkowujaca kazdemu profilowi strategii $s = (s_1, \\dots, s_n)$ konkretny wynik fizyczny $f(s) \\in O$.</li>
          </ul>
          <p>
            Aby przeksztalcic ramke gry w pelna gre, kazdemu graczowi $i \\in I$ przypisujemy relacje preferencji $\\succsim_i$ nad zbiorem rezultatow $O$.
            Relacja $\\succsim_i$ musi spelniac dwa aksjomaty racjonalnosci:
          </p>
          <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside">
            <li><strong>Zupelnosc (Completeness):</strong> $\\forall o_1, o_2 \\in O: o_1 \\succsim_i o_2 \\lor o_2 \\succsim_i o_1$.</li>
            <li><strong>Przechodniosc (Transitivity):</strong> $\\forall o_1, o_2, o_3 \\in O: (o_1 \\succsim_i o_2 \\land o_2 \\succsim_i o_3) \\implies o_1 \\succsim_i o_3$.</li>
          </ul>
          <p>
            Relacja scislej preferencji definiowana jest jako $o_1 \\succ_i o_2 \\iff (o_1 \\succsim_i o_2 \\land \\neg(o_2 \\succsim_i o_1))$, zas relacja obojetnosci jako $o_1 \\sim_i o_2 \\iff (o_1 \\succsim_i o_2 \\land o_2 \\succsim_i o_1)$.
            Funkcja $U_i: O \\to \\mathbb{R}$ jest <strong>porzadkowa funkcja uzytecznosci (Definicja 1.2)</strong>, gdy dla dowolnych $o_1, o_2 \\in O$:
          </p>
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 font-mono text-xs overflow-x-auto">
            $$U_i(o_1) > U_i(o_2) \\iff o_1 \\succ_i o_2 \\quad \\text{oraz} \\quad U_i(o_1) = U_i(o_2) \\iff o_1 \\sim_i o_2$$
          </div>
          <p>
            <strong>Przyklad: Teleturniej "Split or Steal" (Golden Balls):</strong> Dwoch uczestnikow (Sarah i Stephen) wybiera niezaleznie "Podziel" (Split) lub "Ukradnij" (Steal). Pula wynosi 100 000 GBP.
            Rezultaty fizyczne: $o_1$ (oboje dziela: po 50k), $o_2$ (Sarah kradnie, Stephen dzieli: 100k dla Sarah, 0 dla Stephena), $o_3$ (Sarah dzieli, Stephen kradnie: 0 dla Sarah, 100k dla Stephena), $o_4$ (oboje kradna: 0 dla obu).
            Jesli Sarah jest chciwa i samolubna, jej uzytecznosci to $U(o_2)=4 > U(o_1)=3 > U(o_4)=2 > U(o_3)=1$. Wtedy Steal jest dla niej strategia scisle dominujaca.
            Jesli jednak Sarah ceni sprawiedliwosc i nienawidzi kradziezy, jej ranking to $U(o_1)=4 > U(o_2)=3 > U(o_4)=2 > U(o_3)=1$. Ta sama ramka gry, lecz zupelnie inna gra decyzyjna!
          </p>
        </div>

        <!-- 1.2 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            1.2. Dominacja Scisla i Slaba (Strict and Weak Dominance)
          </h4>
          <p>
            Niech $S_{-i} = \\times_{j \\ne i} S_j$ oznacza zbior profili strategii rywali gracza $i$. Wektor wyplat gracza $i$ przy wyborze $s_i \\in S_i$ i reakcji rywali $s_{-i} \\in S_{-i}$ to $\\pi_i(s_i, s_{-i}) = U_i(f(s_i, s_{-i}))$.
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 1.4: Relacje Dominacji</span>
            <ul class="text-xs text-slate-700 space-y-1.5 list-disc list-inside">
              <li>
                <strong>Scisla dominacja:</strong> Strategia $a \\in S_i$ <em>scisle dominuje</em> strategie $b \\in S_i$, gdy:
                $$\\forall s_{-i} \\in S_{-i}: \\pi_i(a, s_{-i}) > \\pi_i(b, s_{-i})$$
              </li>
              <li>
                <strong>Slaba dominacja:</strong> Strategia $a \\in S_i$ <em>slabo dominuje</em> strategie $b \\in S_i$, gdy:
                $$\\forall s_{-i} \\in S_{-i}: \\pi_i(a, s_{-i}) \\ge \\pi_i(b, s_{-i}) \\quad \\text{oraz} \\quad \\exists \\bar{s}_{-i} \\in S_{-i}: \\pi_i(a, \\bar{s}_{-i}) > \\pi_i(b, \\bar{s}_{-i})$$
              </li>
              <li>
                <strong>Rownowaznosc:</strong> Strategie $a, b$ sa rownowazne, gdy $\\forall s_{-i} \\in S_{-i}: \\pi_i(a, s_{-i}) = \\pi_i(b, s_{-i})$.
              </li>
            </ul>
          </div>
          <p>
            <strong>Wlasnosc Unikalnosci:</strong> Strategia scisle dominujaca jest unikalna: zaden gracz nie moze posiadac dwoch roznych strategii scisle dominujacych.
            Natomiast gracz moze miec wiele strategii slabo dominujacych, pod warunkiem ze sa one sobie wzajemnie rownowazne.
          </p>
          <p>
            <strong>Dylemat Wieznia i Efektywnosc Pareto (Definicja 1.7):</strong> Rezultat $o$ jest <em>scisle lepszy w sensie Pareto</em> od $o'$, jesli $\\forall i \\in I: o \\succ_i o'$.
            W slynnej grze Doug i Ed obaj podejrzani maja scisle dominujaca strategie "Zeznawaj" (Confess). Profil (Zeznawaj, Zeznawaj) jest jedynym profilem strategii dominujacych, lecz prowadzi do rezultatu (5 lat, 5 lat), ktory jest scisle gorszy w sensie Pareto od profilu (Milcz, Milcz) dajacego (1 rok, 1 rok). Indywidualna racjonalnosc stoi w bezposrednim konflikcie ze spoleczna efektywnoscia!
          </p>
        </div>

        <!-- 1.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            1.3. Aukcja Drugiej Ceny Vickreya (Twierdzenie 1.1)
          </h4>
          <p>
            W zapieczetowanej aukcji drugiej ceny $n$ licytantow sklada jednoczesnie tajne oferty $b_i \\ge 0$. Przedmiot trafia do gracza z najwyzsza oferta $b^* = \\max_j b_j$, ktory placi cene rowna <strong>drugiej najwyzszej ofercie</strong> $p = \\max_{j \\ne i^*} b_j$. W przypadku remisu przedmiot jest losowany.
          </p>
          <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-blue-800 text-xs block uppercase">Twierdzenie 1.1 (William Vickrey, 1961)</span>
            <p class="text-xs text-blue-950 leading-relaxed">
              Niech gracz $i$ posiada prywatna wycene przedmiotu $v_i > 0$. Jesli gracz $i$ jest samolubny i chciwy (jego wyplata wynosi $v_i - p$ przy wygranej za cene $p$ oraz $0$ przy przegranej),
              to zgloszenie oferty dokladnie rownej prawdziwej wycenie:
              $$b_i = v_i$$
              jest <strong>strategia slabo dominujaca</strong>.
            </p>
            <details class="text-xs bg-white p-3 rounded-lg border border-blue-100 cursor-pointer">
              <summary class="font-bold text-blue-700 select-none">Rozwin Scisly Dowod Twierdzenia 1.1 (Appendix 1.A Bonanno)</summary>
              <div class="mt-2 text-slate-700 space-y-2 leading-relaxed">
                <p>
                  Niech $M = \\max_{j \\ne i} b_j$ oznacza najwyzsza oferte zlozona przez rywali gracza $i$. Gracz $i$ nie zna $M$, lecz rozpatrzmy dwa wyczerpujace przypadki:
                </p>
                <p>
                  <strong>Przypadek 1: $M \\le v_i$.</strong> Jesli gracz zaoferuje $b_i = v_i$, wygrywa aukcje i placi cene $M$, uzyskujac wyplate $\\pi_i = v_i - M \\ge 0$.
                  Jakakolwiek inna oferta $b_i' > M$ rowniez wygrywa i placi dokladnie te sama cene $M$, daja te sama wyplate.
                  Oferta $b_i' < M$ sprawia, ze gracz przegrywa aukcje i otrzymuje wyplate $0 \\le v_i - M$.
                  Zatem zadna alternatywna oferta nie moze dac scisle wyzszej wyplaty niz $b_i = v_i$.
                </p>
                <p>
                  <strong>Przypadek 2: $M > v_i$.</strong> Jesli gracz zaoferuje $b_i = v_i$, przegrywa aukcje i placi $0$, uzyskujac wyplate $\\pi_i = 0$.
                  Jakakolwiek oferta $b_i' \\le M$ rowniez przegrywa i daje $0$.
                  Aby wygrac aukcje, gracz musialby zaoferowac $b_i' > M$. Wtedy jednak placi cene $M$, co daje wyplate $v_i - M < 0$ (scisla strate!).
                  Zatem licytowanie $v_i$ daje wyplate co najmniej tak wysoka jak kazda inna oferta, a dla pewnych stanow rywali scisle wyzsza.
                  W konsekwencji oferta $b_i = v_i$ jest slabo dominujaca. $\\blacksquare$
                </p>
              </div>
            </details>
          </div>
          <p class="text-xs text-slate-600">
            <strong>Kontrast z aukcja pierwszej ceny:</strong> W aukcji pierwszej ceny zwyciezca placi wlasna oferte $b_i$. Oferta $b_i = v_i$ gwarantuje zysk $v_i - v_i = 0$.
            Gracz musi zatem strategicznie zanizac oferte ($b_i < v_i$), aby uzyskac dodatni zysk. W aukcji pierwszej ceny prawdomownosc nigdy nie jest strategia dominujaca!
          </p>
        </div>

        <!-- 1.4 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            1.4. Mechanizm Pivotowy Clarke'a (Twierdzenie 1.2)
          </h4>
          <p>
            Wyobrazmy sobie spolecznosc decydujaca o budowie dobra publicznego (mostu, parku, biblioteki) o koszcie $C > 0$. Kazdy czlonek ponosi z gory okreslony koszt $c_i > 0$ (gdzie $\\sum c_i = C$).
            Prywatna korzysc kazdego gracza wynosi $v_i$. Projekt jest efektywny w sensie Pareto wtedy i tylko wtedy, gdy $\\sum v_i > C$, czyli $\\sum (v_i - c_i) > 0$.
            Poniewaz wyceny sa prywatna informacja, gracze maja pokuse znieksztalcania deklaracji (free-riding).
          </p>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Twierdzenie 1.2 (Edward Clarke, 1971 / Theodore Groves, 1973)</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              W mechanizmie pivotowym kazdy gracz deklaruje wartosc $w_i$. Projekt jest realizowany, gdy $\\sum w_j > C$.
              Gracz $i$ jest <strong>pivotowy (pivotal)</strong>, jesli jego obecnosc zmienia decyzje spoleczna, tj. $\\text{znak}\\left(\\sum_{j=1}^n (w_j - c_j)\\right) \\ne \\text{znak}\\left(\\sum_{j \\ne i} (w_j - c_j)\\right)$.
              Gracz pivotowy placi podatek w wysokosci straty narzuconej reszcie spoleczenstwa:
              $$t_i = \\left| \\sum_{j \\ne i} (w_j - c_j) \\right|$$
              Gracz niebedacy pivotowym placi podatek $t_i = 0$.
              Dla kazdego gracza prawdomowne zgloszenie $w_i = v_i$ jest <strong>strategia slabo dominujaca</strong>!
            </p>
          </div>
        </div>

        <!-- 1.5 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            1.5. Procedury Eliminacji Iteracyjnej: IDSDS a IDWDS
          </h4>
          <p>
            Jesli strategia jest scisle zdominowana, zaden racjonalny gracz jej nie wybierze. Co wiecej, jesli fakt racjonalnosci jest wiedza powszechna, mozemy usunac strategie zdominowane wszystkich graczy, uzyskujac zredukowana gre, i powtorzyc te procedure w kolejnych rundach.
          </p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
              <span class="font-bold text-slate-800 text-xs font-mono uppercase block">IDSDS (Strict Dominance)</span>
              <p class="text-xs text-slate-600 leading-relaxed">
                Iterowana eliminacja strategii scisle zdominowanych generuje zstepujacy ciag gier $G = G^0 \\supset G^1 \\supset \\dots \\supset G^\\infty$.
                <strong>Kluczowe Twierdzenie:</strong> W kazdej skonczonej grze porzadek eliminacji w IDSDS jest <em>calkowicie nieistotny</em>.
                Niezaleznie od tego, czy usuwamy strategie jeden po drugim, czy symetrycznie, zbior koncowy $G^\\infty$ jest identyczny!
              </p>
            </div>
            <div class="p-4 bg-amber-50/70 border border-amber-200 rounded-xl space-y-2">
              <span class="font-bold text-amber-900 text-xs font-mono uppercase block">IDWDS (Weak Dominance) &bull; Pulapka Kolejnosci</span>
              <p class="text-xs text-amber-950 leading-relaxed">
                Iterowana eliminacja strategii <strong>slabo</strong> zdominowanych zalezy od kolejnosci!
                Jak dowodzi Bonanno w Uwadze 1.6, usuniecie strategii slabo zdominowanej w jednym kroku moze zapobiec eliminacji innej strategii w kolejnym.
                Dlatego konwencja Bonanno nakazuje w kazdym kroku usuwac <em>jednoczesnie wszystkie</em> strategie slabo zdominowane.
              </p>
            </div>
          </div>
        </div>

        <!-- 1.6 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            1.6. Rownowaga Nasha i Cztery Interpretacje Filozoficzne
          </h4>
          <p>
            Rownowaga Nasha stanowi centralne pojecie teorii gier niekooperacyjnych:
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 1.9 &bull; Rownowaga Nasha w Postaci Strategicznej</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              Profil strategii $s^* = (s_1^*, s_2^*, \\dots, s_n^*) \\in S$ jest <strong>rownowaga Nasha</strong>, gdy dla kazdego gracza $i \\in I$ i kazdej alternatywnej strategii $s_i \\in S_i$:
              $$\\pi_i(s_i^*, s_{-i}^*) \\ge \\pi_i(s_i, s_{-i}^*)$$
            </p>
          </div>
          <p>
            Rownowaga Nasha to punkt staly korespondencji najlepszych odpowiedzi: $s^* \\in \\times_{i=1}^n BR_i(s_{-i}^*)$, gdzie $BR_i(s_{-i}) = \\arg\\max_{s_i} \\pi_i(s_i, s_{-i})$.
            Bonanno wyrznia cztery glwne interpretacje:
          </p>
          <ol class="text-xs text-slate-600 space-y-1 list-decimal list-inside pl-2">
            <li><strong>Punkt centralny (Focal Point / Schelling):</strong> Oczywiste rozwiazanie wyznaczone przez kulture lub kontekst.</li>
            <li><strong>Samoegzekwujace sie porozumienie:</strong> Gdyby gracze mogli sie spotkac przed gra i ustalic strategie bez prawa do podpisania umowy, dotrzymaja slowa wtedy i tylko wtedy, gdy uklad tworzy rownowage Nasha!</li>
            <li><strong>Stabilna konwencja spoleczna:</strong> Np. zasada ruchu prawostronnego.</li>
            <li><strong>Stan stacjonarny uczenia sie / ewolucji:</strong> Do ktorego zbiegaja powtarzane interakcje populacyjne.</li>
          </ol>
        </div>

        <!-- 1.7 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            1.7. Gry z Nieskonczonymi Zbiorami Strategii: Duopol Cournota
          </h4>
          <p>
            Gdy zbiory strategii sa ciagle (np. poziomy produkcji $q_i \\ge 0$), rownowage wyznaczamy za pomoca rachunku rozniczkowego.
            W modelu <strong>duopolu Cournota (1838)</strong> dwie firmy wybieraja jednoczesnie wielkosci produkcji $q_1, q_2$. Odwrotna funkcja popytu wynosi $P(Q) = a - b(q_1 + q_2)$ dla $Q < a/b$, a koszt krancowy kazdej firmy wynosi $c$ ($a > c > 0$).
          </p>
          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-2 font-mono text-xs overflow-x-auto">
            <div>Zysk Firmy 1: $\\pi_1(q_1, q_2) = (a - b q_1 - b q_2 - c) q_1$</div>
            <div>Warunek pierwszego rzedu (FOC): $\\frac{\\partial \\pi_1}{\\partial q_1} = a - c - 2b q_1 - b q_2 = 0$</div>
            <div>Krzywa reakcji Firmy 1: $R_1(q_2) = \\frac{a - c - b q_2}{2b}$</div>
          </div>
          <p>
            Rozwiazujac symetryczny uklad dwoch rownan reakcji ($q_1 = R_1(q_2)$, $q_2 = R_2(q_1)$), otrzymujemy unikalna rownowage Nasha-Cournota:
          </p>
          <div class="p-3 bg-emerald-50 border border-emerald-200 rounded-xl font-mono text-xs text-emerald-950 overflow-x-auto">
            $$q_1^* = q_2^* = \\frac{a - c}{3b}, \\quad Q^* = \\frac{2(a - c)}{3b}, \\quad P^* = \\frac{a + 2c}{3}, \\quad \\pi_1^* = \\pi_2^* = \\frac{(a - c)^2}{9b}$$
          </div>
          <p class="text-xs text-slate-600">
            Warto zauwazyc, ze laczna produkcja $Q^* = \\frac{2}{3} \\frac{a-c}{b}$ lezy scisle pomiedzy monopolem ($Q_M = \\frac{1}{2} \\frac{a-c}{b}$) a doskonala konkurencja ($Q_C = \\frac{a-c}{b}$).
          </p>
        </div>

        <!-- ZADANIE 1.23 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyrznione Zadanie 1.23 z Odpowiedziami (Zanieczyszczenie Rzeki i Regula Sedziego Posnera)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 1.E &bull; s. 49</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Tresc Zadania:</strong> Zaklad chemiczny Mondevil generuje zysk $\\Pi > 0$, lecz zanieczyszcza rzeke Sacramento, przynoszac szkode rybakom w wysokosci $L > 0$.
            Sedzia Richard Posner stosuje regule: obie strony skladaja w sadzie jednoczesnie deklaracje $x \\ge 0$ (Mondevil) oraz $y \\ge 0$ (rybacy).
            Jesli $y > x$, sad zamyka fabryke (wyplaty: 0 dla fabryki, 0 dla rybakow).
            Jesli $x \\ge y$, fabryka dziala, lecz musi wyplacic rybakom odszkodowanie $y$ (wyplata fabryki $\\Pi - y$, wyplata rybakow $y - L$).
          </p>
          <details class="text-xs bg-white p-3 rounded-lg border border-slate-200 cursor-pointer">
            <summary class="font-bold text-slate-800 select-none">Pokaz Pelne Rozwiazanie Krok po Kroku (Appendix 1.S Bonanno)</summary>
            <div class="mt-2 text-slate-700 space-y-2 leading-relaxed">
              <p>
                <strong>Krok 1: Analiza fabryki Mondevil.</strong> Niech rybacy zadeklaruja $y$.
                Jesli $x < y$, zysk wynosi 0. Jesli $x \\ge y$, zysk wynosi $\\Pi - y$.
                Deklaracja $x = \\Pi$ gwarantuje, ze fabryka dziala wtedy i tylko wtedy, gdy $\\Pi \\ge y$ (czyli gdy jej zysk netto jest nieujemny).
                Gdyby zadeklarowala $x > \\Pi$, ryzykowalaby dzialanie przy $y > \\Pi$, co przyniosloby strate netto.
                Gdyby zadeklarowala $x < \\Pi$, moglaby zostac zamknieta przy $\\Pi > y > x$, tracac zysk $\\Pi - y > 0$.
                Zatem dla fabryki deklaracja $x = \\Pi$ jest <strong>strategia slabo dominujaca</strong>!
              </p>
              <p>
                <strong>Krok 2: Analiza rybakow.</strong> Wiedzac, ze fabryka wybierze $x = \\Pi$, rybacy wybieraja $y$:
                Jesli $\\Pi > L$, fabryka przynosi wieksza wartosc niz strata. Rybacy moga zadeklarowac $y = \\Pi$, otrzymujac odszkodowanie $\\Pi$ i zysk netto $\\Pi - L > 0$.
                Jesli $L > \\Pi$, strata przewyzsza zysk fabryki. Wtedy kazde $y > \\Pi$ zamyka fabryke, chroniac rybakow przed strata $L - \\Pi > 0$.
              </p>
              <p>
                <strong>Wniosek ekonomiczny:</strong> Mechanizm Posnera zawsze wymusza wynik efektywny w sensie Pareto (Coase Theorem): fabryka dziala, gdy $\\Pi > L$, a zostaje zamknieta, gdy $L > \\Pi$!
              </p>
            </div>
          </details>
        </div>
      </section>
    """

def get_chapter_2():
    return """
      <!-- ROZDZIAL 2: DYNAMICZNE GRY O DOSKONALEJ INFORMACJI -->
      <section id="rozdzial-2" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Czesc I &bull; Rozdzial 2</span>
          <span class="text-xs font-mono text-slate-400">Gry Dynamiczne &bull; Strony 65-106</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdzial 2: Dynamiczne Gry o Doskonalej Informacji</h3>

        <!-- 2.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            2.1. Drzewa Gry, Ramki Ekstensywne i Gry o Doskonalej Informacji
          </h4>
          <p>
            Gra w postaci ekstensywnej modeluje kolejnosc zdarzen w czasie za pomoca skierowanego drzewa matematycznego $T = (V, E)$.
            Drzewo posiada unikalny <strong>korzen (root)</strong> $r \\in V$ o stopniu wejsciowym zero.
            Wierzcholki dziela sie na <strong>wezly decyzyjne</strong> $D$ oraz <strong>wezly koncowe (terminal nodes)</strong> $Z = V \\setminus D$.
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 2.1 &bull; Gra Ekstensywna o Doskonalej Informacji</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              Struktura $\\Gamma = \\langle T, I, \\iota, O, g, (\\succsim_i)_{i \\in I} \\rangle$, gdzie:
            </p>
            <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside">
              <li>$T$ to drzewo ukorzenione.</li>
              <li>$\\iota: D \\to I$ to funkcja przypisania decydentow, okreslajaca ktory gracz podejmuje decyzje w wezle $x \\in D$.</li>
              <li>W kazdym wezle $x \\in D$ krawedzie wychodzace odpowiadaja akcjom ze zbioru $A(x)$.</li>
              <li>$g: Z \\to O$ przypisuje kazdemu wezlowi koncowemu fizyczny rezultat gry.</li>
              <li>$\\succsim_i$ to relacje preferencji graczy nad rezultatami $O$.</li>
            </ul>
          </div>
          <p>
            Cecha dystynktywna gier o <strong>doskonalej informacji</strong> jest fakt, ze kazdy wezel decyzyjny stanowi samodzielny, jednoelementowy zbior informacyjny.
            W kazdym momencie gry gracz dokladnie wie, w ktorym wezle drzewa sie znajduje i jakie ruchy zostaly wykonane wczesniej.
          </p>
        </div>

        <!-- 2.2 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            2.2. Algorytm Indukcji Wstecznej (Backward Induction)
          </h4>
          <p>
            Podstawowym narzedziem rozwiazywania gier o doskonalej informacji jest algorytm indukcji wstecznej, sformalizowany przez Zermelo (1913) i Kuhna (1953):
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Algorytm Indukcji Wstecznej (Definicja 2.3)</span>
            <ol class="text-xs text-slate-700 space-y-1.5 list-decimal list-inside">
              <li>Wybierz wezel decyzyjny $x \\in D$, ktorego wszyscy bezposredni nastepcy sa wezlami koncowymi $z \\in Z$ z przypisanymi wyplatami.</li>
              <li>Niech $i = \\iota(x)$ bedzie graczem podejmujacym decyzje w $x$. Gracz ten wybiera akcje $a^* \\in A(x)$ prowadzaca do wezla nastepczego o najwyzszej wyplacie dla gracza $i$.</li>
              <li>Zastap wezel $x$ wektorem wyplat wybranego nastepcy (zwijanie drzewa).</li>
              <li>Powtarzaj kroki 1-3, az wyplaty zostana przypisane do korzenia drzewa $r$.</li>
            </ol>
          </div>
          <p>
            <strong>Twierdzenie o Istnieniu i Jednoznacznosci:</strong> W kazdej skonczonej grze o doskonalej informacji algorytm indukcji wstecznej zawsze znajduje rozwiazanie.
            Jesli zaden gracz nie jest obojetny miedzy zadnymi dwoma wezlami koncowymi, rozwiazanie indukcji wstecznej jest <em>scisle unikalne</em>!
          </p>
          <div class="p-3 bg-amber-50/70 border border-amber-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-amber-900 text-xs uppercase block">Paradoks Gry Stonoga (Centipede Game &bull; Rosenthal, 1981)</span>
            <p class="text-xs text-amber-950 leading-relaxed">
              Wyobrazmy sobie gre trwajaca 100 rund, w ktorej w kazdym kroku gracz moze "Zakonczyc" (Take) lub "Przekazac" (Pass).
              W kazdym kroku pula rosnie, lecz gracz konczacy gre otrzymuje wiekszy udzial.
              Indukcja wsteczna zwija gre od setnego wezla az do samego korzenia: <strong>Gracz 1 konczy gre w pierwszym ruchu</strong>, zabierajac skromna wyplate (1, 1) zamiast potencjalnych milionow!
              W eksperymentach laboratoryjnych ludzie niemal nigdy nie wybieraja natychmiastowego zakonczenia gry, grajac kooperacyjnie przez wiele rund.
            </p>
          </div>
        </div>

        <!-- 2.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            2.3. Strategie w Grach o Doskonalej Informacji
          </h4>
          <p>
            Jednym z najwazniejszych i najczesciej nierozumianych pojec w teorii gier jest definicja strategii w postaci ekstensywnej:
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 2.4: Strategia w Grze Ekstensywnej</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              Strategia gracza $i$ to funkcja $s_i: D_i \\to \\bigcup_{x \\in D_i} A(x)$ przyporzadkowujaca akcje $s_i(x) \\in A(x)$ <strong>kazdemu wezlowi decyzyjnemu</strong> tego gracza w calym drzewie gry,
              <strong>w tym rowniez wezlom, ktore nigdy nie zostana osiagniete</strong> z powodu wczesniejszych wyborow samego gracza lub jego rywali!
            </p>
          </div>
          <p class="text-xs text-slate-600">
            <strong>Dlaczego kompletny plan jest konieczny?</strong> Aby przeanalizowac rozumowanie kontrfaktyczne rywala (<em>"Co zrobilby gracz $i$, gdybym wybral opcje B zamiast A?"</em>), rywal musi znac zamiary gracza $i$ we wszystkich potencjalnych poddrzewach.
            Liczba strategii gracza wynosi $|S_i| = \\prod_{x \\in D_i} |A(x)|$.
          </p>
        </div>

        <!-- 2.4 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            2.4. Relacja Miedzy Indukcja Wsteczna a Rownowaga Nasha: Niewiarygodne Grozby
          </h4>
          <p>
            Kazda gre ekstensywna mozemy przeksztalcic w rownowazna postac strategiczna (macierzowa).
            Zachodzi nastepujaca fundamentalna relacja:
          </p>
          <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-blue-800 text-xs block uppercase">Twierdzenie 2.1: Indukcja Wsteczna a Rownowaga Nasha</span>
            <p class="text-xs text-blue-950 leading-relaxed">
              1. Kazde rozwiazanie indukcji wstecznej indukuje <strong>rownowage Nasha</strong> powiazanej postaci strategicznej gry.<br>
              2. Jednak postac strategiczna moze zawierac dodatkowe rownowagi Nasha, ktore <strong>nie sa rozwiazaniami indukcji wstecznej</strong>, poniewaz opieraja sie na <strong>niewiarygodnych grozbach (Incredible Threats)</strong>!
            </p>
          </div>
          <p>
            <strong>Przyklad: Gra Wejscia na Rynek (Market Entry):</strong> Pretendent decyduje: Wejsc (In) czy Zostac na zewnatrz (Out). Monopolista decyduje: Walczyc wojna cenowa (Fight) czy Przystosowac sie (Accommodate).
            Wyplaty: Out daje (0, 3). Przy In: Accommodate daje (2, 1), a Fight daje (-1, -1).
            Indukcja wsteczna: Monopolista po wejsciu wybiera Accommodate (1 > -1), wiec pretendent wchodzi (In) z wyplata 2.
            W postaci macierzowej profilem rownowagi Nasha jest rowniez (Out, Fight): jesli monopolista grozi wojna cenowa, pretendent woli Out (0 > -1); a przy Out wybor monopolisty nie ma znaczenia.
            Jednak grozba "Fight" jest <em>niewiarygodna</em>: gdy pretendent juz wejdzie, racjonalny monopolista nigdy jej nie zrealizuje!
          </p>
        </div>

        <!-- 2.5 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            2.5. Gry Dwuosobowe o Sumie Zerowej i Uogolnienie Twierdzenia Zermelo
          </h4>
          <p>
            W grach o doskonalej informacji, gdzie interesy graczy sa scisle sprzeczne (wygrana jednego oznacza przegrana drugiego):
          </p>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Twierdzenie 2.2 & 2.3 (Ernst Zermelo, 1913)</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              W kazdej skonczonej dwuosobowej grze o doskonalej informacji:
            </p>
            <ul class="text-xs text-emerald-900 space-y-1 list-disc list-inside">
              <li>Jesli nie ma remisow (gra typu wygrana-przegrana, np. Nim, Race to 100), to jeden z graczy posiada <strong>strategie scisle wygrywajaca</strong>.</li>
              <li>Jesli dozwolone sa remisy (szachy, warcaby, kolko i krzyzyk), to zachodzi dokladnie jedna z trzech mozliwosci: (1) Gracz 1 ma strategie wygrywajaca, (2) Gracz 2 ma strategie wygrywajaca, lub (3) obaj gracze maja strategie gwarantujace co najmniej remis!</li>
            </ul>
          </div>
        </div>

        <!-- ZADANIE 2.13 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyrznione Zadanie 2.13 (Mechanizm Sadur Krola Salomona &bull; Glazer i Ma 1989)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 2.E &bull; s. 89</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Kontekst biblijny w ujeciu teorii gier:</strong> Dwie kobiety (Anna i Maria) spieraja sie o niemowle.
            Prawdziwa matka wycenia dziecko na $v_H = 100$, zas oszustka na $v_L = 40$. Salomon nie wie, ktora jest prawdziwa matka.
            Glazer i Ma zaprojektowali dynamiczna gre ekstensywna: Salomon pyta najpierw Anne: "Czy dziecko jest twoje?". Jesli Anna powie "Nie", dziecko trafia do Marii bez oplat.
            Jesli Anna powie "Tak", Salomon pyta Marie: "Czy kwestionujesz jej slowa?". Jesli Maria nie kwestionuje, dziecko trafia do Anny.
            Jesli Maria zakwestionuje, musi zaplacic kare $F = 50$, dziecko trafia do Marii, lecz Anna placi grzywne $G = 60$.
          </p>
          <details class="text-xs bg-white p-3 rounded-lg border border-slate-200 cursor-pointer">
            <summary class="font-bold text-slate-800 select-none">Pokaz Rozwiazanie przez Indukcje Wsteczna (Appendix 2.S Bonanno)</summary>
            <div class="mt-2 text-slate-700 space-y-2 leading-relaxed">
              <p>
                <strong>Przypadek A: Anna jest prawdziwa matka ($v_A = 100, v_M = 40$).</strong>
                Jesli Anna powie "Tak", Maria kwestionujac zaplacilaby $F = 50$, uzyskujac zysk $40 - 50 = -10 < 0$. Maria nie kwestionuje.
                Wiec Anna smialo mowi "Tak" i dostaje dziecko z zyskiem 100 bez oplat!
              </p>
              <p>
                <strong>Przypadek B: Maria jest prawdziwa matka ($v_A = 40, v_M = 100$).</strong>
                Jesli Anna powie "Tak", Maria kwestionujac placi 50, lecz dostaje dziecko warte 100, osiagajac zysk $100 - 50 = 50 > 0$. Maria zakwestionuje!
                Wtedy Anna otrzyma kare $G = 60$ (zysk -60).
                Anna, przewidujac to wstecznie, w pierwszym ruchu mowi "Nie" (zysk 0 > -60). Dziecko natychmiast trafia do Marii bez oplat!
              </p>
              <p>
                <strong>Sukces mechanizmu:</strong> W indukcji wstecznej dziecko w obu przypadkach trafia do prawdziwej matki, zadna kara nie zostaje naliczona, a prawda zostaje ujawniona w pelni!
              </p>
            </div>
          </details>
        </div>
      </section>
    """

def get_chapter_3():
    return """
      <!-- ROZDZIAL 3: OGOLNE GRY DYNAMICZNE I SPE -->
      <section id="rozdzial-3" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Czesc I &bull; Rozdzial 3</span>
          <span class="text-xs font-mono text-slate-400">Ogolne Gry Dynamiczne &bull; Strony 107-156</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdzial 3: Ogolne Gry Dynamiczne, Podgry i Rownowaga SPE</h3>

        <!-- 3.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            3.1. Niedoskonala Informacja i Zbiory Informacyjne
          </h4>
          <p>
            Gdy gracze nie obserwuja pewnych ruchow rywali lub Natury (np. ukryte karty w pokerze, rownoczesne skladanie ofert w grze sekwencyjnej), wezly decyzyjne grupuja sie w <strong>zbiory informacyjne (Information Sets)</strong>.
            Zbiory informacyjne tworza partycje wierzcholkow decyzyjnych gracza $i$.
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 3.1: Warunek Doskonalej Pamieci (Perfect Recall)</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              Gra spelnia warunek doskonalej pamieci, jesli zaden gracz nigdy nie zapomina wlasnych wczesniejszych decyzji ani informacji, ktore kiedys posiadal:
            </p>
            <ol class="text-xs text-slate-600 space-y-1 list-decimal list-inside pl-2">
              <li>Dla kazdego zbioru informacyjnego $h$, wszystkie wezly $x, x' \\in h$ maja dokladnie ten sam zbior dostepnych akcji: $A(x) = A(x')$.</li>
              <li>Zaden wezel w zbiorze informacyjnym $h$ nie moze byc poprzednikiem innego wezla w tym samym zbiorze $h$ (brak amnezji wlasnych ruchow).</li>
              <li>Jesli wezel $x$ poprzedza $y$, gracz $i$ w wezle $x$ wybral akcje $a$, a $y$ nalezy do zbioru informacyjnego $h$, to kazdy inny wezel $y' \\in h$ musi rowniez miec poprzednika $x'$ nalezacego do zbioru $x$, z ktorego wyprowadzono te sama akcje $a$!</li>
            </ol>
          </div>
        </div>

        <!-- 3.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            3.3. Definicja Podgry Wlasciwej (Subgames)
          </h4>
          <p>
            Pojecie podgry jest fundamentem uszczegolawiania rownowag w grach dynamicznych:
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 3.3 &bull; Podgra Wlasciwa (Subgame)</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              Poddrzewo $G$ rozpoczynajace sie w wezle $x_0 \\in D$ jest <strong>podgra</strong>, jesli:
            </p>
            <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside">
              <li>Wezel poczatkowy $x_0$ stanowi <em>jednoelementowy zbior informacyjny</em> (singleton: $h(x_0) = \\{x_0\\}$).</li>
              <li>$G$ zawiera wezel $x_0$ oraz <strong>wszystkich jego potomkow</strong> w drzewie gry.</li>
              <li>$G$ <strong>nie rozcina zadnego zbioru informacyjnego</strong>: jesli wezel $y$ nalezy do $G$, a wezel $y'$ nalezy do tego samego zbioru informacyjnego co $y$ ($y' \\in h(y)$), to $y'$ musi rowniez nalezec do $G$!</li>
            </ul>
          </div>
          <p class="text-xs text-slate-600">
            Podgra jest <em>wlasciwa (proper subgame)</em>, jesli nie jest cala wyjsciowa gra ($x_0 \\ne r$).
          </p>
        </div>

        <!-- 3.4 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            3.4. Rownowaga Doskonala w Podgrach (Subgame-Perfect Equilibrium &bull; SPE)
          </h4>
          <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-blue-800 text-xs block uppercase">Definicja 3.5 (Reinhard Selten, 1965) &bull; Rownowaga SPE</span>
            <p class="text-xs text-blue-950 leading-relaxed">
              Profil strategii $s^* \\in S$ jest <strong>rownowaga doskonala w podgrach (Subgame-Perfect Equilibrium - SPE)</strong>, jesli:
              1. Jest rownowaga Nasha calej gry $\\Gamma$, oraz<br>
              2. W kazdej wlasciwej podgrze $G$ restrykcja profilu $s^*|_G$ tworzy rownowage Nasha tej podgry $G$.
            </p>
          </div>
          <p>
            <strong>Algorytm Wyznaczania SPE (Definicja 3.6):</strong>
            Zastepujemy minimalne podgry wektorami wyplat z ich rownowag Nasha i powtarzamy procedure w gore drzewa.
            Jesli pewna podgra nie posiada rownowagi Nasha w strategiach czystych, w grze porzadkowej czyste SPE moze nie istniec!
          </p>
        </div>

        <!-- 3.5 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            3.5. Ruchy Losowe Natury i Loterie
          </h4>
          <p>
            Natura jest traktowana jako fikcyjny Gracz 0, ktory wykonuje ruchy z obiektywnymi, znanymi prawdopodobienstwami.
            Gdy Natura wykonuje ruch, rezultaty gry staja sie loteriami.
            W grach o wyplatach porzadkowych gracze musza uszeregowac loterie.
            Jesli gracze sa neutralni wobec ryzyka, wartosc loterii jest rowna jej wartosci oczekiwanej $\\mathbb{E}[L] = \\sum p_k x_k$.
          </p>
        </div>

        <!-- ZADANIE 3.14 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyrznione Zadanie 3.14 (Odstraszanie od Wejscia i Nieodwracalne Inwestycje)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 3.E &bull; s. 138</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Tresc Zadania:</strong> Monopolista decyduje, czy zainwestowac w duze moce produkcyjne ($K_H$), czy male ($K_L$).
            Nastepnie pretendent obserwuje te decyzje i wybiera: Wejsc (In) czy Zostac (Out).
            Jesli pretendent wejdzie, firmy graja w jednoczesna podgre cenowa.
            Zadanie dowodzi, ze wczesniejsza nieodwracalna inwestycja w duze moce $K_H$ wiarygodnie obniza koszt krancowy monopolisty w podgrze, sprawiajac ze grozba wojny cenowej staje sie wiarygodna w SPE i skutecznie odstrasza rywala od wejscia!
          </p>
        </div>
      </section>
    """
