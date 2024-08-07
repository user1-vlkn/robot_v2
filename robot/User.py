
import sys
sys.path.append('..')
from default.Print import Print
import nodriver as uc
import time
import sys

from default.Sleep import Sleep


class User:
    
    # async def __init__(self, data) -> None: self.data = data
    
    async def walk(self):
        
        try:
            browser = await uc.start()
            page = await browser.get('https://www.nowsecure.nl')
            await page.get_content()
            await page.scroll_down(150)
            
            Sleep.zZz(2)
            
            await page.close()
            
        except Exception as e:
            Print.log(e)
    
    async def start(self,a):
        try:
            
            await self.walk()
            
        except Exception as e:
            Print.error('[+] Error in user start')
            Print.error(e)
    


if __name__ == "__main__":
    try:
        
        args = sys.argv if sys.argv != None else False
        
        if args: uc.loop().run_until_complete(User().start(args))
        
    
    except Exception as e:
        Print.error('[+] Error in user main')
        Print.error(e)