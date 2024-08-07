
from flask import Flask, request, render_template, url_for, make_response, redirect
import sys
sys.path.append('..')
from default.Print import Print
import os
import json
import random
from pathlib import Path



class Server:
    
    def __init__(self, ip='0.0.0.0', port=7777, debug=True) -> None:
        self.debug = debug
        self.ip = ip
        self.port = port
        self.app = Flask(__name__)
    
    # add endpoint
    def add_endpoint(self, endpoint, endpoint_name, handler, req_methods):
        self.app.add_url_rule(endpoint, endpoint_name, handler, methods=req_methods)
    
    

    # ====== Routers =======
    def index(self):
        
        try:
            Print.log("[+] Request to index")
            return render_template('index.html')
        
        except Exception as e:
            Print.log(e)
    
    
    # start server
    def run(self):
        
        self.add_endpoint('/', 'index', self.index, ['GET'])
        
        # ======= run serve =======
        self.app.run(host=self.ip, port=self.port, debug=True)
    

if __name__ == '__main__':

    try:
        
        Server().run()
        
    except Exception as e:
        Print.error(e)