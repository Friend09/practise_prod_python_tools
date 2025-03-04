from playwright.sync_api import sync_playwright


def capture_website_screenshot(url: str, filepath: str) -> None:
    """
    Captures a screenshot of a given website and saves it to a specified file.

    Args:
        url (str): The URL of the website to capture.
        filepath (str): The path to save the screenshot.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        print(page.title())
        page.screenshot(path=filepath)
        browser.close()


if __name__ == "__main__":
    capture_website_screenshot(
        "https://practicetestautomation.com/practice-test-login/",
        "/Users/vamsi_mbmax/Library/CloudStorage/OneDrive-Personal/01_vam_PROJECTS/LEARNING/proj_Productivity/dev_proj_Productivity/practise_prod_python_tools/files/example.png"
    )
