# Part 1: Chapters 0, 1, 2, 3 for Lyceum Game Theory
# Zero em-dashes strictly enforced.

def get_chapter_0():
    return """
      <!-- ROZDZIAŁ 0: WPROWADZENIE I GENEZA TEORII GIER -->
      <section id="rozdzial-0" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Wprowadzenie</span>
          <span class="text-xs font-mono text-slate-400">Giacomo Bonanno &bull; Rozdział 0 &bull; Strony 1-5</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdział 0: Geneza, Metodologia i Paradygmat Homo Rationalis</h3>

        <!-- 0.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            0.1. Rys Historyczny i Cztery Fale Nagród Nobla
          </h4>
          <p>
            Teoria gier powstała jako ścisły dział matematyki badający interaktywne sytuacje decyzyjne, w których wynik zależy od jednoczesnych lub sekwencyjnych działań wielu niezależnych podmiotów (zwanych graczami).
            Pionierami dyscypliny w pierwszej połowie XX wieku byli <strong>Ernst Zermelo (1913)</strong>, który sformułował pierwsze twierdzenie o determinizmie w grach takich jak szachy, oraz <strong>John von Neumann (1928)</strong>, autor twierdzenia o minimaksie w grach dwuosobowych o sumie zerowej.
          </p>
          <p>
            Punktem zwrotnym stała się fundamentalna monografia Johna von Neumanna i Oskara Morgensterna z 1944 roku pt. <em>Theory of Games and Economic Behavior</em>.
            Kolejna dekada przyniosła rewolucyjne odkrycia <strong>Johna Nasha (1950, 1951)</strong> (pojęcie równowagi w strategiach mieszanych), <strong>Lloyda Shapleya (1953)</strong> (wartość Shapleya w grach kooperacyjnych) oraz <strong>Harolda Kuhna (1953)</strong> (postać ekstensywna i strategie behawioralne).
          </p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
            <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
              <span class="text-xs font-mono font-bold text-blue-700 block uppercase">Fale Nagród Nobla w Dziedzinie Teorii Gier:</span>
              <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside">
                <li><strong>1994:</strong> John Nash, John Harsanyi, Reinhard Selten (za analizę równowag w teorii gier niekooperacyjnych).</li>
                <li><strong>2005:</strong> Robert Aumann, Thomas Schelling (za pogłębienie rozumienia konfliktu i kooperacji).</li>
                <li><strong>2007:</strong> Leonid Hurwicz, Eric Maskin, Roger Myerson (za fundamenty teorii projektowania mechanizmów - Mechanism Design).</li>
                <li><strong>2012:</strong> Lloyd Shapley, Alvin Roth (za teorię stabilnych alokacji i projektowanie rynków).</li>
              </ul>
            </div>
            <div class="p-4 bg-blue-50/60 border border-blue-200 rounded-xl space-y-2">
              <span class="text-xs font-mono font-bold text-blue-900 block uppercase">Praktyczny Triumf: Aukcje FCC (1994)</span>
              <p class="text-xs text-blue-950 leading-relaxed">
                W 1994 roku Federalna Komisja Łączności USA (FCC) użyła zaawansowanej teorii gier do zaprojektowania równoczesnej aukcji wielorundowej pasma radiowego o wartości 7 miliardów dolarów.
                Aukcja ta zapobiegła spekulacjom, wyeliminowała zjawisko "klątwy zwycięzcy" (Winner's Curse) i stała się światowym standardem alokacji częstotliwości telekomunikacyjnych.
              </p>
            </div>
          </div>
        </div>

        <!-- 0.2 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            0.2. Aksjomat Homo Rationalis i Granice Racjonalności
          </h4>
          <p>
            Tradycyjna teoria gier opiera się na precyzyjnie zdefiniowanym modelu decydenta. Jak zauważa laureat Nagrody Nobla Robert Aumann:
          </p>
          <div class="p-4 bg-slate-50 border-l-4 border-blue-600 rounded-r-xl text-xs sm:text-sm text-slate-800 leading-relaxed italic">
            "Mówiąc krótko, teoria gier i ekonomia zajmują się interaktywnym zachowaniem <em>Homo rationalis</em> - człowieka racjonalnego.
            Homo rationalis to gatunek, który zawsze działa zarówno celowo, jak i logicznie, posiada ściśle określone cele, jest motywowany wyłącznie pragnieniem
            zbliżenia się do tych celów tak bardzo, jak to możliwe, i ma zdolności kalkulacyjne wymagane, aby to uczynić."
            <div class="text-right text-xs font-sans font-semibold text-slate-500 not-italic mt-1">- Robert Aumann (1985, s. 35)</div>
          </div>
          <p>
            W podręczniku Giacomo Bonanno przyjmuje ten klasyczny paradygmat: gracze są w pełni inteligentni, zdolni do bezbłędnej dedukcji, a także świadomi, że ich partnerzy i rywale są również racjonalni.
            Odróżnia to tradycyjną teorię gier od biologii ewolucyjnej (gdzie "graczami" są bezmyślne organizmy podlegające doborowi naturalnemu) oraz behawioralnej teorii gier (analizującej poznawcze ograniczenia i błędy heurystyczne ludzi).
          </p>
        </div>

        <!-- 0.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            0.3. Pięć Fundamentalnych Dychotomii Podziału Gier
          </h4>
          <p>
            Teoria gier dzieli interakcje decyzyjne według pięciu fundamentalnych wymiarów formalnych:
          </p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
            <div class="p-3 bg-white border border-slate-200 rounded-xl space-y-1 shadow-sm">
              <strong class="text-blue-700 block font-mono">1. Gry Kooperacyjne vs Niekooperacyjne</strong>
              <p class="text-slate-600">
                W grach kooperacyjnych gracze mogą zawierać wiążące prawnie porozumienia (binding agreements) egzekwowane przez sąd lub arbitra.
                W grach niekooperacyjnych (którym poświęcony jest ten podręcznik) porozumienia muszą być <strong>samoegzekwujące się (self-enforcing)</strong>.
              </p>
            </div>
            <div class="p-3 bg-white border border-slate-200 rounded-xl space-y-1 shadow-sm">
              <strong class="text-blue-700 block font-mono">2. Postać Strategiczna vs Postać Ekstensywna</strong>
              <p class="text-slate-600">
                Postać strategiczna (macierzowa) opisuje gry jednoczesne, gdzie gracze wybierają strategie w izolacji.
                Postać ekstensywna (drzewo decyzyjne) uwzględnia upływ czasu, kolejność posunięć i dynamiczną strukturę informacji.
              </p>
            </div>
            <div class="p-3 bg-white border border-slate-200 rounded-xl space-y-1 shadow-sm">
              <strong class="text-blue-700 block font-mono">3. Informacja Doskonała vs Niedoskonałość Informacji</strong>
              <p class="text-slate-600">
                Informacja jest doskonała, gdy w każdym momencie gracz podejmujący decyzję dokładnie zna całą przeszłą historię ruchów.
                Informacja jest niedoskonała, gdy pewne węzły decyzyjne tworzą nieodróżnialne zbiory informacyjne (np. poker, ruchy równoczesne).
              </p>
            </div>
            <div class="p-3 bg-white border border-slate-200 rounded-xl space-y-1 shadow-sm">
              <strong class="text-blue-700 block font-mono">4. Informacja Pełna vs Informacja Niepełna</strong>
              <p class="text-slate-600">
                Informacja jest pełna, gdy reguły gry i funkcje wypłat są wspólną wiedzą wszystkich graczy.
                Informacja jest niepełna, gdy gracze nie znają funkcji wypłat rywali (modele Harsanyiego z typami graczy i ruchem Natury).
              </p>
            </div>
            <div class="p-3 bg-white border border-slate-200 rounded-xl space-y-1 shadow-sm md:col-span-2">
              <strong class="text-blue-700 block font-mono">5. Wypłaty Porządkowe (Ordinal) vs Wypłaty Kardynalne (Cardinal)</strong>
              <p class="text-slate-600">
                Wypłaty porządkowe (Część I) wymagają wyłącznie uszeregowania rezultatów (wystarczy wiedzieć co gracz woli bardziej).
                Wypłaty kardynalne (Części II-V) opierają się na teorii oczekiwanej użyteczności von Neumanna-Morgensterna, umożliwiając analizę ryzyka, loterii i strategii mieszanych.
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
            Tradycyjna literatura pytała: <em>"Jaka jest równowaga tej gry?"</em>.
            Nowoczesne podejście epistemiczne (rozwijane w Częściach III i IV przez Aumanna, Brandenburgera, Dekela oraz Giacomo Bonanno) stawia głębsze pytanie:
            <strong>"Co gracze muszą wiedzieć i w co muszą wierzyć na temat gry oraz na temat wzajemnej racjonalności, aby uzasadnić wybór konkretnej strategii?"</strong>.
            To właśnie ten epistemologiczny rygor wyznacza unikalny charakter całego podręcznika Bonanno.
          </p>
        </div>
      </section>
    """

