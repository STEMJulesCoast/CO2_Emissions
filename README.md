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

Die Ausführung der Jupyter Notebooks wird am besten mit der Installation von Anaconda durchgeführt, wobei mindestens Python 3.11 empfohlen wird. Anaconda vereinfacht die Paketverwaltung und die Einrichtung von virtuellen Umgebungen. Sie können Anaconda von [hier](https://www.anaconda.com/products/individual) herunterladen und installieren.

### Ohne Anaconda

Falls Anaconda nicht installiert ist oder Sie es vorziehen, ohne Anaconda zu arbeiten, ist Python 3.10 erforderlich. Zusätzlich müssen die in der `requirements.txt` Datei aufgeführten Pakete installiert werden. Die Verwendung eines virtuellen Umfelds (`venv`) wird empfohlen, um die Paketabhängigkeiten zu isolieren und Konflikte zu vermeiden. 

#### Einrichtung eines virtuellen Umfelds und Installation der Abhängigkeiten:

1. Erstellen Sie ein neues virtuelles Umfeld:


### Anleitung

1. **Klone das Repository**: Klone das gesamte Repository auf deinen lokalen Computer für Zugriff auf alle Dateien und Ordner des Projekts.

2. **Bereite deine Umgebung vor**: Stelle sicher, dass Python 3.10 und Jupyter (Lab oder Notebook) auf deinem System installiert sind. 

3. **Erstelle ein virtuelles Umfeld**:
    ```
    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # Unix/Mac
    ```

4. **Installiere die benötigten Pakete**:
    ```shell
    pip install -r requirements.txt
    ```
    #### Probleme bei der Installation von Cartopy
    
    Wenn Anaconda oder Miniconda verwendet werden und Probleme bei der Installation von Cartopy auftreten, empfiehlt es sich, Cartopy über Conda zu installieren. Conda kann oft Abhängigkeitskonflikte besser auflösen und erleichtert die Installation von Paketen, die native Bibliotheken erfordern. Cartopy mit Conda aus dem `conda-forge` Kanal zu installieren:
    
 ```shell
conda install -c conda-forge cartopy
 ```
    



5. **Ausführung der Skripte**: Öffne das Notebook oder das Python-Skript in deiner bevorzugten Entwicklungsumgebung. Beachte, dass bei Verwendung einer anderen Umgebung möglicherweise Anpassungen erforderlich sind.



