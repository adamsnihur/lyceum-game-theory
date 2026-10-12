# Part 2: Chapters 4, 5, 6 for Lyceum Game Theory
# Zero em-dashes strictly enforced.

def get_chapter_4():
    return """
      <!-- ROZDZIAL 4: TEORIA OCZEKIWANEJ UZYTECZNOSCI -->
      <section id="rozdzial-4" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Czesc II &bull; Rozdzial 4</span>
          <span class="text-xs font-mono text-slate-400">Wyplaty Kardynalne &bull; Strony 158-185</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdzial 4: Teoria Oczekiwanej Uzytecznosci von Neumanna-Morgensterna</h3>

        <!-- 4.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            4.1. Loterie Pieniezne, Postawy Wobec Ryzyka i Miary Arrowa-Pratta
          </h4>
          <p>
            Gdy rezultaty gry wiaza sie z niepewnoscia i losowoscia, sama wartosc oczekiwana kwot nie wystarcza do przewidzenia zachowan decydenta.
            Formalnie <strong>loteria pieniezna (money lottery)</strong> to rozklad prawdopodobienstwa nad skonczonym zbiorem kwot:
          </p>
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 font-mono text-xs overflow-x-auto">
            $$L = \\begin{pmatrix} x_1 & x_2 & \\dots & x_m \\\\ p_1 & p_2 & \\dots & p_m \\end{pmatrix}, \\quad \\sum_{k=1}^m p_k = 1, \\quad p_k \\ge 0$$
          </div>
          <p>
            Wartosc oczekiwana loterii to $\\mathbb{E}[L] = \\sum_{k=1}^m p_k x_k$.
            Dla dwukrotnie rozniczkowalnej funkcji uzytecznosci majatku $U(w)$ postawy wobec ryzyka charakteryzowane sa przez relacje miedzy uzytecznoscia wartosci oczekiwanej a oczekiwana uzytecznoscia (Nierownosc Jensena):
          </p>
          <ul class="text-xs text-slate-600 space-y-1.5 list-disc list-inside">
            <li>
              <strong>Awersja do ryzyka (Risk Aversion):</strong> Decydent scisle woli pewna kwote $\\mathbb{E}[L]$ od udzialu w loterii $L$:
              $$U(\\mathbb{E}[L]) > \\mathbb{E}[U(L)] = \\sum_{k=1}^m p_k U(x_k)$$
              Odpowiada to <em>scisle wkleslej</em> funkcji uzytecznosci ($U''(w) < 0$).
            </li>
            <li>
              <strong>Neutralnosc wobec ryzyka (Risk Neutrality):</strong> Decydent jest obojetny miedzy pewna kwota a loteria ($U(\\mathbb{E}[L]) = \\mathbb{E}[U(L)]$), funkcja uzytecznosci jest liniowa ($U''(w) = 0$).
            </li>
            <li>
              <strong>Sklonnosc do ryzyka (Risk Loving):</strong> Decydent woli loterie od pewnej wyplaty ($U(\\mathbb{E}[L]) < \\mathbb{E}[U(L)]$), funkcja uzytecznosci jest <em>scisle wypukla</em> ($U''(w) > 0$).
            </li>
          </ul>
          <p>
            <strong>Ekwiwalent Pewnosci (Certainty Equivalent &bull; $CE(L)$):</strong> Pewna kwota pieniezna dajaca dokladnie taka sama uzytecznosc jak udzial w loterii: $U(CE(L)) = \\mathbb{E}[U(L)]$.
            Roznica $RP(L) = \\mathbb{E}[L] - CE(L)$ to <strong>premia za ryzyko (Risk Premium)</strong>.
          </p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 pt-2">
            <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-1 text-xs">
              <strong class="text-blue-700 block font-mono">Bezwzgledna Awersja do Ryzyka (CARA):</strong>
              Wspolczynnik Arrowa-Pratta: $r_A(w) = -\\frac{U''(w)}{U'(w)}$.
              Stala awersja bezwzgledna (CARA) opisana jest funkcja $U(w) = -e^{-\\alpha w}$ (gdzie $\\alpha > 0$). Wybor ubezpieczenia nie zalezy od poziomu wyjsciowego bogactwa.
            </div>
            <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-1 text-xs">
              <strong class="text-blue-700 block font-mono">Wzgledna Awersja do Ryzyka (CRRA):</strong>
              Wspolczynnik relatywny: $r_R(w) = -\\frac{w U''(w)}{U'(w)}$.
              Stala awersja wzgledna (CRRA): $U(w) = \\frac{w^{1-\\gamma}}{1-\\gamma}$ (dla $\\gamma \\ne 1$) oraz $U(w) = \\ln(w)$ (dla $\\gamma = 1$). Proporcja majatku lokowana w ryzykowne aktywa jest stala.
            </div>
          </div>
        </div>

        <!-- 4.2 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            4.2. Twierdzenie o Reprezentacji Uzytecznosci vNM i Niezmienniczosc Afiniczna
          </h4>
          <p>
            Niech $O$ bedzie zbiorem podstawowych rezultatow, a $\\mathcal{L}(O)$ zbiorem loterii nad $O$.
            Relacja preferencji $\\succsim$ nad $\\mathcal{L}(O)$ jest relacja vNM, jesli spelnia aksjomaty teorii uzytecznosci.
          </p>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Twierdzenie 4.1 (John von Neumann & Oskar Morgenstern, 1944)</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              Jesli preferencje $\\succsim$ nad loteriami spelniaja aksjomaty vNM, to istnieje funkcja uzytecznosci $U: O \\to \\mathbb{R}$ taka, ze dla dowolnych dwoch loterii $L, L' \\in \\mathcal{L}(O)$:
              $$L \\succ L' \\iff \\mathbb{E}[U(L)] > \\mathbb{E}[U(L')] \\quad \\text{oraz} \\quad L \\sim L' \\iff \\mathbb{E}[U(L)] = \\mathbb{E}[U(L')]$$
            </p>
          </div>
          <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-blue-800 text-xs block uppercase">Twierdzenie 4.2: Dodatnia Transformacja Afiniczna</span>
            <p class="text-xs text-blue-950 leading-relaxed">
              Funkcja uzytecznosci vNM jest okreslona na <strong>skali przedzialowej (kardynalnej)</strong>:
              funkcja $V: O \\to \\mathbb{R}$ reprezentuje te same preferencje vNM wtedy i tylko wtedy, gdy istnieja stale $a > 0$ oraz $b \\in \\mathbb{R}$ takie, ze:
              $$V(o) = a \\cdot U(o) + b \\quad \\forall o \\in O$$
              W przeciwienstwie do teorii porzadkowej, dowolne rosnace przeksztalcenie nieliniowe (np. podniesienie do kwadratu) zmienia relacje oczekiwanej uzytecznosci!
            </p>
          </div>
          <p class="text-xs text-slate-600">
            <strong>Uzytecznosc Znormalizowana (Normalized Utility):</strong> Dla skonczonego zbioru rezultatow mozemy zawsze ustalic $U(o_{\\text{worst}}) = 0$ oraz $U(o_{\\text{best}}) = 1$. Wtedy dla kazdego posredniego rezultatu $o$, uzytecznosc $U(o)$ to dokladnie prawdopodobienstwo $p$, przy ktorym decydent jest obojetny miedzy pewnym $o$ a loteria $[p \\cdot o_{\\text{best}} + (1-p) \\cdot o_{\\text{worst}}]$.
          </p>
        </div>

        <!-- 4.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            4.3. Aksjomaty vNM i Paradoksy Behawioralne (Allais i Ellsberg)
          </h4>
          <p>
            Twierdzenie vNM wynika z czterech scislych aksjomatow:
          </p>
          <ol class="text-xs text-slate-600 space-y-1 list-decimal list-inside pl-2">
            <li><strong>Zupelnosc i Przechodniosc:</strong> Porzadek nad wszystkimi mozliwymi loteriami.</li>
            <li><strong>Monotonicznosc (Monotonicity):</strong> Wyzsze prawdopodobienstwo najlepszego rezultatu jest scisle preferowane.</li>
            <li><strong>Ciaglosc (Continuity / Archimedean):</strong> Brak nieskonczenie dobrych ani nieskonczenie zlych rezultatow: dla kazdego $o$ istnieje $p \\in [0, 1]$ dajace obojetnosc z loteria skrajna.</li>
            <li><strong>Niezaleznosc (Independence / Sure-Thing Principle):</strong> Jesli $L_1 \\succ L_2$, to dla dowolnej trzeciej loterii $L_3$ i $\\alpha \\in (0, 1]$: $[\\alpha L_1 + (1-\\alpha)L_3] \\succ [\\alpha L_2 + (1-\\alpha)L_3]$.</li>
          </ol>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
            <div class="p-4 bg-rose-50 border border-rose-200 rounded-xl space-y-2">
              <span class="font-mono font-bold text-rose-900 text-xs block uppercase">Paradoks Maurice'a Allais (1953)</span>
              <p class="text-xs text-rose-950 leading-relaxed">
                Eksperyment z loteriami:
                $A = (1\\text{ mln USD}, 1.0)$ vs $B = (5\\text{ mln}, 0.10; 1\\text{ mln}, 0.89; 0, 0.01)$. Wiekszosc wybiera $A \\succ B$.
                Nastepnie: $C = (1\\text{ mln}, 0.11; 0, 0.89)$ vs $D = (5\\text{ mln}, 0.10; 0, 0.90)$. Wiekszosc wybiera $D \\succ C$.
                Podstawiajac uzytecznosci: $A \\succ B \\iff 0.11 U(1) > 0.10 U(5)$, podczas gdy $D \\succ C \\iff 0.10 U(5) > 0.11 U(1)$.
                Sprzecznosc ta dowodzi systematycznego naruszania aksjomatu niezaleznosci (efekt pewnosci).
              </p>
            </div>
            <div class="p-4 bg-amber-50 border border-amber-200 rounded-xl space-y-2">
              <span class="font-mono font-bold text-amber-900 text-xs block uppercase">Paradoks Daniela Ellsberga (1961)</span>
              <p class="text-xs text-amber-950 leading-relaxed">
                Urna z 30 kulami czerwonymi i 60 czarnymi lub zoltymi.
                Decydenci wola stawiac na kule o znanych obiektywnych prawdopodobienstwach niz na zdarzenia o nieznanej proporcji.
                Zjawisko to, zwane <strong>awersja do niejednoznacznosci (Ambiguity Aversion)</strong>, dowodzi ze w realnym swiecie niepewnosc Knightowska rozni sie jakosciowo od ryzyka probabilistycznego.
              </p>
            </div>
          </div>
        </div>

        <!-- ZADANIE 4.14 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyrznione Zadanie 4.14 (Zatruty Kielich i Kalibracja Ubezpieczenia)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 4.E &bull; s. 180</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Tresc Zadania:</strong> Decydent o majatku $W = 100$ i funkcji uzytecznosci $U(w) = \\sqrt{w}$ stoi w obliczu ryzyka kradziezy: z prawdopodobienstwem $p = 0.2$ traci 64 USD (zostaje z majatkiem 36 USD), a z prawdopodobienstwem $0.8$ nie traci nic.
            Zadanie wymaga obliczenia wartosci oczekiwanej straty, oczekiwanej uzytecznosci, ekwiwalentu pewnosci oraz maksymalnej skladki ubezpieczeniowej, jaka decydent zgodzi sie zaplacic.
          </p>
          <details class="text-xs bg-white p-3 rounded-lg border border-slate-200 cursor-pointer">
            <summary class="font-bold text-slate-800 select-none">Pokaz Scisle Obliczenia Krok po Kroku (Appendix 4.S Bonanno)</summary>
            <div class="mt-2 text-slate-700 space-y-2 leading-relaxed">
              <p>
                <strong>1. Wartosc oczekiwana majatku:</strong> $\\mathbb{E}[W] = 0.8 \\times 100 + 0.2 \\times 36 = 80 + 7.2 = 87.2$ USD. Oczekiwana strata wynosi $100 - 87.2 = 12.8$ USD.
              </p>
              <p>
                <strong>2. Oczekiwana uzytecznosc:</strong> $\\mathbb{E}[U] = 0.8 \\times \\sqrt{100} + 0.2 \\times \\sqrt{36} = 0.8 \\times 10 + 0.2 \\times 6 = 8 + 1.2 = 9.2$.
              </p>
              <p>
                <strong>3. Ekwiwalent pewnosci ($CE$):</strong> $\\sqrt{CE} = 9.2 \\implies CE = (9.2)^2 = 84.64$ USD.
              </p>
              <p>
                <strong>4. Maksymalna skladka ubezpieczeniowa:</strong> Decydent jest sklonny oddac caly majatek powyzej $CE$, czyli $P_{\\max} = 100 - 84.64 = 15.36$ USD.
                Poniewaz $15.36 > 12.8$, decydent placi premie za ryzyko $RP = 15.36 - 12.8 = 2.56$ USD ubezpieczycielowi, co stanowi fundament ekonomiczny calego sektora ubezpieczeniowego!
              </p>
            </div>
          </details>
        </div>
      </section>
    """

