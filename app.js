// Lyceum: Teoria Gier (Giacomo Bonanno) - Interactive Core Engine

document.addEventListener("DOMContentLoaded", () => {
  // 1. Navigation & Scrollspy
  initNavigation();

  // 2. Hero 60 FPS Canvas Animation
  initHeroCanvas();

  // 3. Lab 1: Interactive Payoff Matrix & Nash Solver
  initMatrixSolver();

  // 4. Lab 2: Interactive Extensive Tree & Backward Induction
  initTreeSolver();

  // 5. Lab 3: Interactive Bayes & Monty Hall Engine
  initBayesEngine();

  // 6. Lab 4: Interactive Aumann Knowledge Graph
  initAumannGraph();

  // 7. Interactive Diagnostic Quiz
  initQuiz();

  // 8. Copy code snippet button
  initCodeCopy();

  // 9. Initial KaTeX render on document
  if (window.renderMathInElement) {
    renderMathInElement(document.body, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false },
        { left: "\\(", right: "\\)", display: false },
        { left: "\\[", right: "\\]", display: true }
      ],
      throwOnError: false
    });
  }
});

// ==========================================
// 1. NAVIGATION & SCROLLSPY
// ==========================================
function initNavigation() {
  const navLinks = document.querySelectorAll(".nav-link");
  const sections = [];
  navLinks.forEach(link => {
    const targetId = link.getAttribute("href")?.substring(1);
    if (targetId) {
      const el = document.getElementById(targetId);
      if (el) sections.push({ id: targetId, el, link });
    }
  });

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          navLinks.forEach(l => l.classList.remove("active"));
          const activeSec = sections.find(s => s.el === entry.target);
          if (activeSec) {
            activeSec.link.classList.add("active");
          }
        }
      });
    }, { rootMargin: "-10% 0px -75% 0px", threshold: 0 });

    sections.forEach(s => observer.observe(s.el));
  }

  // Search filter in sidebar
  const searchInput = document.getElementById("navSearchInput");
  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      const q = e.target.value.toLowerCase().trim();
      navLinks.forEach(link => {
        const text = link.innerText.toLowerCase();
        link.style.display = text.includes(q) ? "flex" : "none";
      });
    });
  }
}

