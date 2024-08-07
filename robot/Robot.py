

from Print import Print

class Robot:
    
    
    def __init__(self) -> None:
        pass
    
    
    def run(self):
        try:
            Print.log('[+] Start Robot')
        
        except Exception as e:
            Print.error('[+] Error in method run')
            Print.error(e)


if __name__ == "__main__":
    Robot().run()