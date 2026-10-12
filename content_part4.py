# Part 4: Chapters 10, 11, 12 for Lyceum Game Theory
# Zero em-dashes strictly enforced.

def get_chapter_10():
    return """
      <!-- ROZDZIAL 10: SLABA ROWNOWAGA SEKWENCYJNA -->
      <section id="rozdzial-10" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Czesc IV &bull; Rozdzial 10</span>
          <span class="text-xs font-mono text-slate-400">Uszczegolowienia SPE &bull; Strony 354-388</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdzial 10: Pierwsza Proba: Slaba Rownowaga Sekwencyjna (WSE)</h3>

        <!-- 10.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            10.1. Oceny (Assessments) i Racjonalnosc Sekwencyjna
          </h4>
          <p>
            Aby uzasadnic wybory graczy w grach dynamicznych z niedoskonala informacja, musimy jawnie zamodelowac ich subiektywne przekonania w kazdym punkcie decyzyjnym.
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 10.1 &bull; Pojecie Oceny (Assessment)</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              <strong>Ocena</strong> to para $(\\sigma, \\mu)$, gdzie:
            </p>
            <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside">
              <li>$\\sigma = (\\sigma_1, \\dots, \\sigma_n)$ to profil strategii behawioralnych przyporzadkowujacy rozklad prawdopodobienstwa $\\sigma_i(h) \\in \\Delta(A(h))$ w kazdym zbiorze informacyjnym $h$.</li>
              <li>$\\mu$ to <strong>system przekonan (system of beliefs)</strong> przypisujacy kazdemu zbiorowi informacyjnemu $h \\in \\mathcal{H}$ rozklad prawdopodobienstwa $\\mu_h \\in \\Delta(h)$ nad wezlami nalezacymi do tego zbioru (czyli subiektywna ocene: $\\sum_{x \\in h} \\mu(x) = 1$, gdzie $\\mu(x) \\ge 0$).</li>
            </ul>
          </div>
          <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-blue-800 text-xs block uppercase">Definicja 10.2 &bull; Racjonalnosc Sekwencyjna (Sequential Rationality)</span>
            <p class="text-xs text-blue-950 leading-relaxed">
              Ocena $(\\sigma, \\mu)$ jest <strong>sekwencyjnie racjonalna</strong>, jesli w kazdym zbiorze informacyjnym $h \\in \\mathcal{H}_i$ gracz podejmujacy decyzje wybiera strategie maksymalizujaca jego oczekiwana wyplate,
              biorac pod uwage przekonania $\\mu_h$ na wezlach zbioru $h$ oraz zakladajac, ze we wszystkich nastepnych zbiorach informacyjnych gracze beda postepowac zgodnie z profilem $\\sigma$.
            </p>
          </div>
        </div>

        <!-- 10.2 & 10.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            10.2 - 10.3. Aktualizacja Bayesa w Osiaganych Zbiorach i Ograniczenia WSE
          </h4>
          <p>
            Zbior informacyjny $h$ jest <strong>osiagany z dodatnim prawdopodobienstwem</strong> pod profilem $\\sigma$ ($P(h | \\sigma) > 0$), jesli istnieje co najmniej jedna sciezka z korzenia do pewnego wezla $x \\in h$, w ktorej wszystkie akcje sa grane z dodatnim prawdopodobienstwem.
          </p>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Definicja 10.5 &bull; Slaba Rownowaga Sekwencyjna (Weak Sequential Equilibrium &bull; WSE)</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              Ocena $(\\sigma, \\mu)$ jest <strong>Slaba Rownowaga Sekwencyjna (WSE)</strong>, jesli:
              1. Jest <strong>sekwencyjnie racjonalna</strong> we wszystkich zbiorach informacyjnych, oraz<br>
              2. Spelnia <strong>aktualizacje bayesowska w osiaganych zbiorach informacyjnych (Definicja 10.4)</strong>:
              dla kazdego $h$ z $P(h | \\sigma) > 0$ i kazdego $x \\in h$:
              $$\\mu(x) = \\frac{P(x | \\sigma)}{P(h | \\sigma)}$$
            </p>
          </div>
          <div class="p-4 bg-rose-50 border border-rose-200 rounded-xl space-y-2 text-xs text-rose-950 leading-relaxed">
            <strong class="font-mono uppercase block text-rose-900">Fatalna Wada WSE (Dlaczego WSE NIE jest uszczegolowieniem SPE!):</strong>
            <strong>Twierdzenie 10.1:</strong> Kazda WSE indukuje rownowage Nasha calej gry.<br>
            Jednak WSE <strong>nie uszczegolawia Rownowagi Doskonalej w Podgrach (SPE)</strong>!
            W nieosiaganych zbiorach informacyjnych ($P(h | \\sigma) = 0$), regula Bayesa nie naklada zadnych ograniczen na przekonania $\\mu_h$.
            Przekonania moga byc calkowicie arbitralne, co pozwala graczom wybierac akcje niebedace rownowaga Nasha w nieosiaganej podgrze (Rysunki 10.9 i 10.10 w podreczniku Bonanno).
            Zatem zbiory WSE i SPE przecinaja sie, lecz zaden nie zawiera sie w drugim!
          </div>
        </div>

        <!-- ZADANIE 10.8 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyrznione Zadanie 10.8 (Gra z Hakerem Poczty Elektronicznej)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 10.E &bull; s. 378</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Tresc Zadania:</strong> Uzytkownik decyduje, czy wlaczyc szyfrowanie wiadomosci, a haker decyduje, czy podjac probe ataku.
            Zadanie wymaga wyznaczenia wszystkich ocen bedacych WSE oraz wykazania, ze pewne WSE dopuszczaja nieracjonalne skorelowanie przekonan hakera na temat hasla poza sciezka gry, co motywuje przejscie do pelnej Rownowagi Sekwencyjnej Krepsa-Wilsona.
          </p>
        </div>
      </section>
    """

