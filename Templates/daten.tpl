<!DOCTYPE HTML SYSTEM>
<html>
	<head>
		<title>${typ_s}</title>
		<style  type="text/css">
			@import url(${css_addr});
		</style>
		<script type="text/javascript"  src="/Content/Javascript/tabellen_bearbeitung.js"></script>
	</head>
	<body>
		<h1 class="clHeader">${typ_s}</h1>
		
		<table id="idTable"><tr>
			% for key_s in key_list:
			<th>
				${key_s}
			</th>
			% endfor
			</tr>
				% for dict_o in dict_list:
				<tr id="${dict_o["Id"]}">
					% for key_s in key_list:
					<td>
						${dict_o[key_s]}
					</td>
					% endfor
				</tr>			
			%endfor
		</table>
		<div class="clButtons" id="idButtonArea">
		<a href="/index">zurueck zur Startseite</a>
		<a href="/${typ}/eingabe">${typ} hinzufuengen</a>
		<a href="/${typ}/edit">${typ} editieren</a>
		<a href="/${typ}/delete">${typ} entfernen</a>
		%if (typ=="Projekte"):
			<a href="/${typ}/aufwendungen/show">Woechentliche Aufwendungen</a>
		%endif
		
		</div>
	</body>		
</html>