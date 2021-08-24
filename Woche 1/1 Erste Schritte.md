# Erste Schritte
Um die praktischen Aufgaben zu lösen, benötigen Sie eine Juypter Notebook Umgebung. Diese können Sie entweder direkt bei sich auf den Computer installieren oder auf einen Online-Service wie Google Colab oder myBinder zurückgreifen. Nachdem Sie eine Lösung gewählt haben, probieren Sie zunächst die Basis Funktionen von Jupyter Notebooks anhand eines unsere Beispiele aus.

## Ausführen von Code

Jupyter Notebooks sind in Zellen von Code und Text organisiert, die ausgeführt werden müssen um Ergebnisse (`outputs`) zu produzieren
Eine einzelne Zelle kann über die Menüleiste ausgeführt werden. In Google Colab hat jede Zelle einen `▶️` Button, bei eine Lokalen Installation muss die Zelle zuerst ausgewählt werden, z.B. durch einen Mausklick auf die Zelle.
Anschließend kann mittels `▶️ Run`oder `Run Cells`, welches unter `Cell` in der Menüleiste zu finden ist, die Zelle ausgeführt werden. 
Alternativ kann dies durch das gleichzeitige Drücken von `Shift`+`Enter` erfolgen.
Sollen alle Zellen eines Notebooks ausgeführt werden, kann unter `Cell` `Run All` ausgewählt werden.

Im nachfolgenden werden mögliche Probleme beschrieben.

### Neustarten des Kernels

Intern wird alles, was der/die Benutzende an Aktionen ausführt vom Kernel ausgeführt.
Sollte das Notebook nicht mehr reagieren oder parallel ein neues Package installiert worden sein, muss dieser neu gestartet werden.
Dies kann über die Menüleiste via `Kernel` und dann `Restart` erfolgen.

### ModuleNotFoundError

Sollte, nach der Ausführung, unterhalb einer Zelle ``ModuleNotFoundError`` (in rot) auftauchen, ist ein benötigtes Paket (engl. package) nicht installiert.
In Packages findet sich Funktionalität, die von anderen programmiert worden ist und frei verwendet werden kann.
Beispielsweise sind `pandas`, `random` oder `tensorflow` solche Packete.
Fehlende Packete können mithilfe der Anaconda Prompt nachinstalliert werden.
In der Regel ist ein Vermerk in den Notebooks enthalten, falls ein Package, dass nicht vorinstalliert sein sollte, verwendet wird.
Dieser Vermerk beinhaltet einen Befehl, der in die Anaconda Promt eingegeben werden muss, um das fehlende Package zu installieren.

In Woche 1 wird bspw. die Bibliothek `matplotlib` zum Anzeigen von Graphen verwendet.
Der Befehl zur Installation hierfür lautet:

    conda install -c conda-forge matplotlib
    
Dieser muss in die Anaconda Prompt eingegeben werden.
Nachdem die Eingabe mittels Enter bestätigt wurde, beginnt Anaconda das Packet sowie mögliche Abhängigkeiten zu suchen.
Sobald diese gefunden wurden, wird der/die Benutzende gefragt, ob er/sie das Packet (das bzw. die im Terminal angezeit wird/ werden) installieren möchte.
Um dies zu bestätigen, muss ein y eingegeben und mit Enter bestätigt werden.
Nun wird das Paket bzw. die Pakete installiert.

### FileNotFoundError
Sollte beim Ausführen ein `FileNotFoundError` auftreten, kann einer der Gründe sein, dass eine benötigte Datei nicht verfügbar ist.
Überprüfen Sie dass der gewünschte Ordner und die Datei darin existiert. 

In Google Colab müssen Sie ggf. Datein hochladen
Wird bspw. die Datei `daten.csv` aus einem Ordner namens `data` eingelesen, muss diese Struktur in Google Colab vorhanden sein.
Hierzu existiert auf der linken Seite ein weiteres Menü, in dem das Untermenü `Dateien` vorhanden ist. 
Mittels diesem können z.B. weitere Daten sowie Ordner hochgeladen werden.

## Lokale Verwendung
Dieser Abschnitt beschreibt die Installation von Anaconda und den Abhänigkeiten auf Ihrem Rechner.

### Installation von Anaconda

