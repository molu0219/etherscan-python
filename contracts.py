#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Joey Chen
"""

import requests

class contracts():
    
    def __init__(self,api_key):
        self.api_key = api_key
    
    def get_contract_abi(self,contract_address):
        
  
        url = ( 
                "https://api.etherscan.io/api"+
                "?module=contract"+
                "&action=getabi"+
                "&address="+contract_address+
                "&apikey="+self.api_key
                
            )

        r = requests.get(url)
        
        return r.json()['result']
        
    
    def get_contract_source_code(self,contract_address):
        
  
        url = ( 
                "https://api.etherscan.io/api"+
                "?module=contract"+
                "&action=getsourcecode"+
                "&address="+contract_address+
                "&apikey="+self.api_key
                
            )

        r = requests.get(url)
        
        return r.json()['result']
    
    def get_contract_creation(self,contract_address):
        
  
        url = ( 
                "https://api.etherscan.io/api"+
                "?module=contract"+
                "&action=getcontractcreation"+
                "&contractaddresses="+contract_address+
                "&apikey="+self.api_key
                
            )

        r = requests.get(url)
        
        return r.json()
        
