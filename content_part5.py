# Part 5: Chapters 13, 14, 15 for Lyceum Game Theory
# Zero em-dashes strictly enforced.

def get_chapter_13():
    return """
      <!-- ROZDZIAŁ 13: INFORMACJA NIEPEŁNA W GRACH STATYCZNYCH -->
      <section id="rozdzial-13" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Część V &bull; Rozdział 13</span>
          <span class="text-xs font-mono text-slate-400">Informacja Niepełna &bull; Strony 471-509</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdział 13: Informacja Niepełna w Grach Statycznych i Transformacja Harsanyiego</h3>

        <!-- 13.1 & 13.2 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            13.1 - 13.2. Sytuacje z Informacją Niepełną i Transformacja Harsanyiego (BNE)
          </h4>
          <p>
            Informacja niepełna zachodzi wtedy, gdy gracze nie posiadają pełnej wiedzy o samych <strong>regułach gry lub funkcjach wypłat rywali</strong> (np. nie znają kosztów krańcowych konkurenta lub prywatnej wyceny licytanta).
            Pionier dyscypliny <strong>John Harsanyi (1967-1968)</strong> dokonał przełomowego odkrycia:
            każdą grę z informacją niepełną można przekształcić w standardową grę ekstensywną o <strong>niedoskonałej informacji</strong> z początkowym ruchem <strong>Natury</strong> (tzw. <strong>Transformacja Harsanyiego</strong>)!
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Struktura Gry Bayesowskiej (Bayesian Game)</span>
            <ul class="text-xs text-slate-600 space-y-1.5 list-disc list-inside">
              <li>Zbiór graczy $I = \\{1, \\dots, n\\}$.</li>
              <li>Zbiory typów graczy $T_i$. Typ $t_i \\in T_i$ koduje prywatną informację gracza $i$ (np. jego koszt lub użyteczność).</li>
              <li>Wspólny rozkład pierwotny Natury $P$ nad profilami typów $T = T_1 \\times \\dots \\times T_n$.</li>
              <li>Strategia czysta gracza $i$ to funkcja $s_i: T_i \\to S_i$ przyporządkowująca akcję <em>każdemu możliwemu typowi</em> tego gracza!</li>
            </ul>
          </div>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Definicja: Bayesowska Równowaga Nasha (Bayesian Nash Equilibrium &bull; BNE)</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              Profil strategii $s^* = (s_1^*, \\dots, s_n^*)$ jest <strong>Bayesowską Równowagą Nasha (BNE)</strong>, jeśli dla każdego gracza $i \\in I$ i dla <strong>każdego typu</strong> $t_i \\in T_i$ akcja $s_i^*(t_i)$ maksymalizuje oczekiwaną wypłatę gracza względem warunkowego rozkładu prawdopodobieństwa o typach rywali $P(t_{-i} | t_i)$.
            </p>
          </div>
          <p class="text-xs text-slate-600">
            <strong>Trzy Perspektywy Czasowe:</strong>
            (1) <em>Ex-ante:</em> przed wylosowaniem typów przez Naturę;
            (2) <em>Interim:</em> gdy gracz zna własny typ $t_i$, lecz nie zna typów rywali;
            (3) <em>Ex-post:</em> gdy wszystkie typy zostały ujawnione. BNE gwarantuje optymalność w ujęciu interim dla każdego typu z osobna!
          </p>
        </div>

        <!-- 13.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            13.3. Aukcja Pierwszej Ceny z Wycenami Ciągłymi (Wyprowadzenie Analityczne)
          </h4>
          <p>
            Rozważmy $n$ licytantów w zapieczętowanej aukcji pierwszej ceny, gdzie wyceny $v_i$ są niezależnymi zmiennymi losowymi o rozkładzie jednostajnym na $[0, 1]$ ($v_i \\sim U[0, 1]$).
            Szukamy symetrycznej, ściśle rosnącej strategii licytacji $b(v)$:
          </p>
          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-2 font-mono text-xs overflow-x-auto">
            <div>Oczekiwany zysk gracza o wycenie $v$ składającego ofertę $b$:</div>
            $$\\Pi(b; v) = (v - b) \\cdot P(\\text{wygrana}) = (v - b) \\cdot [P(b(V_j) < b)]^{n-1} = (v - b) \\cdot [b^{-1}(b)]^{n-1}$$
            <div>Różniczkując względem $b$ i przyrównując do zera dla $b = b(v)$, otrzymujemy równanie różniczkowe:</div>
            $$b'(v) \\cdot v - (n-1)(v - b(v)) = 0 \\implies b^*(v) = \\frac{n-1}{n} \\cdot v$$
          </div>
          <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-blue-800 text-xs block uppercase">Twierdzenie o Równoważności Przychodów (Revenue Equivalence Theorem)</span>
            <p class="text-xs text-blue-950 leading-relaxed">
              Dla dwóch licytantów ($n=2$): w aukcji pierwszej ceny gracze licytują $b^*(v) = v/2$.
              W aukcji drugiej ceny licytują $b^*(v) = v$.
              Mimo całkowicie odmiennych strategii, <strong>oczekiwany przychód sprzedawcy w obu aukcjach jest dokładnie identyczny</strong> i wynosi $\\frac{n-1}{n+1} = \\frac{1}{3}$!
            </p>
          </div>
        </div>

        <!-- ZADANIE 13.8 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyróżnione Zadanie 13.8 (Asymetryczny Duopol Cournota z Prywatnymi Kosztami)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 13.E &bull; s. 493</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Treść Zadania:</strong> Firma 1 ma znany koszt $c_1$. Firma 2 z prawdopodobieństwem $p$ ma wysoki koszt $c_H$, a z prawdopodobieństwem $1-p$ niski koszt $c_L$.
            Zadanie prowadzi przez układy trzech równań reakcji i dowodzi, jak informacja prywatna firmy 2 wpływa na optymalny wolumen produkcji firmy 1.
          </p>
        </div>
      </section>
    """

