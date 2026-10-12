# Part 5: Chapters 13, 14, 15 for Lyceum Game Theory
# Zero em-dashes strictly enforced.

def get_chapter_13():
    return """
      <!-- ROZDZIAL 13: INFORMACJA NIEPELNA W GRACH STATYCZNYCH -->
      <section id="rozdzial-13" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Czesc V &bull; Rozdzial 13</span>
          <span class="text-xs font-mono text-slate-400">Informacja Niepelna &bull; Strony 471-509</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdzial 13: Informacja Niepelna w Grach Statycznych i Transformacja Harsanyiego</h3>

        <!-- 13.1 & 13.2 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            13.1 - 13.2. Sytuacje z Informacja Niepelna i Transformacja Harsanyiego (BNE)
          </h4>
          <p>
            Informacja niepelna zachodzi wtedy, gdy gracze nie posiadaja pelnej wiedzy o samych <strong>regulach gry lub funkcjach wyplat rywali</strong> (np. nie znaja kosztow krancowych konkurenta lub prywatnej wyceny licytanta).
            Pionier dyscypliny <strong>John Harsanyi (1967-1968)</strong> dokonal przelomowego odkrycia:
            kazda gre z informacja niepelna mozna przeksztalcic w standardowa gre ekstensywna o <strong>niedokonalej informacji</strong> z poczatkowym ruchem <strong>Natury</strong> (tzw. <strong>Transformacja Harsanyiego</strong>)!
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Struktura Gry Bayesowskiej (Bayesian Game)</span>
            <ul class="text-xs text-slate-600 space-y-1.5 list-disc list-inside">
              <li>Zbior graczy $I = \\{1, \\dots, n\\}$.</li>
              <li>Zbiory typow graczy $T_i$. Typ $t_i \\in T_i$ koduje prywatna informacje gracza $i$ (np. jego koszt lub uzytecznosc).</li>
              <li>Wspolny rozklad pierwotny Natury $P$ nad profilami typow $T = T_1 \\times \\dots \\times T_n$.</li>
              <li>Strategia czysta gracza $i$ to funkcja $s_i: T_i \\to S_i$ przyporzadkowujaca akcje <em>kazdemu mozliwemu typowi</em> tego gracza!</li>
            </ul>
          </div>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Definicja: Bayesowska Rownowaga Nasha (Bayesian Nash Equilibrium &bull; BNE)</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              Profil strategii $s^* = (s_1^*, \\dots, s_n^*)$ jest <strong>Bayesowska Rownowaga Nasha (BNE)</strong>, jesli dla kazdego gracza $i \\in I$ i dla <strong>kazdego typu</strong> $t_i \\in T_i$ akcja $s_i^*(t_i)$ maksymalizuje oczekiwana wyplate gracza wzgledem warunkowego rozkladu prawdopodobienstwa o typach rywali $P(t_{-i} | t_i)$.
            </p>
          </div>
          <p class="text-xs text-slate-600">
            <strong>Trzy Perspektywy Czasowe:</strong>
            (1) <em>Ex-ante:</em> przed wylosowaniem typow przez Nature;
            (2) <em>Interim:</em> gdy gracz zna wlasny typ $t_i$, lecz nie zna typow rywali;
            (3) <em>Ex-post:</em> gdy wszystkie typy zostaly ujawnione. BNE gwarantuje optymalnosc w ujeciu interim dla kazdego typu z osobna!
          </p>
        </div>

        <!-- 13.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            13.3. Aukcja Pierwszej Ceny z Wycenami Ciaglymi (Wyprowadzenie Analityczne)
          </h4>
          <p>
            Rozwazmy $n$ licytantow w zapieczetowanej aukcji pierwszej ceny, gdzie wyceny $v_i$ sa niezaleznymi zmiennymi losowymi o rozkladzie jednostajnym na $[0, 1]$ ($v_i \\sim U[0, 1]$).
            Szukamy symetrycznej, scisle rosnacej strategii licytacji $b(v)$:
          </p>
          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-2 font-mono text-xs overflow-x-auto">
            <div>Oczekiwany zysk gracza o wycenie $v$ skladajacego oferte $b$:</div>
            $$\\Pi(b; v) = (v - b) \\cdot P(\\text{wygrana}) = (v - b) \\cdot [P(b(V_j) < b)]^{n-1} = (v - b) \\cdot [b^{-1}(b)]^{n-1}$$
            <div>Rozniczkujac wzgledem $b$ i przyrownujac do zera dla $b = b(v)$, otrzymujemy rownanie rozniczkowe:</div>
            $$b'(v) \\cdot v - (n-1)(v - b(v)) = 0 \\implies b^*(v) = \\frac{n-1}{n} \\cdot v$$
          </div>
          <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-blue-800 text-xs block uppercase">Twierdzenie o Rownowaznosci Przychodow (Revenue Equivalence Theorem)</span>
            <p class="text-xs text-blue-950 leading-relaxed">
              Dla dwoch licytantow ($n=2$): w aukcji pierwszej ceny gracze licytuja $b^*(v) = v/2$.
              W aukcji drugiej ceny licytuja $b^*(v) = v$.
              Mimo calkowicie odmiennych strategii, <strong>oczekiwany przychod sprzedawcy w obu aukcjach jest dokladnie identyczny</strong> i wynosi $\\frac{n-1}{n+1} = \\frac{1}{3}$!
            </p>
          </div>
        </div>

        <!-- ZADANIE 13.8 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyrznione Zadanie 13.8 (Asymetryczny Duopol Cournota z Prywatnymi Kosztami)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 13.E &bull; s. 493</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Tresc Zadania:</strong> Firma 1 ma znany koszt $c_1$. Firma 2 z prawdopodobienstwem $p$ ma wysoki koszt $c_H$, a z prawdopodobienstwem $1-p$ niski koszt $c_L$.
            Zadanie prowadzi przez uklady trzech rownan reakcji i dowodzi, jak informacja prywatna firmy 2 wplywa na optymalny wolumen produkcji firmy 1.
          </p>
        </div>
      </section>
    """

