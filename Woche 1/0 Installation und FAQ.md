# Installation
Um die praktischen Aufgaben zu lösen, benötigen Sie eine Juypter Notebook Umgebung. Diese können Sie entweder direkt bei sich auf den Computer installieren oder auf einen Online-Service wie Google Colab oder myBinder zurückgreifen. Nachdem Sie eine Lösung gewählt haben, probieren Sie zunächst die Basis Funktionen von Jupyter Notebooks anhand eines unsere [Beispiele](1%20Erste%20Schritte.ipynb) aus.


## Lokale Verwendung
Dieser Abschnitt beschreibt die Installation von Anaconda und den Abhänigkeiten auf Ihrem Rechner.

### Installation von Anaconda

Die Jupyter Notebooks werden mithilfe von _Anaconda_ im Webbrowser angezeigt und ausgeführt.
Hierzu muss Anaconda installiert sein.
Anaconda ist kostenlos und kann [hier](https://www.anaconda.com/products/individual) heruntergeladen werden.
Anschließend muss das Programm installiert werden - hierbei darauf achten, dass Python 3.X und nicht Python 2.X installiert wird.

### Daten und Notebooks laden
Außerdem benötigen Sie noch die hier bereitgestellten Daten. Für eine lokale Installation empfehlen wir einen vollständigen Download aller Wochen.
Über [diesen Direkt-Link](https://github.com/KI-Campus/AMALEA/archive/refs/heads/master.zip) oder auf der Startseite dieses Repositories unter `Code`-->`Download ZIP` erhalten sie ein ZIP Archiv mit allen benötigten Dateien.

Falls Sie Erfahrung mit dem Versionsverwaltungstool git haben oder sammeln möchten, könne Sie dieses Repository auch direkt mit git clonen (`git clone https://github.com/KI-Campus/AMALEA.git`). Eine Einführung in git finden Sie beispielsweise [hier](https://open.hpi.de/courses/git2020). 

### Virtuelle Umgebung (einmalig)

Bevor wir nun mit dem Ausführen des Codes beginnen, müssen wir vorher eine virtuelle Umgebung erstellen.
Der Vorteil einer virtuellen Umgebung ist, dass alles, was innerhalb dieser Umgebung installiert wird, sich nicht auf das restliche System auswirkt.
Außerdem kann, mithilfe der `amalea.yml` alle benötigten Pakete installiert werden, sodass dies später nicht nachgeholt werden muss.

Um eine virtuelle Umgebung mithilfe der `amalea.yml` zu erstellen muss in die Anaconda Prompt lediglich

    conda env create --file amalea.yml
    
eingegeben und mittels Enter bestätigt werden.
Da, wie bereits beschrieben, benötigte Pakete installiert werden, kann dieser Vorgang etwas Zeit in Anspruch nehmen.

Sobald die Installation abgeschlossen ist, kann mittels

    conda activate amalea

die virtuelle Umgebung aktiviert und mittels `jupyter notebook .`  die Jupyter Notebook Umgebung gestartet werden.

### Starten von Anaconda

Um an den Übungen zu arbeiten, muss als erstes die _Anaconda Prompt_ (auch _Anaconda Prompt (Anaconda3)_) gestartet werden.
Diese taucht als installiertes Programm in der Programmliste auf. Unter Mac (oder) Linux kann direkt das Terminal aufgerufen werden und die anleitung hier weiter befolgt werden
Nun muss noch der Pfad zu den Notebooks herausgefunden werden.
Wurden diese heruntergeladen, können diese z.B. im Downloadordner liegen.
Ein Beispiel hierfür wäre: `C:\Users\Max\Downloads\AMALEA`

Nun wird dieser Pfad mit einem Vorangestellten "cd " in die Anaconda Prompt eingegeben.
In dem genannten Beispiel also:

    cd C:\Users\Max\Downloads\AMALEA

und anschließend mittels Enter bestätigen.Für  Mac und Linux Nutzer unterscheidet sich der Befehl leicht im Dateipfad z.B. `cd ~/Downloads/AMALEA/`
Als Nächstes muss in das Terminal noch

    jupyter notebook .
    
eingegeben und wieder mittels Enter bestätigt, werden.
Nun sollte im Terminal etwas angezeigt werden - was im folgenden nicht mehr wichtig ist - und sich ein neues Browser-Fester bzw. -Reiter öffnen.
Nun sollten die im _AMALEA_ Ordner abgelegt Jupyter Notebooks (bzw. deren Überordner) angezeigt werden - beides kann durch einen Mausklick geöffnet werden und das entsprechende Notebook öffnet sich.

Schließen lässt sich die Umgebung im Terminal mit der Tastenkombination `Ctrl+C` bzw. `Ctrl-Break` und anschließender Bestätigung mit `y` (für "yes").

## Google Colab

Google Colab ist unter [Link](https://research.google.com/colaboratory/) erreichbar.
Bevor Notebooks hochgeladen und ausgeführt werden können, muss eine Anmeldung mit dem eigenen Google Account erfolgen.
Anschließend gibt es zwei Möglichkeiten über die in der README bereitgestellten Links (<a href='https://colab.research.google.com/github/KI-Campus/AMALEA/blob/master/Woche%201/2%20Pandas%20retten%20den%20Tag.ipynb'><img src='https://colab.research.google.com/assets/colab-badge.svg' alt='Open In Colab'></a>) können Sie direkt auf eine interaktive Version des gewünschten Notebooks zugreifen. Alternativ können Sie Notebook-Dateien (mit der Endung `*.ipynb`) direkt hochladen, dazu:

* Falls bereits ein Fenster mit gelbem Menü geöffnet ist, kann in diesem direkt auf _Hochladen_ geklickt werden. Anschließend kann via Drag'n' drop oder mittels _Datei auswählen_ das gewünschte Notebook hochgeladen und anschließend bearbeitet, sowie ausgeführt werden.
* Falls sich kein Fenster öffnet, kann im Menü der Punkt _Datei_ ausgewählt werden. Anschließend kann via _Notebook hochladen_ das Notebook per Drag'n' drop oder mittels _Datei auswählen_ hochgeladen sowie anschließend bearbeitet und ausgeführt werden.
* Beachten Sie, dass Sie zusätzliche Daten und Bilder hier ggf. manuell hochladen müssen

Notebooks, die externe Daten benötigen starten mit einer Zeile, mit der diese Daten automatisch heruntergeladen werden. Bitte führen Sie diese Zelle aus!

## myBinder
[MyBinder](https://mybinder.org/) ist eine Plattform, die kostenlos und ohne Anmeldung interaktive Notebook Umgebungen zur Verfügung stellt. Über die in der README verfügbaren Links <a href='https://mybinder.org/v2/gh/KI-Campus/AMALEA/HEAD?filepath=Woche%201/3%20Sherlock%20Pandas%20und%20Data%20Watson.ipynb'><img src='https://mybinder.org/badge_logo.svg' alt='Open In myBinder'></a> können die einzelnen Notebooks direkt aufgerufen werden. myBinder kopiert automatisch alle benötigten Daten und installiert notwendige Packete, daher sollte es hier zu keinen Problem kommen. Sie können auch alle Programmierübungen auf einmal öffnen, klicken Sie dazu <a href='https://mybinder.org/v2/gh/KI-Campus/AMALEA/HEAD'><img src='https://mybinder.org/badge_logo.svg' alt='Open In myBinder'></a> . Anschließend können Sie die gewünschte Übung aus dem entsprechenden Übungsorder auswählen.

Bitte beachten Sie, dass das Starten von myBinder - je nach Auslastung - mehrere Minuten dauern kann und in der Umgebung keine GPUs zur Verfügung stehen, sodass das Training von Neuronalen Netzen (ab Woche 5) länger dauern kann.

# FAQ

Im nachfolgenden werden mögliche Probleme und Lösungen beschrieben.
Grundsätzliche empfehlen wir folgendes Vorgehen: 

1. Bitte starten Sie den Kernel neu.
2. Überprüfen Sie das alle Abhängigkeiten, also benötigte Pakete und Daten vorhanden sind und Sie auf diese zugreifen können.
3. Suchen Sie hier in unserer FAQ, im Forum oder Online nach Unterstützung.

### Neustarten des Kernels

Intern wird alles, was der/die Benutzende an Aktionen ausführt, vom Kernel ausgeführt.
Sollte das Notebook nicht mehr reagieren oder parallel ein neues Package installiert worden sein, muss dieser neu gestartet werden.
Dies kann über die Menüleiste via `Kernel` und dann `Restart` erfolgen.

### ModuleNotFoundError

Sollte, nach der Ausführung, unterhalb einer Zelle ``ModuleNotFoundError`` (in rot) auftauchen, ist ein benötigtes Paket (engl. package) nicht installiert.
In Packages findet sich Funktionalität, die von anderen programmiert worden ist und frei verwendet werden kann.
Beispielsweise sind `pandas`, `random` oder `tensorflow` solche Pakete.
Fehlende Pakete können mithilfe der Anaconda Prompt nachinstalliert werden.
In der Regel ist ein Vermerk in den Notebooks enthalten, falls ein Package, dass nicht vorinstalliert sein sollte, verwendet wird.
Dieser Vermerk beinhaltet einen Befehl, der in die Anaconda Prompt eingegeben werden muss, um das fehlende Package zu installieren.

In Woche 1 wird bspw. die Bibliothek `matplotlib` zum Anzeigen von Graphen verwendet.
Der Befehl zur Installation hierfür lautet:

    conda install -c conda-forge matplotlib
    
Dieser muss in die Anaconda Prompt eingegeben werden.
Nachdem die Eingabe mittels Enter bestätigt wurde, beginnt Anaconda das Paket sowie mögliche Abhängigkeiten zu suchen.
Sobald diese gefunden wurden, wird der/die Benutzende gefragt, ob er/sie das Paket (das bzw. die im Terminal angezeigt wird/ werden) installieren möchte.
Um dies zu bestätigen, muss ein y eingegeben und mit Enter bestätigt werden.
Nun wird das Paket bzw. die Pakete installiert.

### FileNotFoundError
Sollte beim Ausführen ein `FileNotFoundError` auftreten, kann einer der Gründe sein, dass eine benötigte Datei nicht verfügbar ist.
Überprüfen , dass der gewünschte Ordner und die Datei darin existiert. 

In Google Colab müssen Sie ggf. Dateien hochladen
Wird bspw. die Datei `daten.csv` aus einem Ordner namens `data` eingelesen, muss diese Struktur in Google Colab vorhanden sein.
Hierzu existiert auf der linken Seite ein weiteres Menü, in dem das Untermenü `Dateien` vorhanden ist. 
Mittels diesem können z.B. weitere Daten sowie Ordner hochgeladen werden.
