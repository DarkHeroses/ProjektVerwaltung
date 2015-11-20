# coding: utf-8
import cherrypy
import json
from collections import OrderedDict
from mako.template import Template
from app import Projekte
from app import Kunden

css_addr="/Content/CSS/style.css"
#--------------------------------------
class Application_cl(object):
#--------------------------------------
    #----------------------------------
    def __init__(self):
    #--------------------------------------
        self.Projekte=Projekte.Projekte_cl()
        self.Kunden=Kunden.Kunden_cl()
        # constructor
        pass

    #-------------------------------------
    def index(self):
    #-------------------------------------
        mytemplate = Template(filename='Templates\index.tpl')
        
        return mytemplate.render(css_addr=css_addr)

    index.exposed=True
        
       
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