def get_chapter_14():
    return """
      <!-- ROZDZIAL 14: INFORMACJA NIEPELNA W GRACH DYNAMICZNYCH -->
      <section id="rozdzial-14" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Czesc V &bull; Rozdzial 14</span>
          <span class="text-xs font-mono text-slate-400">Gry Sygnalizacyjne &bull; Strony 510-556</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdzial 14: Informacja Niepelna w Grach Dynamicznych, Gry Sygnalizacyjne i Reputacja</h3>

        <!-- 14.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            14.1. Gry Sygnalizacyjne (Spence 1973) i Kryterium Intuicyjne Cho-Krepsa
          </h4>
          <p>
            W grze sygnalizacyjnej gracz poinformowany (Nadawca / Sender) posiada prywatny typ $\\theta \\in \\Theta$ wybrany przez Nature.
            Nadawca wysyla sygnal $m \\in M$. Odbiorca (Receiver) obserwuje sygnal $m$ (lecz nie zna typu $\\theta$), aktualizuje przekonania $\\mu(\\theta | m)$ i podejmuje dzialanie $a \\in A$.
          </p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
              <span class="font-bold text-slate-800 text-xs font-mono uppercase block">Rownowaga Rozdzielajaca (Separating)</span>
              <p class="text-xs text-slate-600 leading-relaxed">
                Rozne typy Nadawcy wybieraja rozne sygnaly ($m(\\theta_1) \\ne m(\\theta_2)$).
                Sygnal w 100% ujawnia typ Odbiorcy. Przekonania a posteriori wynosza $\\mu(\\theta_1 | m(\\theta_1)) = 1$.
              </p>
            </div>
            <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
              <span class="font-bold text-slate-800 text-xs font-mono uppercase block">Rownowaga Zlewajaca (Pooling)</span>
              <p class="text-xs text-slate-600 leading-relaxed">
                Wszystkie typy Nadawcy wysylaja dokladnie ten sam sygnal ($m(\\theta_1) = m(\\theta_2) = m^*$).
                Sygnal nie wnosi zadnej nowej informacji, wiec przekonania a posteriori sa rowne rozkladowi poczatkowemu $\\mu = P$.
              </p>
            </div>
          </div>
          <p>
            <strong>Warunek Pojedynczego Przeciecia (Single-Crossing Property &bull; Spence-Mirrlees):</strong>
            Aby rownowaga rozdzielajaca byla mozliwa, koszt wyslania sygnalu dla typu gorszego musi byc scisle wyzszy niz dla typu lepszego:
            $\\frac{\\partial c}{\\partial e}(\\theta_L) > \\frac{\\partial c}{\\partial e}(\\theta_H)$.
            Dzieki temu pracownik o wysokiej produktywnosci moze uzyskac dyplom uniwersytecki jako wiarygodny sygnal, ktorego pracownik o niskiej produktywnosci nie jest w stanie oplacalnie nasladowac!
          </p>
          <div class="p-4 bg-purple-50 border border-purple-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-purple-900 text-xs block uppercase">Kryterium Intuicyjne (In-K Cho & David Kreps, 1987 &bull; Gra Beer-Quiche)</span>
            <p class="text-xs text-purple-950 leading-relaxed">
              Wiele rownowag zlewajacych mozna podtrzymac tylko dzieki "zlosliwym", nielogicznym przekonaniom Odbiorcy poza sciezka gry (np. ze kazde odstępstwo pochodzi od najgorszego typu).
              Kryterium Intuicyjne nakazuje przypisac prawdopodobienstwo 0 typom, dla ktorych dane odstepstwo przyniosloby strate wzgledem wyplaty rownowagowej przy kazdej mozliwej najlepszej odpowiedzi Odbiorcy.
              Kryterium to unikalnie eliminuje sztuczne rownowagi zlewajace na korzysc efektywnej rownowagi rozdzielajacej Rileya!
            </p>
          </div>
        </div>

        <!-- 14.2 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            14.2. Rozwiazanie Paradoksu Seltena przez Teorie Reputacji (Kreps-Wilson-Milgrom-Roberts)
          </h4>
          <p>
            W Rozdziale 2 widzielismy zalamanie sie indukcji wstecznej w Paradoksie Sieci Sklepow Seltena: monopolista w kazdym miescie ulegal pretendentom.
            W 1982 roku David Kreps, Robert Wilson, Paul Milgrom i John Roberts udowodnili, ze <strong>wystarczy mikroskopijna asymetria informacyjna</strong>, aby calkowicie odmienic ten wynik!
          </p>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Model Reputacji (Gang of Four &bull; 1982)</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              Niech pretendenci przypisuja nawet nieskonczenie male prawdopodobienstwo $\\epsilon = 0.01$, ze monopolista jest "furiatem" (typem irracjonalnym, ktory czerpie przyjemnosc z walki).
              Wtedy racjonalny, spokojny monopolista <strong>bedzie celowo walczyl w poczatkowych miastach</strong>!
              Ponoszac przejsciowy koszt walki, buduje reputacje furiata w oczach kolejnych pretendentow, co skutecznie odstrasza ich od wejscia we wszystkich kolejnych rundach az do samego konca gry!
            </p>
          </div>
        </div>

        <!-- ZADANIE 14.7 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyrznione Zadanie 14.7 (Ugoda Przedsadowa i Proces Cywilny)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 14.E &bull; s. 538</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Tresc Zadania:</strong> Poszkodowany zna prawde o sile dowodow, a pozwany jej nie zna.
            Poszkodowany proponuje kwote ugody pozasadowej. Pozwany decyduje: zaakceptowac ugodę czy isc do sadu i poniesc koszty procesu.
            Zadanie modeluje kwote zadania jako sygnal sily materialu dowodowego i wyznacza unikalna rownowage PBE spelniajaca Kryterium Intuicyjne.
          </p>
        </div>
      </section>
    """