def get_chapter_11():
    return """
      <!-- ROZDZIAL 11: ROWNOWAGA SEKWENCYJNA KREPSA-WILSONA -->
      <section id="rozdzial-11" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Czesc IV &bull; Rozdzial 11</span>
          <span class="text-xs font-mono text-slate-400">Kreps-Wilson 1982 &bull; Strony 389-417</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdzial 11: Rownowaga Sekwencyjna Krepsa-Wilsona (1982)</h3>

        <!-- 11.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            11.1. Oceny Spojne (KW-Consistency) i Granice Ciagow Zaburzen
          </h4>
          <p>
            Aby wyeliminowac arbitralne przekonania poza sciezka gry, David Kreps i Robert Wilson (1982) wprowadzili koncepcje aproksymacji gry strategiami <strong>calkowicie mieszanymi (completely mixed strategies)</strong>:
            jesli kazda akcja w drzewie gry jest wybierana z prawdopodobienstwem scisle dodatnim $\\sigma(a) > 0$, to <strong>kazdy zbior informacyjny jest osiagany</strong>, a przekonania $\\mu$ sa jednoznacznie zdeterminowane przez regule Bayesa!
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 11.1 &bull; Spojnosc w Sensie Krepsa-Wilsona (KW-Consistency)</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              Ocena $(\\sigma, \\mu)$ jest <strong>spojna (consistent)</strong>, jesli istnieje nieskonczony ciag profili strategii calkowicie mieszanych $\\{\\sigma^k\\}_{k=1}^\\infty$
              (gdzie $\\sigma^k(a) > 0$ dla kazdej akcji $a$) taki, ze:
              $$\\lim_{k \\to \\infty} \\sigma^k = \\sigma \\quad \\text{oraz} \\quad \\lim_{k \\to \\infty} \\mu^k = \\mu$$
              gdzie $\\mu^k$ to unikalny system przekonan wyprowadzony z $\\sigma^k$ za pomoca reguly Bayesa w kazdym wezle gry!
            </p>
          </div>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 text-xs">
            <strong class="text-blue-700 block font-mono">Przyklad Selten's Horse (Rysunek 11.4):</strong>
            Trzech graczy: Gracz 1 wybiera C lub D. Przy D gra sie konczy. Przy C ruch ma Gracz 2 (wybiera c lub d).
            Gracz 3 podejmuje decyzje w dwuelementowym zbiorze informacyjnym $\\{x_1, x_2\\}$, nie wiedzac czy ruch wykonal Gracz 1 czy Gracz 2.
            Dla profilu $(D, c, R)$, sciezka gry omija zbior Gracza 3.
            KW-spojnosc wymusza rozpatrzenie zaburzen $\\sigma^k(C) = \\epsilon_k, \\sigma^k(d) = \\delta_k$.
            Wtedy przekonanie w wezle $x_2$ wynosi $\\mu(x_2) = \\frac{\\epsilon_k \\delta_k}{\\epsilon_k \\delta_k + (1-\\epsilon_k)} \\to 0$.
            Kreps-Wilson eliminuje nielogiczne skorelowanie bledow!
          </div>
        </div>

        <!-- 11.2 & 11.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            11.2 - 11.3. Rownowaga Sekwencyjna (SE) i Krytyka Topologiczna
          </h4>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Definicja 11.2 & Twierdzenia 11.1 & 11.2 (Kreps & Wilson, 1982)</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              Ocena $(\\sigma, \\mu)$ jest <strong>Rownowaga Sekwencyjna (Sequential Equilibrium &bull; SE)</strong>, jesli jest <strong>sekwencyjnie racjonalna</strong> oraz <strong>spojna (KW-consistent)</strong>.
            </p>
            <ul class="text-xs text-emerald-900 space-y-1 list-disc list-inside">
              <li><strong>Twierdzenie o Istnieniu:</strong> Kazda skonczona gra ekstensywna o wyplatach kardynalnych posiada <strong>co najmniej jedna rownowage sekwencyjna</strong>.</li>
              <li><strong>Hierarchia Uszczegolowien:</strong> Kazda rownowaga sekwencyjna jest zarowno rownowaga SPE, jak i WSE:
                $$\\text{Sequential Equilibrium (SE)} \\subset (\\text{SPE} \\cap \\text{WSE}) \\subset \\text{Nash}$$
              </li>
            </ul>
          </div>
          <div class="p-3 sm:p-4 bg-amber-50/70 border border-amber-200 rounded-xl text-xs text-amber-950 leading-relaxed">
            <strong>Krytyka Metodologiczna Bonanno (Sekcja 11.3):</strong>
            Dlaczego racjonalni gracze mieliby uzasadniac swoje przekonania braniem granic ciagow zaburzen (tzw. "drzenia rak" - trembles)?
            Pojecie granicy topologicznej ciagu nie posiada zadnej bezposredniej interpretacji decyzyjnej ani epistemologicznej!
            To wlasnie ten zarzut sklonil Giacomo Bonanno do stworzenia alternatywnej teorii opartej na logice epistemicznej AGM.
          </div>
        </div>

        <!-- ZADANIE 11.6 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyrznione Zadanie 11.6 (Dwurundowe Negocjacje i Zaburzenia Przekonan)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 11.E &bull; s. 403</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Tresc Zadania:</strong> Konstrukcja ciagu $\\sigma^k = (1 - \\epsilon_k, \\epsilon_k)$ z $\\epsilon_k \\to 0$ w dynamicznej grze przetargowej Rubinstena.
            Zadanie pokazuje krok po kroku, jak policzyc iloraz bayesowski i udowodnic spojnosc przekonan na wezlach terminalnych.
          </p>
        </div>
      </section>
    """

