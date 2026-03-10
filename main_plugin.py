from qgis.PyQt.QtWidgets import QAction, QInputDialog, QMessageBox
from qgis.PyQt.QtGui import QIcon
import os
import subprocess

class VerifPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_name = "Vérif Accès"
        self.action = None
        self.plugin_dir = os.path.dirname(__file__)

    def update_plugin(self):
        plugin_dir = os.path.dirname(__file__)
        try:
            result = subprocess.run(["git", "-C", plugin_dir, "pull"],capture_output=True,text=True)
            print("Plugin mis à jour")
        except:
            print(result.stdout)
    
    
    def initGui(self):
        self.update_plugin()
        # Chemin vers l’icône
        icon_path = os.path.join(self.plugin_dir, "icon.png")

        # Création de l’action avec icône
        self.action = QAction(
            QIcon(icon_path),
            self.plugin_name,
            self.iface.mainWindow()
        )

        self.action.triggered.connect(self.demander_mot_de_passe)

        # Ajout à la barre d’outils et au menu
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Vérif Accès", self.action)

    def demander_mot_de_passe(self):
        MOT_DE_PASSE = "1234567"
        mdp, ok = QInputDialog.getText(
            None,
            "Accès restreint",
            "Entrez le mot de passe :",
            echo=2
        )

        if ok:
            if mdp == MOT_DE_PASSE:
                QMessageBox.information(
                    None,
                    "Accès autorisé",
                    "✅ Mot de passe correct. Accès validé."
                )
            else:
                QMessageBox.warning(
                    None,
                    "Erreur",
                    "❌ Mot de passe incorrect. Accès refusé."
                )

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu("&Vérif Accès", self.action)