def get_chapter_15():
    return """
      <!-- ROZDZIAL 15: PODEJSCIE OPARTY NA PRZESTRZENI TYPOW -->
      <section id="rozdzial-15" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Czesc V &bull; Rozdzial 15</span>
          <span class="text-xs font-mono text-slate-400">Type Spaces vs Kripke &bull; Strony 557-575</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdzial 15: Podejscie Oparte na Przestrzeni Typów i Most do Struktur Kripkego</h3>

        <!-- 15.1 - 15.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            15.1 - 15.3. Przestrzenie Typow Harsanyiego a Struktury Stanow Kripkego
          </h4>
          <p>
            W teorii Harsanyiego kazdy gracz posiada zbior typow $T_i$.
            Typ $t_i$ okresla wlasna funkcje wyplat $u_i(\\cdot, t_i)$ oraz rozklad prawdopodobienstwa $p_i(t_i) \\in \\Delta(T_{-i})$ nad typami pozostalych graczy.
            Bonanno dowodzi fundamentalnego twierdzenia o <strong>pelnej, dwukierunkowej rownowaznosci</strong> miedzy modelem typow Harsanyiego a modalnymi strukturami stanow Kripkego z Czesci III:
          </p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
            <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
              <span class="font-bold text-blue-700 text-xs font-mono uppercase block">Algorytm: Ze Stanow do Typow</span>
              <p class="text-xs text-slate-600 leading-relaxed">
                Niech $\\langle \\Omega, (\\mathcal{I}_i), (P_i) \\rangle$ bedzie struktura Kripkego.
                Dla kazdego gracza $i$, <strong>kazda komorka partycji informacyjnej</strong> $I \\in \\mathcal{I}_i$ staje sie pojedynczym typem $t_i$.
                Przekonania typu $t_i$ o typach rywali sa wyznaczane przez prawdopodobienstwo warunkowe na komorce $I$.
              </p>
            </div>
            <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
              <span class="font-bold text-blue-700 text-xs font-mono uppercase block">Algorytm: Z Typow do Stanow</span>
              <p class="text-xs text-slate-600 leading-relaxed">
                Mając przestrzenie typow $T_1, \\dots, T_n$, definiujemy zbior stanow Kripkego jako iloczyn kartezjanski: $\\Omega = T_1 \\times \\dots \\times T_n$.
                Partycja informacyjna gracza $i$ laczy stany o identycznej pierwszej wspolrzednej: $\\mathcal{I}_i(t_1, \\dots, t_n) = \\{ (t_i, t_{-i}') : t_{-i}' \\in T_{-i} \\}$.
              </p>
            </div>
          </div>
          <p class="text-xs text-slate-600 pt-2">
            <strong>Wartosci Wspolzalezne (Interdependent Values &bull; Sekcja 15.3):</strong>
            Bonanno uogolnia te konstrukcje na sytuacje, w ktorych uzytecznosc gracza zależy bezposrednio od informacji posiadanych przez innych graczy: $U_i(s, t_1, \\dots, t_n)$, co modeluje m.in. wspolna wycene zloz ropy naftowej w aukcjach sejsmicznych.
            W takich grach występuje zjawisko <strong>Klatwy Zwyciezcy (Winner's Curse)</strong>: wygrywajacy oferent to ten, ktory najbardziej przecenil wartosc złoża!
          </p>
          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-1 text-xs">
            <strong class="text-blue-700 block font-mono">Uniwersalna Przestrzen Typow (Mertens & Zamir 1985 / Brandenburger & Dekel 1993):</strong>
            Czy przestrzen typow Harsanyiego moze opisac dowolna nieskonczona hierarchie przekonan ("wierze, ze wierzysz, ze wierze...")?
            Twierdzenie Mertensa-Zamira dowodzi istnienia uniwersalnej przestrzeni typow $\\mathcal{T}^*$, ktora w sposob kanoniczny zawiera wszystkie mozliwe spojne hierarchie przekonan wyzszego rzedu!
          </div>
        </div>

        <!-- ZADANIE 15.4 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyrznione Zadanie 15.4 (Pelna Konwersja Dwukierunkowa Typy &harr; Stany)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 15.E &bull; s. 568</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Tresc Zadania:</strong> Konstrukcja macierzy przejscia miedzy 6-stanowym modelem Kripkego a 2x3 przestrzenia typow Harsanyiego z weryfikacja zgodnosci rozkladow brzegowych i warunkowych.
          </p>
        </div>
      </section>
    """
