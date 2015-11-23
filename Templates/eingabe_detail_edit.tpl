<!DOCTYPE html>

<html lang="de" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" /> 
    <title>Projekt editieren</title>
    <style>
        @import url(${css_addr});
    </style>
</head>
<body>
    <h1 class="clHeader">Projekt editieren</h1>
     
    <form action="/${typ}/edit_data" method="post" id="idEingabemaske">
				<label>Id</label></br>
				<input type="text" name="PID" id="PID"	value="${dict_ed["Id"]}" disabled /> </br>
			%for i in range(1,frame_size) :
				<label>${framename[i]}</label></br>
				<input type="text" name="${loop.cycle(frame[i])}" id="${loop.cycle(frame[i])}"	value="${dict_ed[framename[i]]}" required /> </br>
			%endfor

            <input type="submit" value="Speichern" /> </br>
      </form>
	  <div class="clMenu">
	  </br>
		 <a id="idProjektbutton" href="/${typ}/daten">zu den ${typ}</a>
	  </br>
	  </div>
</body>
</html>