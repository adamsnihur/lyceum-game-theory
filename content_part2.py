# Part 2: Chapters 4, 5, 6 for Lyceum Game Theory
# Zero em-dashes strictly enforced.

def get_chapter_4():
    return """
      <!-- ROZDZIAŁ 4: TEORIA OCZEKIWANEJ UŻYTECZNOŚCI -->
      <section id="rozdzial-4" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Część II &bull; Rozdział 4</span>
          <span class="text-xs font-mono text-slate-400">Wypłaty Kardynalne &bull; Strony 158-185</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdział 4: Teoria Oczekiwanej Użyteczności von Neumanna-Morgensterna</h3>

        <!-- 4.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            4.1. Loterie Pieniężne, Postawy Wobec Ryzyka i Miary Arrowa-Pratta
          </h4>
          <p>
            Gdy rezultaty gry wiążą się z niepewnością i losowością, sama wartość oczekiwana kwot nie wystarcza do przewidzenia zachowań decydenta.
            Formalnie <strong>loteria pieniężna (money lottery)</strong> to rozkład prawdopodobieństwa nad skończonym zbiorem kwot:
          </p>
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 font-mono text-xs overflow-x-auto">
            $$L = \\begin{pmatrix} x_1 & x_2 & \\dots & x_m \\\\ p_1 & p_2 & \\dots & p_m \\end{pmatrix}, \\quad \\sum_{k=1}^m p_k = 1, \\quad p_k \\ge 0$$
          </div>
          <p>
            Wartość oczekiwana loterii to $\\mathbb{E}[L] = \\sum_{k=1}^m p_k x_k$.
            Dla dwukrotnie różniczkowalnej funkcji użyteczności majątku $U(w)$ postawy wobec ryzyka charakteryzowane są przez relację między użytecznością wartości oczekiwanej a oczekiwaną użytecznością (Nierówność Jensena):
          </p>
          <ul class="text-xs text-slate-600 space-y-1.5 list-disc list-inside">
            <li>
              <strong>Awersja do ryzyka (Risk Aversion):</strong> Decydent ściśle woli pewną kwotę $\\mathbb{E}[L]$ od udziału w loterii $L$:
              $$U(\\mathbb{E}[L]) > \\mathbb{E}[U(L)] = \\sum_{k=1}^m p_k U(x_k)$$
              Odpowiada to <em>ściśle wklęsłej</em> funkcji użyteczności ($U''(w) < 0$).
            </li>
            <li>
              <strong>Neutralność wobec ryzyka (Risk Neutrality):</strong> Decydent jest obojętny między pewną kwotą a loterią ($U(\\mathbb{E}[L]) = \\mathbb{E}[U(L)]$), funkcja użyteczności jest liniowa ($U''(w) = 0$).
            </li>
            <li>
              <strong>Skłonność do ryzyka (Risk Loving):</strong> Decydent woli loterię od pewnej wypłaty ($U(\\mathbb{E}[L]) < \\mathbb{E}[U(L)]$), funkcja użyteczności jest <em>ściśle wypukła</em> ($U''(w) > 0$).
            </li>
          </ul>
          <p>
            <strong>Ekwiwalent Pewności (Certainty Equivalent &bull; $CE(L)$):</strong> Pewna kwota pieniężna dająca dokładnie taką samą użyteczność jak udział w loterii: $U(CE(L)) = \\mathbb{E}[U(L)]$.
            Różnica $RP(L) = \\mathbb{E}[L] - CE(L)$ to <strong>premia za ryzyko (Risk Premium)</strong>.
          </p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 pt-2">
            <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-1 text-xs">
              <strong class="text-blue-700 block font-mono">Bezwzględna Awersja do Ryzyka (CARA):</strong>
              Współczynnik Arrowa-Pratta: $r_A(w) = -\\frac{U''(w)}{U'(w)}$.
              Stała awersja bezwzględna (CARA) opisana jest funkcją $U(w) = -e^{-\\alpha w}$ (gdzie $\\alpha > 0$). Wybór ubezpieczenia nie zależy od poziomu wyjściowego bogactwa.
            </div>
            <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-1 text-xs">
              <strong class="text-blue-700 block font-mono">Względna Awersja do Ryzyka (CRRA):</strong>
              Współczynnik relatywny: $r_R(w) = -\\frac{w U''(w)}{U'(w)}$.
              Stała awersja względna (CRRA): $U(w) = \\frac{w^{1-\\gamma}}{1-\\gamma}$ (dla $\\gamma \\ne 1$) oraz $U(w) = \\ln(w)$ (dla $\\gamma = 1$). Proporcja majątku lokowana w ryzykowne aktywa jest stała.
            </div>
          </div>
        </div>

        <!-- 4.2 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            4.2. Twierdzenie o Reprezentacji Użyteczności vNM i Niezmienniczość Afiniczna
          </h4>
          <p>
            Niech $O$ będzie zbiorem podstawowych rezultatów, a $\\mathcal{L}(O)$ zbiorem loterii nad $O$.
            Relacja preferencji $\\succsim$ nad $\\mathcal{L}(O)$ jest relacją vNM, jeśli spełnia aksjomaty teorii użyteczności.
          </p>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Twierdzenie 4.1 (John von Neumann & Oskar Morgenstern, 1944)</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              Jeśli preferencje $\\succsim$ nad loteriami spełniają aksjomaty vNM, to istnieje funkcja użyteczności $U: O \\to \\mathbb{R}$ taka, że dla dowolnych dwóch loterii $L, L' \\in \\mathcal{L}(O)$:
              $$L \\succ L' \\iff \\mathbb{E}[U(L)] > \\mathbb{E}[U(L')] \\quad \\text{oraz} \\quad L \\sim L' \\iff \\mathbb{E}[U(L)] = \\mathbb{E}[U(L')]$$
            </p>
          </div>
          <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-blue-800 text-xs block uppercase">Twierdzenie 4.2: Dodatnia Transformacja Afiniczna</span>
            <p class="text-xs text-blue-950 leading-relaxed">
              Funkcja użyteczności vNM jest określona na <strong>skali przedziałowej (kardynalnej)</strong>:
              funkcja $V: O \\to \\mathbb{R}$ reprezentuje te same preferencje vNM wtedy i tylko wtedy, gdy istnieją stałe $a > 0$ oraz $b \\in \\mathbb{R}$ takie, że:
              $$V(o) = a \\cdot U(o) + b \\quad \\forall o \\in O$$
              W przeciwieństwie do teorii porządkowej, dowolne rosnące przekształcenie nieliniowe (np. podniesienie do kwadratu) zmienia relację oczekiwanej użyteczności!
            </p>
          </div>
          <p class="text-xs text-slate-600">
            <strong>Użyteczność Znormalizowana (Normalized Utility):</strong> Dla skończonego zbioru rezultatów możemy zawsze ustalić $U(o_{\\text{worst}}) = 0$ oraz $U(o_{\\text{best}}) = 1$. Wtedy dla każdego pośredniego rezultatu $o$, użyteczność $U(o)$ to dokładnie prawdopodobieństwo $p$, przy którym decydent jest obojętny między pewnym $o$ a loterią $[p \\cdot o_{\\text{best}} + (1-p) \\cdot o_{\\text{worst}}]$.
          </p>
        </div>

        <!-- 4.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            4.3. Aksjomaty vNM i Paradoksy Behawioralne (Allais i Ellsberg)
          </h4>
          <p>
            Twierdzenie vNM wynika z czterech ścisłych aksjomatów:
          </p>
          <ol class="text-xs text-slate-600 space-y-1 list-decimal list-inside pl-2">
            <li><strong>Zupełność i Przechodniość:</strong> Porządek nad wszystkimi możliwymi loteriami.</li>
            <li><strong>Monotoniczność (Monotonicity):</strong> Wyższe prawdopodobieństwo najlepszego rezultatu jest ściśle preferowane.</li>
            <li><strong>Ciągłość (Continuity / Archimedean):</strong> Brak nieskończenie dobrych ani nieskończenie złych rezultatów: dla każdego $o$ istnieje $p \\in [0, 1]$ dające obojętność z loterią skrajną.</li>
            <li><strong>Niezależność (Independence / Sure-Thing Principle):</strong> Jeśli $L_1 \\succ L_2$, to dla dowolnej trzeciej loterii $L_3$ i $\\alpha \\in (0, 1]$: $[\\alpha L_1 + (1-\\alpha)L_3] \\succ [\\alpha L_2 + (1-\\alpha)L_3]$.</li>
          </ol>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
            <div class="p-4 bg-rose-50 border border-rose-200 rounded-xl space-y-2">
              <span class="font-mono font-bold text-rose-900 text-xs block uppercase">Paradoks Maurice'a Allais (1953)</span>
              <p class="text-xs text-rose-950 leading-relaxed">
                Eksperyment z loteriami:
                $A = (1\\text{ mln USD}, 1.0)$ vs $B = (5\\text{ mln}, 0.10; 1\\text{ mln}, 0.89; 0, 0.01)$. Większość wybiera $A \\succ B$.
                Następnie: $C = (1\\text{ mln}, 0.11; 0, 0.89)$ vs $D = (5\\text{ mln}, 0.10; 0, 0.90)$. Większość wybiera $D \\succ C$.
                Podstawiając użyteczności: $A \\succ B \\iff 0.11 U(1) > 0.10 U(5)$, podczas gdy $D \\succ C \\iff 0.10 U(5) > 0.11 U(1)$.
                Sprzeczność ta dowodzi systematycznego naruszania aksjomatu niezależności (efekt pewności).
              </p>
            </div>
            <div class="p-4 bg-amber-50 border border-amber-200 rounded-xl space-y-2">
              <span class="font-mono font-bold text-amber-900 text-xs block uppercase">Paradoks Daniela Ellsberga (1961)</span>
              <p class="text-xs text-amber-950 leading-relaxed">
                Urna z 30 kulami czerwonymi i 60 czarnymi lub żółtymi.
                Decydenci wolą stawiać na kule o znanych obiektywnych prawdopodobieństwach niż na zdarzenia o nieznanej proporcji.
                Zjawisko to, zwane <strong>awersją do niejednoznaczności (Ambiguity Aversion)</strong>, dowodzi, że w realnym świecie niepewność Knightowska różni się jakościowo od ryzyka probabilistycznego.
              </p>
            </div>
          </div>
        </div>

        <!-- ZADANIE 4.14 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyróżnione Zadanie 4.14 (Zatruty Kielich i Kalibracja Ubezpieczenia)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 4.E &bull; s. 180</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Treść Zadania:</strong> Decydent o majątku $W = 100$ i funkcji użyteczności $U(w) = \\sqrt{w}$ stoi w obliczu ryzyka kradzieży: z prawdopodobieństwem $p = 0.2$ traci 64 USD (zostaje z majątkiem 36 USD), a z prawdopodobieństwem $0.8$ nie traci nic.
            Zadanie wymaga obliczenia wartości oczekiwanej straty, oczekiwanej użyteczności, ekwiwalentu pewności oraz maksymalnej składki ubezpieczeniowej, jaką decydent zgodzi się zapłacić.
          </p>
          <details class="text-xs bg-white p-3 rounded-lg border border-slate-200 cursor-pointer">
            <summary class="font-bold text-slate-800 select-none">Pokaż Ścisłe Obliczenia Krok po Kroku (Appendix 4.S Bonanno)</summary>
            <div class="mt-2 text-slate-700 space-y-2 leading-relaxed">
              <p>
                <strong>1. Wartość oczekiwana majątku:</strong> $\\mathbb{E}[W] = 0.8 \\times 100 + 0.2 \\times 36 = 80 + 7.2 = 87.2$ USD. Oczekiwana strata wynosi $100 - 87.2 = 12.8$ USD.
              </p>
              <p>
                <strong>2. Oczekiwana użyteczność:</strong> $\\mathbb{E}[U] = 0.8 \\times \\sqrt{100} + 0.2 \\times \\sqrt{36} = 0.8 \\times 10 + 0.2 \\times 6 = 8 + 1.2 = 9.2$.
              </p>
              <p>
                <strong>3. Ekwiwalent pewności ($CE$):</strong> $\\sqrt{CE} = 9.2 \\implies CE = (9.2)^2 = 84.64$ USD.
              </p>
              <p>
                <strong>4. Maksymalna składka ubezpieczeniowa:</strong> Decydent jest skłonny oddać cały majątek powyżej $CE$, czyli $P_{\\max} = 100 - 84.64 = 15.36$ USD.
                Ponieważ $15.36 > 12.8$, decydent płaci premię za ryzyko $RP = 15.36 - 12.8 = 2.56$ USD ubezpieczycielowi, co stanowi fundament ekonomiczny całego sektora ubezpieczeniowego!
              </p>
            </div>
          </details>
        </div>
      </section>
    """

