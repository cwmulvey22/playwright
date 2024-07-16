from playwright.sync_api import sync_playwright, Playwright

## Everything goes in the run function: 
def run(playwright: Playwright):
    start_url = "https://www.youtube.com/@sahil_bloom/videos"
    browser = playwright.chromium.launch(headless=True, slow_mo=100)
    page = browser.new_page()
    page.goto(start_url)
    print(page.title())

    ## Get the first 5 video links
    video_links = page.locator('a[id="thumbnail"]').all()[:5]

    ## Loop through the first 5 videos
    for link in video_links:
        p = browser.new_page(base_url="https://www.youtube.com/")
        url = link.get_attribute("href")
        if url is not None:
            p.goto(url)
            # Video title
            title = p.locator('h1.ytd-watch-metadata')
            if title:
                print("Title:", title.inner_text())

            # Likes
            likes = p.locator('xpath=/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/segmented-like-dislike-button-view-model/yt-smartimation/div/div/like-button-view-model/toggle-button-view-model/button-view-model/button/div[2]')
            if likes:
                print("Likes:", likes.inner_text())

            # Comments
        

        p.close()

# Run the function 
with sync_playwright() as playwright:
    run(playwright)
