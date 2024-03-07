## Visualisierung der CO2-Emissionen mit EDGAR-Daten

## Über dieses Projekt

Dieses Repository bietet eine detaillierte Visualisierung der CO2-Emissionen basierend auf Daten der EDGAR (Emissionsdatenbank für globale atmosphärische Forschung) Community-Treibhausgasdatenbank Version 8.0 (2023), einschließlich oder basierend auf Daten von IEA (2022) Treibhausgasemissionen aus Energie.

## Quelle

Die verwendeten Daten stammen von der IEA-EDGAR CO2-Datenbank. Weitere Informationen und Daten finden Sie [hier](https://edgar.jrc.ec.europa.eu/report_2023).

## Interaktive Visualisierungen erstellt mit Plotly

- [Top 10 CO2-Emitter](https://chart-studio.plotly.com/~julia_koehler_nat/1.embed)
- [Jährliche Top 10 CO2-Emitter](https://chart-studio.plotly.com/~julia_koehler_nat/5.embed)
- [CO2-Emissionen in Deutschland und globaler jährlicher Durchschnitt](https://chart-studio.plotly.com/~julia_koehler_nat/3.embed)

## Repository-Inhalt

- `Data/ne_10m_admin_0_countries`: Enthält das Shapefile für die räumliche Zuordnung der Emissionen.
- `CO2_emission_visualization.ipynb`: Notebook zur Visualisierung von CO2-Daten aus der EDGAR-Datenbank.
- `CO2_emission_visualization.py`: Python Script zur Visualisierung von CO2-Daten aus der Edgar-Datenbank.
- `Übungen`: Enthält ein Set von Notebooks zur Visualisierung der Emissionsdaten sowie Übungsaufgaben inkl. Lösungen.

## Installation und Nutzung

## Installation

### Mit Anaconda (empfohlen)

Anaconda vereinfacht die Paketverwaltung und die Einrichtung von virtuellen Umgebungen. Anaconda kann von [hier](https://www.anaconda.com/products/individual) herunterladen und installiert werden.

### VS Code

**Python installieren:** Wenn Python noch nicht installiert ist, kann es von  python.org  heruntergeladen werden. Bei der Installation auf Windows darauf achten, die Option "Add Python 3.x to PATH" zu aktivieren, um Python und pip in der Befehlszeile/Shell nutzen zu können.  
**VS Code konfigurieren:** Starten von Visual Studio Code und Strg + Shift + P (Cmd + Shift + P auf Mac) nutzen, um den Python-Interpreter auszuwählen. Hier den Pfad zu python.exe angeben.  
**Pylance und Jupyter installieren:** Über die VS Code Extensions sowohl Pylance für Python-Unterstützung als auch Jupyter für die Arbeit mit Notebooks installieren.  
**Notebook öffnen:** Öffnen des Jupyter Notebooks in VS Code. Mit Strg + Shift + P,  "Select another kernel" auswählen, um ein virtuelles Environment zu erstellen.  
**Abhängigkeiten installieren:** Bei Vorhandensein einer requirements.txt wird man gefragt, ob die die Pakete installiert werden sollen. Auf jeden Fall.  
**Notebook ausführen:** Das Notebook kann nach der Installation der Abhängigkeiten ausgeführt werden. Hier kann nun  mit verschiedenen Funktionen experimentiert und eigene Analysen und Visualisierungen erstellt werden.  


#### Probleme bei der Installation von Cartopy
Wenn Anaconda oder Miniconda verwendet werden und Probleme bei der Installation von Cartopy auftreten, empfiehlt es sich, Cartopy über Conda zu installieren. Conda kann oft Abhängigkeitskonflikte besser auflösen und erleichtert die Installation von Paketen, die native Bibliotheken erfordern. Cartopy mit Conda aus dem `conda-forge` Kanal zu installieren:
    
 ```shell
conda install -c conda-forge cartopy
 ```
    

5. **Ausführung der Skripte**: Öffne das Notebook oder das Python-Skript in deiner bevorzugten Entwicklungsumgebung. Beachte, dass bei Verwendung einer anderen Umgebung möglicherweise Anpassungen erforderlich sind.