def get_chapter_14():
    return """
      <!-- ROZDZIAŁ 14: INFORMACJA NIEPEŁNA W GRACH DYNAMICZNYCH -->
      <section id="rozdzial-14" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Część V &bull; Rozdział 14</span>
          <span class="text-xs font-mono text-slate-400">Gry Sygnalizacyjne &bull; Strony 510-556</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdział 14: Informacja Niepełna w Grach Dynamicznych, Gry Sygnalizacyjne i Reputacja</h3>

        <!-- 14.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            14.1. Gry Sygnalizacyjne (Spence 1973) i Kryterium Intuicyjne Cho-Krepsa
          </h4>
          <p>
            W grze sygnalizacyjnej gracz poinformowany (Nadawca / Sender) posiada prywatny typ $\\theta \\in \\Theta$ wybrany przez Naturę.
            Nadawca wysyła sygnał $m \\in M$. Odbiorca (Receiver) obserwuje sygnał $m$ (lecz nie zna typu $\\theta$), aktualizuje przekonania $\\mu(\\theta | m)$ i podejmuje działanie $a \\in A$.
          </p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
              <span class="font-bold text-slate-800 text-xs font-mono uppercase block">Równowaga Rozdzielająca (Separating)</span>
              <p class="text-xs text-slate-600 leading-relaxed">
                Różne typy Nadawcy wybierają różne sygnały ($m(\\theta_1) \\ne m(\\theta_2)$).
                Sygnał w 100% ujawnia typ Odbiorcy. Przekonania a posteriori wynoszą $\\mu(\\theta_1 | m(\\theta_1)) = 1$.
              </p>
            </div>
            <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
              <span class="font-bold text-slate-800 text-xs font-mono uppercase block">Równowaga Zlewająca (Pooling)</span>
              <p class="text-xs text-slate-600 leading-relaxed">
                Wszystkie typy Nadawcy wysyłają dokładnie ten sam sygnał ($m(\\theta_1) = m(\\theta_2) = m^*$).
                Sygnał nie wnosi żadnej nowej informacji, więc przekonania a posteriori są równe rozkładowi początkowemu $\\mu = P$.
              </p>
            </div>
          </div>
          <p>
            <strong>Warunek Pojedynczego Przecięcia (Single-Crossing Property &bull; Spence-Mirrlees):</strong>
            Aby równowaga rozdzielająca była możliwa, koszt wysłania sygnału dla typu gorszego musi być ściśle wyższy niż dla typu lepszego:
            $\\frac{\\partial c}{\\partial e}(\\theta_L) > \\frac{\\partial c}{\\partial e}(\\theta_H)$.
            Dzięki temu pracownik o wysokiej produktywności może uzyskać dyplom uniwersytecki jako wiarygodny sygnał, którego pracownik o niskiej produktywności nie jest w stanie opłacalnie naśladować!
          </p>
          <div class="p-4 bg-purple-50 border border-purple-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-purple-900 text-xs block uppercase">Kryterium Intuicyjne (In-K Cho & David Kreps, 1987 &bull; Gra Beer-Quiche)</span>
            <p class="text-xs text-purple-950 leading-relaxed">
              Wiele równowag zlewających można podtrzymać tylko dzięki "złośliwym", nielogicznym przekonaniom Odbiorcy poza ścieżką gry (np. że każde odstępstwo pochodzi od najgorszego typu).
              Kryterium Intuicyjne nakazuje przypisać prawdopodobieństwo 0 typom, dla których dane odstępstwo przyniosłoby stratę względem wypłaty równowagowej przy każdej możliwej najlepszej odpowiedzi Odbiorcy.
              Kryterium to unikalnie eliminuje sztuczne równowagi zlewające na korzyść efektywnej równowagi rozdzielającej Rileya!
            </p>
          </div>
        </div>

        <!-- 14.2 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            14.2. Rozwiązanie Paradoksu Seltena przez Teorię Reputacji (Kreps-Wilson-Milgrom-Roberts)
          </h4>
          <p>
            W Rozdziale 2 widzieliśmy załamanie się indukcji wstecznej w Paradoksie Sieci Sklepów Seltena: monopolista w każdym mieście ulegał pretendentom.
            W 1982 roku David Kreps, Robert Wilson, Paul Milgrom i John Roberts udowodnili, że <strong>wystarczy mikroskopijna asymetria informacyjna</strong>, aby całkowicie odmienić ten wynik!
          </p>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Model Reputacji (Gang of Four &bull; 1982)</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              Niech pretendenci przypisują nawet nieskończenie małe prawdopodobieństwo $\\epsilon = 0.01$, że monopolista jest "furiatem" (typem irracjonalnym, który czerpie przyjemność z walki).
              Wtedy racjonalny, spokojny monopolista <strong>będzie celowo walczył w początkowych miastach</strong>!
              Ponosząc przejściowy koszt walki, buduje reputację furiata w oczach kolejnych pretendentów, co skutecznie odstrasza ich od wejścia we wszystkich kolejnych rundach aż do samego końca gry!
            </p>
          </div>
        </div>

        <!-- ZADANIE 14.7 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyróżnione Zadanie 14.7 (Ugoda Przedsądowa i Proces Cywilny)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 14.E &bull; s. 538</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Treść Zadania:</strong> Poszkodowany zna prawdę o sile dowodów, a pozwany jej nie zna.
            Poszkodowany proponuje kwotę ugody pozasądowej. Pozwany decyduje: zaakceptować ugodę czy iść do sądu i ponieść koszty procesu.
            Zadanie modeluje kwotę żądania jako sygnał siły materiału dowodowego i wyznacza unikalną równowagę PBE spełniającą Kryterium Intuicyjne.
          </p>
        </div>
      </section>
    """