def get_chapter_5():
    return """
      <!-- ROZDZIAŁ 5: STRATEGIE MIESZANE W GRACH STRATEGICZNYCH -->
      <section id="rozdzial-5" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Część II &bull; Rozdział 5</span>
          <span class="text-xs font-mono text-slate-400">Strategie Mieszane &bull; Strony 186-223</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdział 5: Strategie Mieszane i Racjonalizowalność</h3>

        <!-- 5.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            5.1 - 5.2. Postać Strategiczna z Wypłatami Kardynalnymi i Strategie Mieszane
          </h4>
          <p>
            Gdy wypłaty są użytecznościami vNM, gra w postaci strategicznej to $G = \\langle I, (S_1, \\dots, S_n), (u_1, \\dots, u_n) \\rangle$, gdzie $u_i: S \\to \\mathbb{R}$.
            <strong>Strategia mieszana (Mixed Strategy)</strong> gracza $i$ to rozkład prawdopodobieństwa $\\sigma_i \\in \\Delta(S_i)$:
          </p>
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 font-mono text-xs overflow-x-auto">
            $$\\sigma_i = (\\sigma_i(s_{i1}), \\dots, \\sigma_i(s_{im})), \\quad \\sum_{k=1}^m \\sigma_i(s_{ik}) = 1, \\quad \\sigma_i(s_{ik}) \\ge 0$$
          </div>
          <p>
            Zbiór czystych strategii zagranych z dodatnim prawdopodobieństwem nazywamy <strong>nośnikiem (support)</strong>: $\\text{supp}(\\sigma_i) = \\{s_i \\in S_i : \\sigma_i(s_i) > 0\\}$.
            Oczekiwana wypłata gracza $i$ przy profilu strategii mieszanych $\\sigma = (\\sigma_1, \\dots, \\sigma_n)$ wynosi:
          </p>
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 font-mono text-xs overflow-x-auto">
            $$\\Pi_i(\\sigma) = \\sum_{s \\in S} \\left( \\prod_{j=1}^n \\sigma_j(s_j) \\right) u_i(s)$$
          </div>
        </div>

        <!-- 5.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            5.3. Twierdzenie Nasha i Zasada Obojętności (The Indifference Principle)
          </h4>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Twierdzenie 5.1 (John Nash, 1950, 1951) &bull; Istnienie Równowagi</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              Każda skończona gra w postaci strategicznej o wypłatach kardynalnych posiada <strong>co najmniej jedną równowagę Nasha</strong> (w strategiach czystych lub mieszanych).
            </p>
          </div>
          <p>
            Jak wyznaczyć te równowagi? Kluczem jest fundamentalne twierdzenie wyjaśnione przez Bonanno:
          </p>
          <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-blue-800 text-xs block uppercase">Twierdzenie 5.2 (Zasada Obojętności &bull; Bishop / Bonanno)</span>
            <p class="text-xs text-blue-950 leading-relaxed">
              Niech $\\sigma^*$ będzie równowagą Nasha. Wtedy dla każdego gracza $i \\in I$ i dla <strong>dowolnych dwóch strategii czystych</strong> $a, b \\in \\text{supp}(\\sigma_i^*)$ z nośnika gracza $i$:
              $$\\Pi_i(a, \\sigma_{-i}^*) = \\Pi_i(b, \\sigma_{-i}^*) = \\Pi_i(\\sigma^*)$$
              Co więcej, dla każdej strategii czystej leżącej poza nośnikiem ($c \\notin \\text{supp}(\\sigma_i^*)$):
              $$\\Pi_i(c, \\sigma_{-i}^*) \\le \\Pi_i(\\sigma^*)$$
            </p>
          </div>
          <div class="p-3 sm:p-4 bg-amber-50/70 border border-amber-200 rounded-xl text-xs text-amber-950 leading-relaxed">
            <strong>Kluczowa Intuicja Filozoficzna:</strong>
            Gracz randomizuje swoje strategie <em>nie po to</em>, by uzyskać wyższą wypłatę dla siebie (jest zupełnie obojętny między wszystkimi opcjami z nośnika!),
            lecz po to, by <strong>uczynić swojego rywala obojętnym</strong> między jego własnymi strategiami!
          </div>
        </div>

        <!-- 5.4 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            5.4. Dominacja przez Strategie Mieszane i Twierdzenie Pearce'a (Racjonalizowalność)
          </h4>
          <p>
            W grach o wypłatach kardynalnych pojawia się zjawisko niemożliwe w grach porządkowych:
            <strong>czysta strategia może być ściśle zdominowana przez pewną strategię mieszaną</strong>, mimo że nie jest zdominowana przez żadną pojedynczą strategię czystą!
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Twierdzenie 5.3 (David Pearce, 1984 / Douglas Bernheim, 1984)</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              W dowolnej skończonej dwuosobowej grze strategicznej:
              czysta strategia $s_i \\in S_i$ <em>nie jest najlepszą odpowiedzią</em> na żadną (czystą lub mieszaną) strategię rywala $\\sigma_j \\in \\Delta(S_j)$
              wtedy i tylko wtedy, gdy $s_i$ jest <strong>ściśle zdominowana przez pewną strategię mieszaną</strong> $\\sigma_i \\in \\Delta(S_i)$.
            </p>
          </div>
          <p class="text-xs text-slate-600">
            Strategie, które przetrwają nieskończoną iterowaną eliminację strategii ściśle zdominowanych przez strategie mieszane, nazywamy <strong>strategiami racjonalizowalnymi (Rationalizable Strategies)</strong>.
          </p>
        </div>

        <!-- ZADANIE 5.15 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyróżnione Zadanie 5.15 (Tonący Pies w Rzece Sacramento &bull; Efekt Widza)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 5.E &bull; s. 211</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Treść Zadania:</strong> $n \\ge 2$ pływaków stoi na brzegu rzeki Sacramento i widzi tonącego psa.
            Jeśli pies zostanie uratowany, każdy pływak odczuwa satysfakcję $v > 0$.
            Wystarczy, że <em>jeden</em> pływak wskoczy do lodowatej wody, aby uratować psa. Koszt skoku wynosi $c$ ($0 < c < v$).
            Jeśli nikt nie skoczy, wypłata każdego wynosi 0.
            Zadanie wymaga wyznaczenia symetrycznej równowagi w strategiach mieszanych oraz zbadania prawdopodobieństwa, że pies utonie, w zależności od liczby świadków $n$.
          </p>
          <details class="text-xs bg-white p-3 rounded-lg border border-slate-200 cursor-pointer">
            <summary class="font-bold text-slate-800 select-none">Pokaż Ścisły Dowód i Równanie Bystander Effect (Appendix 5.S Bonanno)</summary>
            <div class="mt-2 text-slate-700 space-y-2 leading-relaxed">
              <p>
                <strong>Krok 1: Warunek obojętności.</strong>
                Niech każdy z pozostałych $n-1$ pływaków skacze z prawdopodobieństwem $p$.
                Jeśli Gracz 1 skoczy (strategia czysta Skok), pies zostaje uratowany na pewno, a wypłata Gracza 1 wynosi $v - c$.
                Jeśli Gracz 1 nie skoczy (strategia czysta Brzeg), otrzymuje $v$, jeśli co najmniej jeden inny pływak skoczy, oraz 0, jeśli nikt nie skoczy.
                Prawdopodobieństwo, że nikt z $n-1$ rywali nie skoczy wynosi $(1-p)^{n-1}$.
                Oczekiwana wypłata z pozostania na brzegu: $\\Pi_1(\\text{Brzeg}) = v \\cdot [1 - (1-p)^{n-1}]$.
              </p>
              <p>
                <strong>Krok 2: Wyznaczenie $p^*$.</strong> Z Zasady Obojętności (Twierdzenie 5.2):
                $$v - c = v \\cdot [1 - (1-p)^{n-1}] \\iff v - c = v - v(1-p)^{n-1} \\iff v(1-p)^{n-1} = c$$
                $$(1-p)^{n-1} = \\frac{c}{v} \\implies 1 - p = \\left(\\frac{c}{v}\\right)^{\\frac{1}{n-1}} \\implies p^* = 1 - \\left(\\frac{c}{v}\\right)^{\\frac{1}{n-1}}$$
              </p>
              <p>
                <strong>Krok 3: Prawdopodobieństwo śmierci psa ($P_{\\text{smierc}}$).</strong>
                Pies tonie wtedy i tylko wtedy, gdy <strong>żaden</strong> z $n$ pływaków nie skoczy:
                $$P_{\\text{smierc}} = (1 - p^*)^n = \\left[ \\left(\\frac{c}{v}\\right)^{\\frac{1}{n-1}} \\right]^n = \\left(\\frac{c}{v}\\right)^{\\frac{n}{n-1}}$$
                Ponieważ $\\frac{c}{v} < 1$, a wykładnik $\\frac{n}{n-1} = 1 + \\frac{1}{n-1}$ maleje wraz ze wzrostem $n$, wartość $(c/v)^{\\frac{n}{n-1}}$ <strong>rośnie wraz z liczbą świadków $n$</strong>!
              </p>
              <p>
                <strong>Wniosek społeczny:</strong> Im więcej ludzi obserwuje wypadek, tym większe ryzyko, że nikt nie pomoże (zjawisko dyfuzji odpowiedzialności i Bystander Effect udowodnione ściśle na gruncie teorii gier!).
              </p>
            </div>
          </details>
        </div>
      </section>
    """