Die Jupyter Notebooks werden mithilfe von _Anaconda_ im Webbrowser angezeigt und ausgeführt.
Hierzu muss Anaconda installiert sein.
Anaconda ist kostenlos und kann [hier](https://www.anaconda.com/products/individual) heruntergeladen werden.
Anschließend muss das Programm installiert werden - hierbei darauf achten, dass Python 3.X und nicht Python 2.X installiert wird.

### Starten von Anaconda

Nun muss die _Anaconda Prompt_ (auch _Anaconda Prompt (Anaconda3)_) gestartet werden.
Diese taucht als installiertes Programm in der Programmliste auf.
Nun muss noch der Pfad zu den Notebooks herausgefunden werden.
Wurden diese heruntergeladen, können diese z.B. im Downloadordner liegen.
Ein Beispiel hierfür wäre: `C:\Users\Max\Downloads\notebooks`

Nun wird dieser Pfad mit einem Vorangestellten "cd " in die Anaconda Prompt eingegeben.
In dem genannten Beispiel also:

    cd C:\Users\Max\Downloads\notebooks

und anschließend mittels Enter bestätigen.
Als Nächstes muss in das Terminal noch

    jupyter notebook .
    
eingegeben und wieder mittels Enter bestätigt, werden.
Nun sollte im Terminal etwas angezeigt werden - was im folgenden nicht mehr wichtig ist - und sich ein neues Browser-Fester bzw. -Reiter öffnen.
Nun sollten die im _notebooks_ Ordner abgelegt Jupyter Notebooks (bzw. deren Überordner) angezeigt werden - beides kann durch einen Mausklick geöffnet werden und das Notebook öffnet sich.

### Virtuelle Umgebung

Bevor wir nun mit dem Ausführen des Codes beginnen, müssen wir vorher eine virtuelle Umgebung erstellen.
Der Vorteil einer virtuellen Umgebung ist, dass alles, was innerhalb dieser Umgebung installiert wird, sich nicht auf das restliche System auswirkt.
Außerdem kann, mithilfe der `amalea.yml` alle benötigten Pakete installiert werden, sodass dies später nicht nachgeholt werden muss.

Um eine virtuelle Umgebung mithilfe der `amalea.yml` zu erstellen muss in die Anaconda Promt lediglich

    conda env create --file amalea.yml
    
eingegeben und mittels Enter bestätigt werden.
Da, wie bereits beschrieben, benötigte Pakete installiert werden, kann dieser Vorgang etwas Zeit in Anspruch nehmen.

Sobald die Installation abgeschlossen ist, kann mittels

    conda activate amalea

die virtuelle Umgebung aktiviert und mittels `jupyter notebook`. Jupyter Notebook gestartet werden.

### Daten und Notebooks laden
Zuletzt benötigen Sie noch die hier bereitgestellten Daten. Für eine lokale Installation empfehlen wir einen vollständigen Download aller Wochen.
Über [diesen Direkt-Link](https://github.com/KI-Campus/AMALEA/archive/refs/heads/master.zip) oder auf der Startseite diese Repositories unter `Code`-->`Download ZIP` erhalten sie ein ZIP Archiv mit allen benötigten Datein.

Falls Sie Erfahrung mit dem Versionsverwaltungstool git haben oder sammeln wollen, könne Sie dieses Repository auch direkt `clonen`. Eine Einführung finden Sie beispielsweise [hier](https://open.hpi.de/courses/git2020). 


## Google Colab

Google Colab ist unter [Link](https://research.google.com/colaboratory/) erreichbar.
Bevor Notebooks hochgeladen und ausgeführt werden können, muss eine Anmeldung mit dem eigenen Google Account erfolgen.
Anschließend gibt es zwei Möglichkeiten über die in der ReadME bereitgestellten Links können Sie direkt auf eine interaktive Version des gewünschten Notebooks zugreifen. Alternativ können Sie Notebook-Datein (mit der Endung `*.ipynb`) direkt hochladen, dazu:

* Falls bereits ein Fenster mit gelbem Menü geöffnet ist, kann in diesem direkt auf _Hochladen_ geklickt werden. Anschließend kann via Drag'n' drop oder mittels _Datei auswählen_ das gewünschte Notebook hochgeladen und anschließend bearbeitet, sowie ausgeführt werden.
* Falls sich kein Fenster öffnet, kann im Menü der Punkt _Datei_ ausgewählt werden. Anschließend kann via _Notebook hochladen_ das Notebook per Drag'n' drop oder mittels _Datei auswählen_ hochgeladen sowie anschließend bearbeitet und ausgeführt werden.
