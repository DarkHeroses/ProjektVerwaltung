import cherrypy
import json 
from collections import OrderedDict
from mako.template import Template
import os

class aufwendungen_cl(object):
    #---------------------------------
    def show_all(self):
    #---------------------------------
        json_f = open('data/aufwendungsdaten.json')	
        data = json.load(json_f, object_pairs_hook=OrderedDict)
        json_f.close() 

        mytemplate = Template(filename='Templates\aufwendungen.tpl')

        return mytemplate(data=data)
        
        
    show_all.exposed=True

    #---------------------------------
    def show(self, DID):
    #---------------------------------
        json_f = open('data/aufwendungsdaten.json')	
        data = json.load(json_f, object_pairs_hook=OrderedDict)
        json_f.close()   
        
        for dict_i in data:
            for entry_i in dict_i:
                if  dict_i[entry_i]==DID:
                    print("FOUND!!!!!!!!!")
                    dict_ed=dict_i
                    found=True   
        
    show.exposed=True


