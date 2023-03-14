#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Joey Chen
"""

import requests

class accounts():
    
    def __init__(self,api_key):
        self.api_key = api_key
    
    def get_eth_balance(self,address,tag):
        
  
        url = ( "https://api.etherscan.io/api"+
               "?module=account"+
               "&action=balance"+
               "&address="+address+
               "&tag="+tag+
               "&apikey="+self.api_key
                
            )

        r = requests.get(url)
        
        return r.json()['result']
        
    
    def get_eth_balance_multi(self,address,tag):
            
        url = ( "https://api.etherscan.io/api"+
               "?module=account"+
               "&action=balancemulti"+
               "&address="+address+
               "&tag="+tag+
               "&apikey="+self.api_key
               
            )

        r = requests.get(url)
        
        return r.json()['result']
    
    def get_normal_txn_by_address(self,address,startblk,endblk,page,offset,sort):
        
        url = (
                "https://api.etherscan.io/api"+
                "?module=account"+
                "&action=txlist"+
                "&address="+address+
                "&startblock="+str(startblk)+
                "&endblock="+str(endblk)+
                "&page="+str(page)+
                "&offset="+str(offset)+
                "&sort="+sort+
                "&apikey="+self.api_key
            )
        r = requests.get(url)
        
        return r.json()['result']
    
    def get_internal_txn_by_address(self,address,startblk,endblk,page,offset,sort):
        
        url = (
                "https://api.etherscan.io/api"+
                "?module=account"+
                "&action=txlistinternal"+
                "&address="+address+
                "&startblock="+str(startblk)+
                "&endblock="+str(endblk)+
                "&page="+str(page)+
                "&offset="+str(offset)+
                "&sort="+sort+
                "&apikey="+self.api_key
            )
        r = requests.get(url)
        
        return r.json()['result']
    
    def get_erc20_transfer_txn_by_address(self,address,contract_address,page,offset,startblk,endblk,sort):
        
        url = (
                "https://api.etherscan.io/api"+
                "?module=account"+
                "&action=tokentx"+
                "&contractaddress="+contract_address+
                "&address="+address+
                "&page="+str(page)+
                "&offset="+str(offset)+
                "&startblock="+str(startblk)+
                "&endblock="+str(endblk)+
                "&sort="+sort+
                "&apikey="+self.api_key
            )
        
        r = requests.get(url)
        return r.json()['result']
    
    def get_erc721_transfer_txn_by_address(self,address,contract_address,page,offset,startblk,endblk,sort):
        
        url = (
                "https://api.etherscan.io/api"+
                "?module=account"+
                "&action=tokennfttx"+
                "&contractaddress="+contract_address+
                "&address="+address+
                "&page="+str(page)+
                "&offset="+str(offset)+
                "&startblock="+str(startblk)+
                "&endblock="+str(endblk)+
                "&sort="+sort+
                "&apikey="+self.api_key
            )
        
        r = requests.get(url)
        return r.json()['result']
    
    def get_erc1155_transfer_txn_by_address(self,address,contract_address,page,offset,startblk,endblk,sort):
        
        url = (
                "https://api.etherscan.io/api"+
                "?module=account"+
                "&action=token1155tx"+
                "&contractaddress="+contract_address+
                "&address="+address+
                "&page="+str(page)+
                "&offset="+str(offset)+
                "&startblock="+str(startblk)+
                "&endblock="+str(endblk)+
                "&sort="+sort+
                "&apikey="+self.api_key
            )
        
        r = requests.get(url)
        return r.json()['result']
        
