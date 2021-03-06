﻿import cherrypy
import json
from collections import OrderedDict
from mako.template import Template
import os

#-------------------------------------
def zaehlen():
#-------------------------------------
    json_f = open('data/kundendaten.json')	
    data = json.load(json_f, object_pairs_hook=OrderedDict)
    json_f.close()
    count=1
    
    while(True):
        found=False
        for dict_i in data:
            for entry_i in dict_i:
                if  dict_i[entry_i]==("KID"+str(count)):
                    found=True

            

        if found==True:
            count=count+1
        else:
            break
        
    return count



class Kunden_cl(object):

    css_addr="/Content/CSS/style.css"
    frame=['PID','PNr','PName','PCon','PPlace']
    framename=['Id','Nummer','Bezeichnung','Ansprechpartner','Ort']

    #-------------------------------------
    def daten(self): 
    #-------------------------------------
        
        json_f = open('data/kundendaten.json')	
        data = json.load(json_f, object_pairs_hook=OrderedDict)
        json_f.close()
          
        typ_s = 'Kundendaten'
               
        mytemplate = Template(filename='Templates\daten.tpl')
        
        return mytemplate.render(typ='Kunden',key_list = self.framename , dict_list = data, typ_s = typ_s,css_addr=self.css_addr)
            
        
    daten.exposed = True
    

    #-------------------------------------
    def eingabe(self):
    #-------------------------------------

        
        mytemplate = Template(filename='Templates\eingabe.tpl')
        return mytemplate.render(typ='Kunden',framename=self.framename,frame=self.frame,frame_size=len(self.frame),css_addr=self.css_addr)

    eingabe.exposed=True

    #-------------------------------------
    def new(self,**kwargs):
    #-------------------------------------
        data=[]
        path='data/kundendaten.json'
        json_f = open(path)
        if 	os.path.getsize(path)> 0:
            data = json.load(json_f, object_pairs_hook=OrderedDict)
        json_f.close()

        eintrag={}
        eintrag.update({self.framename[0]:"KID"+str(zaehlen())})

        for i in range(1,len(self.frame)):
            eintrag.update({self.framename[i]:kwargs[self.frame[i]]})
       
        data.append(eintrag)
        
        json_e =open('data/kundendaten.json','w')
        json.dump(data,json_e,)

        json_e.close()
        return self.daten()

    new.exposed=True 

        #---------------------------------------------
    def edit(self,DID):
    #---------------------------------------------
        json_f = open('data/kundendaten.json')	
        data = json.load(json_f, object_pairs_hook=OrderedDict)
        json_f.close()

        found = False
        dict_ed={}
        for dict_i in data:
            for entry_i in dict_i:
                if  dict_i[entry_i]==DID:
                    print("FOUND!!!!!!!!!")
                    dict_ed=dict_i
                    found=True
                    
        if found ==True:
            mytemplate = Template(filename='Templates\eingabe_detail_edit.tpl')
            return mytemplate.render(typ='Kunden',framename=self.framename,frame=self.frame,frame_size=len(self.frame),css_addr=self.css_addr,dict_ed=dict_ed)
        else:
            error_s="Kunden mit ID: "+ kwargs["PID"] +" nicht gefunden!"
            raise cherrypy.HTTPError(404,error_s)

    
    edit.exposed=True

    #---------------------------------------------
    def edit_data(self,**kwargs):
    #---------------------------------------------
        json_f = open('data/kundendaten.json')	
        data = json.load(json_f, object_pairs_hook=OrderedDict)
        json_f.close() 
        found = False
        
        dict_in=0

        for dict_i in data:
            for entry_i in dict_i:
                if  dict_i[entry_i]==kwargs["PID"]:
                    print("FOUND!!!!!!!!!:"+dict_i[entry_i])
                    dict_in=data.index(dict_i)
                    found=True
                    break  
                    
        if (found==True):
            for i in range(len(self.frame)):
                data[dict_in][self.framename[i]]=kwargs[self.frame[i]]
            json_e =open('data/kundendaten.json','w')
            json.dump(data,json_e)
            json_e.close()
        else:
            error_s="Kunden mit ID: "+ kwargs["PID"] +" nicht gefunden!"
            raise cherrypy.HTTPError(404,error_s)

        return self.daten()
    edit_data.exposed=True

    #---------------------------------------------    
    def delete(self, DID):
    #---------------------------------------------
        json_f = open('data/kundendaten.json')	
        data = json.load(json_f, object_pairs_hook=OrderedDict)
        json_f.close()

        found = False

        for dict_i in data:
            for entry_i in dict_i:
                if  dict_i[entry_i]==DID:
                    print("FOUND!!!!!!!!!")
                    dict_del=data.index(dict_i)
                    found=True
                    break
                
                    
        if found ==True:
            data.pop(dict_del)
        else:
            error_s="Kunden mit ID: "+ DID +" nicht gefunden1"
            raise cherrypy.HTTPError(404,error_s)
        
                    
        json_e =open('data/kundendaten.json','w')
        json.dump(data,json_e)

        json_e.close()
        return self.daten()
    delete.exposed=True    

   

#--------------------------------------
def default(self, *arglist, **kwargs):
#--------------------------------------
    msg_s = "unbekannte Anforderung: " + \
        str(arglist) + \
        '' +\
        str(kwargs)
    raise cherrypy.HTTPError(404, msg_s)
default.exposed = True
# EOF
