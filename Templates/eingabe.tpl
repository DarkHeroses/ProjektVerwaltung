<!DOCTYPE html>

<html lang="de" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" /> 
    <title>Neues Projekt</title>
    <style>
        @import url(${css_addr});
    </style>
</head>
<body>
    <h1 class="clHeader">Neues Projekt</h1>
     
    <form action="/${typ}/new" method="post" id="idEingabemaske">
		
			%for i in range(frame_size) :
				<label>${framename[i]}</label></br>
				<input type="text" name="${loop.cycle(frame[i])}" id="${loop.cycle(frame[i])}" required /> </br>
			%endfor

            <input type="submit" value="Speichern" /> </br>
      </form>
	  <div class="clMenu">
	  </br>
		 <a id="idProjektbutton" href="/${typ}/daten">zu den Projekte</a>
	  </br>
	  </div>
</body>
</html>