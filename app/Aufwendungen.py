#coding: utf-8
import cherrypy
import json 
from collections import OrderedDict
from mako.template import Template
import os

def zaehlen():
#-------------------------------------
    json_f = open('data/aufwendungsdaten.json')	
    data = json.load(json_f, object_pairs_hook=OrderedDict)
    json_f.close()
    count=1
    
    while(True):
        found=False
        for dict_i in data:
            for entry_i in dict_i:
                if  dict_i["Woche"+str(count)]!=None:
                    found=True

            

        if found==True:
            count=count+1
        else:
            break
        
    return count

class aufwendungen_cl(object):
    css_addr="/Content/CSS/style.css"

    #---------------------------------
    def show_all(self):
    #---------------------------------
        json_f = open('data/aufwendungsdaten.json')	
        data = json.load(json_f, object_pairs_hook=OrderedDict)
        json_f.close() 
       

        mytemplate = Template(filename='Templates\\aufwendungen.tpl')
        
        return mytemplate.render(dict_list=data,css_addr=self.css_addr)
        
        
    show_all.exposed=True

    #---------------------------------
    def show(self, DID):
    #---------------------------------
        json_f = open('data/aufwendungsdaten.json')	
        data = json.load(json_f, object_pairs_hook=OrderedDict)
        json_f.close()   
        dict_ed=[]
        
        found=False
        for dict_i in data:
            for entry_i in dict_i:
                if  dict_i[entry_i]==DID:
                    print("FOUND!!!!!!!!!")
                    dict_ed.append(dict_i)
                    found=True   

        if found==True:
            mytemplate = Template(filename='Templates\\aufwendungen.tpl')
            return mytemplate.render(dict_list=dict_ed , css_addr=self.css_addr)
        else:
            mytemplate = Template(filename='Templates\\aufwendungen_new.tpl')
            return mytemplate.render(css_addr=self.css_addr,ID=DID)

    show.exposed=True

    #----------------------------------
    def show_new(self, DID):
    #----------------------------------

        mytemplate = Template(filename='Templates\\aufwendungen_new.tpl')
        return mytemplate.render(css_addr=self.css_addr,ID=DID)

    show_new.exposed=True

    #---------------------------------
    def new(self,**kwargs):
    #---------------------------------
        json_f = open('data/aufwendungsdaten.json')	
        data = json.load(json_f, object_pairs_hook=OrderedDict)
        json_f.close()   
        
        found=False
        for dict_i in data:
            for entry_i in dict_i:
                if  dict_i[entry_i]==kwargs['ProjektID']:
                    print("FOUND!!!!!!!!!")
                    index_dat=data.index(dict_i)
                    found=True   
        if found==True:
            data[index_dat].update({"Woche"+str(len(data[index_dat])):kwargs['NEWW']+"Std"})
        else:
            data.append({'Id':kwargs['ProjektID'],'Woche1':kwargs['NEWW']+"Std"})

        json_e =open('data/aufwendungsdaten.json','w')
        json.dump(data,json_e,)

        json_e.close()
        return self.show(kwargs['ProjektID'])

    new.exposed=True

