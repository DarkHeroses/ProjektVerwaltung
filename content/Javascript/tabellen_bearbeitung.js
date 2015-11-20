window.onload = function () {

    var element_o;

    document.getElementById("idTable").onclick = function (event_opl) {
        if (event_opl.target.tagName.toLowerCase() == 'td') {
            element_o = document.querySelector(".clSelected");

            if (element_o != null) {
                element_o.className = "";
            }

            element_o = event_opl.target.parentNode;
            element_o.className = "clSelected";
        }
    }
        document.getElementById("idButtonArea").onclick = function (event_opl) {
            var element_o;
            if (event_opl.target.tagName.toLowerCase() == 'a') {
                var path_s = event_opl.target.href;
                var do_b = false;
                if ((event_opl.target.href.indexOf('/Projekte/eingabe') > 0)||(event_opl.target.href.indexOf('/Kunden/eingabe') > 0)) {
                    do_b = true;
                }else if(event_opl.target.href.indexOf('/index') > 0)
                { do_b = true;}
                else if ((event_opl.target.href.indexOf('/Projekte/edit') > 0) || (event_opl.target.href.indexOf('/Kunden/edit') > 0)) {
                    element_o = document.querySelector(".clSelected");
                    if (element_o != null) {
                        path_s += "/" + element_o.id.substr(1);
                        do_b = true;
                    } else {
                        alert("Wählen Sie bitte einen Eintrag in der Tabelle aus!");
                    }
                } else if ((event_opl.target.href.indexOf('/Projekte/delete') > 0) || (event_opl.target.href.indexOf('/Kunden/delete') > 0)) {
                    element_o = document.querySelector(".clSelected");
                    if (element_o != null) {
                        if (confirm("Soll der Datensatz wirklich gelöscht werden?")) {
                            path_s += "/" + element_o.id.substr(0);
                            do_b = true;
                        }
                    } else {
                        alert("Wählen Sie bitte einen Eintrag in der Tabelle aus!");
                    }
                }
                if (do_b) {
                    console.log("Wechsel von: " + window.location.href + " zu: " + path_s);
                    window.location.href = path_s;
                }
                event_opl.stopPropagation();
                event_opl.preventDefault();
            }
        }
}