// ==========================================
// 2. HERO 60 FPS CANVAS (Replicator Dynamics & Vector Field)
// ==========================================
function initHeroCanvas() {
  const canvas = document.getElementById("heroCanvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  if (!ctx) return;

  let width = canvas.width = canvas.parentElement.clientWidth || 800;
  let height = canvas.height = 280;

  window.addEventListener("resize", () => {
    width = canvas.width = canvas.parentElement.clientWidth || 800;
    height = canvas.height = 280;
  });

  // Particle swarm on 2D simplex / phase plane
  const numParticles = 65;
  const particles = [];
  let mode = "hawk-dove"; // 'hawk-dove', 'matching-pennies', 'prisoners'

  for (let i = 0; i < numParticles; i++) {
    particles.push({
      x: Math.random() * (width - 60) + 30,
      y: Math.random() * (height - 60) + 30,
      vx: (Math.random() - 0.5) * 1.5,
      vy: (Math.random() - 0.5) * 1.5,
      radius: Math.random() * 2.5 + 1.5,
      color: i % 2 === 0 ? "#3b82f6" : "#10b981",
      history: []
    });
  }

  function getField(x, y) {
    // Normalized coordinates [0, 1]
    const nx = (x - 40) / (width - 80);
    const ny = (y - 40) / (height - 80);
    let dx = 0;
    let dy = 0;

    if (mode === "hawk-dove") {
      // Internal attractor (ESS / mixed equilibrium) at (0.6, 0.4)
      const eqX = 0.55;
      const eqY = 0.45;
      const rx = nx - eqX;
      const ry = ny - eqY;
      dx = -ry * 1.8 - rx * 0.8;
      dy = rx * 1.8 - ry * 0.8;
    } else if (mode === "matching-pennies") {
      // Limit cycle around center (0.5, 0.5)
      const rx = nx - 0.5;
      const ry = ny - 0.5;
      dx = -ry * 2.2;
      dy = rx * 2.2;
    } else {
      // Prisoner's dilemma: dominant convergence to bottom-right (Defect, Defect)
      dx = (1.0 - nx) * 1.2;
      dy = (1.0 - ny) * 1.2;
    }
    return { dx, dy };
  }

  function render() {
    ctx.fillStyle = "rgba(9, 13, 22, 0.25)";
    ctx.fillRect(0, 0, width, height);

    // Draw background grid & vector hints
    ctx.strokeStyle = "rgba(255, 255, 255, 0.04)";
    ctx.lineWidth = 1;
    for (let gx = 40; gx < width; gx += 40) {
      ctx.beginPath();
      ctx.moveTo(gx, 0);
      ctx.lineTo(gx, height);
      ctx.stroke();
    }
    for (let gy = 40; gy < height; gy += 40) {
      ctx.beginPath();
      ctx.moveTo(0, gy);
      ctx.lineTo(width, gy);
      ctx.stroke();
    }

    // Draw equilibrium point
    let eqPx = width * 0.55;
    let eqPy = height * 0.45;
    if (mode === "matching-pennies") {
      eqPx = width * 0.5;
      eqPy = height * 0.5;
    } else if (mode === "prisoners") {
      eqPx = width - 50;
      eqPy = height - 50;
    }

    // Glow around equilibrium
    const grad = ctx.createRadialGradient(eqPx, eqPy, 2, eqPx, eqPy, 35);
    grad.addColorStop(0, "rgba(59, 130, 246, 0.4)");
    grad.addColorStop(1, "rgba(59, 130, 246, 0)");
    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.arc(eqPx, eqPy, 35, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = "#60a5fa";
    ctx.beginPath();
    ctx.arc(eqPx, eqPy, 4, 0, Math.PI * 2);
    ctx.fill();

    // Text annotation for equilibrium
    ctx.font = "10px JetBrains Mono, monospace";
    ctx.fillStyle = "rgba(147, 197, 253, 0.7)";
    ctx.fillText(mode === "prisoners" ? "Równowaga (D, D)" : "Punkt Równowagi (Nash ESS)", eqPx - 70, eqPy - 10);

    // Update and draw particles
    particles.forEach(p => {
      const f = getField(p.x, p.y);
      p.vx = p.vx * 0.92 + f.dx * 0.4;
      p.vy = p.vy * 0.92 + f.dy * 0.4;

      p.x += p.vx;
      p.y += p.vy;

      if (p.x < 20) p.x = width - 30;
      if (p.x > width - 20) p.x = 30;
      if (p.y < 20) p.y = height - 30;
      if (p.y > height - 20) p.y = 30;

      p.history.push({ x: p.x, y: p.y });
      if (p.history.length > 8) p.history.shift();

      // Trail
      if (p.history.length > 1) {
        ctx.beginPath();
        ctx.moveTo(p.history[0].x, p.history[0].y);
        for (let h = 1; h < p.history.length; h++) {
          ctx.lineTo(p.history[h].x, p.history[h].y);
        }
        ctx.strokeStyle = p.color === "#3b82f6" ? "rgba(59, 130, 246, 0.3)" : "rgba(16, 185, 129, 0.3)";
        ctx.lineWidth = 1;
        ctx.stroke();
      }

      // Point
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
      ctx.fillStyle = p.color;
      ctx.fill();
    });

    requestAnimationFrame(render);
  }
  requestAnimationFrame(render);

  // Mode buttons in Hero
  const btnHawk = document.getElementById("heroBtnHawk");
  const btnPennies = document.getElementById("heroBtnPennies");
  const btnPrisoners = document.getElementById("heroBtnPrisoners");

  function setMode(newMode, btn) {
    mode = newMode;
    [btnHawk, btnPennies, btnPrisoners].forEach(b => {
      if (b) {
        b.classList.remove("bg-blue-600", "text-white");
        b.classList.add("bg-slate-800", "text-slate-300");
      }
    });
    if (btn) {
      btn.classList.remove("bg-slate-800", "text-slate-300");
      btn.classList.add("bg-blue-600", "text-white");
    }
  }

  if (btnHawk) btnHawk.addEventListener("click", () => setMode("hawk-dove", btnHawk));
  if (btnPennies) btnPennies.addEventListener("click", () => setMode("matching-pennies", btnPennies));
  if (btnPrisoners) btnPrisoners.addEventListener("click", () => setMode("prisoners", btnPrisoners));
}

// ==========================================
// 3. LAB 1: INTERACTIVE MATRIX & NASH SOLVER
// ==========================================
const MATRIX_PRESETS = {
  prisoners: {
    r1: "Współpraca", r2: "Zdrada",
    c1: "Współpraca", c2: "Zdrada",
    tl: [3, 3], tr: [0, 5],
    bl: [5, 0], br: [1, 1],
    desc: "Klasyczny Dylemat Więźnia: Zdrada jest ściśle dominująca dla obu graczy. Równowaga (Zdrada, Zdrada) = (1,1) jest Pareto-gorsza od (3,3)."
  },
  battle: {
    r1: "Opera", r2: "Mecz",
    c1: "Opera", c2: "Mecz",
    tl: [3, 2], tr: [0, 0],
    bl: [0, 0], br: [2, 3],
    desc: "Bitwa Płci: Dwie równowagi w strategiach czystych (Opera, Opera) i (Mecz, Mecz) oraz jedna równowaga mieszana."
  },
  pennies: {
    r1: "Orzeł", r2: "Reszka",
    c1: "Orzeł", c2: "Reszka",
    tl: [1, -1], tr: [-1, 1],
    bl: [-1, 1], br: [1, -1],
    desc: "Dopasowywanie Monet: Gra o sumie zerowej bez równowagi w strategiach czystych. Unikalna równowaga w strategiach mieszanych (1/2, 1/2)."
  },
  stag: {
    r1: "Jeleń", r2: "Zając",
    c1: "Jeleń", c2: "Zając",
    tl: [4, 4], tr: [0, 2],
    bl: [2, 0], br: [2, 2],
    desc: "Polowanie na Jelenia (Stag Hunt): Równowaga dominująca w sensie wypłat (4,4) vs równowaga dominująca w sensie ryzyka (2,2)."
  },
  cournot: {
    r1: "Niska (q=4)", r2: "Wysoka (q=6)",
    c1: "Niska (q=4)", c2: "Wysoka (q=6)",
    tl: [32, 32], tr: [24, 36],
    bl: [36, 24], br: [25, 25],
    desc: "Dyskretny Duopol Cournota: Gracze konkurują ilościowo. Nadprodukcja obniża cenę rynkową, prowadząc do równowagi (25, 25)."
  }
};

function initMatrixSolver() {
  const presetSelect = document.getElementById("matrixPresetSelect");
  const inputs = {
    r1: document.getElementById("labelRow1"),
    r2: document.getElementById("labelRow2"),
    c1: document.getElementById("labelCol1"),
    c2: document.getElementById("labelCol2"),
    tl1: document.getElementById("cellTL1"),
    tl2: document.getElementById("cellTL2"),
    tr1: document.getElementById("cellTR1"),
    tr2: document.getElementById("cellTR2"),
    bl1: document.getElementById("cellBL1"),
    bl2: document.getElementById("cellBL2"),
    br1: document.getElementById("cellBR1"),
    br2: document.getElementById("cellBR2")
  };

  function loadPreset(name) {
    const p = MATRIX_PRESETS[name];
    if (!p) return;
    if (inputs.r1) inputs.r1.value = p.r1;
    if (inputs.r2) inputs.r2.value = p.r2;
    if (inputs.c1) inputs.c1.value = p.c1;
    if (inputs.c2) inputs.c2.value = p.c2;

    if (inputs.tl1) inputs.tl1.value = p.tl[0];
    if (inputs.tl2) inputs.tl2.value = p.tl[1];
    if (inputs.tr1) inputs.tr1.value = p.tr[0];
    if (inputs.tr2) inputs.tr2.value = p.tr[1];
    if (inputs.bl1) inputs.bl1.value = p.bl[0];
    if (inputs.bl2) inputs.bl2.value = p.bl[1];
    if (inputs.br1) inputs.br1.value = p.br[0];
    if (inputs.br2) inputs.br2.value = p.br[1];

    const descEl = document.getElementById("matrixPresetDesc");
    if (descEl) descEl.innerText = p.desc;

    solveMatrix();
  }

  if (presetSelect) {
    presetSelect.addEventListener("change", (e) => loadPreset(e.target.value));
  }

  // Bind input listeners
  Object.values(inputs).forEach(inp => {
    if (inp) inp.addEventListener("input", solveMatrix);
  });

  // Calculate and display solutions
  function solveMatrix() {
    const tl1 = parseFloat(inputs.tl1?.value || 0);
    const tl2 = parseFloat(inputs.tl2?.value || 0);
    const tr1 = parseFloat(inputs.tr1?.value || 0);
    const tr2 = parseFloat(inputs.tr2?.value || 0);
    const bl1 = parseFloat(inputs.bl1?.value || 0);
    const bl2 = parseFloat(inputs.bl2?.value || 0);
    const br1 = parseFloat(inputs.br1?.value || 0);
    const br2 = parseFloat(inputs.br2?.value || 0);

    const r1Name = inputs.r1?.value || "R1";
    const r2Name = inputs.r2?.value || "R2";
    const c1Name = inputs.c1?.value || "C1";
    const c2Name = inputs.c2?.value || "C2";

    // Update table header labels
    const dispR1 = document.getElementById("dispRow1Name");
    const dispR2 = document.getElementById("dispRow2Name");
    const dispC1 = document.getElementById("dispCol1Name");
    const dispC2 = document.getElementById("dispCol2Name");
    if (dispR1) dispR1.innerText = r1Name;
    if (dispR2) dispR2.innerText = r2Name;
    if (dispC1) dispC1.innerText = c1Name;
    if (dispC2) dispC2.innerText = c2Name;

    // Best responses for Player 1 (Columns: C1 and C2)
    const p1_best_in_c1 = tl1 >= bl1 ? (tl1 > bl1 ? ["TL"] : ["TL", "BL"]) : ["BL"];
    const p1_best_in_c2 = tr1 >= br1 ? (tr1 > br1 ? ["TR"] : ["TR", "BR"]) : ["BR"];

    // Best responses for Player 2 (Rows: R1 and R2)
    const p2_best_in_r1 = tl2 >= tr2 ? (tl2 > tr2 ? ["TL"] : ["TL", "TR"]) : ["TR"];
    const p2_best_in_r2 = bl2 >= br2 ? (bl2 > br2 ? ["BL"] : ["BL", "BR"]) : ["BR"];

    // Underline best replies in display
    const cellTL = document.getElementById("tdTL");
    const cellTR = document.getElementById("tdTR");
    const cellBL = document.getElementById("tdBL");
    const cellBR = document.getElementById("tdBR");

    const p1Underline = {
      TL: p1_best_in_c1.includes("TL"),
      BL: p1_best_in_c1.includes("BL"),
      TR: p1_best_in_c2.includes("TR"),
      BR: p1_best_in_c2.includes("BR")
    };
    const p2Underline = {
      TL: p2_best_in_r1.includes("TL"),
      TR: p2_best_in_r1.includes("TR"),
      BL: p2_best_in_r2.includes("BL"),
      BR: p2_best_in_r2.includes("BR")
    };

    function formatCell(id, v1, v2) {
      const u1 = p1Underline[id] ? `<u class="text-blue-600 font-bold decoration-blue-500 underline-offset-4">${v1}</u>` : `${v1}`;
      const u2 = p2Underline[id] ? `<u class="text-emerald-600 font-bold decoration-emerald-500 underline-offset-4">${v2}</u>` : `${v2}`;
      return `(${u1}, ${u2})`;
    }

    if (cellTL) cellTL.innerHTML = formatCell("TL", tl1, tl2);
    if (cellTR) cellTR.innerHTML = formatCell("TR", tr1, tr2);
    if (cellBL) cellBL.innerHTML = formatCell("BL", bl1, bl2);
    if (cellBR) cellBR.innerHTML = formatCell("BR", br1, br2);

    // Identify Pure Nash Equilibria
    const pureNash = [];
    const checkNash = (cellId, rName, cName, el) => {
      if (p1Underline[cellId] && p2Underline[cellId]) {
        pureNash.push(`(${rName}, ${cName})`);
        if (el) el.classList.add("nash-cell");
      } else {
        if (el) el.classList.remove("nash-cell");
      }
    };
    checkNash("TL", r1Name, c1Name, cellTL);
    checkNash("TR", r1Name, c2Name, cellTR);
    checkNash("BL", r2Name, c1Name, cellBL);
    checkNash("BR", r2Name, c2Name, cellBR);

    // Dominance analysis
    let domReport = [];
    // Player 1 dominance
    if (tl1 > bl1 && tr1 > br1) domReport.push(`Dla Gracza 1 strategia <strong>${r1Name}</strong> ściśle dominuje <strong>${r2Name}</strong>.`);
    else if (bl1 > tl1 && br1 > tr1) domReport.push(`Dla Gracza 1 strategia <strong>${r2Name}</strong> ściśle dominuje <strong>${r1Name}</strong>.`);
    else if (tl1 >= bl1 && tr1 >= br1 && (tl1 > bl1 || tr1 > br1)) domReport.push(`Dla Gracza 1 strategia <strong>${r1Name}</strong> słabo dominuje <strong>${r2Name}</strong>.`);
    else if (bl1 >= tl1 && br1 >= tr1 && (bl1 > tl1 || br1 > tr1)) domReport.push(`Dla Gracza 1 strategia <strong>${r2Name}</strong> słabo dominuje <strong>${r1Name}</strong>.`);
    else domReport.push(`Gracz 1 nie posiada strategii zdominowanych.`);

    // Player 2 dominance
    if (tl2 > tr2 && bl2 > br2) domReport.push(`Dla Gracza 2 strategia <strong>${c1Name}</strong> ściśle dominuje <strong>${c2Name}</strong>.`);
    else if (tr2 > tl2 && br2 > bl2) domReport.push(`Dla Gracza 2 strategia <strong>${c2Name}</strong> ściśle dominuje <strong>${c1Name}</strong>.`);
    else if (tl2 >= tr2 && bl2 >= br2 && (tl2 > tr2 || bl2 > br2)) domReport.push(`Dla Gracza 2 strategia <strong>${c1Name}</strong> słabo dominuje <strong>${c2Name}</strong>.`);
    else if (tr2 >= tl2 && br2 >= bl2 && (tr2 > tl2 || br2 > bl2)) domReport.push(`Dla Gracza 2 strategia <strong>${c2Name}</strong> słabo dominuje <strong>${c1Name}</strong>.`);
    else domReport.push(`Gracz 2 nie posiada strategii zdominowanych.`);

    // Mixed Nash Calculation
    // P2 indifference: tl1 * q + tr1 * (1-q) = bl1 * q + br1 * (1-q)
    // q*(tl1 - bl1 - tr1 + br1) = br1 - tr1 => q = (br1 - tr1) / ((tl1 - bl1) + (br1 - tr1))
    // P1 indifference: tl2 * p + bl2 * (1-p) = tr2 * p + br2 * (1-p)
    // p*(tl2 - tr2 - bl2 + br2) = br2 - bl2 => p = (br2 - bl2) / ((tl2 - tr2) + (br2 - bl2))
    const denomQ = (tl1 - bl1) - (tr1 - br1);
    const numQ = br1 - tr1;
    let qStar = null;
    if (denomQ !== 0) {
      const qVal = numQ / denomQ;
      if (qVal > 0 && qVal < 1) qStar = qVal;
    }

    const denomP = (tl2 - tr2) - (bl2 - br2);
    const numP = br2 - bl2;
    let pStar = null;
    if (denomP !== 0) {
      const pVal = numP / denomP;
      if (pVal > 0 && pVal < 1) pStar = pVal;
    }

    // Render results in UI
    const resEl = document.getElementById("matrixResultsPanel");
    if (resEl) {
      let html = `<div class="space-y-3">`;
      html += `<div><span class="text-xs font-semibold uppercase text-slate-500">Równowagi w strategiach czystych:</span> `;
      if (pureNash.length > 0) {
        html += `<span class="inline-flex gap-1.5 ml-1">${pureNash.map(n => `<span class="px-2 py-0.5 bg-emerald-100 text-emerald-800 rounded font-semibold text-xs">${n}</span>`).join(" ")}</span>`;
      } else {
        html += `<span class="text-xs text-slate-600 font-medium ml-1">Brak równowagi w strategiach czystych.</span>`;
      }
      html += `</div>`;

      html += `<div><span class="text-xs font-semibold uppercase text-slate-500">Równowaga w strategiach mieszanych:</span> `;
      if (pStar !== null && qStar !== null) {
        const pPct = (pStar * 100).toFixed(1);
        const qPct = (qStar * 100).toFixed(1);
        const eu1 = (tl1 * qStar + tr1 * (1 - qStar)).toFixed(2);
        const eu2 = (tl2 * pStar + bl2 * (1 - pStar)).toFixed(2);
        html += `<div class="mt-1 p-2.5 bg-blue-50 border border-blue-200 rounded-lg text-xs space-y-1">
          <div>Gracz 1 gra <strong>${r1Name}</strong> z prawdopodobieństwem $p^* = ${pStar.toFixed(3)}$ (${pPct}%), a <strong>${r2Name}</strong> z $(1-p^*) = ${(1-pStar).toFixed(3)}$.</div>
          <div>Gracz 2 gra <strong>${c1Name}</strong> z prawdopodobieństwem $q^* = ${qStar.toFixed(3)}$ (${qPct}%), a <strong>${c2Name}</strong> z $(1-q^*) = ${(1-qStar).toFixed(3)}$.</div>
          <div class="text-slate-600 pt-1 border-t border-blue-200">Oczekiwana wypłata: $\\mathbb{E}[\\pi_1] = ${eu1}$, $\\mathbb{E}[\\pi_2] = ${eu2}$.</div>
        </div>`;
      } else {
        html += `<span class="text-xs text-slate-600 font-medium ml-1">Brak wewnętrznej równowagi mieszanej (istnieją tylko zdegenerowane równowagi czyste).</span>`;
      }
      html += `</div>`;

      html += `<div class="text-xs text-slate-600 pt-1 border-t border-slate-100">
        <span class="font-semibold uppercase text-slate-500 block mb-1">Analiza dominacji:</span>
        <ul class="list-disc list-inside space-y-0.5">
          ${domReport.map(r => `<li>${r}</li>`).join("")}
        </ul>
      </div>`;

      html += `</div>`;
      resEl.innerHTML = html;

      // Re-render KaTeX in matrix results
      if (window.renderMathInElement) {
        renderMathInElement(resEl, {
          delimiters: [{ left: "$", right: "$", display: false }]
        });
      }
    }
  }

  // Load default preset on startup
  loadPreset("prisoners");
}

// ==========================================
// 4. LAB 2: EXTENSIVE TREE & BACKWARD INDUCTION
// ==========================================
function initTreeSolver() {
  const container = document.getElementById("treeCanvasContainer");
  if (!container) return;

  const sliderAmy50 = document.getElementById("treeAmyOffer50");
  const sliderBethFair = document.getElementById("treeBethFairness");

  function drawTree() {
    const svg = document.getElementById("treeSvg");
    if (!svg) return;

    // Parameters
    const amyOffer = sliderAmy50 ? parseInt(sliderAmy50.value) : 50; // Amy offer for Player 2 (k USD)
    const bethFairness = sliderBethFair ? parseInt(sliderBethFair.value) : 10; // beth value of punishing unfairness

    // Terminal payoffs:
    // Branch 1: Amy offers 50-50 (50k each)
    // Beth Accept: Amy 50, Beth 50
    // Beth Reject: Amy 40, Beth 20 (litigation cost)
    // Branch 2: Amy offers 70-30 (Amy 70, Beth 30)
    // Beth Accept: Amy 70, Beth 30 - bethFairness (disutility of being mistreated)
    // Beth Reject: Amy 40, Beth 20

    const t1_amy = 50, t1_beth = 50;
    const t2_amy = 40, t2_beth = 20;
    const t3_amy = 70, t3_beth = 30 - bethFairness;
    const t4_amy = 40, t4_beth = 20;

    // Backward induction decisions:
    // At node 2 (after 50-50): Beth compares t1_beth vs t2_beth
    const beth_50_choice = t1_beth >= t2_beth ? "Accept" : "Reject";
    const v2_50_amy = beth_50_choice === "Accept" ? t1_amy : t2_amy;
    const v2_50_beth = beth_50_choice === "Accept" ? t1_beth : t2_beth;

    // At node 3 (after 70-30): Beth compares t3_beth vs t4_beth
    const beth_70_choice = t3_beth >= t4_beth ? "Accept" : "Reject";
    const v2_70_amy = beth_70_choice === "Accept" ? t3_amy : t4_amy;
    const v2_70_beth = beth_70_choice === "Accept" ? t3_beth : t4_beth;

    // At Root (Amy): compares v2_50_amy vs v2_70_amy
    const amy_choice = v2_70_amy >= v2_50_amy ? "Offer 70-30" : "Offer 50-50";

    // Update labels in UI
    const txtChoice = document.getElementById("treeOutcomeReport");
    if (txtChoice) {
      txtChoice.innerHTML = `
        <div class="space-y-1 text-xs">
          <div>Decyzja Beth przy ofercie 50-50: <span class="font-bold text-emerald-700">${beth_50_choice}</span> (Wypłaty: ${v2_50_amy}k, ${v2_50_beth}k)</div>
          <div>Decyzja Beth przy ofercie 70-30: <span class="font-bold ${beth_70_choice === 'Reject' ? 'text-rose-700' : 'text-emerald-700'}">${beth_70_choice}</span> (Wypłaty: ${v2_70_amy}k, ${v2_70_beth}k)</div>
          <div class="pt-1 border-t border-slate-200">Wsteczna indukcja Amy (Korzeń): <span class="font-bold text-blue-700">${amy_choice}</span>. 
          ${amy_choice === 'Offer 50-50' ? 'Amy przewiduje, że oferta 70-30 wywoła proces sądowy (Odrzucenie), więc oferuje 50-50!' : 'Amy przewiduje, że Beth zaakceptuje 70-30, więc maksymalizuje swój zysk!'}</div>
        </div>
      `;
    }

    // Redraw SVG paths
    const stroke50 = amy_choice === "Offer 50-50" ? "#2563eb" : "#cbd5e1";
    const width50 = amy_choice === "Offer 50-50" ? "3.5" : "1.5";
    const stroke70 = amy_choice === "Offer 70-30" ? "#2563eb" : "#cbd5e1";
    const width70 = amy_choice === "Offer 70-30" ? "3.5" : "1.5";

    const strokeB1 = beth_50_choice === "Accept" ? "#059669" : "#cbd5e1";
    const widthB1 = beth_50_choice === "Accept" ? "3" : "1.5";
    const strokeB2 = beth_50_choice === "Reject" ? "#059669" : "#cbd5e1";
    const widthB2 = beth_50_choice === "Reject" ? "3" : "1.5";

    const strokeB3 = beth_70_choice === "Accept" ? "#059669" : "#cbd5e1";
    const widthB3 = beth_70_choice === "Accept" ? "3" : "1.5";
    const strokeB4 = beth_70_choice === "Reject" ? "#059669" : "#cbd5e1";
    const widthB4 = beth_70_choice === "Reject" ? "3" : "1.5";

    svg.innerHTML = `
      <!-- Edges from Root -->
      <line x1="280" y1="40" x2="140" y2="120" stroke="${stroke50}" stroke-width="${width50}" />
      <line x1="280" y1="40" x2="420" y2="120" stroke="${stroke70}" stroke-width="${width70}" />

      <!-- Edges from Left Node (50-50) -->
      <line x1="140" y1="120" x2="70" y2="200" stroke="${strokeB1}" stroke-width="${widthB1}" />
      <line x1="140" y1="120" x2="200" y2="200" stroke="${strokeB2}" stroke-width="${widthB2}" />

      <!-- Edges from Right Node (70-30) -->
      <line x1="420" y1="120" x2="350" y2="200" stroke="${strokeB3}" stroke-width="${widthB3}" />
      <line x1="420" y1="120" x2="480" y2="200" stroke="${strokeB4}" stroke-width="${widthB4}" />

      <!-- Root Node (Amy) -->
      <circle cx="280" cy="40" r="14" fill="#2563eb" />
      <text x="280" y="44" fill="#ffffff" font-size="11" font-family="Plus Jakarta Sans" font-weight="700" text-anchor="middle">Amy</text>
      <text x="195" y="70" fill="#475569" font-size="10" font-family="Plus Jakarta Sans" font-weight="600" text-anchor="middle">Oferta 50-50</text>
      <text x="365" y="70" fill="#475569" font-size="10" font-family="Plus Jakarta Sans" font-weight="600" text-anchor="middle">Oferta 70-30</text>

      <!-- Beth Nodes -->
      <circle cx="140" cy="120" r="14" fill="#059669" />
      <text x="140" y="124" fill="#ffffff" font-size="11" font-family="Plus Jakarta Sans" font-weight="700" text-anchor="middle">Beth</text>

      <circle cx="420" cy="120" r="14" fill="#059669" />
      <text x="420" y="124" fill="#ffffff" font-size="11" font-family="Plus Jakarta Sans" font-weight="700" text-anchor="middle">Beth</text>

      <!-- Sub-branch labels -->
      <text x="90" y="155" fill="#475569" font-size="9" font-family="Plus Jakarta Sans" text-anchor="middle">Akceptuj</text>
      <text x="185" y="155" fill="#475569" font-size="9" font-family="Plus Jakarta Sans" text-anchor="middle">Odrzuć</text>
      <text x="370" y="155" fill="#475569" font-size="9" font-family="Plus Jakarta Sans" text-anchor="middle">Akceptuj</text>
      <text x="465" y="155" fill="#475569" font-size="9" font-family="Plus Jakarta Sans" text-anchor="middle">Odrzuć</text>

      <!-- Terminal Payoffs -->
      <circle cx="70" cy="200" r="4" fill="#0f172a" />
      <text x="70" y="216" fill="#0f172a" font-size="10" font-family="JetBrains Mono" font-weight="700" text-anchor="middle">(${t1_amy}, ${t1_beth})</text>

      <circle cx="200" cy="200" r="4" fill="#0f172a" />
      <text x="200" y="216" fill="#0f172a" font-size="10" font-family="JetBrains Mono" font-weight="700" text-anchor="middle">(${t2_amy}, ${t2_beth})</text>

      <circle cx="350" cy="200" r="4" fill="#0f172a" />
      <text x="350" y="216" fill="#0f172a" font-size="10" font-family="JetBrains Mono" font-weight="700" text-anchor="middle">(${t3_amy}, ${t3_beth})</text>

      <circle cx="480" cy="200" r="4" fill="#0f172a" />
      <text x="480" y="216" fill="#0f172a" font-size="10" font-family="JetBrains Mono" font-weight="700" text-anchor="middle">(${t4_amy}, ${t4_beth})</text>
    `;
  }

  if (sliderBethFair) {
    sliderBethFair.addEventListener("input", (e) => {
      const lbl = document.getElementById("treeValFairness");
      if (lbl) lbl.innerText = `${e.target.value}k USD`;
      drawTree();
    });
  }

  drawTree();
}

// ==========================================
// 5. LAB 3: INTERACTIVE BAYES & MONTY HALL
// ==========================================
function initBayesEngine() {
  const btnSimulate = document.getElementById("bayesRunSimBtn");
  const btnReset = document.getElementById("bayesResetBtn");
  const stayWinEl = document.getElementById("bayesStayWinRate");
  const switchWinEl = document.getElementById("bayesSwitchWinRate");
  const trialsCountEl = document.getElementById("bayesTrialsCount");

  let totalTrials = 0;
  let stayWins = 0;
  let switchWins = 0;

  function runTrials(n = 500) {
    for (let i = 0; i < n; i++) {
      const carDoor = Math.floor(Math.random() * 3); // 0, 1, 2
      const playerDoor = Math.floor(Math.random() * 3);

      // Host opens a door that is not player's door and not carDoor
      let hostDoor;
      const available = [0, 1, 2].filter(d => d !== playerDoor && d !== carDoor);
      if (available.length === 1) {
        hostDoor = available[0];
      } else {
        hostDoor = available[Math.floor(Math.random() * available.length)];
      }

      // Switch choice: the door that is not playerDoor and not hostDoor
      const switchDoor = [0, 1, 2].find(d => d !== playerDoor && d !== hostDoor);

      if (playerDoor === carDoor) stayWins++;
      if (switchDoor === carDoor) switchWins++;
      totalTrials++;
    }

    if (trialsCountEl) trialsCountEl.innerText = totalTrials;
    if (stayWinEl) stayWinEl.innerText = `${((stayWins / totalTrials) * 100).toFixed(1)}%`;
    if (switchWinEl) switchWinEl.innerText = `${((switchWins / totalTrials) * 100).toFixed(1)}%`;
  }

  if (btnSimulate) {
    btnSimulate.addEventListener("click", () => runTrials(500));
  }

  if (btnReset) {
    btnReset.addEventListener("click", () => {
      totalTrials = 0;
      stayWins = 0;
      switchWins = 0;
      if (trialsCountEl) trialsCountEl.innerText = "0";
      if (stayWinEl) stayWinEl.innerText = "33.3%";
      if (switchWinEl) switchWinEl.innerText = "66.7%";
    });
  }
}

// ==========================================
// 6. LAB 4: INTERACTIVE AUMANN KNOWLEDGE GRAPH
// ==========================================
function initAumannGraph() {
  const selectState = document.getElementById("aumannStateSelect");
  const resPanel = document.getElementById("aumannResultPanel");

  // States W = {a, b, c, d, e}
  // Partition 1: {a, b, c}, {d, e}
  // Partition 2: {a, b}, {c, d}, {e}
  const part1 = [["a", "b", "c"], ["d", "e"]];
  const part2 = [["a", "b"], ["c", "d"], ["e"]];

  function computeCommonKnowledge(state) {
    // BFS reachability to find connected component in graph
    const visited = new Set([state]);
    const queue = [state];

    while (queue.length > 0) {
      const cur = queue.shift();
      // Neighbor states via P1
      const p1Cell = part1.find(c => c.includes(cur)) || [];
      p1Cell.forEach(s => {
        if (!visited.has(s)) {
          visited.add(s);
          queue.push(s);
        }
      });
      // Neighbor states via P2
      const p2Cell = part2.find(c => c.includes(cur)) || [];
      p2Cell.forEach(s => {
        if (!visited.has(s)) {
          visited.add(s);
          queue.push(s);
        }
      });
    }

    const ckCell = Array.from(visited).sort();
    const p1StateCell = part1.find(c => c.includes(state)) || [];
    const p2StateCell = part2.find(c => c.includes(state)) || [];

    if (resPanel) {
      resPanel.innerHTML = `
        <div class="space-y-2 text-xs">
          <div>Stan świata: <strong class="text-blue-700 font-mono text-sm">${state}</strong></div>
          <div>Zbiór informacyjny Gracza 1: $\\mathcal{I}_1(${state}) = \\{${p1StateCell.join(", ")}\\}$</div>
          <div>Zbiór informacyjny Gracza 2: $\\mathcal{I}_2(${state}) = \\{${p2StateCell.join(", ")}\\}$</div>
          <div class="p-3 bg-purple-50 border border-purple-200 rounded-lg text-purple-950 font-medium">
            Komórka Wspólnej Wiedzy: $\\mathcal{I}_{CK}(${state}) = \\{${ckCell.join(", ")}\\}$<br>
            <span class="text-slate-600 text-[11px] block mt-1">
              ${ckCell.length === 5 ? 'Cała przestrzeń stanów tworzy jedną komórkę wspólnej wiedzy! Żadne nietrywialne zdarzenie nie jest wspólną wiedzą.' : 'Wspólna wiedza jest ograniczona do podzbioru stanów osiągalnych.'}
            </span>
          </div>
        </div>
      `;
      if (window.renderMathInElement) {
        renderMathInElement(resPanel, {
          delimiters: [{ left: "$", right: "$", display: false }]
        });
      }
    }
  }

  if (selectState) {
    selectState.addEventListener("change", (e) => computeCommonKnowledge(e.target.value));
    computeCommonKnowledge(selectState.value);
  }
}

// ==========================================
// 7. DIAGNOSTIC QUIZ ENGINE
// ==========================================
const QUIZ_QUESTIONS = [
  {
    q: "W aukcji drugiej ceny Vickreya (William Vickrey, 1961), dlaczego licytowanie prawdziwej wyceny ($b_i = v_i$) jest strategią słabo dominującą tylko przy założeniu, że gracze są egoistyczni i chciwi?",
    opts: [
      "A. Ponieważ twierdzenie Vickreya nie zakłada istnienia racjonalności graczy.",
      "B. Ponieważ licytujący złośliwy (spiteful) może woleć podbić stawkę rywala powyżej wyceny, a licytujący altruistyczny woli zaniżyć ofertę, by rywal zapłacił mniej.",
      "C. Ponieważ w aukcji Vickreya zwycięzca zawsze płaci własną ofertę.",
      "D. Ponieważ słaba dominacja zachodzi wyłącznie w grach o sumie zerowej."
    ],
    correct: 1,
    exp: "Dokładnie tak! Jak dowodzi Bonanno w Twierdzeniu 1.1, jeśli gracz ma motywacje złośliwe (chce, by przegrany lub zwycięzca poniósł maksymalny koszt) lub altruistyczne, funkcja wypłat nie zależy wyłącznie od jego własnego zysku netto $v_i - p$, co niszczy słabą dominację prawdomówności."
  },
  {
    q: "W zagadce trzech kapeluszy (Rozdział 7), dlaczego publiczne ogłoszenie profesora: 'Co najmniej jeden kapelusz jest czerwony' zmienia stan gry, skoro każdy ze studentów widzi dwa czerwone kapelusze i już to wie?",
    opts: [
      "A. Ponieważ ogłoszenie dostarcza studentom nowych informacji o kolorze ich własnego kapelusza bezpośrednio.",
      "B. Ponieważ przed ogłoszeniem fakt ten był wiedzą każdego z osobna ($K_1 E, K_2 E, K_3 E$), lecz NIE był wspólną wiedzą (nie zachodziło $K_1 K_2 K_3 E$). Publiczne ogłoszenie tworzy wspólną wiedzę $CKE$.",
      "C. Ponieważ studenci nie posiadają doskonałej pamięci (perfect recall).",
      "D. Ponieważ informacja ta eliminuje stany o niezerowym prawdopodobieństwie w sensie Bayesa."
    ],
    correct: 1,
    exp: "Znakomita odpowiedź! To centralny punkt epistemologii Aumanna. Przed ogłoszeniem Student 1 widzi 2 czerwone kapelusze, ale dopuszcza, że ma biały; wówczas Student 2 widziałby 1 czerwony i 1 biały i dopuszczałby, że Student 3 widzi 2 białe i uważa, że wszystkie są białe. Publiczne ogłoszenie przecina ten łańcuch i tworzy Wspólną Wiedzę $CKE$."
  },
  {
    q: "Co orzeka słynne Twierdzenie Aumanna o Zgodzie (Robert Aumann, 1976: 'Agreeing to Disagree')?",
    opts: [
      "A. Racjonalni gracze nigdy nie mogą dojść do porozumienia w negocjacjach o sumie zerowej.",
      "B. Jeśli dwaj racjonalni agenci posiadają wspólny rozkład a priori (Common Prior) i prawdopodobieństwa ich przekonań a posteriori stają się wspólną wiedzą, to te prawdopodobieństwa muszą być identyczne ($p = q$).",
      "C. Każda gra w postaci ekstensywnej o wypłatach kardynalnych posiada unikalną równowagę Nasha.",
      "D. Agenci o różnych informacjach prywatnych zawsze blefują w równowadze rozdzielającej."
    ],
    correct: 1,
    exp: "Świetnie! Twierdzenie Aumanna dowodzi, że racjonalni agenci o wspólnych przekonaniach pierwotnych nie mogą 'zgodzić się na niezgodę'. Jeżeli ich subiektywne prawdopodobieństwa staną się wspólną wiedzą, asymetria informacyjna zostaje zniwelowana i $p$ musi równać się $q$."
  },
  {
    q: "W równowadze w strategiach mieszanych Nasha (Rozdział 5), jaka jest kluczowa cecha wypłat z czystych strategii należących do nośnika gracza?",
    opts: [
      "A. Gracz uzyskuje ściśle wyższą wypłatę ze strategii granej z większym prawdopodobieństwem.",
      "B. Zgodnie z Zasadą Obojętności (Twierdzenie 5.2), gracz uzyskuje identyczną oczekiwaną wypłatę ze wszystkich czystych strategii w swoim nośniku. Randomizuje wyłącznie po to, by uczynić rywala obojętnym!",
      "C. Wszystkie strategie rywala zostają natychmiast słabo zdominowane.",
      "D. Oczekiwana wypłata każdego gracza musi być równa zeru."
    ],
    correct: 1,
    exp: "Prawda! To fundamentalny wniosek Bonanno: w równowadze mieszanej sam gracz jest obojętny między swoimi opcjami z nośnika. Cel randomizacji leży w motywowaniu rywala do niezmieniania swojej strategii."
  },
  {
    q: "Dlaczego Słaba Równowaga Sekwencyjna (WSE, Rozdział 10) NIE jest ścisłym uszczegółowieniem Równowagi Doskonałej w Podgrach (SPE)?",
    opts: [
      "A. Ponieważ WSE nie wymaga racjonalności sekwencyjnej.",
      "B. Ponieważ w nieosiąganych zbiorach informacyjnych reguła Bayesa nie narzuca żadnych ograniczeń na przekonania, co pozwala na arbitralne przekonania naruszające równowagę Nasha w nieosiąganej podgrze!",
      "C. Ponieważ WSE stosuje się wyłącznie do gier statycznych.",
      "D. Ponieważ twierdzenie Nasha nie obowiązuje dla ocen $(\\sigma, \\mu)$."
    ],
    correct: 1,
    exp: "Wybitna precyzja! WSE wymaga aktualizacji bayesowskiej tylko w zbiorach osiąganych. W nieosiąganych podgrach przekonania mogą być zupełnie dowolne, co sprawia, że profil strategii w WSE może nie tworzyć równowagi Nasha w owej podgrze. Dlatego WSE i SPE przecinają się, ale żadne nie zawiera drugiego w całości!"
  },
  {
    q: "Na czym polega przełomowe twierdzenie Giacomo Bonanno (2015) łączące Doskonałą Równowagę Bayesowską (PBE) z Równowagą Sekwencyjną Krepsa-Wilsona?",
    opts: [
      "A. Bonanno wykazał, że równowaga Krepsa-Wilsona nigdy nie istnieje w grach z naturą.",
      "B. Bonanno udowodnił, że ocena $(\\sigma, \\mu)$ jest Równowagą Sekwencyjną wtedy i tylko wtedy, gdy jest PBE spełniającym mierzalność wyborów (CM) porządku wiarygodności oraz jednorodną spójność bayesowską, eliminując konieczność ciągów i granic topologicznych!",
      "C. Bonanno zastąpił pojęcie przekonań regułą minimaksu von Neumanna.",
      "D. Dowiódł, że teorie Harsanyiego i Kripkego są matematycznie sprzeczne."
    ],
    correct: 1,
    exp: "Fenomenalnie! Twierdzenie 12.5 Bonanno (2015) całkowicie uwalnia teorię równowag sekwencyjnych od sztucznego, nieintuicyjnego aparatu zbieżności ciągów zaburzonych strategii (Kreps-Wilson 1982), zastępując go przejrzystą, algebraiczną strukturą porządku wiarygodności AGM z zachowaniem proporcji odległości (Choice Measurability)."
  }
];

function initQuiz() {
  const container = document.getElementById("quizQuestionsContainer");
  const scoreEl = document.getElementById("quizScoreTracker");
  if (!container) return;

  let answeredCount = 0;
  let correctCount = 0;

  let html = "";
  QUIZ_QUESTIONS.forEach((qObj, qIdx) => {
    html += `
      <div class="p-5 bg-slate-50 border border-slate-200 rounded-xl space-y-3" id="quiz_q_${qIdx}">
        <div class="flex items-start justify-between gap-3">
          <span class="text-xs font-bold uppercase tracking-wider text-blue-600 font-mono">Pytanie 0${qIdx + 1}</span>
          <span class="text-xs text-slate-400 font-mono" id="q_${qIdx}_badge">Czeka na odpowiedź</span>
        </div>
        <p class="text-sm font-semibold text-slate-900 leading-snug">${qObj.q}</p>
        <div class="space-y-2 pt-1" id="q_${qIdx}_opts">
          ${qObj.opts.map((opt, oIdx) => `
            <button class="quiz-opt-btn" id="q_${qIdx}_opt_${oIdx}" data-q="${qIdx}" data-opt="${oIdx}">
              ${opt}
            </button>
          `).join("")}
        </div>
        <div class="hidden p-3 rounded-lg text-xs leading-relaxed" id="q_${qIdx}_exp"></div>
      </div>
    `;
  });

  container.innerHTML = html;

  // Bind option clicks
  const allBtns = container.querySelectorAll(".quiz-opt-btn");
  allBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const qIdx = parseInt(btn.getAttribute("data-q") || 0);
      const oIdx = parseInt(btn.getAttribute("data-opt") || 0);
      const qObj = QUIZ_QUESTIONS[qIdx];
      const parentOpts = document.getElementById(`q_${qIdx}_opts`);
      if (!parentOpts) return;

      // Disable further clicks on this question
      const siblingBtns = parentOpts.querySelectorAll(".quiz-opt-btn");
      siblingBtns.forEach(b => b.disabled = true);

      const expDiv = document.getElementById(`q_${qIdx}_exp`);
      const badge = document.getElementById(`q_${qIdx}_badge`);

      if (oIdx === qObj.correct) {
        btn.classList.add("correct");
        correctCount++;
        if (badge) {
          badge.innerText = "Poprawnie!";
          badge.className = "text-xs font-mono font-bold text-emerald-600";
        }
        if (expDiv) {
          expDiv.className = "p-3 bg-emerald-50 border border-emerald-200 text-emerald-950 rounded-lg text-xs leading-relaxed";
          expDiv.innerHTML = `<strong>Prawidłowa odpowiedź:</strong> ${qObj.exp}`;
          expDiv.classList.remove("hidden");
        }
      } else {
        btn.classList.add("wrong");
        const correctBtn = document.getElementById(`q_${qIdx}_opt_${qObj.correct}`);
        if (correctBtn) correctBtn.classList.add("correct");
        if (badge) {
          badge.innerText = "Błąd";
          badge.className = "text-xs font-mono font-bold text-rose-600";
        }
        if (expDiv) {
          expDiv.className = "p-3 bg-rose-50 border border-rose-200 text-rose-950 rounded-lg text-xs leading-relaxed";
          expDiv.innerHTML = `<strong>Błędna odpowiedź.</strong> ${qObj.exp}`;
          expDiv.classList.remove("hidden");
        }
      }

      answeredCount++;
      if (scoreEl) {
        scoreEl.innerText = `${correctCount} / ${QUIZ_QUESTIONS.length}`;
      }

      // Re-render KaTeX on the explanation and question card
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById(`quiz_q_${qIdx}`), {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false },
            { left: "\\(", right: "\\)", display: false }
          ],
          throwOnError: false
        });
      }
    });
  });

  // Re-render KaTeX on initial quiz injection
  if (window.renderMathInElement) {
    renderMathInElement(container, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false },
        { left: "\\(", right: "\\)", display: false }
      ],
      throwOnError: false
    });
  }
}

// ==========================================
// 8. CODE SNIPPET COPY BUTTON
// ==========================================
function initCodeCopy() {
  const copyBtn = document.getElementById("copyCodeBtn");
  const codeBlock = document.getElementById("pythonCodeBlock");
  if (!copyBtn || !codeBlock) return;

  copyBtn.addEventListener("click", () => {
    const text = codeBlock.innerText;
    navigator.clipboard.writeText(text).then(() => {
      const orig = copyBtn.innerHTML;
      copyBtn.innerHTML = `✓ Skopiowano!`;
      copyBtn.classList.remove("bg-slate-800", "text-slate-300");
      copyBtn.classList.add("bg-emerald-600", "text-white");
      setTimeout(() => {
        copyBtn.innerHTML = orig;
        copyBtn.classList.remove("bg-emerald-600", "text-white");
        copyBtn.classList.add("bg-slate-800", "text-slate-300");
      }, 2000);
    });
  });
}
