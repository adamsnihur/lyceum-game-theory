# Part 4: Chapters 10, 11, 12 for Lyceum Game Theory
# Zero em-dashes strictly enforced.

def get_chapter_10():
    return """
      <!-- ROZDZIAŁ 10: SŁABA RÓWNOWAGA SEKWENCYJNA -->
      <section id="rozdzial-10" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Część IV &bull; Rozdział 10</span>
          <span class="text-xs font-mono text-slate-400">Uszczegółowienia SPE &bull; Strony 354-388</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdział 10: Pierwsza Próba: Słaba Równowaga Sekwencyjna (WSE)</h3>

        <!-- 10.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            10.1. Oceny (Assessments) i Racjonalność Sekwencyjna
          </h4>
          <p>
            Aby uzasadnić wybory graczy w grach dynamicznych z niedoskonałą informacją, musimy jawnie zamodelować ich subiektywne przekonania w każdym punkcie decyzyjnym.
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 10.1 &bull; Pojęcie Oceny (Assessment)</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              <strong>Ocena</strong> to para $(\\sigma, \\mu)$, gdzie:
            </p>
            <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside">
              <li>$\\sigma = (\\sigma_1, \\dots, \\sigma_n)$ to profil strategii behawioralnych przyporządkowujący rozkład prawdopodobieństwa $\\sigma_i(h) \\in \\Delta(A(h))$ w każdym zbiorze informacyjnym $h$.</li>
              <li>$\\mu$ to <strong>system przekonań (system of beliefs)</strong> przypisujący każdemu zbiorowi informacyjnemu $h \\in \\mathcal{H}$ rozkład prawdopodobieństwa $\\mu_h \\in \\Delta(h)$ nad węzłami należącymi do tego zbioru (czyli subiektywną ocenę: $\\sum_{x \\in h} \\mu(x) = 1$, gdzie $\\mu(x) \\ge 0$).</li>
            </ul>
          </div>
          <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-blue-800 text-xs block uppercase">Definicja 10.2 &bull; Racjonalność Sekwencyjna (Sequential Rationality)</span>
            <p class="text-xs text-blue-950 leading-relaxed">
              Ocena $(\\sigma, \\mu)$ jest <strong>sekwencyjnie racjonalna</strong>, jeśli w każdym zbiorze informacyjnym $h \\in \\mathcal{H}_i$ gracz podejmujący decyzję wybiera strategię maksymalizującą jego oczekiwaną wypłatę,
              biorąc pod uwagę przekonania $\\mu_h$ na węzłach zbioru $h$ oraz zakładając, że we wszystkich następnych zbiorach informacyjnych gracze będą postępować zgodnie z profilem $\\sigma$.
            </p>
          </div>
        </div>

        <!-- 10.2 & 10.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            10.2 - 10.3. Aktualizacja Bayesa w Osiąganych Zbiorach i Ograniczenia WSE
          </h4>
          <p>
            Zbiór informacyjny $h$ jest <strong>osiągany z dodatnim prawdopodobieństwem</strong> pod profilem $\\sigma$ ($P(h | \\sigma) > 0$), jeśli istnieje co najmniej jedna ścieżka z korzenia do pewnego węzła $x \\in h$, w której wszystkie akcje są grane z dodatnim prawdopodobieństwem.
          </p>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Definicja 10.5 &bull; Słaba Równowaga Sekwencyjna (Weak Sequential Equilibrium &bull; WSE)</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              Ocena $(\\sigma, \\mu)$ jest <strong>Słabą Równowagą Sekwencyjną (WSE)</strong>, jeśli:
              1. Jest <strong>sekwencyjnie racjonalna</strong> we wszystkich zbiorach informacyjnych, oraz<br>
              2. Spełnia <strong>aktualizację bayesowską w osiąganych zbiorach informacyjnych (Definicja 10.4)</strong>:
              dla każdego $h$ z $P(h | \\sigma) > 0$ i każdego $x \\in h$:
              $$\\mu(x) = \\frac{P(x | \\sigma)}{P(h | \\sigma)}$$
            </p>
          </div>
          <div class="p-4 bg-rose-50 border border-rose-200 rounded-xl space-y-2 text-xs text-rose-950 leading-relaxed">
            <strong class="font-mono uppercase block text-rose-900">Fatalna Wada WSE (Dlaczego WSE NIE jest uszczegółowieniem SPE!):</strong>
            <strong>Twierdzenie 10.1:</strong> Każda WSE indukuje równowagę Nasha całej gry.<br>
            Jednak WSE <strong>nie uszczegóławia Równowagi Doskonałej w Podgrach (SPE)</strong>!
            W nieosiąganych zbiorach informacyjnych ($P(h | \\sigma) = 0$), reguła Bayesa nie nakłada żadnych ograniczeń na przekonania $\\mu_h$.
            Przekonania mogą być całkowicie arbitralne, co pozwala graczom wybierać akcje niebędące równowagą Nasha w nieosiąganej podgrze (Rysunki 10.9 i 10.10 w podręczniku Bonanno).
            Zatem zbiory WSE i SPE przecinają się, lecz żaden nie zawiera się w drugim!
          </div>
        </div>

        <!-- ZADANIE 10.8 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyróżnione Zadanie 10.8 (Gra z Hakerem Poczty Elektronicznej)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 10.E &bull; s. 378</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Treść Zadania:</strong> Użytkownik decyduje, czy włączyć szyfrowanie wiadomości, a haker decyduje, czy podjąć próbę ataku.
            Zadanie wymaga wyznaczenia wszystkich ocen będących WSE oraz wykazania, że pewne WSE dopuszczają nieracjonalne skorelowanie przekonań hakera na temat hasła poza ścieżką gry, co motywuje przejście do pełnej Równowagi Sekwencyjnej Krepsa-Wilsona.
          </p>
        </div>
      </section>
    """