def get_chapter_6():
    return """
      <!-- ROZDZIAŁ 6: DYNAMICZNE GRY KARDYNALNE I TWIERDZENIE KUHNA -->
      <section id="rozdzial-6" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Część II &bull; Rozdział 6</span>
          <span class="text-xs font-mono text-slate-400">Gry Dynamiczne Kardynalne &bull; Strony 224-251</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdział 6: Dynamiczne Gry Kardynalne i Twierdzenie Kuhna</h3>

        <!-- 6.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            6.1. Strategie Behawioralne a Strategie Mieszane (Twierdzenie Kuhna)
          </h4>
          <p>
            W grach ekstensywnych gracz może losować na dwa zupełnie różne sposoby:
          </p>
          <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside">
            <li>
              <strong>Strategia mieszana (Mixed Strategy):</strong> Gracz przed rozpoczęciem gry losuje z kapelusza <em>jeden kompletny plan działania</em> $\\sigma_i \\in \\Delta(S_i)$ dla całego drzewa gry.
            </li>
            <li>
              <strong>Strategia behawioralna (Behavioral Strategy):</strong> Gracz w każdym swoim zbiorze informacyjnym $h \\in \\mathcal{H}_i$ rzuca <em>niezależną monetą</em>, wybierając rozkład $\\beta_i(h) \\in \\Delta(A(h))$.
            </li>
          </ul>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Twierdzenie 6.1 (Harold W. Kuhn, 1953) &bull; Równoważność Strategii</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              W każdej skończonej grze w postaci ekstensywnej spełniającej warunek <strong>doskonałej pamięci (Perfect Recall)</strong>:
              dla każdej strategii mieszanej $\\sigma_i$ istnieje równoważna strategia behawioralna $\\beta_i$ (i odwrotnie),
              która generuje dokładnie taki sam rozkład prawdopodobieństwa nad wszystkimi węzłami końcowymi $Z$ dla dowolnych strategii rywali!
            </p>
            <div class="p-3 bg-white border border-emerald-200 rounded-lg text-xs font-mono text-slate-800">
              Formuła Iloczynowa Kuhna dla węzła końcowego $z \\in Z$:
              $$P(z | \\beta) = \\prod_{a \\in \\text{path}(z)} \\beta_{\\iota(a)}(a | h(a))$$
            </div>
          </div>
          <p class="text-xs text-slate-600">
            Znaczenie praktyczne: Przestrzeń strategii behawioralnych ma wymiar $\\sum |A(h)|$ (liniowy), podczas gdy przestrzeń strategii mieszanych ma wymiar $\\prod |A(h)|$ (wykładniczy). Twierdzenie Kuhna pozwala uniknąć klątwy wymiarowości!
          </p>
        </div>

        <!-- 6.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            6.3. Ograniczenia i Załamanie Się Równowagi Doskonałej w Podgrach (SPE)
          </h4>
          <p>
            Mimo elegancji, pojęcie Subgame-Perfect Equilibrium (SPE) okazuje się poważnie ułomne w grach dynamicznych z niedoskonałą informacją.
            Rozważmy grę, w której <strong>jedyną podgrą jest cała gra</strong> (np. gra Seltena Horse lub dowolna gra sygnalizacyjna):
          </p>
          <div class="p-4 bg-rose-50 border border-rose-200 rounded-xl space-y-2 text-xs text-rose-950 leading-relaxed">
            <strong class="font-mono uppercase block text-rose-900">Dlaczego SPE zawodzi w grach bez podgier właściwych?</strong>
            Ponieważ gra nie zawiera właściwych podgier, wymóg SPE redukuje się wyłącznie do warunku zwykłej równowagi Nasha całej gry!
            W konsekwencji SPE dopuszcza profile strategii, w których gracz podejmujący decyzję w nieosiąganym zbiorze informacyjnym wybiera działanie <strong>ściśle zdominowane</strong> w tym zbiorze!
            SPE nie nakłada bowiem żadnych ograniczeń na to, w co gracze <em>wierzą</em>, gdy znajdą się poza ścieżką równowagi.
          </div>
          <p>
            Ta fundamentalna luka doprowadziła do powstania nowoczesnej teorii uszczegóławiania równowag (Refinements): Słabej Równowagi Sekwencyjnej (Rozdział 10), Równowagi Sekwencyjnej Krepsa-Wilsona (Rozdział 11) oraz Doskonałej Równowagi Bayesowskiej Bonanno (Rozdział 12).
          </p>
        </div>
      </section>
    """
