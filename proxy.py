#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Joey Chen
"""

import requests

class proxy():
    
    def __init__(self,api_key):
        self.api_key = api_key
        
    def eth_block_num(self):
        
        url = ( 
                "https://api.etherscan.io/api"+
                "?module=proxy"+
                "&action=eth_blockNumber"+
                "&apikey="+self.api_key
                
            )

        r = requests.get(url)
        
        return r.json()['result']
        
    
    def eth_txn_counts(self,address,tag):
        
  
        url = ( 
                "https://api.etherscan.io/api"+
                "?module=proxy"+
                "&action=eth_getTransactionCount"+
                "&address="+address+
                "&tag="+tag+
                "&apikey="+self.api_key
                
            )

        r = requests.get(url)
        
        return r.json()['result']
    
    def eth_send_Raw_Transaction(self,hex):
        
  
        url = ( 
                "https://api.etherscan.io/api"+
                "?module=proxy"+
                "&action=eth_sendRawTransaction"+
                "&hex="+hex+
                "&apikey="+self.api_key
                
            )

        r = requests.get(url)
        
        return r.json()['result']
    
    def eth_gas_price(self):
        
        url = ( 
                "https://api.etherscan.io/api"+
                "?module=proxy"+
                "&action=eth_gasPrice"+
                "&apikey="+self.api_key
                
            )

        r = requests.get(url)
        
        return r.json()['result']
    
    def eth_estimatedG_gas(self,data,to,value,gasPrice,gas):
        
        url = ( 
                "https://api.etherscan.io/api"+
                "?module=proxy"+
                "&action=eth_estimateGas"+
                "&data="+data+
                "&to="+to+
                "&value="+value+
                "&gasPrice="+gasPrice+
                "&gas="+gas+
                "&apikey="+self.api_key
                
            )

        r = requests.get(url)
        
        return r.json()['result']
    

        
