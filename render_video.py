import asyncio
import os
import subprocess
from playwright.async_api import async_playwright

async def render():
    target_dir = os.path.dirname(os.path.abspath(__file__))
    output_mp4 = os.path.join(target_dir, "explainer_preview.mp4")
    temp_dir = os.path.join(target_dir, ".video_temp")
    os.makedirs(temp_dir, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-setuid-sandbox"])
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            record_video_dir=temp_dir,
            record_video_size={"width": 1920, "height": 1080}
        )
        page = await context.new_page()

        file_path = "file://" + os.path.join(target_dir, "index.html")
        print(f"Loading {file_path} for programmatic video render...")
        await page.goto(file_path, wait_until="domcontentloaded")
        await page.wait_for_timeout(2000)

        # 1. Hero overview
        await page.wait_for_timeout(2500)

        # 2. Scroll to Lab 1 (Matrix solver)
        lab1 = page.locator("#lab-sekcja")
        if await lab1.count() > 0:
            await lab1.scroll_into_view_if_needed()
            await page.wait_for_timeout(1500)
            preset_select = page.locator("#matrixPresetSelect")
            if await preset_select.count() > 0:
                await preset_select.select_option("battle")
                await page.wait_for_timeout(1500)
                await preset_select.select_option("pennies")
                await page.wait_for_timeout(1500)

        # 3. Scroll to Lab 2 (Tree solver) and slide fairness
        slider = page.locator("#treeBethFairness")
        if await slider.count() > 0:
            await slider.scroll_into_view_if_needed()
            await page.wait_for_timeout(1000)
            for val in ["5", "10", "15", "20"]:
                await slider.fill(val)
                await page.wait_for_timeout(500)

        await page.close()
        await context.close()
        await browser.close()

    video_files = [os.path.join(temp_dir, f) for f in os.listdir(temp_dir) if f.endswith(".webm")]
    if not video_files:
        raise RuntimeError("No recorded video found in temp dir")

    recorded_webm = video_files[0]
    print(f"Recorded webm: {recorded_webm}, transcoding to MP4 via ffmpeg...")

    cmd = [
        "/opt/homebrew/bin/ffmpeg", "-y",
        "-i", recorded_webm,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-crf", "18",
        "-preset", "fast",
        "-movflags", "+faststart",
        output_mp4
    ]
    subprocess.run(cmd, check=True)

    for f in os.listdir(temp_dir):
        os.remove(os.path.join(temp_dir, f))
    os.rmdir(temp_dir)

    print(f"Successfully generated: {output_mp4}")

if __name__ == "__main__":
    asyncio.run(render())
