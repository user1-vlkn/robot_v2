

from Print import Print
from User import User
import subprocess
import time
from Sleep import Sleep

class Robot:
    
    
    def __init__(self) -> None:
        pass
    
    
    def run(self):
        
        try:
            Print.log('[+] Start Robot')
            
            while True:
                
                try:
                    Print.log("[+] New Step While Walk")
                    
                    args = "1212"
                    
                    subprocess.call(f'python User.py {args}', shell=True)
                
                except Exception as e:
                    Print.error("[+] Error in While")
                    Print.error(e)
                
                Sleep.zZz(2)
                
                
                
        
        except Exception as e:
            Print.error('[+] Error in method run')
            Print.error(e)


if __name__ == "__main__":
    Robot().run()