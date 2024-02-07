# Visualisierung der CO2-Emissionen mit EDGAR-Daten

### Über dieses Projekt

Dieses Repository bietet eine detaillierte Visualisierung der CO2-Emissionen basierend auf Daten der EDGAR (Emissionsdatenbank für globale atmosphärische Forschung) Community-Treibhausgasdatenbank Version 8.0 (2023), einschließlich oder basierend auf Daten von IEA (2022) Treibhausgasemissionen aus Energie.

### Quelle

Die verwendeten Daten stammen von der IEA-EDGAR CO2-Datenbank. Weitere Informationen und Daten finden Sie hier: https://edgar.jrc.ec.europa.eu/report_2023


### Interaktive Visualisierungen erstellt mit Plotly:

    Top 10 CO2-Emitter: https://chart-studio.plotly.com/~julia_koehler_nat/1.embed
    Jährliche Top 10 CO2-Emitter: https://chart-studio.plotly.com/~julia_koehler_nat/5.embed
    CO2-Emissionen in Deutschland und globaler jährlicher Durchschnitt: https://chart-studio.plotly.com/~julia_koehler_nat/3.embed


### Repository-Inhalt

    ne_10m_admin_0_countries: Enthält das Shapefile für die räumliche Zuordnung der Emissionen.
    CO2_emission_visualization.ipynb: Python-Skript zur Visualisierung der CO2-Daten von der EDGAR-Datenbank.

### Installation und Nutzung

Zur Verwendung des Visualisierungsskripts müssen bestimmte Bibliotheken installiert und importiert werden. Das Skript umfasst Funktionen zur Installation fehlender Bibliotheken, zum Laden und Verarbeiten der Emissionsdaten, zur räumlichen Aggregation der Emissionen auf Länderebene und zur Erstellung verschiedener Visualisierungen.

### Anleitung

Klone das Repository: Klone das gesamte Repository auf deinen lokalen Computer. Dies ermöglicht dir den Zugriff auf alle Dateien und Ordner des Projekts.

Bereite deine Umgebung vor: Stelle sicher, dass Python und Jupyter (Lab oder Notebook) auf deinem System installiert sind, um die .ipynb-Dateien ausführen zu können.

Installiere die benötigten Pakete: Das Notebook enthält eine Funktion, die die fehlenden Bibliotheken installiert. Sollte dies nicht funktionieren, navigiere in das Verzeichnis des Projekts, das die requirements.txt-Datei enthält, und führe `pip install -r requirements.txt` aus, um alle benötigten Bibliotheken zu installieren. Beachte, dass sich für verschiedene Teile des Projekts requirements.txt-Dateien in entsprechenden Unterordnern befinden können. Befolge die spezifischen Anleitungen in den jeweiligen README-Dateien dieser Ordner.

Ausführung der Skripte: Öffne das Visualisierungsskript in Jupyter Lab oder Jupyter Notebook. Beachte, dass bei Verwendung einer anderen Umgebung möglicherweise Anpassungen erforderlich sind. Weitere Informationen findest du im README der jeweiligen Übungen.





