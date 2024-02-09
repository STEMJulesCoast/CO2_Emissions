# Visualisierung der CO2-Emissionen mit EDGAR-Daten

### Über dieses Projekt

Dieses Repository bietet eine detaillierte Visualisierung der CO2-Emissionen basierend auf Daten der EDGAR (Emissionsdatenbank für globale atmosphärische Forschung) Community-Treibhausgasdatenbank Version 8.0 (2023), einschließlich oder basierend auf Daten von IEA (2022) Treibhausgasemissionen aus Energie.

### Quelle

Die verwendeten Daten stammen von der IEA-EDGAR CO2-Datenbank. Weitere Informationen und Daten finden Sie hier: https://edgar.jrc.ec.europa.eu/report_2023


### Interaktive Visualisierungen erstellt mit Plotly:

- Top 10 CO2-Emitter: https://chart-studio.plotly.com/~julia_koehler_nat/1.embed
- Jährliche Top 10 CO2-Emitter: https://chart-studio.plotly.com/~julia_koehler_nat/5.embed
- CO2-Emissionen in Deutschland und globaler jährlicher Durchschnitt: https://chart-studio.plotly.com/~julia_koehler_nat/3.embed

### Repository-Inhalt

- `ne_10m_admin_0_countries`: Enthält das Shapefile für die räumliche Zuordnung der Emissionen.
- `CO2_emission_visualization.ipynb`: Ein Python-Skript zur Visualisierung von CO2-Daten aus der EDGAR-Datenbank.
- `Übungen`: Beinhaltet ein Set von Notebooks zur Visualisierung der Emsissionsdaten. Es umfasst ein separates Notebook für das Laden und Verarbeiten von Daten und Module für Plot-Funktionen, um die Lesbarkeit des Codes zu erhöhen und das Erlernen von Programmierung durch Anpassung von Code-Snippets zu erleichtern. Ein `requirements.txt`-File ist vorhanden, um die notwendigen Bibliotheken zu installieren. Das Hauptnotebook führt dieses separate Notebook für Datenladen und -verarbeitung innerhalb seiner Ausführung aus, was den Code übersichtlicher macht und eine praktische Einführung in das Konzept der Code-Wiederverwendung und Modularität bietet.


### Installation und Nutzung

Um das Notebook zu nutzen, ist eine aktuelle Installation von Python sowie Jupyter Notebook oder JupyterLab notwendig, da das Skript in einem Jupyter-Umfeld läuft. Das Skript integriert Funktionen, die automatisch fehlende Bibliotheken installieren, Emissionsdaten laden und verarbeiten, die Daten räumlich auf Länderebene aggregieren und diverse Visualisierungen erzeugen. 

### Anleitung

Klone das Repository: Klone das gesamte Repository auf deinen lokalen Computer. Dies ermöglicht dir den Zugriff auf alle Dateien und Ordner des Projekts.

Bereite deine Umgebung vor: Stelle sicher, dass Python und Jupyter (Lab oder Notebook) auf deinem System installiert sind, um die .ipynb-Dateien ausführen zu können.

Installiere die benötigten Pakete: Das Notebook enthält eine Funktion, die die fehlenden Bibliotheken installiert. Sollte dies nicht funktionieren, navigiere in das Verzeichnis des Projekts, das die requirements.txt-Datei enthält, und führe `pip install -r requirements.txt` aus, um alle benötigten Bibliotheken zu installieren und passe den import im Notebook dementsprechend an. 

Ausführung der Skripte: Öffne das Notebook in Jupyter Lab oder Jupyter Notebook. Beachte, dass bei Verwendung einer anderen Umgebung möglicherweise Anpassungen erforderlich sind. 




