<!DOCTYPE html>

<html lang="de" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" /> 
    <title>Aufwendungen</title>
    <style>
        @import url(${css_addr});
    </style>
</head>
<body>
    <h1 class="clHeader">Aufwendungen je Woche hinzufuegen</h1>
    <form action="/Projekte/Aufwendungen/new" method="post" id="idEingabemaske">
		<label>ID</label></br>
		<input type="text" name=ProjektID id=PID value="${ID}" readonly /> </br>	
			
		<label>Aufwendungsstunde diese Woche</label></br>
		<input type="text" name=NEWW id=NEWW required /> </br>		
		<input type="submit" value="Speichern" /> </br>
      </form>
	  <div class="clMenu">
		  </br>
			 <a id="idProjektbutton" href="/Projekte/daten">zu den Projekten</a>
		  </br>
	  </div>
</body>
</html>