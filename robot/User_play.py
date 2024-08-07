


import sys
sys.path.append('..')

from default.Print import Print
# from default.Sleep import Sleep
import time

from playwright.sync_api import sync_playwright

class User_play:
    
    def __init__(self) -> None:
        pass
    
    def start(self):
        try:
             with sync_playwright() as playwright:
                
                try:
                    
                    self.ch = "chrome"
                
                    self.browser = playwright.chromium.launch(args=['--start-maximized'], headless=False, channel=self.ch)
                
                    self.context = self.browser.new_context(no_viewport=True)

                    self.page = self.context.new_page()
                    
                    self.page.goto("http://192.168.88.245:7777/")
                    
                    # Sleep.zZz(2)
                    
                    time.sleep(2)
                    
                    
                    self.page.mouse.move(100, 100)
                    
                    for i in range(0, 100):
                        time.sleep(.1)
                        self.page.mouse.move(100 + i, 100 + i)
                    
                    
                    
                    time.sleep(2)
                    
                    
                
                except Exception as e:
                    Print.error(e)
        
        except Exception as e:
            Print.error(e)


if __name__ == "__main__":
    User_play().start()