def get_chapter_1():
    return """
      <!-- ROZDZIAŁ 1: GRY PORZĄDKOWE W POSTACI STRATEGICZNEJ -->
      <section id="rozdzial-1" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Część I &bull; Rozdział 1</span>
          <span class="text-xs font-mono text-slate-400">Gry w Postaci Strategicznej &bull; Strony 6-64</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdział 1: Gry Porządkowe w Postaci Strategicznej</h3>

        <!-- 1.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            1.1. Ramki Gry a Gry (Game Frames and Games)
          </h4>
          <p>
            W podręczniku Bonanno kluczowym rozróżnieniem jest separacja fizycznej struktury decyzyjnej od psychologicznych motywacji decydentów.
            Formalnie sytuację interaktywną bez przypisania preferencji określamy jako <strong>ramkę gry w postaci strategicznej (Definicja 1.1)</strong>:
          </p>
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 font-mono text-xs overflow-x-auto">
            $$\\mathcal{F} = \\langle I, (S_1, S_2, \\dots, S_n), O, f \\rangle$$
          </div>
          <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside">
            <li>$I = \\{1, 2, \\dots, n\\}$ to skończony zbiór graczy ($n \\ge 2$).</li>
            <li>$S_i$ to zbiór strategii dostępnych dla gracza $i$. Zbiór profili strategii to iloczyn kartezjański $S = S_1 \\times S_2 \\times \\dots \\times S_n$.</li>
            <li>$O$ to zbiór możliwych fizycznych rezultatów gry (outcomes).</li>
            <li>$f: S \\to O$ to funkcja rezultatu przyporządkowująca każdemu profilowi strategii $s = (s_1, \\dots, s_n)$ konkretny wynik fizyczny $f(s) \\in O$.</li>
          </ul>
          <p>
            Aby przekształcić ramkę gry w pełną grę, każdemu graczowi $i \\in I$ przypisujemy relację preferencji $\\succsim_i$ nad zbiorem rezultatów $O$.
            Relacja $\\succsim_i$ musi spełniać dwa aksjomaty racjonalności:
          </p>
          <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside">
            <li><strong>Zupełność (Completeness):</strong> $\\forall o_1, o_2 \\in O: o_1 \\succsim_i o_2 \\lor o_2 \\succsim_i o_1$.</li>
            <li><strong>Przechodniość (Transitivity):</strong> $\\forall o_1, o_2, o_3 \\in O: (o_1 \\succsim_i o_2 \\land o_2 \\succsim_i o_3) \\implies o_1 \\succsim_i o_3$.</li>
          </ul>
          <p>
            Relacja ścisłej preferencji definiowana jest jako $o_1 \\succ_i o_2 \\iff (o_1 \\succsim_i o_2 \\land \\neg(o_2 \\succsim_i o_1))$, zaś relacja obojętności jako $o_1 \\sim_i o_2 \\iff (o_1 \\succsim_i o_2 \\land o_2 \\succsim_i o_1)$.
            Funkcja $U_i: O \\to \\mathbb{R}$ jest <strong>porządkową funkcją użyteczności (Definicja 1.2)</strong>, gdy dla dowolnych $o_1, o_2 \\in O$:
          </p>
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 font-mono text-xs overflow-x-auto">
            $$U_i(o_1) > U_i(o_2) \\iff o_1 \\succ_i o_2 \\quad \\text{oraz} \\quad U_i(o_1) = U_i(o_2) \\iff o_1 \\sim_i o_2$$
          </div>
          <p>
            <strong>Przykład: Teleturniej "Split or Steal" (Golden Balls):</strong> Dwóch uczestników (Sarah i Stephen) wybiera niezależnie "Podziel" (Split) lub "Ukradnij" (Steal). Pula wynosi 100 000 GBP.
            Rezultaty fizyczne: $o_1$ (oboje dzielą: po 50k), $o_2$ (Sarah kradnie, Stephen dzieli: 100k dla Sarah, 0 dla Stephena), $o_3$ (Sarah dzieli, Stephen kradnie: 0 dla Sarah, 100k dla Stephena), $o_4$ (oboje kradną: 0 dla obu).
            Jeśli Sarah jest chciwa i samolubna, jej użyteczności to $U(o_2)=4 > U(o_1)=3 > U(o_4)=2 > U(o_3)=1$. Wtedy Steal jest dla niej strategią ściśle dominującą.
            Jeśli jednak Sarah ceni sprawiedliwość i nienawidzi kradzieży, jej ranking to $U(o_1)=4 > U(o_2)=3 > U(o_4)=2 > U(o_3)=1$. Ta sama ramka gry, lecz zupełnie inna gra decyzyjna!
          </p>
        </div>

        <!-- 1.2 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            1.2. Dominacja Ścisła i Słaba (Strict and Weak Dominance)
          </h4>
          <p>
            Niech $S_{-i} = \\times_{j \\ne i} S_j$ oznacza zbiór profili strategii rywali gracza $i$. Wektor wypłat gracza $i$ przy wyborze $s_i \\in S_i$ i reakcji rywali $s_{-i} \\in S_{-i}$ to $\\pi_i(s_i, s_{-i}) = U_i(f(s_i, s_{-i}))$.
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 1.4: Relacje Dominacji</span>
            <ul class="text-xs text-slate-700 space-y-1.5 list-disc list-inside">
              <li>
                <strong>Ścisła dominacja:</strong> Strategia $a \\in S_i$ <em>ściśle dominuje</em> strategię $b \\in S_i$, gdy:
                $$\\forall s_{-i} \\in S_{-i}: \\pi_i(a, s_{-i}) > \\pi_i(b, s_{-i})$$
              </li>
              <li>
                <strong>Słaba dominacja:</strong> Strategia $a \\in S_i$ <em>słabo dominuje</em> strategię $b \\in S_i$, gdy:
                $$\\forall s_{-i} \\in S_{-i}: \\pi_i(a, s_{-i}) \\ge \\pi_i(b, s_{-i}) \\quad \\text{oraz} \\quad \\exists \\bar{s}_{-i} \\in S_{-i}: \\pi_i(a, \\bar{s}_{-i}) > \\pi_i(b, \\bar{s}_{-i})$$
              </li>
              <li>
                <strong>Równoważność:</strong> Strategie $a, b$ są równoważne, gdy $\\forall s_{-i} \\in S_{-i}: \\pi_i(a, s_{-i}) = \\pi_i(b, s_{-i})$.
              </li>
            </ul>
          </div>
          <p>
            <strong>Własność Unikalności:</strong> Strategia ściśle dominująca jest unikalna: żaden gracz nie może posiadać dwóch różnych strategii ściśle dominujących.
            Natomiast gracz może mieć wiele strategii słabo dominujących, pod warunkiem że są one sobie wzajemnie równoważne.
          </p>
          <p>
            <strong>Dylemat Więźnia i Efektywność Pareto (Definicja 1.7):</strong> Rezultat $o$ jest <em>ściśle lepszy w sensie Pareto</em> od $o'$, jeśli $\\forall i \\in I: o \\succ_i o'$.
            W słynnej grze Doug i Ed obaj podejrzani mają ściśle dominującą strategię "Zeznawaj" (Confess). Profil (Zeznawaj, Zeznawaj) jest jedynym profilem strategii dominujących, lecz prowadzi do rezultatu (5 lat, 5 lat), który jest ściśle gorszy w sensie Pareto od profilu (Milcz, Milcz) dającego (1 rok, 1 rok). Indywidualna racjonalność stoi w bezpośrednim konflikcie ze społeczną efektywnością!
          </p>
        </div>

        <!-- 1.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            1.3. Aukcja Drugiej Ceny Vickreya (Twierdzenie 1.1)
          </h4>
          <p>
            W zapieczętowanej aukcji drugiej ceny $n$ licytantów składa jednocześnie tajne oferty $b_i \\ge 0$. Przedmiot trafia do gracza z najwyższą ofertą $b^* = \\max_j b_j$, który płaci cenę równą <strong>drugiej najwyższej ofercie</strong> $p = \\max_{j \\ne i^*} b_j$. W przypadku remisu przedmiot jest losowany.
          </p>
          <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-blue-800 text-xs block uppercase">Twierdzenie 1.1 (William Vickrey, 1961)</span>
            <p class="text-xs text-blue-950 leading-relaxed">
              Niech gracz $i$ posiada prywatną wycenę przedmiotu $v_i > 0$. Jeśli gracz $i$ jest samolubny i chciwy (jego wypłata wynosi $v_i - p$ przy wygranej za cenę $p$ oraz $0$ przy przegranej),
              to zgłoszenie oferty dokładnie równej prawdziwej wycenie:
              $$b_i = v_i$$
              jest <strong>strategią słabo dominującą</strong>.
            </p>
            <details class="text-xs bg-white p-3 rounded-lg border border-blue-100 cursor-pointer">
              <summary class="font-bold text-blue-700 select-none">Rozwiń Ścisły Dowód Twierdzenia 1.1 (Appendix 1.A Bonanno)</summary>
              <div class="mt-2 text-slate-700 space-y-2 leading-relaxed">
                <p>
                  Niech $M = \\max_{j \\ne i} b_j$ oznacza najwyższą ofertę złożoną przez rywali gracza $i$. Gracz $i$ nie zna $M$, lecz rozpatrzmy dwa wyczerpujące przypadki:
                </p>
                <p>
                  <strong>Przypadek 1: $M \\le v_i$.</strong> Jeśli gracz zaoferuje $b_i = v_i$, wygrywa aukcję i płaci cenę $M$, uzyskując wypłatę $\\pi_i = v_i - M \\ge 0$.
                  Jakakolwiek inna oferta $b_i' > M$ również wygrywa i płaci dokładnie tę samą cenę $M$, dając tę samą wypłatę.
                  Oferta $b_i' < M$ sprawia, że gracz przegrywa aukcję i otrzymuje wypłatę $0 \\le v_i - M$.
                  Zatem żadna alternatywna oferta nie może dać ściśle wyższej wypłaty niż $b_i = v_i$.
                </p>
                <p>
                  <strong>Przypadek 2: $M > v_i$.</strong> Jeśli gracz zaoferuje $b_i = v_i$, przegrywa aukcję i płaci $0$, uzyskując wypłatę $\\pi_i = 0$.
                  Jakakolwiek oferta $b_i' \\le M$ również przegrywa i daje $0$.
                  Aby wygrać aukcję, gracz musiałby zaoferować $b_i' > M$. Wtedy jednak płaci cenę $M$, co daje wypłatę $v_i - M < 0$ (ścisłą stratę!).
                  Zatem licytowanie $v_i$ daje wypłatę co najmniej tak wysoką jak każda inna oferta, a dla pewnych stanów rywali ściśle wyższą.
                  W konsekwencji oferta $b_i = v_i$ jest słabo dominująca. $\\blacksquare$
                </p>
              </div>
            </details>
          </div>
          <p class="text-xs text-slate-600">
            <strong>Kontrast z aukcją pierwszej ceny:</strong> W aukcji pierwszej ceny zwycięzca płaci własną ofertę $b_i$. Oferta $b_i = v_i$ gwarantuje zysk $v_i - v_i = 0$.
            Gracz musi zatem strategicznie zaniżać ofertę ($b_i < v_i$), aby uzyskać dodatni zysk. W aukcji pierwszej ceny prawdomówność nigdy nie jest strategią dominującą!
          </p>
        </div>

        <!-- 1.4 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            1.4. Mechanizm Pivotowy Clarke'a (Twierdzenie 1.2)
          </h4>
          <p>
            Wyobraźmy sobie społeczność decydującą o budowie dobra publicznego (mostu, parku, biblioteki) o koszcie $C > 0$. Każdy członek ponosi z góry określony koszt $c_i > 0$ (gdzie $\\sum c_i = C$).
            Prywatna korzyść każdego gracza wynosi $v_i$. Projekt jest efektywny w sensie Pareto wtedy i tylko wtedy, gdy $\\sum v_i > C$, czyli $\\sum (v_i - c_i) > 0$.
            Ponieważ wyceny są prywatną informacją, gracze mają pokusę zniekształcania deklaracji (free-riding).
          </p>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Twierdzenie 1.2 (Edward Clarke, 1971 / Theodore Groves, 1973)</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              W mechanizmie pivotowym każdy gracz deklaruje wartość $w_i$. Projekt jest realizowany, gdy $\\sum w_j > C$.
              Gracz $i$ jest <strong>pivotowy (pivotal)</strong>, jeśli jego obecność zmienia decyzję społeczną, tj. $\\text{znak}\\left(\\sum_{j=1}^n (w_j - c_j)\\right) \\ne \\text{znak}\\left(\\sum_{j \\ne i} (w_j - c_j)\\right)$.
              Gracz pivotowy płaci podatek w wysokości straty narzuconej reszcie społeczeństwa:
              $$t_i = \\left| \\sum_{j \\ne i} (w_j - c_j) \\right|$$
              Gracz niebędący pivotowym płaci podatek $t_i = 0$.
              Dla każdego gracza prawdomówne zgłoszenie $w_i = v_i$ jest <strong>strategią słabo dominującą</strong>!
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
            Jeśli strategia jest ściśle zdominowana, żaden racjonalny gracz jej nie wybierze. Co więcej, jeśli fakt racjonalności jest wiedzą powszechną, możemy usunąć strategie zdominowane wszystkich graczy, uzyskując zredukowaną grę, i powtórzyć tę procedurę w kolejnych rundach.
          </p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
              <span class="font-bold text-slate-800 text-xs font-mono uppercase block">IDSDS (Strict Dominance)</span>
              <p class="text-xs text-slate-600 leading-relaxed">
                Iterowana eliminacja strategii ściśle zdominowanych generuje zstępujący ciąg gier $G = G^0 \\supset G^1 \\supset \\dots \\supset G^\\infty$.
                <strong>Kluczowe Twierdzenie:</strong> W każdej skończonej grze porządek eliminacji w IDSDS jest <em>całkowicie nieistotny</em>.
                Niezależnie od tego, czy usuwamy strategie jeden po drugim, czy symetrycznie, zbiór końcowy $G^\\infty$ jest identyczny!
              </p>
            </div>
            <div class="p-4 bg-amber-50/70 border border-amber-200 rounded-xl space-y-2">
              <span class="font-bold text-amber-900 text-xs font-mono uppercase block">IDWDS (Weak Dominance) &bull; Pułapka Kolejności</span>
              <p class="text-xs text-amber-950 leading-relaxed">
                Iterowana eliminacja strategii <strong>słabo</strong> zdominowanych zależy od kolejności!
                Jak dowodzi Bonanno w Uwadze 1.6, usunięcie strategii słabo zdominowanej w jednym kroku może zapobiec eliminacji innej strategii w kolejnym.
                Dlatego konwencja Bonanno nakazuje w każdym kroku usuwać <em>jednocześnie wszystkie</em> strategie słabo zdominowane.
              </p>
            </div>
          </div>
        </div>

        <!-- 1.6 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            1.6. Równowaga Nasha i Cztery Interpretacje Filozoficzne
          </h4>
          <p>
            Równowaga Nasha stanowi centralne pojęcie teorii gier niekooperacyjnych:
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 1.9 &bull; Równowaga Nasha w Postaci Strategicznej</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              Profil strategii $s^* = (s_1^*, s_2^*, \\dots, s_n^*) \\in S$ jest <strong>równowagą Nasha</strong>, gdy dla każdego gracza $i \\in I$ i każdej alternatywnej strategii $s_i \\in S_i$:
              $$\\pi_i(s_i^*, s_{-i}^*) \\ge \\pi_i(s_i, s_{-i}^*)$$
            </p>
          </div>
          <p>
            Równowaga Nasha to punkt stały korespondencji najlepszych odpowiedzi: $s^* \\in \\times_{i=1}^n BR_i(s_{-i}^*)$, gdzie $BR_i(s_{-i}) = \\arg\\max_{s_i} \\pi_i(s_i, s_{-i})$.
            Bonanno wyróżnia cztery główne interpretacje:
          </p>
          <ol class="text-xs text-slate-600 space-y-1 list-decimal list-inside pl-2">
            <li><strong>Punkt centralny (Focal Point / Schelling):</strong> Oczywiste rozwiązanie wyznaczone przez kulturę lub kontekst.</li>
            <li><strong>Samoegzekwujące się porozumienie:</strong> Gdyby gracze mogli się spotkać przed grą i ustalić strategie bez prawa do podpisania umowy, dotrzymają słowa wtedy i tylko wtedy, gdy układ tworzy równowagę Nasha!</li>
            <li><strong>Stabilna konwencja społeczna:</strong> Np. zasada ruchu prawostronnego.</li>
            <li><strong>Stan stacjonarny uczenia się / ewolucji:</strong> Do którego zbiegają powtarzane interakcje populacyjne.</li>
          </ol>
        </div>

        <!-- 1.7 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            1.7. Gry z Nieskończonymi Zbiorami Strategii: Duopol Cournota
          </h4>
          <p>
            Gdy zbiory strategii są ciągłe (np. poziomy produkcji $q_i \\ge 0$), równowagę wyznaczamy za pomocą rachunku różniczkowego.
            W modelu <strong>duopolu Cournota (1838)</strong> dwie firmy wybierają jednocześnie wielkości produkcji $q_1, q_2$. Odwrotna funkcja popytu wynosi $P(Q) = a - b(q_1 + q_2)$ dla $Q < a/b$, a koszt krańcowy każdej firmy wynosi $c$ ($a > c > 0$).
          </p>
          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-2 font-mono text-xs overflow-x-auto">
            <div>Zysk Firmy 1: $\\pi_1(q_1, q_2) = (a - b q_1 - b q_2 - c) q_1$</div>
            <div>Warunek pierwszego rzędu (FOC): $\\frac{\\partial \\pi_1}{\\partial q_1} = a - c - 2b q_1 - b q_2 = 0$</div>
            <div>Krzywa reakcji Firmy 1: $R_1(q_2) = \\frac{a - c - b q_2}{2b}$</div>
          </div>
          <p>
            Rozwiązując symetryczny układ dwóch równań reakcji ($q_1 = R_1(q_2)$, $q_2 = R_2(q_1)$), otrzymujemy unikalną równowagę Nasha-Cournota:
          </p>
          <div class="p-3 bg-emerald-50 border border-emerald-200 rounded-xl font-mono text-xs text-emerald-950 overflow-x-auto">
            $$q_1^* = q_2^* = \\frac{a - c}{3b}, \\quad Q^* = \\frac{2(a - c)}{3b}, \\quad P^* = \\frac{a + 2c}{3}, \\quad \\pi_1^* = \\pi_2^* = \\frac{(a - c)^2}{9b}$$
          </div>
          <p class="text-xs text-slate-600">
            Warto zauważyć, że łączna produkcja $Q^* = \\frac{2}{3} \\frac{a-c}{b}$ leży ściśle pomiędzy monopolem ($Q_M = \\frac{1}{2} \\frac{a-c}{b}$) a doskonałą konkurencją ($Q_C = \\frac{a-c}{b}$).
          </p>
        </div>

        <!-- ZADANIE 1.23 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyróżnione Zadanie 1.23 z Odpowiedziami (Zanieczyszczenie Rzeki i Reguła Sędziego Posnera)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 1.E &bull; s. 49</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Treść Zadania:</strong> Zakład chemiczny Mondevil generuje zysk $\\Pi > 0$, lecz zanieczyszcza rzekę Sacramento, przynosząc szkodę rybakom w wysokości $L > 0$.
            Sędzia Richard Posner stosuje regułę: obie strony składają w sądzie jednocześnie deklaracje $x \\ge 0$ (Mondevil) oraz $y \\ge 0$ (rybacy).
            Jeśli $y > x$, sąd zamyka fabrykę (wypłaty: 0 dla fabryki, 0 dla rybaków).
            Jeśli $x \\ge y$, fabryka działa, lecz musi wypłacić rybakom odszkodowanie $y$ (wypłata fabryki $\\Pi - y$, wypłata rybaków $y - L$).
          </p>
          <details class="text-xs bg-white p-3 rounded-lg border border-slate-200 cursor-pointer">
            <summary class="font-bold text-slate-800 select-none">Pokaż Pełne Rozwiązanie Krok po Kroku (Appendix 1.S Bonanno)</summary>
            <div class="mt-2 text-slate-700 space-y-2 leading-relaxed">
              <p>
                <strong>Krok 1: Analiza fabryki Mondevil.</strong> Niech rybacy zadeklarują $y$.
                Jeśli $x < y$, zysk wynosi 0. Jeśli $x \\ge y$, zysk wynosi $\\Pi - y$.
                Deklaracja $x = \\Pi$ gwarantuje, że fabryka działa wtedy i tylko wtedy, gdy $\\Pi \\ge y$ (czyli gdy jej zysk netto jest nieujemny).
                Gdyby zadeklarowała $x > \\Pi$, ryzykowałaby działanie przy $y > \\Pi$, co przyniosłoby stratę netto.
                Gdyby zadeklarowała $x < \\Pi$, mogłaby zostać zamknięta przy $\\Pi > y > x$, tracąc zysk $\\Pi - y > 0$.
                Zatem dla fabryki deklaracja $x = \\Pi$ jest <strong>strategią słabo dominującą</strong>!
              </p>
              <p>
                <strong>Krok 2: Analiza rybaków.</strong> Wiedząc, że fabryka wybierze $x = \\Pi$, rybacy wybierają $y$:
                Jeśli $\\Pi > L$, fabryka przynosi większą wartość niż strata. Rybacy mogą zadeklarować $y = \\Pi$, otrzymując odszkodowanie $\\Pi$ i zysk netto $\\Pi - L > 0$.
                Jeśli $L > \\Pi$, strata przewyższa zysk fabryki. Wtedy każde $y > \\Pi$ zamyka fabrykę, chroniąc rybaków przed stratą $L - \\Pi > 0$.
              </p>
              <p>
                <strong>Wniosek ekonomiczny:</strong> Mechanizm Posnera zawsze wymusza wynik efektywny w sensie Pareto (Coase Theorem): fabryka działa, gdy $\\Pi > L$, a zostaje zamknięta, gdy $L > \\Pi$!
              </p>
            </div>
          </details>
        </div>
      </section>
    """

