## coding: utf-8

##${Platzhalter}
<!DOCTYPE HTML SYSTEM>
<meta charset="utf-8">

<html>
	<head>
		<meta charset="utf-8">
		<title>${typ_s}</title>
		<style>
			@import url(${css_addr});
		</style>
		<script type="text/javascript"  src="/Content/Javascript/tabellen_bearbeitung.js"></script>
	</head>
	<body>
		<h1 class="clHeader">${typ_s}</h1>
		
		<table id="idTable">
			% for key_s in key_list:
			<th>
				${key_s}
			</th>
			% endfor
				% for dict_o in dict_list:
				<tr id=${dict_o["Id"]}>
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
		
		
		</div>
	</body>		
</html>