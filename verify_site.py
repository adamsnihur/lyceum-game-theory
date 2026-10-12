import asyncio
import os
import re
from playwright.async_api import async_playwright

async def run_tests():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await context.new_page()

        console_errors = []
        page_errors = []

        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: page_errors.append(str(err)))

        target = "Lyceum/game-theory/index.html" if os.path.exists("Lyceum/game-theory/index.html") else "index.html"
        file_path = "file://" + os.path.abspath(target)
        print(f"Loading {file_path}...")
        await page.goto(file_path, wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(2500)

        print("Console errors on load:", console_errors)
        print("Page errors on load:", page_errors)
        assert len(console_errors) == 0, f"Found console errors: {console_errors}"
        assert len(page_errors) == 0, f"Found page errors: {page_errors}"

        # 1. KaTeX rendering verification
        katex_count = await page.locator(".katex").count()
        print(f"KaTeX rendered elements count: {katex_count}")
        assert katex_count > 15, f"KaTeX elements did not render properly! Count: {katex_count}"

        # 1.5. Hero controls verification (Play/Pause & Reset)
        print("Testing Hero Replicator Canvas Controls...")
        play_btn = page.locator("#heroPlayPauseBtn")
        reset_btn = page.locator("#heroResetBtn")
        fps_metric = page.locator("#heroFpsMetric")
        traj_count = page.locator("#heroTrajCount")

        assert await play_btn.is_visible(), "heroPlayPauseBtn is not visible!"
        assert await reset_btn.is_visible(), "heroResetBtn is not visible!"
        initial_play_text = (await play_btn.inner_text()).strip()
        assert initial_play_text == "Zatrzymaj", f"Expected initial text 'Zatrzymaj', got '{initial_play_text}'"

        # Click pause
        await play_btn.click()
        await page.wait_for_timeout(300)
        paused_play_text = (await play_btn.inner_text()).strip()
        assert paused_play_text == "Wznów", f"Expected 'Wznów' after click, got '{paused_play_text}'"
        fps_text = (await fps_metric.inner_text()).strip()
        assert "Zatrzymano" in fps_text, f"Expected 'Zatrzymano' in FPS metric, got '{fps_text}'"

        # Click resume
        await play_btn.click()
        await page.wait_for_timeout(300)
        resumed_play_text = (await play_btn.inner_text()).strip()
        assert resumed_play_text == "Zatrzymaj", f"Expected 'Zatrzymaj' after resume, got '{resumed_play_text}'"

        # Click reset
        await reset_btn.click()
        await page.wait_for_timeout(300)
        traj_text = (await traj_count.inner_text()).strip()
        assert "cząstek" in traj_text, f"Expected particle count after reset, got '{traj_text}'"

        # Check for visible literal "\\n" in DOM (excluding KaTeX mathml annotations and code)
        print("Checking for visible literal '\\n' characters in body...")
        literal_slash_n = await page.evaluate('''() => {
            const bad = [];
            const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
            while (walker.nextNode()) {
                const node = walker.currentNode;
                if (node.parentElement && (
                    node.parentElement.closest('.katex') ||
                    node.parentElement.tagName === 'ANNOTATION' ||
                    node.parentElement.tagName === 'SCRIPT' ||
                    node.parentElement.tagName === 'STYLE' ||
                    node.parentElement.tagName === 'CODE' ||
                    node.parentElement.tagName === 'PRE'
                )) {
                    continue;
                }
                const t = node.textContent;
                if (t.includes('\\\\n')) {
                    bad.push({ tag: node.parentElement ? node.parentElement.tagName : 'NONE', text: t.trim() });
                }
            }
            return bad;
        }''')
        print(f"Literal visible '\\n' occurrences: {len(literal_slash_n)}")
        assert len(literal_slash_n) == 0, f"Found visible literal '\\n' in DOM: {literal_slash_n}"

        # 2. Unrendered LaTeX Gate
        print("Checking for unrendered LaTeX syntax in visible DOM...")
        unrendered_latex = await page.evaluate('''() => {
            const regex = /\\$[^\\$]+(?:\\\\[a-zA-Z]+|\\^|_)[^\\$]*\\$/;
            const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
            const bad = [];
            while (walker.nextNode()) {
                const node = walker.currentNode;
                if (node.parentElement && (node.parentElement.closest('.katex') || node.parentElement.tagName === 'CODE' || node.parentElement.tagName === 'PRE' || node.parentElement.tagName === 'SCRIPT')) {
                    continue;
                }
                const text = node.textContent;
                if (regex.test(text)) {
                    bad.push({ tag: node.parentElement ? node.parentElement.tagName : 'NONE', text: text.trim().substring(0, 100) });
                }
            }
            return bad;
        }''')
        print(f"Unrendered LaTeX occurrences: {len(unrendered_latex)}")
        assert len(unrendered_latex) == 0, f"Found unrendered LaTeX strings: {unrendered_latex}"

        # 3. Test Lab 1 Matrix Solver
        print("Testing Lab 1 Matrix Solver...")
        preset_select = page.locator("#matrixPresetSelect")
        await preset_select.select_option("battle")
        await page.wait_for_timeout(500)
        res_text = await page.locator("#matrixResultsPanel").inner_text()
        print(f"Battle of Sexes result summary: {res_text[:80]}...")
        assert "Opera" in res_text

        await preset_select.select_option("pennies")
        await page.wait_for_timeout(500)
        pennies_res = await page.locator("#matrixResultsPanel").inner_text()
        print(f"Matching Pennies result summary: {pennies_res[:80]}...")
        assert "Brak równowagi w strategiach czystych" in pennies_res

        # 4. Test Lab 2 Extensive Tree
        print("Testing Lab 2 Extensive Tree...")
        slider = page.locator("#treeBethFairness")
        await slider.fill("5")
        await page.wait_for_timeout(500)
        report_5 = await page.locator("#treeOutcomeReport").inner_text()
        print(f"Tree report with Beth fairness=5: {report_5[:70]}...")

        await slider.fill("20")
        await page.wait_for_timeout(500)
        report_20 = await page.locator("#treeOutcomeReport").inner_text()
        print(f"Tree report with Beth fairness=20: {report_20[:70]}...")
        assert "Odrzucenie" in report_20 or "Offer 50-50" in report_20

        # 5. Test Lab 3 Monty Hall Bayes Engine
        print("Testing Lab 3 Monty Hall Simulation...")
        btn_sim = page.locator("#bayesRunSimBtn")
        await btn_sim.click()
        await page.wait_for_timeout(500)
        trials = await page.locator("#bayesTrialsCount").inner_text()
        print(f"Trials executed: {trials}")
        assert int(trials) >= 500

        # 6. Test Lab 4 Aumann Knowledge Graph
        print("Testing Lab 4 Aumann Graph...")
        aumann_select = page.locator("#aumannStateSelect")
        await aumann_select.select_option("c")
        await page.wait_for_timeout(500)
        aumann_res = await page.locator("#aumannResultPanel").inner_text()
        print(f"Aumann Result for state c: {aumann_res[:70]}...")
        assert "Stan świata: c" in aumann_res

        # 7. Test Diagnostic Quiz
        print("Testing Diagnostic Quiz...")
        opt_q0 = page.locator("#q_0_opt_1") # Correct for Q1
        await opt_q0.scroll_into_view_if_needed()
        await opt_q0.click()
        await page.wait_for_timeout(400)
        exp_0 = await page.locator("#q_0_exp").is_visible()
        print(f"Quiz Q0 explanation visible: {exp_0}")
        assert exp_0 == True

        # Test remaining quiz buttons
        for q_idx in range(1, 6):
            btn = page.locator(f"#q_{q_idx}_opt_1")
            await btn.scroll_into_view_if_needed()
            await btn.click()
            await page.wait_for_timeout(200)

        score_text = await page.locator("#quizScoreTracker").inner_text()
        print(f"Final Quiz Score: {score_text}")

        # 8. SVG Text Clipping Gate
        print("Running Quality Gate: SVG Text Clipping & DOM Overflow Check...")
        clipped_svg = await page.evaluate('''() => {
            const issues = [];
            document.querySelectorAll('svg').forEach(svg => {
                const vb = svg.viewBox.baseVal;
                if (!vb || vb.width === 0) return;
                svg.querySelectorAll('text, tspan').forEach(t => {
                    const text = t.textContent.trim();
                    if (!text) return;
                    try {
                        const bbox = t.getBBox();
                        if (bbox.x < vb.x - 3 || (bbox.x + bbox.width) > (vb.x + vb.width + 3)) {
                            issues.push({ text: text, x: bbox.x, width: bbox.width, vb_x: vb.x, vb_w: vb.width });
                        }
                    } catch (e) {}
                });
            });
            return issues;
        }''')
        print(f"SVG Text clipping issues found: {len(clipped_svg)}")
        assert len(clipped_svg) == 0, f"Found clipped SVG text elements: {clipped_svg}"

        # 9. Multi-viewport Responsive Layout Tests
        viewports = [
            ("Desktop 1440px", {"width": 1440, "height": 900}),
            ("Tablet 768px", {"width": 768, "height": 1024}),
            ("Mobile 375px", {"width": 375, "height": 812})
        ]
        for name, vp in viewports:
            await page.set_viewport_size(vp)
            await page.wait_for_timeout(300)
            has_h_scroll = await page.evaluate('''() => {
                return document.documentElement.scrollWidth > window.innerWidth + 2;
            }''')
            print(f"Viewport {name} -> Horizontal scroll detected: {has_h_scroll}")
            assert not has_h_scroll, f"Horizontal scroll detected on {name}!"

        # 10. Capture screenshot
        await page.set_viewport_size({"width": 1440, "height": 900})
        ss_path = "Lyceum/game-theory/screenshot_verified.png" if os.path.exists("Lyceum/game-theory") else "screenshot_verified.png"
        await page.screenshot(path=ss_path, full_page=True)
        print(f"Saved {ss_path}")

        await browser.close()
        print("All tests passed with 0 errors!")

if __name__ == "__main__":
    asyncio.run(run_tests())
