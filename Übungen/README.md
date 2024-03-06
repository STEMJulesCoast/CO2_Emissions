### Übungen zur Analyse von CO2-Emissionen

## Über dieses Repository

Dieses Repository enthält Übungsaufgaben, die speziell für Einsteiger:innen im textbasierten Programmieren konzipiert sind. Im Fokus stehen die Analyse und Visualisierung von CO2-Emissionsdaten unter Verwendung von Python, basierend auf dem Jupyter Notebook `CO2_emissions_exercises.ipynb`.

Die Übungen sind in einer Jupyter Notebook-Umgebung durchzuführen, wobei der Code in Anaconda3 getestet wurde. Anaconda ist eine populäre Distribution, die das Arbeiten mit wissenschaftlichen Paketen in Python vereinfacht und eine nahtlose Integration mit Jupyter Notebooks bietet.

### Anaconda mit Visual Studio Code verknüpfen

Um eine effiziente Entwicklungsumgebung zu schaffen, kann Anaconda direkt mit Visual Studio Code (VS Code) verknüpft werden. Dies ermöglicht es, Jupyter Notebooks direkt in VS Code zu bearbeiten und auszuführen, wodurch eine konsistente und leistungsstarke Arbeitsumgebung für die Datenanalyse geschaffen wird. Um Anaconda mit VS Code zu verknüpfen:

1. Anaconda auf dem System installieren.
2. Python-Erweiterung in VS Code installieren, falls noch nicht geschehen.
3. Öffnen von VS Code und in den Einstellungen zu `Python: Select Interpreter` navigieren.
4. Wählen des Anaconda-Interpreter aus der Liste der verfügbaren Interpreter.

Durch diese Verknüpfung profitiert man von der umfangreichen Paketverwaltung durch Conda und der flexiblen Entwicklungsumgebung von VS Code.


## Übersicht

**CO2_emissions_exercises.ipynb:** Dieses Jupyter-Notebook enthält eine Reihe von Übungen, die darauf abzielen, Anfänger:innen im textbasierten Programmieren zu unterstützen. Die Übungen basieren auf der Analyse und Visualisierung von CO2-Emissionsdaten.

**load_and_process_data.ipynb:** Dieses Skript wird innerhalb des Notebooks `CO2_emissions_exercises.ipynb` ausgeführt. Es lädt und verarbeitet die CO2-Emissionsdaten, um sie für die Visualisierung und Analyse vorzubereiten.

**plot_emission_data.py:** Ein Modul für die Visualisierung der Emissionsdaten.

## Anleitung
Download des Repositories (https://github.com/STEMJulesCoast/CO2_Emissions.git) und öffnen des CO2_emissions_exercises.ipynb - Notebooks in einer Jupyter Notebook-Umgebung. Befolgen Sie die Anweisungen und bearbeiten Sie die Übungen im Notebook. 

## Anforderungen

Was wird benötigt:

Stellen Sie sicher, dass Python auf Ihrem System installiert ist und dass Sie Jupyter Notebook oder JupyterLab zur Ausführung der .ipynb-Dateien verwenden können. Jupyter ist in diesem Fall die Entwicklungsumgebung für die interaktive Programmierung mit Python.

### Wichtige Schritte vor dem Start:

Installation der benötigten Bibliotheken: Vor dem Starten der Übungen müssen alle erforderlichen Bibliotheken installiert sein. 
Dies kann auf zwei Arten erfolgen:  

**Via Console:** Führen Sie 
```shell
pip install -r requirements.txt 
```
im Verzeichnis aus, in dem requirements.txt liegt, um alle benötigten Bibliotheken zu installieren.

**Innerhalb des Jupyter Notebooks:** Die erste Code-Zelle im `load_and_process_data.ipynb` kann zur Installation aus dem Notebook heraus auskommentiert werden.

## Anpassungen:

Passen Sie gegebenenfalls die Pfade zum Shapefile und den Pfad, wo die Daten abgelegt werden sollen, an.

## Beitrag

Vorschläge, Verbesserungen oder neue Übungen können gerne durch das Öffnen eines Issues oder eines Pull-Requests erfolgen.

Viel Spaß beim Programmieren!
