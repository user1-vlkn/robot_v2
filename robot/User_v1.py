

from Print import Print
import asyncio
import nodriver as uc


class User:
    
    async def start(self, e):
        print("start")
    


if __name__ == "__main__":
    try:
        
        uc.loop().run_until_complete(User().start('sd'))
        
    
    except Exception as e:
        Print.error('[+] Error in user main')
        Print.error(e)
            