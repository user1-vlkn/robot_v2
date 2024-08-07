


from Print import Print

class User:
    
    def __init__(self) -> None:
        
        # some args
        pass
    
    def run(self):
        
        try:
            
            Print.log|("[+] Start User")
        
        except Exception as e:
            Print.error('[+] Error in method User(run)')
            Print.error(e)
            
            