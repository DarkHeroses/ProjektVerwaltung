<!DOCTYPE HTML SYSTEM>
<html>
	<head>
		<title>Aufwendungen je Woche</title>

		<style>
			@import url(${css_addr});
		</style>

		

	</head>
	<body>
		<h1 class="clHeader">Aufwendungen je Woche</h1>
		
		<table>
			<col>
				%for dict_i in dict_list:
					<td>
					<table id="idAw">
						%for i in range(len(dict_i)):
						<tr>
							%if i == 0:
								<th>Id</th><td>${dict_i["Id"]}</td>
							%else:
								<th>${i}. Woche</th><td>${dict_i["Woche"+str(i)]}</td>
							%endif
						</tr>
						%endfor
					</table>
					</td>
				%endfor
			</col>		
		</table>
		
		<div class="clButtons" id="idButtonArea">
		<a href="/index">zurueck zur Startseite</a>
		%if (len(dict_list) == 1):
			<a href="/Projekte/Aufwendungen/show_new/${dict_i["Id"]}"> neue Woche hinzufuegen</a>
		%endif
		</div>
	</body>		
</html>