def get_chapter_11():
    return """
      <!-- ROZDZIAŁ 11: RÓWNOWAGA SEKWENCYJNA KREPSA-WILSONA -->
      <section id="rozdzial-11" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Część IV &bull; Rozdział 11</span>
          <span class="text-xs font-mono text-slate-400">Kreps-Wilson 1982 &bull; Strony 389-417</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdział 11: Równowaga Sekwencyjna Krepsa-Wilsona (1982)</h3>

        <!-- 11.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            11.1. Oceny Spójne (KW-Consistency) i Granice Ciągów Zaburzeń
          </h4>
          <p>
            Aby wyeliminować arbitralne przekonania poza ścieżką gry, David Kreps i Robert Wilson (1982) wprowadzili koncepcję aproksymacji gry strategiami <strong>całkowicie mieszanymi (completely mixed strategies)</strong>:
            jeśli każda akcja w drzewie gry jest wybierana z prawdopodobieństwem ściśle dodatnim $\\sigma(a) > 0$, to <strong>każdy zbiór informacyjny jest osiągany</strong>, a przekonania $\\mu$ są jednoznacznie zdeterminowane przez regułę Bayesa!
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 11.1 &bull; Spójność w Sensie Krepsa-Wilsona (KW-Consistency)</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              Ocena $(\\sigma, \\mu)$ jest <strong>spójna (consistent)</strong>, jeśli istnieje nieskończony ciąg profili strategii całkowicie mieszanych $\\{\\sigma^k\\}_{k=1}^\\infty$
              (gdzie $\\sigma^k(a) > 0$ dla każdej akcji $a$) taki, że:
              $$\\lim_{k \\to \\infty} \\sigma^k = \\sigma \\quad \\text{oraz} \\quad \\lim_{k \\to \\infty} \\mu^k = \\mu$$
              gdzie $\\mu^k$ to unikalny system przekonań wyprowadzony z $\\sigma^k$ za pomocą reguły Bayesa w każdym węźle gry!
            </p>
          </div>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 text-xs">
            <strong class="text-blue-700 block font-mono">Przykład Selten's Horse (Rysunek 11.4):</strong>
            Trzech graczy: Gracz 1 wybiera C lub D. Przy D gra się kończy. Przy C ruch ma Gracz 2 (wybiera c lub d).
            Gracz 3 podejmuje decyzję w dwuelementowym zbiorze informacyjnym $\\{x_1, x_2\\}$, nie wiedząc czy ruch wykonał Gracz 1 czy Gracz 2.
            Dla profilu $(D, c, R)$, ścieżka gry omija zbiór Gracza 3.
            KW-spójność wymusza rozpatrzenie zaburzeń $\\sigma^k(C) = \\epsilon_k, \\sigma^k(d) = \\delta_k$.
            Wtedy przekonanie w węźle $x_2$ wynosi $\\mu(x_2) = \\frac{\\epsilon_k \\delta_k}{\\epsilon_k \\delta_k + (1-\\epsilon_k)} \\to 0$.
            Kreps-Wilson eliminuje nielogiczne skorelowanie błędów!
          </div>
        </div>

        <!-- 11.2 & 11.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            11.2 - 11.3. Równowaga Sekwencyjna (SE) i Krytyka Topologiczna
          </h4>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Definicja 11.2 & Twierdzenia 11.1 & 11.2 (Kreps & Wilson, 1982)</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              Ocena $(\\sigma, \\mu)$ jest <strong>Równowagą Sekwencyjną (Sequential Equilibrium &bull; SE)</strong>, jeśli jest <strong>sekwencyjnie racjonalna</strong> oraz <strong>spójna (KW-consistent)</strong>.
            </p>
            <ul class="text-xs text-emerald-900 space-y-1 list-disc list-inside">
              <li><strong>Twierdzenie o Istnieniu:</strong> Każda skończona gra ekstensywna o wypłatach kardynalnych posiada <strong>co najmniej jedną równowagę sekwencyjną</strong>.</li>
              <li><strong>Hierarchia Uszczegółowień:</strong> Każda równowaga sekwencyjna jest zarówno równowagą SPE, jak i WSE:
                $$\\text{Sequential Equilibrium (SE)} \\subset (\\text{SPE} \\cap \\text{WSE}) \\subset \\text{Nash}$$
              </li>
            </ul>
          </div>
          <div class="p-3 sm:p-4 bg-amber-50/70 border border-amber-200 rounded-xl text-xs text-amber-950 leading-relaxed">
            <strong>Krytyka Metodologiczna Bonanno (Sekcja 11.3):</strong>
            Dlaczego racjonalni gracze mieliby uzasadniać swoje przekonania braniem granic ciągów zaburzeń (tzw. "drżenia rąk" - trembles)?
            Pojęcie granicy topologicznej ciągu nie posiada żadnej bezpośredniej interpretacji decyzyjnej ani epistemologicznej!
            To właśnie ten zarzut skłonił Giacomo Bonanno do stworzenia alternatywnej teorii opartej na logice epistemicznej AGM.
          </div>
        </div>

        <!-- ZADANIE 11.6 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyróżnione Zadanie 11.6 (Dwurundowe Negocjacje i Zaburzenia Przekonań)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 11.E &bull; s. 403</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Treść Zadania:</strong> Konstrukcja ciągu $\\sigma^k = (1 - \\epsilon_k, \\epsilon_k)$ z $\\epsilon_k \\to 0$ w dynamicznej grze przetargowej Rubinsteina.
            Zadanie pokazuje krok po kroku, jak policzyć iloraz bayesowski i udowodnić spójność przekonań na węzłach terminalnych.
          </p>
        </div>
      </section>
    """

