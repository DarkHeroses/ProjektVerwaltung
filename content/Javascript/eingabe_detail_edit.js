var g_FormContentOrg_o = {
    'PID':'',
    'PName': '',
    'PNr': '',
    'PDesc': '',
    'PTime': '',
    'PMoney': '',
    'PIDK': '',
    'PWeek': ''
};

function storeFormContent_p() {
    g_FormContentOrg_o['PID'] = document.getElementById("PID").value;
    g_FormContentOrg_o['PName'] = document.getElementById("PName").value;
    g_FormContentOrg_o['PNr'] = document.getElementById("PNr").value;
    g_FormContentOrg_o['PDesc'] = document.getElementById("PDesc").value;
    g_FormContentOrg_o['PTime'] = document.getElementById("PTime").value;
    g_FormContentOrg_o['PMoney'] = document.getElementById("PMoney").value;
    g_FormContentOrg_o['PIDK'] = document.getElementById("PIDK").value;
    g_FormContentOrg_o['PWeek'] = document.getElementById("PWeek").value;
}

function isModified_p() {
   var mod_b = 
   g_FormContentOrg_o['PID'] != document.getElementById("PID").value||
   g_FormContentOrg_o['PName'] != document.getElementById("PName").value||
   g_FormContentOrg_o['PNr'] != document.getElementById("PNr").value||
   g_FormContentOrg_o['PDesc'] != document.getElementById("PDesc").value||
   g_FormContentOrg_o['PTime'] != document.getElementById("PTime").value||
   g_FormContentOrg_o['PMoney'] != document.getElementById("PMoney").value||
   g_FormContentOrg_o['PIDK'] != document.getElementById("PIDK").value||
   g_FormContentOrg_o['PWeek'] != document.getElementById("PWeek").value;

   return mod_b;
}

window.onload = function () {

   
   storeFormContent_p();


   document.getElementById("idEingabemaske").onclick = function (event_opl) {
      if (event_opl.target.tagName.toLowerCase() == 'a') {
         
         if (isModified_p()) {
            if (confirm("Es gibt nicht gespeicherte Änderungen - trotzdem zurück?")) {

               window.location.href = event_opl.target.href;
            }
         } else {
         
            window.location.href = event_opl.target.href;
         }
         
         event_opl.stopPropagation();
         event_opl.preventDefault();
      }
   }

}
