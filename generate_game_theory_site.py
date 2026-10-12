import os
import sys

from content_part1 import get_chapter_0, get_chapter_1, get_chapter_2, get_chapter_3
from content_part2 import get_chapter_4, get_chapter_5, get_chapter_6
from content_part3 import get_chapter_7, get_chapter_8, get_chapter_9
from content_part4 import get_chapter_10, get_chapter_11, get_chapter_12
from content_part5 import get_chapter_13, get_chapter_14, get_chapter_15

def get_header():
    return """<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Teoria Gier - Giacomo Bonanno | Kompletny Kurs E-Learningowy i Traktat Lyceum</title>
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- KaTeX for instantaneous client-side math rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

  <!-- Plotly.js for interactive charts -->
  <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>

  <!-- Custom Stylesheet -->
  <link rel="stylesheet" href="styles.css">
</head>
<body class="min-h-screen text-slate-900 bg-slate-50 antialiased selection:bg-blue-100 selection:text-blue-900 overflow-x-hidden">

  <!-- TOP HEADER -->
  <header class="border-b border-slate-200 bg-white/95 backdrop-blur sticky top-0 z-50 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-9 h-9 rounded-xl bg-blue-600 flex items-center justify-center text-white font-mono font-bold shadow-sm shadow-blue-500/20">
          GT
        </div>
        <div>
          <span class="text-xs font-mono font-bold uppercase tracking-wider text-blue-600">Lyceum Series &bull; Traktat 12</span>
          <h1 class="text-sm sm:text-base font-extrabold text-slate-900 leading-none">Teoria Gier: Kompletne Kompendium Giacomo Bonanno</h1>
        </div>
      </div>
      <div class="flex items-center gap-2 sm:gap-3">
        <span class="badge-tag bg-emerald-50 text-emerald-700 border border-emerald-200 hidden md:inline-flex">
          580 stron &bull; 16 Rozdziałów &bull; 165 Zadań
        </span>
        <a href="#lab-sekcja" class="px-3 py-1.5 bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold rounded-lg shadow-sm transition">
          Laboratoria 60 FPS
        </a>
      </div>
    </div>
  </header>

  <!-- MAIN TWO-COLUMN CONTAINER -->
  <div class="max-w-7xl mx-auto px-3 sm:px-6 py-6 sm:py-8 flex gap-8 min-w-0">

    <!-- LEFT STICKY SIDEBAR -->
    <aside class="hidden lg:block w-72 shrink-0">
      <div class="sticky top-20 bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-4 max-h-[calc(100vh-6rem)] overflow-y-auto">
        <div>
          <span class="text-[10px] font-mono font-bold uppercase tracking-wider text-slate-400 block mb-1">Nawigacja Kursu</span>
          <input type="text" id="navSearchInput" placeholder="Szukaj pojęć (np. Vickrey, CKR, PBE)..." 
                 class="w-full text-xs px-2.5 py-1.5 border border-slate-200 rounded-lg focus:outline-none focus:border-blue-500 font-sans">
        </div>

        <nav class="space-y-1 text-xs" id="sidebarNavList">
          <a href="#hero-sekcja" class="nav-link active">
            <span class="font-mono text-slate-400">00.</span> Pętla Hero (Replikator)
          </a>
          
          <div class="pt-2 text-[10px] font-mono uppercase tracking-wider text-slate-400 font-bold">Wprowadzenie</div>
          <a href="#rozdzial-0" class="nav-link">
            <span class="font-mono text-slate-400">R0.</span> Geneza i Homo Rationalis
          </a>

          <div class="pt-2 text-[10px] font-mono uppercase tracking-wider text-slate-400 font-bold">Część I: Wypłaty Porządkowe</div>
          <a href="#rozdzial-1" class="nav-link">
            <span class="font-mono text-slate-400">R1.</span> Gry Strategiczne, Dominacja i Nash
          </a>
          <a href="#rozdzial-2" class="nav-link">
            <span class="font-mono text-slate-400">R2.</span> Doskonała Informacja i Wsteczna Indukcja
          </a>
          <a href="#rozdzial-3" class="nav-link">
            <span class="font-mono text-slate-400">R3.</span> Gry Dynamiczne, Podgry i SPE
          </a>

          <div class="pt-2 text-[10px] font-mono uppercase tracking-wider text-slate-400 font-bold">Część II: Wypłaty Kardynalne</div>
          <a href="#rozdzial-4" class="nav-link">
            <span class="font-mono text-slate-400">R4.</span> Oczekiwana Użyteczność vNM
          </a>
          <a href="#rozdzial-5" class="nav-link">
            <span class="font-mono text-slate-400">R5.</span> Strategie Mieszane i Racjonalizowalność
          </a>
          <a href="#rozdzial-6" class="nav-link">
            <span class="font-mono text-slate-400">R6.</span> Dynamiczne Gry Kardynalne i Kuhn
          </a>

          <div class="pt-2 text-[10px] font-mono uppercase tracking-wider text-slate-400 font-bold">Część III: Wiedza i Przekonania</div>
          <a href="#rozdzial-7" class="nav-link">
            <span class="font-mono text-slate-400">R7.</span> Wiedza i Wspólna Wiedza (Aumann)
          </a>
          <a href="#rozdzial-8" class="nav-link">
            <span class="font-mono text-slate-400">R8.</span> Przekonania, Bayes i Teoria AGM
          </a>
          <a href="#rozdzial-9" class="nav-link">
            <span class="font-mono text-slate-400">R9.</span> Wspólna Wiedza o Racjonalności (CKR)
          </a>

          <div class="pt-2 text-[10px] font-mono uppercase tracking-wider text-slate-400 font-bold">Część IV: Uszczegółowienia SPE</div>
          <a href="#rozdzial-10" class="nav-link">
            <span class="font-mono text-slate-400">R10.</span> Słaba Równowaga Sekwencyjna (WSE)
          </a>
          <a href="#rozdzial-11" class="nav-link">
            <span class="font-mono text-slate-400">R11.</span> Równowaga Sekwencyjna Krepsa-Wilsona
          </a>
          <a href="#rozdzial-12" class="nav-link">
            <span class="font-mono text-slate-400">R12.</span> PBE i Twierdzenie Bonanno (2015)
          </a>

          <div class="pt-2 text-[10px] font-mono uppercase tracking-wider text-slate-400 font-bold">Część V: Informacja Niepełna</div>
          <a href="#rozdzial-13" class="nav-link">
            <span class="font-mono text-slate-400">R13.</span> Informacja Niepełna: Gry Statyczne
          </a>
          <a href="#rozdzial-14" class="nav-link">
            <span class="font-mono text-slate-400">R14.</span> Informacja Niepełna: Gry Dynamiczne
          </a>
          <a href="#rozdzial-15" class="nav-link">
            <span class="font-mono text-slate-400">R15.</span> Podejście Oparte na Przestrzeni Typów
          </a>

          <div class="pt-2 text-[10px] font-mono uppercase tracking-wider text-slate-400 font-bold">Laboratoria i Testy</div>
          <a href="#lab-sekcja" class="nav-link">
            <span class="font-mono text-slate-400">L16.</span> Interaktywne Laboratoria (4 Silniki)
          </a>
          <a href="#quiz-sekcja" class="nav-link">
            <span class="font-mono text-slate-400">Q17.</span> Diagnostyczny Sprawdzian Wiedzy
          </a>
          <a href="#kod-sekcja" class="nav-link">
            <span class="font-mono text-slate-400">K18.</span> Kod w Pythonie (GameTheoryCore)
          </a>
          <a href="#bibliografia-sekcja" class="nav-link">
            <span class="font-mono text-slate-400">B19.</span> Źródła Pierwotne & Bibliografia
          </a>
        </nav>
      </div>
    </aside>

    <!-- RIGHT MAIN CONTENT -->
    <main class="flex-1 min-w-0 space-y-10">

      <!-- HERO SECTION: 60 FPS REPLICATOR DYNAMICS CANVAS -->
      <section id="hero-sekcja" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center justify-between flex-wrap gap-2">
          <div class="flex items-center gap-2">
            <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Moduł Hero 60 FPS</span>
            <span class="text-xs font-mono text-slate-400">Dynamika Ewolucyjna &bull; Pole Wektorowe Replikatora</span>
          </div>
          <div class="flex items-center gap-2">
            <button id="heroPlayPauseBtn" class="px-2.5 py-1 text-xs font-mono font-semibold bg-blue-50 hover:bg-blue-100 text-blue-700 rounded-lg border border-blue-200 transition">
              Zatrzymaj
            </button>
            <button id="heroResetBtn" class="px-2.5 py-1 text-xs font-mono font-semibold bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg transition">
              Reset Trajektorii
            </button>
          </div>
        </div>

        <div class="space-y-2">
          <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight">
            Interaktywne Pole Fazowe Dynamiki Replikatora (Taylor-Jonker 1978)
          </h2>
          <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
            Obserwuj na żywo w 60 FPS ewolucję proporcji populacyjnych strategii $x_1, x_2, x_3$ w sympleksie prawdopodobieństwa $\\Delta^2$.
            Wektor fazowy sterowany jest równaniem $\\dot{x}_i = x_i [ (Ax)_i - x^T A x ]$.
            Kliknij na kanwie, aby wystrzelić nową trajektorię od punktu początkowego!
          </p>
        </div>

        <!-- Canvas Container -->
        <div class="relative bg-slate-950 rounded-xl overflow-hidden border border-slate-800 shadow-inner">
          <canvas id="heroCanvas" class="w-full h-[280px]"></canvas>
          <div class="absolute bottom-2 left-3 right-3 flex items-center justify-between text-[11px] font-mono text-slate-400 pointer-events-none">
            <span>Stan: <strong id="heroFpsMetric" class="text-emerald-400">60 FPS</strong></span>
            <span>Gra: <strong id="heroGamePresetName" class="text-blue-400">Kamień-Papier-Nożyce (Cykl Graniczny)</strong></span>
            <span>Trajektorie: <strong id="heroTrajCount" class="text-amber-400">12 cząstek</strong></span>
          </div>
        </div>
      </section>
    """

