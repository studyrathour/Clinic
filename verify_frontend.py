from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        pages_to_screenshot = [
            {'url': 'http://localhost:5000/', 'name': 'home'},
            {'url': 'http://localhost:5000/about', 'name': 'about'},
            {'url': 'http://localhost:5000/gallery', 'name': 'gallery'},
        ]

        for p_info in pages_to_screenshot:
            print(f"Screenshotting {p_info['name']}...")
            page.goto(p_info['url'])
            page.wait_for_timeout(1000)
            page.screenshot(path=f"/app/screenshot_{p_info['name']}.png", full_page=True)
            print(f"Saved {p_info['name']}")

        browser.close()
        print("Done.")

run()