def get_chapter_12():
    return """
      <!-- ROZDZIAL 12: DOSKONALA ROWNOWAGA BAYESOWSKA I PRZELOM BONANNO -->
      <section id="rozdzial-12" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Czesc IV &bull; Rozdzial 12</span>
          <span class="text-xs font-mono text-slate-400">PBE i Twierdzenie Bonanno &bull; Strony 418-469</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdzial 12: Doskonala Rownowaga Bayesowska (PBE) i Przelom Giacomo Bonanno (2015)</h3>

        <!-- 12.1 - 12.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            12.1 - 12.3. Historie Gry i Spojnosc w Sensie AGM (AGM-Consistency)
          </h4>
          <p>
            W rewolucyjnym podejsciu Giacomo Bonanno, gra ekstensywna jest definiowana nie przez geometryczne drzewo, lecz przez <strong>zbior historii sekwencyjnych $H$</strong> (Appendix 12.A).
            Kazda historia $h = a_1 a_2 \\dots a_k$ to ciag wykonanych akcji.
            Zamiast ciagow zbieznych z prawdopodobienstwami, graczom przypisujemy <strong>porzadek wiarygodnosci (Plausibility Order)</strong> $\\precsim$ na historiach $H$.
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 12.2 &bull; Ocena Spojna w Sensie AGM (AGM-Consistency)</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              Ocena $(\\sigma, \\mu)$ jest <strong>spojna w sensie AGM</strong> wzgledem porzadku wiarygodnosci $\\precsim$, jesli:
            </p>
            <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside">
              <li>Akcje podejmowane z dodatnim prawdopodobienstwem zachowuja pelna wiarygodnosc historii: jesli $\\sigma(a | h) > 0$, to historia przedluzona $ha$ jest <em>rownie wiarygodna</em> jak $h$ ($h \\sim ha$).</li>
              <li>Akcje o prawdopodobienstwie zero prowadza do historii scisle mniej wiarygodnych ($ha \\succ h$).</li>
              <li>Przekonania $\\mu_h$ w kazdym zbiorze informacyjnym skupiaja sie wylacznie na historiach <strong>najbardziej wiarygodnych</strong> wewnatrz danego zbioru informacyjnego!</li>
            </ul>
          </div>
          <p>
            Wymog aktualizacji bayesowskiej w kazdym zbiorze informacyjnym tak dlugo, jak to tylko mozliwe (Definicja 12.3), definiuje <strong>Doskonala Rownowage Bayesowska (Perfect Bayesian Equilibrium &bull; PBE &bull; Definicja 12.4)</strong>.
          </p>
        </div>

        <!-- 12.4 - 12.5 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            12.4 - 12.5. Warunek Niezaleznosci i Koronne Twierdzenie 12.5 Bonanno (2015)
          </h4>
          <p>
            Standardowe definicje PBE w literaturze (np. Fudenberg i Tirole 1991) cierpialy na brak precyzji poza grami sygnalizacyjnymi.
            Bonanno uzupelnia definicje o dwa kluczowe aksjomaty:
          </p>
          <ul class="text-xs text-slate-600 space-y-1.5 list-disc list-inside">
            <li>
              <strong>Niezaleznosc ("No Signaling What You Don't Know" &bull; Definicja 12.5):</strong> Posuniecia gracza w wezlach nieskorelowanych nie moga sygnalizowac informacji, ktorych ten gracz sam nie posiada.
            </li>
            <li>
              <strong>Mierzalnosc Wyborow (Choice Measurability &bull; CM &bull; Definicja 12.7):</strong> Porzadek wiarygodnosci $\\precsim$ dopuszcza funkcje rangi $F: H \\to \\mathbb{N}$ taka, ze roznica rang dwoch historii jest niezmiennicza na dodanie wspolnej akcji: $F(ha) - F(h'a) = F(h) - F(h')$.
            </li>
            <li>
              <strong>Jednorodna Spojnosc Bayesowska (Uniformly Bayesian &bull; UB &bull; Definicja 12.8):</strong> Relatywne proporcje prawdopodobienstw wewnatrz klas rownej wiarygodnosci sa zachowane.
            </li>
          </ul>
          <div class="p-4 sm:p-5 bg-blue-50 border-2 border-blue-500/50 rounded-2xl space-y-3">
            <div class="flex items-center justify-between flex-wrap gap-2">
              <span class="font-mono font-bold text-blue-900 text-xs uppercase block">Twierdzenie 12.5 (Giacomo Bonanno, 2015 &bull; International Journal of Game Theory)</span>
              <span class="badge-tag bg-blue-600 text-white text-[10px]">Kamien Milowy Teorii Gier</span>
            </div>
            <p class="text-xs sm:text-sm text-blue-950 leading-relaxed font-semibold">
              Rozwazmy dowolna skonczona gre w postaci ekstensywnej oraz ocene $(\\sigma, \\mu)$. Nastepujace warunki sa rownowazne:
            </p>
            <div class="p-3 bg-white border border-blue-200 rounded-xl space-y-2 text-xs font-mono text-slate-800">
              <div>(A) Ocena $(\\sigma, \\mu)$ jest Rownowaga Sekwencyjna Krepsa-Wilsona (SE).</div>
              <div class="text-center font-bold text-blue-600 text-sm">&Updownarrow</div>
              <div>(B) Ocena $(\\sigma, \\mu)$ jest Doskonala Rownowaga Bayesowska (PBE), ktora jest racjonalizowana przez porzadek wiarygodnosci spelniajacy warunek Mierzalnosci Wyborow (Choice Measurability) oraz jest wzgledem niego Jednorodnie Bayesowska (Uniformly Bayesian).</div>
            </div>
            <p class="text-xs text-blue-950 leading-relaxed">
              <strong>Dlaczego to twierdzenie jest przelomowe?</strong>
              Zamyka ono 33-letnia luke w literaturze naukowej: uwalnia definicje Rownowagi Sekwencyjnej Krepsa-Wilsona od sztucznych, nieintuicyjnych granic ciagow zaburzen (drzenia rak),
              zastepujac je w 100% przejrzystymi, jakosciowymi aksjomatami rewizji przekonan w duchu logiki epistemicznej AGM!
            </p>
          </div>
        </div>

        <!-- ZADANIE 12.11 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyrznione Zadanie 12.11 (Wielostadiowa Gra Sygnalizacyjna i PBE)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 12.E &bull; s. 452</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Tresc Zadania:</strong> Konstrukcja porzadku wiarygodnosci $\\precsim$ i weryfikacja warunku Choice Measurability dla zloznonego drzewa decyzyjnego z Rysunku 12.15 w podreczniku Bonanno, prowadzaca do wykluczenia sztucznych rownowag PBE niebedacych rownowagami Krepsa-Wilsona.
          </p>
        </div>
      </section>
    """