def get_chapter_12():
    return """
      <!-- ROZDZIAŁ 12: DOSKONAŁA RÓWNOWAGA BAYESOWSKA I PRZEŁOM BONANNO -->
      <section id="rozdzial-12" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Część IV &bull; Rozdział 12</span>
          <span class="text-xs font-mono text-slate-400">PBE i Twierdzenie Bonanno &bull; Strony 418-469</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdział 12: Doskonała Równowaga Bayesowska (PBE) i Przełom Giacomo Bonanno (2015)</h3>

        <!-- 12.1 - 12.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            12.1 - 12.3. Historie Gry i Spójność w Sensie AGM (AGM-Consistency)
          </h4>
          <p>
            W rewolucyjnym podejściu Giacomo Bonanno, gra ekstensywna jest definiowana nie przez geometryczne drzewo, lecz przez <strong>zbiór historii sekwencyjnych $H$</strong> (Appendix 12.A).
            Każda historia $h = a_1 a_2 \\dots a_k$ to ciąg wykonanych akcji.
            Zamiast ciągów zbieżnych z prawdopodobieństwami, graczom przypisujemy <strong>porządek wiarygodności (Plausibility Order)</strong> $\\precsim$ na historiach $H$.
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Definicja 12.2 &bull; Ocena Spójna w Sensie AGM (AGM-Consistency)</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              Ocena $(\\sigma, \\mu)$ jest <strong>spójna w sensie AGM</strong> względem porządku wiarygodności $\\precsim$, jeśli:
            </p>
            <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside">
              <li>Akcje podejmowane z dodatnim prawdopodobieństwem zachowują pełną wiarygodność historii: jeśli $\\sigma(a | h) > 0$, to historia przedłużona $ha$ jest <em>równie wiarygodna</em> jak $h$ ($h \\sim ha$).</li>
              <li>Akcje o prawdopodobieństwie zero prowadzą do historii ściśle mniej wiarygodnych ($ha \\succ h$).</li>
              <li>Przekonania $\\mu_h$ w każdym zbiorze informacyjnym skupiają się wyłącznie na historiach <strong>najbardziej wiarygodnych</strong> wewnątrz danego zbioru informacyjnego!</li>
            </ul>
          </div>
          <p>
            Wymóg aktualizacji bayesowskiej w każdym zbiorze informacyjnym tak długo, jak to tylko możliwe (Definicja 12.3), definiuje <strong>Doskonałą Równowagę Bayesowską (Perfect Bayesian Equilibrium &bull; PBE &bull; Definicja 12.4)</strong>.
          </p>
        </div>

        <!-- 12.4 - 12.5 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            12.4 - 12.5. Warunek Niezależności i Koronne Twierdzenie 12.5 Bonanno (2015)
          </h4>
          <p>
            Standardowe definicje PBE w literaturze (np. Fudenberg i Tirole 1991) cierpiały na brak precyzji poza grami sygnalizacyjnymi.
            Bonanno uzupełnia definicję o dwa kluczowe aksjomaty:
          </p>
          <ul class="text-xs text-slate-600 space-y-1.5 list-disc list-inside">
            <li>
              <strong>Niezależność ("No Signaling What You Don't Know" &bull; Definicja 12.5):</strong> Posunięcia gracza w węzłach nieskorelowanych nie mogą sygnalizować informacji, których ten gracz sam nie posiada.
            </li>
            <li>
              <strong>Mierzalność Wyborów (Choice Measurability &bull; CM &bull; Definicja 12.7):</strong> Porządek wiarygodności $\\precsim$ dopuszcza funkcję rangi $F: H \\to \\mathbb{N}$ taką, że różnica rang dwóch historii jest niezmiennicza na dodanie wspólnej akcji: $F(ha) - F(h'a) = F(h) - F(h')$.
            </li>
            <li>
              <strong>Jednorodna Spójność Bayesowska (Uniformly Bayesian &bull; UB &bull; Definicja 12.8):</strong> Relatywne proporcje prawdopodobieństw wewnątrz klas równej wiarygodności są zachowane.
            </li>
          </ul>
          <div class="p-4 sm:p-5 bg-blue-50 border-2 border-blue-500/50 rounded-2xl space-y-3">
            <div class="flex items-center justify-between flex-wrap gap-2">
              <span class="font-mono font-bold text-blue-900 text-xs uppercase block">Twierdzenie 12.5 (Giacomo Bonanno, 2015 &bull; International Journal of Game Theory)</span>
              <span class="badge-tag bg-blue-600 text-white text-[10px]">Kamień Milowy Teorii Gier</span>
            </div>
            <p class="text-xs sm:text-sm text-blue-950 leading-relaxed font-semibold">
              Rozważmy dowolną skończoną grę w postaci ekstensywnej oraz ocenę $(\\sigma, \\mu)$. Następujące warunki są równoważne:
            </p>
            <div class="p-3 bg-white border border-blue-200 rounded-xl space-y-2 text-xs font-mono text-slate-800">
              <div>(A) Ocena $(\\sigma, \\mu)$ jest Równowagą Sekwencyjną Krepsa-Wilsona (SE).</div>
              <div class="text-center font-bold text-blue-600 text-sm">&Updownarrow</div>
              <div>(B) Ocena $(\\sigma, \\mu)$ jest Doskonałą Równowagą Bayesowską (PBE), która jest racjonalizowana przez porządek wiarygodności spełniający warunek Mierzalności Wyborów (Choice Measurability) oraz jest względem niego Jednorodnie Bayesowska (Uniformly Bayesian).</div>
            </div>
            <p class="text-xs text-blue-950 leading-relaxed">
              <strong>Dlaczego to twierdzenie jest przełomowe?</strong>
              Zamyka ono 33-letnią lukę w literaturze naukowej: uwalnia definicję Równowagi Sekwencyjnej Krepsa-Wilsona od sztucznych, nieintuicyjnych granic ciągów zaburzeń (drżenia rąk),
              zastępując je w 100% przejrzystymi, jakościowymi aksjomatami rewizji przekonań w duchu logiki epistemicznej AGM!
            </p>
          </div>
        </div>

        <!-- ZADANIE 12.11 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyróżnione Zadanie 12.11 (Wielostadiowa Gra Sygnalizacyjna i PBE)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 12.E &bull; s. 452</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Treść Zadania:</strong> Konstrukcja porządku wiarygodności $\\precsim$ i weryfikacja warunku Choice Measurability dla złożonego drzewa decyzyjnego z Rysunku 12.15 w podręczniku Bonanno, prowadząca do wykluczenia sztucznych równowag PBE niebędących równowagami Krepsa-Wilsona.
          </p>
        </div>
      </section>
    """