def get_chapter_2():
    return """
      <!-- ROZDZIAŁ 2: DYNAMICZNE GRY O DOSKONAŁEJ INFORMACJI -->
      <section id="rozdzial-2" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Część I &bull; Rozdział 2</span>
          <span class="text-xs font-mono text-slate-400">Gry Dynamiczne &bull; Strony 65-106</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdział 2: Dynamiczne Gry o Doskonałej Informacji</h3>

        <!-- 2.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            2.1. Drzewa Gry, Ramki Ekstensywne i Gry o Doskonałej Informacji
          </h4>
          <p>
            Gra w postaci ekstensywnej modeluje kolejność zdarzeń w czasie za pomocą skierowanego drzewa matematycznego $T = (V, E)$.
            Drzewo posiada unikalny <strong>korzeń (root)</strong> $r \\in V$ o stopniu wejściowym zero.
            Wierzchołki dzielą się na <strong>węzły decyzyjne</strong> $D$ oraz <strong>węzły końcowe (terminal nodes)</strong> $Z = V \\setminus D$.
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 2.1 &bull; Gra Ekstensywna o Doskonałej Informacji</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              Struktura $\\Gamma = \\langle T, I, \\iota, O, g, (\\succsim_i)_{i \\in I} \\rangle$, gdzie:
            </p>
            <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside">
              <li>$T$ to drzewo ukorzenione.</li>
              <li>$\\iota: D \\to I$ to funkcja przypisania decydentów, określająca który gracz podejmuje decyzję w węźle $x \\in D$.</li>
              <li>W każdym węźle $x \\in D$ krawędzie wychodzące odpowiadają akcjom ze zbioru $A(x)$.</li>
              <li>$g: Z \\to O$ przypisuje każdemu węzłowi końcowemu fizyczny rezultat gry.</li>
              <li>$\\succsim_i$ to relacje preferencji graczy nad rezultatami $O$.</li>
            </ul>
          </div>
          <p>
            Cechą dystynktywną gier o <strong>doskonałej informacji</strong> jest fakt, że każdy węzeł decyzyjny stanowi samodzielny, jednoelementowy zbiór informacyjny.
            W każdym momencie gry gracz dokładnie wie, w którym węźle drzewa się znajduje i jakie ruchy zostały wykonane wcześniej.
          </p>
        </div>

        <!-- 2.2 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            2.2. Algorytm Indukcji Wstecznej (Backward Induction)
          </h4>
          <p>
            Podstawowym narzędziem rozwiązywania gier o doskonałej informacji jest algorytm indukcji wstecznej, sformalizowany przez Zermelo (1913) i Kuhna (1953):
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Algorytm Indukcji Wstecznej (Definicja 2.3)</span>
            <ol class="text-xs text-slate-700 space-y-1.5 list-decimal list-inside">
              <li>Wybierz węzeł decyzyjny $x \\in D$, którego wszyscy bezpośredni następcy są węzłami końcowymi $z \\in Z$ z przypisanymi wypłatami.</li>
              <li>Niech $i = \\iota(x)$ będzie graczem podejmującym decyzję w $x$. Gracz ten wybiera akcję $a^* \\in A(x)$ prowadzącą do węzła następczego o najwyższej wypłacie dla gracza $i$.</li>
              <li>Zastąp węzeł $x$ wektorem wypłat wybranego następcy (zwijanie drzewa).</li>
              <li>Powtarzaj kroki 1-3, aż wypłaty zostaną przypisane do korzenia drzewa $r$.</li>
            </ol>
          </div>
          <p>
            <strong>Twierdzenie o Istnieniu i Jednoznaczności:</strong> W każdej skończonej grze o doskonałej informacji algorytm indukcji wstecznej zawsze znajduje rozwiązanie.
            Jeśli żaden gracz nie jest obojętny między żadnymi dwoma węzłami końcowymi, rozwiązanie indukcji wstecznej jest <em>ściśle unikalne</em>!
          </p>
          <div class="p-3 bg-amber-50/70 border border-amber-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-amber-900 text-xs uppercase block">Paradoks Gry Stonoga (Centipede Game &bull; Rosenthal, 1981)</span>
            <p class="text-xs text-amber-950 leading-relaxed">
              Wyobraźmy sobie grę trwającą 100 rund, w której w każdym kroku gracz może "Zakończyć" (Take) lub "Przekazać" (Pass).
              W każdym kroku pula rośnie, lecz gracz kończący grę otrzymuje większy udział.
              Indukcja wsteczna zwija grę od setnego węzła aż do samego korzenia: <strong>Gracz 1 kończy grę w pierwszym ruchu</strong>, zabierając skromną wypłatę (1, 1) zamiast potencjalnych milionów!
              W eksperymentach laboratoryjnych ludzie niemal nigdy nie wybierają natychmiastowego zakończenia gry, grając kooperacyjnie przez wiele rund.
            </p>
          </div>
        </div>

        <!-- 2.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            2.3. Strategie w Grach o Doskonałej Informacji
          </h4>
          <p>
            Jednym z najważniejszych i najczęściej nierozumianych pojęć w teorii gier jest definicja strategii w postaci ekstensywnej:
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 2.4: Strategia w Grze Ekstensywnej</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              Strategia gracza $i$ to funkcja $s_i: D_i \\to \\bigcup_{x \\in D_i} A(x)$ przyporządkowująca akcję $s_i(x) \\in A(x)$ <strong>każdemu węzłowi decyzyjnemu</strong> tego gracza w całym drzewie gry,
              <strong>w tym również węzłom, które nigdy nie zostaną osiągnięte</strong> z powodu wcześniejszych wyborów samego gracza lub jego rywali!
            </p>
          </div>
          <p class="text-xs text-slate-600">
            <strong>Dlaczego kompletny plan jest konieczny?</strong> Aby przeanalizować rozumowanie kontrfaktyczne rywala (<em>"Co zrobiłby gracz $i$, gdybym wybrał opcję B zamiast A?"</em>), rywal musi znać zamiary gracza $i$ we wszystkich potencjalnych poddrzewach.
            Liczba strategii gracza wynosi $|S_i| = \\prod_{x \\in D_i} |A(x)|$.
          </p>
        </div>

        <!-- 2.4 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            2.4. Relacja Między Indukcją Wsteczną a Równowagą Nasha: Niewiarygodne Groźby
          </h4>
          <p>
            Każdą grę ekstensywną możemy przekształcić w równoważną postać strategiczną (macierzową).
            Zachodzi następująca fundamentalna relacja:
          </p>
          <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-blue-800 text-xs block uppercase">Twierdzenie 2.1: Indukcja Wsteczna a Równowaga Nasha</span>
            <p class="text-xs text-blue-950 leading-relaxed">
              1. Każde rozwiązanie indukcji wstecznej indukuje <strong>równowagę Nasha</strong> powiązanej postaci strategicznej gry.<br>
              2. Jednak postać strategiczna może zawierać dodatkowe równowagi Nasha, które <strong>nie są rozwiązaniami indukcji wstecznej</strong>, ponieważ opierają się na <strong>niewiarygodnych groźbach (Incredible Threats)</strong>!
            </p>
          </div>
          <p>
            <strong>Przykład: Gra Wejścia na Rynek (Market Entry):</strong> Pretendent decyduje: Wejść (In) czy Zostać na zewnątrz (Out). Monopolista decyduje: Walczyć wojną cenową (Fight) czy Przystosować się (Accommodate).
            Wypłaty: Out daje (0, 3). Przy In: Accommodate daje (2, 1), a Fight daje (-1, -1).
            Indukcja wsteczna: Monopolista po wejściu wybiera Accommodate (1 > -1), więc pretendent wchodzi (In) z wypłatą 2.
            W postaci macierzowej profilem równowagi Nasha jest również (Out, Fight): jeśli monopolista grozi wojną cenową, pretendent woli Out (0 > -1); a przy Out wybór monopolisty nie ma znaczenia.
            Jednak groźba "Fight" jest <em>niewiarygodna</em>: gdy pretendent już wejdzie, racjonalny monopolista nigdy jej nie zrealizuje!
          </p>
        </div>

        <!-- 2.5 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            2.5. Gry Dwuosobowe o Sumie Zerowej i Uogólnienie Twierdzenia Zermelo
          </h4>
          <p>
            W grach o doskonałej informacji, gdzie interesy graczy są ściśle sprzeczne (wygrana jednego oznacza przegraną drugiego):
          </p>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Twierdzenie 2.2 & 2.3 (Ernst Zermelo, 1913)</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              W każdej skończonej dwuosobowej grze o doskonałej informacji:
            </p>
            <ul class="text-xs text-emerald-900 space-y-1 list-disc list-inside">
              <li>Jeśli nie ma remisów (gra typu wygrana-przegrana, np. Nim, Race to 100), to jeden z graczy posiada <strong>strategię ściśle wygrywającą</strong>.</li>
              <li>Jeśli dozwolone są remisy (szachy, warcaby, kółko i krzyżyk), to zachodzi dokładnie jedna z trzech możliwości: (1) Gracz 1 ma strategię wygrywającą, (2) Gracz 2 ma strategię wygrywającą, lub (3) obaj gracze mają strategie gwarantujące co najmniej remis!</li>
            </ul>
          </div>
        </div>

        <!-- ZADANIE 2.13 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyróżnione Zadanie 2.13 (Mechanizm Sądu Króla Salomona &bull; Glazer i Ma 1989)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 2.E &bull; s. 89</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Kontekst biblijny w ujęciu teorii gier:</strong> Dwie kobiety (Anna i Maria) spierają się o niemowlę.
            Prawdziwa matka wycenia dziecko na $v_H = 100$, zaś oszustka na $v_L = 40$. Salomon nie wie, która jest prawdziwą matką.
            Glazer i Ma zaprojektowali dynamiczną grę ekstensywną: Salomon pyta najpierw Annę: "Czy dziecko jest twoje?". Jeśli Anna powie "Nie", dziecko trafia do Marii bez opłat.
            Jeśli Anna powie "Tak", Salomon pyta Marię: "Czy kwestionujesz jej słowa?". Jeśli Maria nie kwestionuje, dziecko trafia do Anny.
            Jeśli Maria zakwestionuje, musi zapłacić karę $F = 50$, dziecko trafia do Marii, lecz Anna płaci grzywnę $G = 60$.
          </p>
          <details class="text-xs bg-white p-3 rounded-lg border border-slate-200 cursor-pointer">
            <summary class="font-bold text-slate-800 select-none">Pokaż Rozwiązanie przez Indukcję Wsteczną (Appendix 2.S Bonanno)</summary>
            <div class="mt-2 text-slate-700 space-y-2 leading-relaxed">
              <p>
                <strong>Przypadek A: Anna jest prawdziwą matką ($v_A = 100, v_M = 40$).</strong>
                Jeśli Anna powie "Tak", Maria kwestionując zapłaciłaby $F = 50$, uzyskując zysk $40 - 50 = -10 < 0$. Maria nie kwestionuje.
                Więc Anna śmiało mówi "Tak" i dostaje dziecko z zyskiem 100 bez opłat!
              </p>
              <p>
                <strong>Przypadek B: Maria jest prawdziwą matką ($v_A = 40, v_M = 100$).</strong>
                Jeśli Anna powie "Tak", Maria kwestionując płaci 50, lecz dostaje dziecko warte 100, osiągając zysk $100 - 50 = 50 > 0$. Maria zakwestionuje!
                Wtedy Anna otrzyma karę $G = 60$ (zysk -60).
                Anna, przewidując to wstecznie, w pierwszym ruchu mówi "Nie" (zysk 0 > -60). Dziecko natychmiast trafia do Marii bez opłat!
              </p>
              <p>
                <strong>Sukces mechanizmu:</strong> W indukcji wstecznej dziecko w obu przypadkach trafia do prawdziwej matki, żadna kara nie zostaje naliczona, a prawda zostaje ujawniona w pełni!
              </p>
            </div>
          </details>
        </div>
      </section>
    """

