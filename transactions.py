#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Joey Chen
"""

import requests

class transactions():
    
    def __init__(self,api_key):
        self.api_key = api_key
    
    def get_txn_status(self,txn_hash):
        
  
        url = ( 
                "https://api.etherscan.io/api"+
                "?module=transaction"+
                "&action=getstatus"+
                "&txhash="+txn_hash+
                "&apikey="+self.api_key
                
            )

        r = requests.get(url)
        
        return r.json()['result']
    
    def get_txn_receipt_status(self,txn_hash):
        
  
        url = ( 
                "https://api.etherscan.io/api"+
                "?module=transaction"+
                "&action=gettxreceiptstatus"+
                "&txhash="+txn_hash+
                "&apikey="+self.api_key
                
            )

        r = requests.get(url)
        
        return r.json()['result']
        