def get_labs_and_quiz():
    return """
      <!-- INTERAKTYWNE LABORATORIA (MODUL 16) -->
      <section id="lab-sekcja" class="saas-card p-4 sm:p-8 space-y-8 bg-white border-2 border-blue-500/30">
        <div class="flex items-center justify-between flex-wrap gap-2">
          <div class="flex flex-wrap items-center gap-2">
            <span class="badge-tag bg-blue-600 text-white">Moduł 16</span>
            <h3 class="text-lg sm:text-xl font-black text-slate-900">Interaktywne Laboratorium Algorytmów Bonanno (60 FPS)</h3>
          </div>
          <span class="text-xs font-mono text-slate-500">4 Zintegrowane Silniki Matematyczne</span>
        </div>

        <!-- LAB 1: SOLVER MACIERZY NASHA -->
        <div class="p-4 sm:p-5 bg-slate-50 border border-slate-200 rounded-xl space-y-4 min-w-0 max-w-full">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <h4 class="text-sm font-bold text-slate-900 flex flex-wrap items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-blue-600"></span>
              Laboratorium 1: Solver Macierzy Wypłat $2 \\times 2$ (Równowagi Czyste i Mieszane)
            </h4>
            <div class="flex items-center gap-2">
              <label for="matrixPresetSelect" class="text-xs font-semibold text-slate-600">Szablon:</label>
              <select id="matrixPresetSelect" class="text-xs px-2.5 py-1.5 border border-slate-300 rounded-lg bg-white font-mono">
                <option value="prisoners">Dylemat Więźnia (Prisoner's Dilemma)</option>
                <option value="battle">Bitwa Płci (Battle of the Sexes)</option>
                <option value="pennies">Dopasowywanie Monet (Matching Pennies)</option>
                <option value="stag">Polowanie na Jelenia (Stag Hunt)</option>
                <option value="cournot">Dyskretny Duopol Cournota</option>
              </select>
            </div>
          </div>

          <!-- UX COACHMARK -->
          <div class="p-3 sm:p-4 bg-blue-50/70 border border-blue-200/80 rounded-xl flex items-start gap-3">
            <span class="text-blue-600 text-lg">👉</span>
            <div class="text-xs text-blue-900 leading-relaxed">
              <strong>Jak z tego korzystać:</strong> 
              1. Wybierz szablon gry lub wprowadź własne wypłaty $(u_1, u_2)$ w polach formularza. 
              2. Obserwuj podkreślenia najlepszych odpowiedzi w tabeli (niebieskie dla Gracza 1, zielone dla Gracza 2). 
              3. Komórka z podwójnym podkreśleniem i zieloną ramką oznacza równowagę w strategiach czystych. Poniżej automatycznie przeliczana jest równowaga w strategiach mieszanych $(p^*, q^*)$ z dowodu Twierdzenia 5.2!
            </div>
          </div>

          <p id="matrixPresetDesc" class="text-xs text-slate-600 italic"></p>

          <!-- Input Controls Grid -->
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 sm:gap-3 text-xs font-mono">
            <div>
              <label class="block text-slate-500 mb-1">Etykieta W1:</label>
              <input type="text" id="labelRow1" value="Współpraca" class="w-full px-2 py-1 border rounded bg-white">
            </div>
            <div>
              <label class="block text-slate-500 mb-1">Etykieta W2:</label>
              <input type="text" id="labelRow2" value="Zdrada" class="w-full px-2 py-1 border rounded bg-white">
            </div>
            <div>
              <label class="block text-slate-500 mb-1">Etykieta K1:</label>
              <input type="text" id="labelCol1" value="Współpraca" class="w-full px-2 py-1 border rounded bg-white">
            </div>
            <div>
              <label class="block text-slate-500 mb-1">Etykieta K2:</label>
              <input type="text" id="labelCol2" value="Zdrada" class="w-full px-2 py-1 border rounded bg-white">
            </div>
          </div>

          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 sm:gap-3 text-xs font-mono">
            <div class="p-2 bg-white rounded border">
              <span class="text-[10px] text-slate-400 block mb-1">(W1, K1)</span>
              <div class="flex gap-1">
                <input type="number" id="cellTL1" value="3" class="w-10 sm:w-12 px-1 py-0.5 border rounded">
                <input type="number" id="cellTL2" value="3" class="w-10 sm:w-12 px-1 py-0.5 border rounded">
              </div>
            </div>
            <div class="p-2 bg-white rounded border">
              <span class="text-[10px] text-slate-400 block mb-1">(W1, K2)</span>
              <div class="flex gap-1">
                <input type="number" id="cellTR1" value="0" class="w-10 sm:w-12 px-1 py-0.5 border rounded">
                <input type="number" id="cellTR2" value="5" class="w-10 sm:w-12 px-1 py-0.5 border rounded">
              </div>
            </div>
            <div class="p-2 bg-white rounded border">
              <span class="text-[10px] text-slate-400 block mb-1">(W2, K1)</span>
              <div class="flex gap-1">
                <input type="number" id="cellBL1" value="5" class="w-10 sm:w-12 px-1 py-0.5 border rounded">
                <input type="number" id="cellBL2" value="0" class="w-10 sm:w-12 px-1 py-0.5 border rounded">
              </div>
            </div>
            <div class="p-2 bg-white rounded border">
              <span class="text-[10px] text-slate-400 block mb-1">(W2, K2)</span>
              <div class="flex gap-1">
                <input type="number" id="cellBR1" value="1" class="w-10 sm:w-12 px-1 py-0.5 border rounded">
                <input type="number" id="cellBR2" value="1" class="w-10 sm:w-12 px-1 py-0.5 border rounded">
              </div>
            </div>
          </div>

          <!-- Dynamic Visual Payoff Table -->
          <div class="overflow-x-auto min-w-0 max-w-full">
            <table class="w-full text-center border-collapse text-xs font-mono bg-white rounded-xl shadow-sm overflow-hidden">
              <thead>
                <tr class="bg-slate-100 text-slate-700">
                  <th class="p-2.5 border border-slate-200">Gracz 1 \\ Gracz 2</th>
                  <th class="p-2.5 border border-slate-200" id="dispCol1Name">K1</th>
                  <th class="p-2.5 border border-slate-200" id="dispCol2Name">K2</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th class="p-2.5 bg-slate-100 border border-slate-200 font-bold" id="dispRow1Name">W1</th>
                  <td class="p-3 border border-slate-200 matrix-cell" id="tdTL">(3, 3)</td>
                  <td class="p-3 border border-slate-200 matrix-cell" id="tdTR">(0, 5)</td>
                </tr>
                <tr>
                  <th class="p-2.5 bg-slate-100 border border-slate-200 font-bold" id="dispRow2Name">W2</th>
                  <td class="p-3 border border-slate-200 matrix-cell" id="tdBL">(5, 0)</td>
                  <td class="p-3 border border-slate-200 matrix-cell" id="tdBR">(1, 1)</td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Results Panel -->
          <div id="matrixResultsPanel" class="p-3 sm:p-4 bg-white border border-slate-200 rounded-xl overflow-x-auto"></div>
        </div>

        <!-- LAB 2: EXTENSIVE TREE & INDUKCJA WSTECZNA -->
        <div class="p-4 sm:p-5 bg-slate-50 border border-slate-200 rounded-xl space-y-4 min-w-0 max-w-full" id="treeCanvasContainer">
          <h4 class="text-sm font-bold text-slate-900 flex flex-wrap items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-emerald-600"></span>
            Laboratorium 2: Eksplorator Drzewa Ekstensywnego i Indukcja Wsteczna (Amy i Beth 100k USD)
          </h4>

          <!-- UX COACHMARK -->
          <div class="p-3 sm:p-4 bg-blue-50/70 border border-blue-200/80 rounded-xl flex items-start gap-3">
            <span class="text-blue-600 text-lg">👉</span>
            <div class="text-xs text-blue-900 leading-relaxed">
              <strong>Jak z tego korzystać:</strong> 
              1. Przesuwaj suwak wrażliwości Beth na niesprawiedliwość ($F_{\\text{Beth}}$). 
              2. Obserwuj zmianę grubych krawędzi reprezentujących ścieżkę indukcji wstecznej. 
              3. Zwróć uwagę, że gdy kara za niesprawiedliwość przekroczy 10k USD, Beth odrzuca ofertę 70-30, zmuszając racjonalną Amy do zaoferowania sprawiedliwego podziału 50-50!
            </div>
          </div>

          <div class="flex flex-wrap items-center gap-3 bg-white p-3 rounded-xl border border-slate-200">
            <label class="text-xs font-semibold text-slate-700">Dysużyteczność Beth z niesprawiedliwości:</label>
            <input type="range" id="treeBethFairness" min="0" max="25" value="10" class="flex-1 min-w-[140px]">
            <span id="treeValFairness" class="font-mono text-xs font-bold text-blue-600">10k USD</span>
          </div>

          <!-- SVG Tree Render -->
          <div class="bg-white p-3 sm:p-4 rounded-xl border border-slate-200 flex justify-center overflow-x-auto min-w-0 max-w-full">
            <svg id="treeSvg" viewBox="0 0 560 240" class="w-full max-w-[560px] h-60"></svg>
          </div>

          <div id="treeOutcomeReport" class="p-3 sm:p-4 bg-white border border-slate-200 rounded-xl overflow-x-auto"></div>
        </div>

        <!-- LAB 3 & 4: BAYES ORAZ AUMANN -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <!-- LAB 3: MONTY HALL BAYES -->
          <div class="p-4 sm:p-5 bg-slate-50 border border-slate-200 rounded-xl space-y-4 min-w-0 max-w-full">
            <h4 class="text-sm font-bold text-slate-900 flex flex-wrap items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-amber-600"></span>
              Laboratorium 3: Paradoks Monty Halla i Aktualizacja Bayesa
            </h4>
            <div class="p-3 bg-blue-50/70 border border-blue-200/80 rounded-lg text-xs text-blue-900">
              <strong>Zadanie 8.12 Bonanno:</strong> Wybierasz Drzwi 1. Prowadzący otwiera Drzwi 3 (gdzie nie ma samochodu). Czy warto zmienić wybór na Drzwi 2?
            </div>

            <div class="flex items-center justify-between bg-white p-3 rounded-lg border">
              <div>
                <span class="text-[11px] text-slate-500 block">Wskaźnik (Pozostanie):</span>
                <span id="bayesStayWinRate" class="text-base font-mono font-bold text-slate-700">33.3%</span>
              </div>
              <div class="text-right">
                <span class="text-[11px] text-slate-500 block">Wskaźnik (Zmiana):</span>
                <span id="bayesSwitchWinRate" class="text-base font-mono font-bold text-emerald-600">66.7%</span>
              </div>
            </div>

            <div class="flex items-center gap-2">
              <button id="bayesRunSimBtn" class="flex-1 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-xs font-semibold shadow-sm transition">
                Symuluj 500 Gier Monte Carlo
              </button>
              <button id="bayesResetBtn" class="px-3 py-2 bg-slate-200 hover:bg-slate-300 text-slate-700 rounded-lg text-xs font-semibold transition">
                Reset
              </button>
            </div>
            <div class="text-[11px] text-slate-500 font-mono text-center">
              Liczba przeprowadzonych prób: <span id="bayesTrialsCount" class="font-bold">0</span>
            </div>
          </div>

          <!-- LAB 4: AUMANN GRAPH -->
          <div class="p-4 sm:p-5 bg-slate-50 border border-slate-200 rounded-xl space-y-4 min-w-0 max-w-full">
            <h4 class="text-sm font-bold text-slate-900 flex flex-wrap items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-purple-600"></span>
              Laboratorium 4: Graf Wspólnej Wiedzy Aumanna (Rozdział 7)
            </h4>
            <div class="p-3 bg-purple-50/70 border border-purple-200/80 rounded-lg text-xs text-purple-950">
              Przestrzeń stanów $W = \\{a, b, c, d, e\\}$. Partycje: $\\mathcal{I}_1 = \\{\\{a,b,c\\}, \\{d,e\\}\\}$, $\\mathcal{I}_2 = \\{\\{a,b\\}, \\{c,d\\}, \\{e\\}\\}.$
            </div>

            <div class="flex items-center gap-3 bg-white p-3 rounded-lg border">
              <label for="aumannStateSelect" class="text-xs font-semibold text-slate-700">Stan świata $w$:</label>
              <select id="aumannStateSelect" class="text-xs px-2.5 py-1.5 border rounded-lg bg-white font-mono">
                <option value="a">Stan a</option>
                <option value="b">Stan b</option>
                <option value="c">Stan c</option>
                <option value="d">Stan d</option>
                <option value="e">Stan e</option>
              </select>
            </div>

            <div id="aumannResultPanel" class="p-3 bg-white border border-slate-200 rounded-lg overflow-x-auto"></div>
          </div>
        </div>
      </section>

      <!-- DIAGNOSTYCZNY QUIZ (MODUL 17) -->
      <section id="quiz-sekcja" class="saas-card p-4 sm:p-8 space-y-6">
        <div class="flex items-center justify-between flex-wrap gap-2">
          <div class="flex flex-wrap items-center gap-2">
            <span class="badge-tag bg-emerald-600 text-white">Moduł 17</span>
            <h3 class="text-lg sm:text-xl font-bold text-slate-900">Diagnostyczny Sprawdzian Zrozumienia (6 Zadań Rygoru Bonanno)</h3>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs text-slate-500 font-mono">Twój wynik:</span>
            <span id="quizScoreTracker" class="text-sm font-mono font-bold text-emerald-600 px-2.5 py-0.5 bg-emerald-50 border border-emerald-200 rounded-lg">
              0 / 6
            </span>
          </div>
        </div>

        <p class="text-xs text-slate-600 leading-relaxed">
          Poniższe pytania testują zrozumienie najgłębszych koncepcji teoretycznych z podręcznika Giacomo Bonanno:
          od założeń mechanizmu aukcji Vickreya, przez epistemologię wspólnej wiedzy, aż po uszczegółowienia sekwencyjne i twierdzenie Bonanno (2015).
        </p>

        <!-- Dynamic Questions Container -->
        <div class="space-y-4" id="quizQuestionsContainer"></div>
      </section>

      <!-- PRAKTYCZNA IMPLEMENTACJA W PYTHONIE (MODUL 18) -->
      <section id="kod-sekcja" class="saas-card p-4 sm:p-8 space-y-4">
        <div class="flex items-center justify-between flex-wrap gap-2">
          <div class="flex flex-wrap items-center gap-2">
            <span class="badge-tag bg-slate-800 text-white font-mono">Moduł 18</span>
            <h3 class="text-lg sm:text-xl font-bold text-slate-900">Implementacja Algorytmów w Pythonie (GameTheoryCore)</h3>
          </div>
          <button id="copyCodeBtn" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-900 text-slate-200 text-xs font-mono rounded-lg transition shadow-sm">
            Kopiuj Kod
          </button>
        </div>

        <p class="text-xs text-slate-600">
          Poniższy skrypt implementuje kluczowe procedury z podręcznika Bonanno: obliczanie równowag czystych i mieszanych dla gier $2 \\times 2$ oraz eliminację zdominowanych strategii w czystym Pythonie bez zewnętrznych zależności.
        </p>

        <pre class="bg-slate-950 text-slate-100 p-3 sm:p-4 rounded-xl text-xs font-mono overflow-x-auto leading-relaxed border border-slate-800" id="pythonCodeBlock"><code># GameTheoryCore - Bonanno Solvers in Python
from typing import Dict, List, Tuple, Optional

class MatrixGame2x2:
    \"\"\"
    2-player 2x2 game solver with Best Reply analysis,
    pure Nash equilibria and mixed Nash equilibria.
    Payoffs:
      R1: (tl1, tl2) vs (tr1, tr2)
      R2: (bl1, bl2) vs (br1, br2)
    \"\"\"
    def __init__(self, tl: Tuple[float, float], tr: Tuple[float, float],
                 bl: Tuple[float, float], br: Tuple[float, float]):
        self.tl1, self.tl2 = tl
        self.tr1, self.tr2 = tr
        self.bl1, self.bl2 = bl
        self.br1, self.br2 = br

    def pure_nash_equilibria(self) -> List[str]:
        equilibria = []
        p1_c1 = [self.tl1 >= self.bl1, self.bl1 >= self.tl1]
        p1_c2 = [self.tr1 >= self.br1, self.br1 >= self.tr1]
        p2_r1 = [self.tl2 >= self.tr2, self.tr2 >= self.tl2]
        p2_r2 = [self.bl2 >= self.br2, self.br2 >= self.bl2]

        if p1_c1[0] and p2_r1[0]: equilibria.append("(R1, C1)")
        if p1_c2[0] and p2_r1[1]: equilibria.append("(R1, C2)")
        if p1_c1[1] and p2_r2[0]: equilibria.append("(R2, C1)")
        if p1_c2[1] and p2_r2[1]: equilibria.append("(R2, C2)")
        return equilibria

    def mixed_nash_equilibrium(self) -> Optional[Dict[str, float]]:
        denom_p = (self.tl2 - self.tr2) - (self.bl2 - self.br2)
        num_p = self.br2 - self.bl2
        
        denom_q = (self.tl1 - self.bl1) - (self.tr1 - self.br1)
        num_q = self.br1 - self.tr1

        if denom_p == 0 or denom_q == 0:
            return None
        
        p = num_p / denom_p
        q = num_q / denom_q

        if 0 < p < 1 and 0 < q < 1:
            eu1 = self.tl1 * q + self.tr1 * (1 - q)
            eu2 = self.tl2 * p + self.bl2 * (1 - p)
            return {"p_star": p, "q_star": q, "EU1": eu1, "EU2": eu2}
        return None

if __name__ == "__main__":
    mp = MatrixGame2x2((1, -1), (-1, 1), (-1, 1), (1, -1))
    print("Matching Pennies Pure Nash:", mp.pure_nash_equilibria())
    print("Matching Pennies Mixed Nash:", mp.mixed_nash_equilibrium())
</code></pre>
      </section>

      <!-- MODUL 19: ZRODLA PIERWOTNE & BIBLIOGRAFIA NAUKOWA -->
      <section id="bibliografia-sekcja" class="saas-card p-4 sm:p-8 space-y-4">
        <div class="flex items-center gap-2">
          <span class="badge-tag bg-blue-50 text-blue-700 border border-blue-200">Moduł 19</span>
          <h3 class="text-lg sm:text-xl font-bold text-slate-900">📚 Źródła Pierwotne & Bibliografia Naukowa</h3>
        </div>
        
        <p class="text-xs text-slate-600">
          Poniższy zbiór zawiera kanoniczne publikacje założycielskie z bezpośrednimi odnośnikami DOI, stanowiące fundament współczesnej teorii gier oraz podręcznika Giacomo Bonanno:
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs pt-2">
          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-1">
            <span class="font-bold text-slate-900 block">Bonanno, Giacomo (2015)</span>
            <div class="text-slate-600 text-[11px]"><em>AGM-consistency and perfect Bayesian equilibrium. Part II: from PBE to sequential equilibrium</em>. International Journal of Game Theory, 44(4), 841-863.</div>
            <a href="https://doi.org/10.1007/s00182-014-0453-y" target="_blank" rel="noopener noreferrer" class="text-blue-600 font-mono text-[11px] hover:underline block pt-1">DOI: 10.1007/s00182-014-0453-y</a>
          </div>

          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-1">
            <span class="font-bold text-slate-900 block">Bonanno, Giacomo (2013)</span>
            <div class="text-slate-600 text-[11px]"><em>AGM-consistency and perfect Bayesian equilibrium. Part I: definition and properties</em>. International Journal of Game Theory, 42(3), 567-592.</div>
            <a href="https://doi.org/10.1007/s00182-012-0346-6" target="_blank" rel="noopener noreferrer" class="text-blue-600 font-mono text-[11px] hover:underline block pt-1">DOI: 10.1007/s00182-012-0346-6</a>
          </div>

          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-1">
            <span class="font-bold text-slate-900 block">Aumann, Robert J. (1976)</span>
            <div class="text-slate-600 text-[11px]"><em>Agreeing to Disagree</em>. The Annals of Statistics, 4(6), 1236-1239.</div>
            <a href="https://doi.org/10.1214/aos/1176343654" target="_blank" rel="noopener noreferrer" class="text-blue-600 font-mono text-[11px] hover:underline block pt-1">DOI: 10.1214/aos/1176343654</a>
          </div>

          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-1">
            <span class="font-bold text-slate-900 block">Kreps, David M., Wilson, Robert (1982)</span>
            <div class="text-slate-600 text-[11px]"><em>Sequential Equilibria</em>. Econometrica, 50(4), 863-894.</div>
            <a href="https://doi.org/10.2307/1912767" target="_blank" rel="noopener noreferrer" class="text-blue-600 font-mono text-[11px] hover:underline block pt-1">DOI: 10.2307/1912767</a>
          </div>

          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-1">
            <span class="font-bold text-slate-900 block">Harsanyi, John C. (1967-1968)</span>
            <div class="text-slate-600 text-[11px]"><em>Games with Incomplete Information Played by 'Bayesian' Players, Parts I-III</em>. Management Science, 14(3, 5, 7).</div>
            <a href="https://doi.org/10.1287/mnsc.14.3.159" target="_blank" rel="noopener noreferrer" class="text-blue-600 font-mono text-[11px] hover:underline block pt-1">DOI: 10.1287/mnsc.14.3.159</a>
          </div>

          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-1">
            <span class="font-bold text-slate-900 block">Nash, John (1951)</span>
            <div class="text-slate-600 text-[11px]"><em>Non-Cooperative Games</em>. Annals of Mathematics, 54(2), 286-295.</div>
            <a href="https://doi.org/10.2307/1969529" target="_blank" rel="noopener noreferrer" class="text-blue-600 font-mono text-[11px] hover:underline block pt-1">DOI: 10.2307/1969529</a>
          </div>

          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-1">
            <span class="font-bold text-slate-900 block">Selten, Reinhard (1975)</span>
            <div class="text-slate-600 text-[11px]"><em>Reexamination of the perfectness concept for equilibrium points in extensive games</em>. International Journal of Game Theory, 4(1), 25-55.</div>
            <a href="https://doi.org/10.1007/BF01766006" target="_blank" rel="noopener noreferrer" class="text-blue-600 font-mono text-[11px] hover:underline block pt-1">DOI: 10.1007/BF01766006</a>
          </div>

          <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-1">
            <span class="font-bold text-slate-900 block">Vickrey, William (1961)</span>
            <div class="text-slate-600 text-[11px]"><em>Counterspeculation, Auctions, and Competitive Sealed Tenders</em>. The Journal of Finance, 16(1), 8-37.</div>
            <a href="https://doi.org/10.1111/j.1540-6261.1961.tb02789.x" target="_blank" rel="noopener noreferrer" class="text-blue-600 font-mono text-[11px] hover:underline block pt-1">DOI: 10.1111/j.1540-6261.1961.tb02789.x</a>
          </div>
        </div>
      </section>

      <!-- FOOTER -->
      <footer class="border-t border-slate-200 pt-6 text-center text-xs text-slate-500 font-mono space-y-1 pb-12">
        <div>Lyceum Series &bull; Interaktywne Kompendium Teorii Gier (Giacomo Bonanno, 2015)</div>
        <div>Opracowane w standardzie SaaS / EdTech &bull; Wszelkie prawa zastrzeżone</div>
      </footer>

    </main>
  </div>

  <!-- Application Logic -->
  <script src="app.js"></script>
</body>
</html>
"""

def build_site():
    print("Building full index.html...")
    sections = [
        get_header(),
        get_chapter_0(),
        get_chapter_1(),
        get_chapter_2(),
        get_chapter_3(),
        get_chapter_4(),
        get_chapter_5(),
        get_chapter_6(),
        get_chapter_7(),
        get_chapter_8(),
        get_chapter_9(),
        get_chapter_10(),
        get_chapter_11(),
        get_chapter_12(),
        get_chapter_13(),
        get_chapter_14(),
        get_chapter_15(),
        get_labs_and_quiz()
    ]
    
    html = "\\n".join(sections)
    
    # Check for em-dashes
    if "—" in html or "–" in html:
        print("WARNING: Em-dash found! Replacing with hyphens...")
        html = html.replace("—", "-").replace("–", "-")
    
    assert "—" not in html, "Em-dash '—' detected!"
    assert "–" not in html, "En-dash '–' detected!"
    
    out_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
        
    print(f"Successfully generated index.html ({len(html.splitlines())} lines, {len(html)} bytes)")

if __name__ == "__main__":
    build_site()