def get_chapter_15():
    return """
      <!-- ROZDZIAŁ 15: PODEJŚCIE OPARTE NA PRZESTRZENI TYPÓW -->
      <section id="rozdzial-15" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Część V &bull; Rozdział 15</span>
          <span class="text-xs font-mono text-slate-400">Type Spaces vs Kripke &bull; Strony 557-575</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdział 15: Podejście Oparte na Przestrzeni Typów i Most do Struktur Kripkego</h3>

        <!-- 15.1 - 15.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            15.1 - 15.3. Przestrzenie Typów Harsanyiego a Struktury Stanów Kripkego
          </h4>
          <p>
            W teorii Harsanyiego każdy gracz posiada zbiór typów $T_i$.
            Typ $t_i$ określa własną funkcję wypłat $u_i(\\cdot, t_i)$ oraz rozkład prawdopodobieństwa $p_i(t_i) \\in \\Delta(T_{-i})$ nad typami pozostałych graczy.
            Bonanno dowodzi fundamentalnego twierdzenia o <strong>pełnej, dwukierunkowej równoważności</strong> między modelem typów Harsanyiego a modalnymi strukturami stanów Kripkego z Części III:
          </p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
            <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
              <span class="font-bold text-blue-700 text-xs font-mono uppercase block">Algorytm: Ze Stanów do Typów</span>
              <p class="text-xs text-slate-600 leading-relaxed">
                Niech $\\langle \\Omega, (\\mathcal{I}_i), (P_i) \\rangle$ będzie strukturą Kripkego.
                Dla każdego gracza $i$, <strong>każda komórka partycji informacyjnej</strong> $I \\in \\mathcal{I}_i$ staje się pojedynczym typem $t_i$.
                Przekonania typu $t_i$ o typach rywali są wyznaczane przez prawdopodobieństwo warunkowe na komórce $I$.
              </p>
            </div>
            <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
              <span class="font-bold text-blue-700 text-xs font-mono uppercase block">Algorytm: Z Typów do Stanów</span>
              <p class="text-xs text-slate-600 leading-relaxed">
                Mając przestrzenie typów $T_1, \\dots, T_n$, definiujemy zbiór stanów Kripkego jako iloczyn kartezjański: $\\Omega = T_1 \\times \\dots \\times T_n$.
                Partycja informacyjna gracza $i$ łączy stany o identycznej pierwszej współrzędnej: $\\mathcal{I}_i(t_1, \\dots, t_n) = \\{ (t_i, t_{-i}') : t_{-i}' \\in T_{-i} \\}$.
              </p>
            </div>
          </div>
          <p class="text-xs text-slate-600 pt-2">
            <strong>Wartości Współzależne (Interdependent Values &bull; Sekcja 15.3):</strong>
            Bonanno uogólnia tę konstrukcję na sytuacje, w których użyteczność gracza zależy bezpośrednio od informacji posiadanych przez innych graczy: $U_i(s, t_1, \\dots, t_n)$, co modeluje m.in. wspólną wycenę złóż ropy naftowej w aukcjach sejsmicznych.
            W takich grach występuje zjawisko <strong>Klątwy Zwycięzcy (Winner's Curse)</strong>: wygrywający oferent to ten, który najbardziej przecenił wartość złoża!
          </p>
          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-1 text-xs">
            <strong class="text-blue-700 block font-mono">Uniwersalna Przestrzeń Typów (Mertens & Zamir 1985 / Brandenburger & Dekel 1993):</strong>
            Czy przestrzeń typów Harsanyiego może opisać dowolną nieskończoną hierarchię przekonań ("wierzę, że wierzysz, że wierzę...")?
            Twierdzenie Mertensa-Zamira dowodzi istnienia uniwersalnej przestrzeni typów $\\mathcal{T}^*$, która w sposób kanoniczny zawiera wszystkie możliwe spójne hierarchie przekonań wyższego rzędu!
          </div>
        </div>

        <!-- ZADANIE 15.4 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyróżnione Zadanie 15.4 (Pełna Konwersja Dwukierunkowa Typy &harr; Stany)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 15.E &bull; s. 568</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Treść Zadania:</strong> Konstrukcja macierzy przejścia między 6-stanowym modelem Kripkego a 2x3 przestrzenią typów Harsanyiego z weryfikacją zgodności rozkładów brzegowych i warunkowych.
          </p>
        </div>
      </section>
    """