def get_chapter_5():
    return """
      <!-- ROZDZIAL 5: STRATEGIE MIESZANE W GRACH STRATEGICZNYCH -->
      <section id="rozdzial-5" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Czesc II &bull; Rozdzial 5</span>
          <span class="text-xs font-mono text-slate-400">Strategie Mieszane &bull; Strony 186-223</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdzial 5: Strategie Mieszane i Racjonalizowalnosc</h3>

        <!-- 5.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            5.1 - 5.2. Postac Strategiczna z Wyplatami Kardynalnymi i Strategie Mieszane
          </h4>
          <p>
            Gdy wyplaty sa uzytecznosciami vNM, gra w postaci strategicznej to $G = \\langle I, (S_1, \\dots, S_n), (u_1, \\dots, u_n) \\rangle$, gdzie $u_i: S \\to \\mathbb{R}$.
            <strong>Strategia mieszana (Mixed Strategy)</strong> gracza $i$ to rozklad prawdopodobienstwa $\\sigma_i \\in \\Delta(S_i)$:
          </p>
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 font-mono text-xs overflow-x-auto">
            $$\\sigma_i = (\\sigma_i(s_{i1}), \\dots, \\sigma_i(s_{im})), \\quad \\sum_{k=1}^m \\sigma_i(s_{ik}) = 1, \\quad \\sigma_i(s_{ik}) \\ge 0$$
          </div>
          <p>
            Zbior czystych strategii zagranych z dodatnim prawdopodobienstwem nazywamy <strong>nosnikiem (support)</strong>: $\\text{supp}(\\sigma_i) = \\{s_i \\in S_i : \\sigma_i(s_i) > 0\\}$.
            Oczekiwana wyplata gracza $i$ przy profilu strategii mieszanych $\\sigma = (\\sigma_1, \\dots, \\sigma_n)$ wynosi:
          </p>
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 font-mono text-xs overflow-x-auto">
            $$\\Pi_i(\\sigma) = \\sum_{s \\in S} \\left( \\prod_{j=1}^n \\sigma_j(s_j) \\right) u_i(s)$$
          </div>
        </div>

        <!-- 5.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            5.3. Twierdzenie Nasha i Zasada Obojetnosci (The Indifference Principle)
          </h4>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Twierdzenie 5.1 (John Nash, 1950, 1951) &bull; Istnienie Rownowagi</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              Kazda skonczona gra w postaci strategicznej o wyplatach kardynalnych posiada <strong>co najmniej jedna rownowage Nasha</strong> (w strategiach czystych lub mieszanych).
            </p>
          </div>
          <p>
            Jak wyznaczyc te rownowagi? Kluczem jest fundamentalne twierdzenie wyjasnione przez Bonanno:
          </p>
          <div class="p-4 bg-blue-50 border border-blue-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-blue-800 text-xs block uppercase">Twierdzenie 5.2 (Zasada Obojetnosci &bull; Bishop / Bonanno)</span>
            <p class="text-xs text-blue-950 leading-relaxed">
              Niech $\\sigma^*$ bedzie rownowaga Nasha. Wtedy dla kazdego gracza $i \\in I$ i dla <strong>dowolnych dwoch strategii czystych</strong> $a, b \\in \\text{supp}(\\sigma_i^*)$ z nosnika gracza $i$:
              $$\\Pi_i(a, \\sigma_{-i}^*) = \\Pi_i(b, \\sigma_{-i}^*) = \\Pi_i(\\sigma^*)$$
              Co wiecej, dla kazdej strategii czystej lezacej poza nosnikiem ($c \\notin \\text{supp}(\\sigma_i^*)$):
              $$\\Pi_i(c, \\sigma_{-i}^*) \\le \\Pi_i(\\sigma^*)$$
            </p>
          </div>
          <div class="p-3 sm:p-4 bg-amber-50/70 border border-amber-200 rounded-xl text-xs text-amber-950 leading-relaxed">
            <strong>Kluczowa Intuicja Filozoficzna:</strong>
            Gracz randomizuje swoje strategie <em>nie po to</em>, by uzyskac wyzsza wyplate dla siebie (jest zupelnie obojetny miedzy wszystkimi opcjami z nosnika!),
            lecz po to, by <strong>uczynic swojego rywala obojetnym</strong> miedzy jego wlasnymi strategiami!
          </div>
        </div>

        <!-- 5.4 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            5.4. Dominacja przez Strategie Mieszane i Twierdzenie Pearce'a (Racjonalizowalnosc)
          </h4>
          <p>
            W grach o wyplatach kardynalnych pojawia sie zjawisko niemozliwe w grach porzadkowych:
            <strong>czysta strategia moze byc scisle zdominowana przez pewna strategie mieszana</strong>, mimo ze nie jest zdominowana przez zadna pojedyncza strategie czysta!
          </p>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-slate-800 text-xs block uppercase">Twierdzenie 5.3 (David Pearce, 1984 / Douglas Bernheim, 1984)</span>
            <p class="text-xs text-slate-700 leading-relaxed">
              W dowolnej skonczonej dwuosobowej grze strategicznej:
              czysta strategia $s_i \\in S_i$ <em>nie jest najlepsza odpowiedzia</em> na zadna (czysta lub mieszana) strategie rywala $\\sigma_j \\in \\Delta(S_j)$
              wtedy i tylko wtedy, gdy $s_i$ jest <strong>scisle zdominowana przez pewna strategie mieszana</strong> $\\sigma_i \\in \\Delta(S_i)$.
            </p>
          </div>
          <p class="text-xs text-slate-600">
            Strategie, ktore przetrwaja nieskonczona iterowana eliminacje strategii scisle zdominowanych przez strategie mieszane, nazywamy <strong>strategiami racjonalizowalnymi (Rationalizable Strategies)</strong>.
          </p>
        </div>

        <!-- ZADANIE 5.15 -->
        <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 border-t border-slate-150 pt-4">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="font-mono font-bold text-blue-700 text-xs uppercase">Wyrznione Zadanie 5.15 (Tonacy Pies w Rzece Sacramento &bull; Efekt Widza)</span>
            <span class="badge-tag bg-blue-100 text-blue-800 text-[10px]">Appendix 5.E &bull; s. 211</span>
          </div>
          <p class="text-xs text-slate-700 leading-relaxed">
            <strong>Tresc Zadania:</strong> $n \\ge 2$ plywakow stoi na brzegu rzeki Sacramento i widzi tonacego psa.
            Jesli pies zostanie uratowany, kazdy plywak odczuwa satysfakcje $v > 0$.
            Wystarczy, ze <em>jeden</em> plywak wskoczy do lodowatej wody, aby uratowac psa. Koszt skoku wynosi $c$ ($0 < c < v$).
            Jesli nikt nie skoczy, wyplata kazdego wynosi 0.
            Zadanie wymaga wyznaczenia symetrycznej rownowagi w strategiach mieszanych oraz zbadania prawdopodobienstwa, ze pies utonie, w zaleznosci od liczby swiadkow $n$.
          </p>
          <details class="text-xs bg-white p-3 rounded-lg border border-slate-200 cursor-pointer">
            <summary class="font-bold text-slate-800 select-none">Pokaz Scisly Dowod i Rownanie Bystander Effect (Appendix 5.S Bonanno)</summary>
            <div class="mt-2 text-slate-700 space-y-2 leading-relaxed">
              <p>
                <strong>Krok 1: Warunek obojetnosci.</strong>
                Niech kazdy z pozostalych $n-1$ plywakow skacze z prawdopodobienstwem $p$.
                Jesli Gracz 1 skoczy (strategia czysta Skok), pies zostaje uratowany na pewno, a wyplata Gracza 1 wynosi $v - c$.
                Jesli Gracz 1 nie skoczy (strategia czysta Brzeg), otrzymuje $v$, jesli co najmniej jeden inny plywak skoczy, oraz 0, jesli nikt nie skoczy.
                Prawdopodobienstwo, ze nikt z $n-1$ rywali nie skoczy wynosi $(1-p)^{n-1}$.
                Oczekiwana wyplata z pozostania na brzegu: $\\Pi_1(\\text{Brzeg}) = v \\cdot [1 - (1-p)^{n-1}]$.
              </p>
              <p>
                <strong>Krok 2: Wyznaczenie $p^*$.</strong> Z Zasady Obojetnosci (Twierdzenie 5.2):
                $$v - c = v \\cdot [1 - (1-p)^{n-1}] \\iff v - c = v - v(1-p)^{n-1} \\iff v(1-p)^{n-1} = c$$
                $$(1-p)^{n-1} = \\frac{c}{v} \\implies 1 - p = \\left(\\frac{c}{v}\\right)^{\\frac{1}{n-1}} \\implies p^* = 1 - \\left(\\frac{c}{v}\\right)^{\\frac{1}{n-1}}$$
              </p>
              <p>
                <strong>Krok 3: Prawdopodobienstwo smierci psa ($P_{\\text{smierc}}$).</strong>
                Pies tonie wtedy i tylko wtedy, gdy <strong>zaden</strong> z $n$ plywakow nie skoczy:
                $$P_{\\text{smierc}} = (1 - p^*)^n = \\left[ \\left(\\frac{c}{v}\\right)^{\\frac{1}{n-1}} \\right]^n = \\left(\\frac{c}{v}\\right)^{\\frac{n}{n-1}}$$
                Poniewaz $\\frac{c}{v} < 1$, a wykladnik $\\frac{n}{n-1} = 1 + \\frac{1}{n-1}$ maleje wraz ze wzrostem $n$, wartosc $(c/v)^{\\frac{n}{n-1}}$ <strong>rosnie wraz z liczba swiadkow $n$</strong>!
              </p>
              <p>
                <strong>Wniosek spoleczny:</strong> Im wiecej ludzi obserwuje wypadek, tym wieksze ryzyko, ze nikt nie pomoze (zjawisko dyfuzji odpowiedzialnosci i Bystander Effect udowodnione scisle na gruncie teorii gier!).
              </p>
            </div>
          </details>
        </div>
      </section>
    """