def get_chapter_3():
    return """
      <!-- ROZDZIAŁ 3: OGÓLNE GRY DYNAMICZNE I SPE -->
      <section id="rozdzial-3" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Część I &bull; Rozdział 3</span>
          <span class="text-xs font-mono text-slate-400">Ogólne Gry Dynamiczne &bull; Strony 107-156</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdział 3: Ogólne Gry Dynamiczne, Podgry i Równowaga SPE</h3>

        <!-- 3.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            3.1. Niedoskonała Informacja i Zbiory Informacyjne
          </h4>
          <p>
            Gdy gracze nie obserwują pewnych ruchów rywali lub Natury (np. ukryte karty w pokerze, równoczesne składanie ofert w grze sekwencyjnej), węzły decyzyjne grupują się w <strong>zbiory informacyjne (Information Sets)</strong>.
            Zbiory informacyjne tworzą partycję wierzchołków decyzyjnych gracza $i$.
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 3.1: Warunek Doskonałej Pamięci (Perfect Recall)</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              Gra spełnia warunek doskonałej pamięci, jeśli żaden gracz nigdy nie zapomina własnych wcześniejszych decyzji ani informacji, które kiedyś posiadał:
            </p>
            <ol class="text-xs text-slate-600 space-y-1 list-decimal list-inside pl-2">
              <li>Dla każdego zbioru informacyjnego $h$, wszystkie węzły $x, x' \\in h$ mają dokładnie ten sam zbiór dostępnych akcji: $A(x) = A(x')$.</li>
              <li>Żaden węzeł w zbiorze informacyjnym $h$ nie może być poprzednikiem innego węzła w tym samym zbiorze $h$ (brak amnezji własnych ruchów).</li>
              <li>Jeśli węzeł $x$ poprzedza $y$, gracz $i$ w węźle $x$ wybrał akcję $a$, a $y$ należy do zbioru informacyjnego $h$, to każdy inny węzeł $y' \\in h$ musi również mieć poprzednika $x'$ należącego do zbioru $x$, z którego wyprowadzono tę samą akcję $a$!</li>
            </ol>
          </div>
        </div>

        <!-- 3.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            3.3. Definicja Podgry Właściwej (Subgames)
          </h4>
          <p>
            Pojęcie podgry jest fundamentem uszczegóławiania równowag w grach dynamicznych:
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 3.3 &bull; Podgra Właściwa (Subgame)</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              Poddrzewo $G$ rozpoczynające się w węźle $x_0 \\in D$ jest <strong>podgrą</strong>, jeśli:
            </p>
            <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside">
              <li>Węzeł początkowy $x_0$ stanowi <em>jednoelementowy zbiór informacyjny</em> (singleton: $h(x_0) = \\{x_0\\}$).</li>
              <li>$G$ zawiera węzeł $x_0$ oraz <strong>wszystkich jego potomków</strong> w drzewie gry.</li>
              <li>$G$ <strong>nie rozcina żadnego zbioru informacyjnego</strong>: jeśli węzeł $y$ należy do $G$, a węzeł $y'$ należy do tego samego zbioru informacyjnego co $y$ ($y' \\in h(y)$), to $y'$ musi również należeć do $G$!</li>
            </ul>
          </div>
          <p class="text-xs text-slate-600">
            Podgra jest <em>właściwa (proper subgame)</em>, jeśli nie jest całą wyjściową grą ($x_0 \\ne r$).
          </p>
        </div>

        <!-- 3.4 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            3.4. Równowaga Doskonała w Podgrach (Subgame-Perfect Equilibrium &bull; SPE)
          </h4>
          <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-blue-800 text-xs block uppercase">Definicja 3.5 (Reinhard Selten, 1965) &bull; Równowaga SPE</span>
            <p class="text-xs text-blue-950 leading-relaxed">
              Profil strategii $s^* \\in S$ jest <strong>równowagą doskonałą w podgrach (Subgame-Perfect Equilibrium - SPE)</strong>, jeśli:
              1. Jest równowagą Nasha całej gry $\\Gamma$, oraz<br>
              2. W każdej właściwej podgrze $G$ restrykcja profilu $s^*|_G$ tworzy równowagę Nasha tej podgry $G$.
            </p>
          </div>
          <p>
            <strong>Algorytm Wyznaczania SPE (Definicja 3.6):</strong>
            Zastępujemy minimalne podgry wektorami wypłat z ich równowag Nasha i powtarzamy procedurę w górę drzewa.
            Jeśli pewna podgra nie posiada równowagi Nasha w strategiach czystych, w grze porządkowej czyste SPE może nie istnieć!
          </p>
        </div>

        <!-- 3.5 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            3.5. Ruchy Losowe Natury i Loterie
          </h4>
          <p>
            Natura jest traktowana jako fikcyjny Gracz 0, który wykonuje ruchy z obiektywnymi, znanymi prawdopodobieństwami.
            Gdy Natura wykonuje ruch, rezultaty gry stają się loteriami.
            W grach o wypłatach porządkowych gracze muszą uszeregować loterie.
            Jeśli gracze są neutralni wobec ryzyka, wartość loterii jest równa jej wartości oczekiwanej $\\mathbb{E}[L] = \\sum p_k x_k$.
          </p>
        </div>

        <!-- ZADANIE 3.14 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyróżnione Zadanie 3.14 (Odstraszanie od Wejścia i Nieodwracalne Inwestycje)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 3.E &bull; s. 138</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Treść Zadania:</strong> Monopolista decyduje, czy zainwestować w duże moce produkcyjne ($K_H$), czy małe ($K_L$).
            Następnie pretendent obserwuje tę decyzję i wybiera: Wejść (In) czy Zostać (Out).
            Jeśli pretendent wejdzie, firmy grają w jednoczesną podgrę cenową.
            Zadanie dowodzi, że wcześniejsza nieodwracalna inwestycja w duże moce $K_H$ wiarygodnie obniża koszt krańcowy monopolisty w podgrze, sprawiając że groźba wojny cenowej staje się wiarygodna w SPE i skutecznie odstrasza rywala od wejścia!
          </p>
        </div>
      </section>
    """
