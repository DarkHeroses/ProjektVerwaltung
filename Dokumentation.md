#Projektverwaltung#

##Allgemeine Beschreibung der Lösung##

Das Program dient der Verwaltung von **Projekten und Kunden**. Dabei können Kunden dynamisch *erstellt* und *bearbeitet* und ebenfalls auch *gelöscht* werden. 

***


##Komponenten##

###application.py###

Diese Datei beinhaltet die Klasse **Application_cl**. Die Klasse dient Hauptsächlich der *Einbindung* der Klassen  **Projekt_cl** und **Kunden_cl**. Desweiteren befindet sich hier der Aufruf der **index(self)** Funktion. Diese Funktion dient dem Aufruf der *Startseite*.

Der Aufruf der Startseite wird durch ein **Mako template: index.tpl** geladen und ausgegeben. Falls eine Adresse Auftritt die nicht behandet wurde, wird ein **404 Fehler** ausgegeben.

###Kunden.py/Projekte.py###

In diesen Daten wird Hauptlogik des gesamten Projekts implementiert. Je nach dem ob es Kunden oder Projekte sind werden die passenden Funktionen ausgeführt.

####Attribute####
* __css_addr__:festlegeung des *CSS* Pfades 
* __frame__:festlegung der *IDs* und *Name* in den generierten Templates.
* __framename__: Legt die *Keys* der gespeicherten *Json-Daten*

####Methoden####

* #####daten(self)######
    * Bei dieser Funktion werden die gespeicherten *Json-Daten* gelesen und über das **daten.tpl** ausgegeben.  

* #####eingabe(self)#####
    * Bei dieser Funktion wird das **Eingabe.tpl** geladen.

* #####new(self,\*\*kwargs)#####

    * Bei dieser Funktion werden vom, *User* eingebenen Daten verarbeitet. Die Verarbeitung erfolgt durch das Laden der bereits vorhandenen *Json-Daten*. Dabei wird geprüft ob die *Json-Datei* leer ist oder nicht. Falls die *Json-Datei* leer ist wird die Datei einfach geschlossen. Falls die *Json-Datei* bereits gespeicherte Daten enthält werden die Daten gelesen. Daraufhin werden die vom *User* eingegeben Daten in einen passenden Datentypen gespeichert. Dieser wird dann an die aus den *Json-Dateien* gelesenen Daten angehängt. Dann wird die Datei die zuvor ausgelesen wurde, wieder geladen und wird mit den aktualisierten Daten überschrieben und dann geschlossen. Zum Schluss wird die **daten(self)** Funktion aufgerufen.

* #####edit(self,DID)#####

    * Bei dieser Funktion werden die vom *User* ausgewählten Daten werden zum editieren zur Verfügung gestellt. Die Verarbeitung erfolgt durch das Laden der vorhandenen *Json-Daten*. Dann werden diese Daten gelesen und der *Ausgewählte Eintrag* rausgesucht. Der rausgesuchte Eintrag wird mit den ausgelesenen Daten an das Template **eingabe_detail_edit.tpl** übergeben. Falls der Eintrag, durch Umstände, nicht gefunden wird gibt der ein **404 Fehler** aus.

* #####edit_data(self,\*\*kwargs)#####

    * Bei dieser Funktion werden die vom *User* ausgewählten Daten editiert. Die Verarbeitung erfolgt durch das Laden der vorhandenen *Json-Daten*. Dann werden diese Daten gelesen und der *übergebene Eintrag* rausgesucht. Daraufhin wird der *rausgesuchte Eintrag* mit den *übergegebenen Daten* ersetzt und wird mit den aktualisierten Daten überschrieben und dann geschlossen. Falls der Eintrag, durch Umstände, nicht gefunden wird gibt der ein **404 Fehler** aus.

* #####delete(self,DID)#####

    * Bei dieser Funktion werden die vom *User* ausgewählten Daten gelöscht. Die Verarbeitung erfolgt durch das Laden der vorhandenen *Json-Daten*. Dann werden diese Daten gelesen und der *Ausgewählte Eintrag* rausgesucht. Daraufhin wird der *gefunden Eintrag* aus den *ausgelesenen Daten* entferntund wird mit den aktualisierten Daten überschrieben und dann geschlossen. Falls der Eintrag, durch Umstände, nicht gefunden wird gibt der ein **404 Fehler** aus.

* #####default(self, \*arglist, \*\*kwargs)#####

    * Falls eine Adresse Auftritt die nicht behandet wurde, wird ein **404 Fehler** ausgegeben.
 
###Templates###
* ####index.tpl####

    * Die Startseite, von wo man auf die **Projekt - und Kundendaten** zugreifen kann.

* ####daten.tpl####

    * Auf dieser Seite werden alle bereits gespeicherten Daten dargestellt. Von dieser Seite kommt auf **Projekte/Kunden hinzufügen**, **Projekte/Kunden editieren** und **Projekte/Kunden löschen**.

* ####eingabe.tpl####

    * Diese Seite bietet eine Eingabemaske für **Projekt- oder Kundendaten**, um diese dem System hinzuzufügen.

* ####eingabe_detail_edit.tpl####

    * Diese Seite biete ein Eingabemaske zum Editieren von **Projekt- oder Kundendaten**.


###tabellen_bearbeitung.js###

Hier ist die Logik zur *Auswahl des Tabellen Einträge* und Ihre weitergabe implementiert. Es wird zu Beginn überprüft ob bereits ein Element ausgewählt wurde. Wenn ja, wird es zurück gesetzt und ein neues Element als Selected markiert.

Bei der Weitergabe der Daten wird das Aktuell ausgewälte Element genommen und davon die *ID* weitergeleitet um das in den Server funktionen verarbeitet zu werden.

###eingabe_detail_edit.js###

Hier ist die Logik zur weitegabe der Daten, welche editiert wurden implementiert. Dabei werden die Daten zwischen gespeichert Überprüft und dann an den Server Weitergegeben.


###Json-Dateien##

###Kunden-&Projektdaten.json###

Dort sind die *Projekt- und Kundendaten* gespeichert.