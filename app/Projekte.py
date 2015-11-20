#coding: utf-8
import cherrypy
import json
from collections import OrderedDict
from mako.template import Template
import os


#---------------------------------------
class Projekte_cl(object):
#---------------------------------------
    css_addr="/Content/CSS/style.css"
    frame=['PName','PID','PNr','PDesc','PTime','PMoney','PIDK','PWeek']
    framename=['Id','Bezeichnung','Nummer','Beschreibung','Bearbeitungszeitraum','Budget','Id des Kunden','erfasste Aufwendungen je Woche']

    #-------------------------------------
    def eingabe(self):
    #-------------------------------------
       
        
        mytemplate = Template(filename='Templates\eingabe.tpl')
        return mytemplate.render(typ='Projekte',framename=self.framename,frame=self.frame,frame_size=len(self.frame),css_addr=self.css_addr)


    eingabe.exposed=True

    #-------------------------------------
    def daten(self): 
    #-------------------------------------
        
        json_f = open('data/projektdaten.json')	
        data = json.load(json_f, object_pairs_hook=OrderedDict)
        json_f.close()
        
        typ_s = 'Projektdaten'
                       
        mytemplate = Template(filename='Templates\daten.tpl')
        
        return mytemplate.render(typ='Projekte',key_list = self.framename , dict_list = data, typ_s = typ_s,css_addr=self.css_addr)
        
    daten.exposed = True
    
    
    
    
 
       
    #-------------------------------------
    def new(self,**kwargs):#,PName,PID,PNr,PDesc,PTime,PMoney,PIDK,PWeek):
    #-------------------------------------
        data=[]
        path='data/projektdaten.json'
        json_f = open(path)
        if 	os.path.getsize(path)> 0:
            data = json.load(json_f, object_pairs_hook=OrderedDict)
        json_f.close()

        eintrag={}

        for i in range(len(self.frame)):
            eintrag.update({self.framename[i]:kwargs[self.frame[i]]})
       
        data.append(eintrag)
        
        json_e =open('data/projektdaten.json','w')
        json.dump(data,json_e,)

        json_e.close()
        return self.daten()

    new.exposed=True 

    #---------------------------------------------    
    def delete(self, DID):
    #---------------------------------------------
        json_f = open('data/projektdaten.json')	
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
            error_s="Projekt mit ID: "+ DID +" nicht gefunden!"
            raise cherrypy.HTTPError(404,error_s)
        
                    
        json_e =open('data/projektdaten.json','w')
        json.dump(data,json_e)

        json_e.close()
        return self.projektdaten()
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