def get_chapter_6():
    return """
      <!-- ROZDZIAL 6: DYNAMICZNE GRY KARDYNALNE I TWIERDZENIE KUHNA -->
      <section id="rozdzial-6" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Czesc II &bull; Rozdzial 6</span>
          <span class="text-xs font-mono text-slate-400">Gry Dynamiczne Kardynalne &bull; Strony 224-251</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Rozdzial 6: Dynamiczne Gry Kardynalne i Twierdzenie Kuhna</h3>

        <!-- 6.1 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            6.1. Strategie Behawioralne a Strategie Mieszane (Twierdzenie Kuhna)
          </h4>
          <p>
            W grach ekstensywnych gracz moze losowac na dwa zupelnie rozne sposoby:
          </p>
          <ul class="text-xs text-slate-600 space-y-1 list-disc list-inside">
            <li>
              <strong>Strategia mieszana (Mixed Strategy):</strong> Gracz przed rozpoczeciem gry losuje z kapelusza <em>jeden kompletny plan dzialania</em> $\\sigma_i \\in \\Delta(S_i)$ dla calego drzewa gry.
            </li>
            <li>
              <strong>Strategia behawioralna (Behavioral Strategy):</strong> Gracz w kazdym swoim zbiorze informacyjnym $h \\in \\mathcal{H}_i$ rzuca <em>niezalezna moneta</em>, wybierajac rozklad $\\beta_i(h) \\in \\Delta(A(h))$.
            </li>
          </ul>
          <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2">
            <span class="font-mono font-bold text-emerald-800 text-xs block uppercase">Twierdzenie 6.1 (Harold W. Kuhn, 1953) &bull; Rownowaznosc Strategii</span>
            <p class="text-xs text-emerald-950 leading-relaxed">
              W kazdej skonczonej grze w postaci ekstensywnej spelniajacej warunek <strong>doskonalej pamieci (Perfect Recall)</strong>:
              dla kazdej strategii mieszanej $\\sigma_i$ istnieje rownowazna strategia behawioralna $\\beta_i$ (i odwrotnie),
              ktora generuje dokladnie taki sam rozklad prawdopodobienstwa nad wszystkimi wezlami koncowymi $Z$ dla dowolnych strategii rywali!
            </p>
            <div class="p-3 bg-white border border-emerald-200 rounded-lg text-xs font-mono text-slate-800">
              Formuła Iloczynowa Kuhna dla węzła końcowego $z \\in Z$:
              $$P(z | \\beta) = \\prod_{a \\in \\text{path}(z)} \\beta_{\\iota(a)}(a | h(a))$$
            </div>
          </div>
          <p class="text-xs text-slate-600">
            Znaczenie praktyczne: Przestrzen strategii behawioralnych ma wymiar $\\sum |A(h)|$ (liniowy), podczas gdy przestrzen strategii mieszanych ma wymiar $\\prod |A(h)|$ (wykladniczy). Twierdzenie Kuhna pozwala uniknac klatwy wymiarowosci!
          </p>
        </div>

        <!-- 6.3 -->
        <div class="space-y-3 text-xs sm:text-sm text-slate-700 leading-relaxed border-t border-slate-150 pt-4">
          <h4 class="font-bold text-slate-900 text-sm sm:text-base flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            6.3. Ograniczenia i Zalamanie Sie Rownowagi Doskonalej w Podgrach (SPE)
          </h4>
          <p>
            Mimo elegancji, pojęcie Subgame-Perfect Equilibrium (SPE) okazuje sie powaznie ułomne w grach dynamicznych z niedoskonala informacja.
            Rozwazmy gre, w ktorej <strong>jedyna podgra jest cala gra</strong> (np. gra Seltena Horse lub dowolna gra sygnalizacyjna):
          </p>
          <div class="p-4 bg-rose-50 border border-rose-200 rounded-xl space-y-2 text-xs text-rose-950 leading-relaxed">
            <strong class="font-mono uppercase block text-rose-900">Dlaczego SPE zawodzi w grach bez podgier wlasciwych?</strong>
            Poniewaz gra nie zawiera wlasciwych podgier, wymog SPE redukuje sie wylacznie do warunku zwyklej rownowagi Nasha calej gry!
            W konsekwencji SPE dopuszcza profile strategii, w ktorych gracz podejmujacy decyzje w nieosiaganym zbiorze informacyjnym wybiera dzialanie <strong>scisle zdominowane</strong> w tym zbiorze!
            SPE nie nakłada bowiem zadnych ograniczen na to, w co gracze <em>wierza</em>, gdy znajda sie poza sciezka rownowagi.
          </div>
          <p>
            Ta fundamentalna luka doprowadzila do powstania nowoczesnej teorii uszczegolawiania rownowag (Refinements): Słabej Równowagi Sekwencyjnej (Rozdział 10), Równowagi Sekwencyjnej Krepsa-Wilsona (Rozdział 11) oraz Doskonałej Równowagi Bayesowskiej Bonanno (Rozdział 12).
          </p>
        </div>
      </section>
    """
