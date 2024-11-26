# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("[name_c]", color="#03f0fc")
define a = Character("[name_a]", color="#bbc400")
define x = character("", color = "#eb3200")
define r = character("Rex", color ="#eb3000")
define b = character("Bolt", color="#03f0fc")
default life_counter = 3
default name_a = "Lehrer"
default name_c = "Mitschüler"
default hint_counter = 3
# The game starts here.

label start:

    menu:
        "experimentelle features" :
            menu:
                "namen ändern":
                    $ name_c = renpy.input("name für Mitschüler ?")
                    $ name_c = name_c.strip()
                    $ name_a = renpy.input("name für Lehrer ?")
                    $ name_a = name_a.strip()
                "heapsort demo":

                    $ n1 = renpy.input("", "", allow="0123456789") # the same as $ z = renpy.input(prompt="", default="", allow="0123456789")
                    $ n1 = int(n1)
                    "[n1]"
                    $ n2 = renpy.input("", "", allow="0123456789") # the same as $ a = renpy.input(prompt="", default="", allow="0123456789")
                    $ n2 = int(n2)
                    "[n2]"
                    $ n3 = renpy.input("", "", allow="0123456789") # the same as $ b = renpy.input(prompt="", default="", allow="0123456789")
                    $ n3 = int(n3)
                    "[n3]"
                    $ n4 = renpy.input("", "", allow="0123456789") # the same as $ c = renpy.input(prompt="", default="", allow="0123456789")
                    $ n4 = int(n4)
                    "[n4]"
                    $ n5 = renpy.input("", "", allow="0123456789") # the same as $ d = renpy.input(prompt="", default="", allow="0123456789")
                    $ n5 = int(n5)
                    "[n5]"
                    $ n6 = renpy.input("", "", allow="0123456789") # the same as $ f = renpy.input(prompt="", default="", allow="0123456789")
                    $ n6 = int(n6)
                    "[n6]"
                    python :
                        def heapify(arr, n, i):
                            renpy.say(a,"[arr]")
                            largest = i # Initialize largest as root
                            l = 2 * i + 1 # left = 2*i + 1
                            r = 2 * i + 2 # right = 2*i + 2
                            if l < n and arr[i] < arr[l]:
                                largest = l
                            if r < n and arr[largest] < arr[r]:
                                largest = r
                            if largest != i:
                                (arr[i], arr[largest]) = (arr[largest], arr[i]) # swap
                                heapify(arr, n, largest)
                                renpy.say(a,"[arr]")
                        def heapSort(arr):
                            n = len(arr)
                            for i in range(n // 2, -1, -1):
                                heapify(arr, n, i)
                            for i in range(n - 1, 0, -1):
                                (arr[i], arr[0]) = (arr[0], arr[i]) # swap
                                heapify(arr, i, 0)
                        arr = [n1, n2, n3, n4, n5, n6, ]
                        heapSort(arr)
                        renpy.say(a,"[arr]")
                        n = len(arr)

                    return
        "normal":
            "ok , normal "
    
    #Storyline

    scene black

    x "Wissen beruht nicht nur auf Wahrheit, sondern auch auf Irrtum. - Carl Jung"
    
    scene future #idk what picture

    x "Jahr 3670"
    x "Bevölkerung 25%"

    x "Was von den größten Errungenschaften der Menschheit übrig blieb, waren längst
    waren längst vergessene Erinnerungen in Schutt und Asche"

    x "Manche geben dem Übermut der Menschen die Schuld: Sie dachten, sie könnten alles haben
    erkannten dann aber, dass das Einzige, dass zwischen uns und allem was wir haben wollten stand,
    die Menschheit selbst war."

    x "Andere gaben den Maschinen die Schuld."

    x "Die Menscheit trug die Sünden derer, die für den Bau schreklicher Massenvernichtungswaffen
    verantwortlich waren. Sie setzten alles aufs Spiel."

    x "Und damit besiegelte sich das Schicksal der Menschen, in einem zweiten dunklen
    Zeitalter zu leben, in dem das Streben nach Wissen Ketzerei ist."

    x "Doch in einer Geschichte, die so alt ist wie die Menschheit selbst, gibt es immer
    Induviduen, die sich dem Griff der Ungewissheit entziehen."

    scene rex #picture missing

    show rex at right with dissolve

    r "Was zur Hölle? Ein Wecker so früh nach der gestrigen Aufgabe?
    Der Arzt ist diese Woche absolut in Höchstform."

    b "Rex an die Kommandozentrale, Rex an die Kommandozentrale! Wir haben endlich
    Informationen für den Sortieralgorithmus gefunden, den wir brauchen."

    scene Kommandozentrale

    show bolt at left with dissolve
    
    b "Ah, da bist du ja, komm mein Junge. Wir haben Arbeit zu erledigen."

    show r at right with dissolve

    r "Morgen Doc, ich dachte wir hätten das Sortieren mit Informationen geknackt, die ich
    gestern von Goldstein und von Neumann im Jahr 1948 stehlen musste?"

    b "Das, Rex, war eine detaillierte Beschreibung und Analyse von Mergesort. Was wir
    heute hier finden müssen, ist Heapsort. Man könnte sagen, ein Verwandter von Mergesort,
    aber in vielerei Hinsicht einzigartig."
    
    r "Das ist ja alles cool Doc, aber müssen wir wirklich alle Sortieralgorithmen verstehen?
    Reicht das, was wir bis jetzt haben nicht aus?"

    b "Rex, Die verschiedenen Sortieralgorithmen haben ihre eigenen praktischen Funktionen.
    Unsere Kollegen aus der Versorgung könnten eine bessere Methode gebrauchen, um die
    Lebensmittelkisten nach ihrem Gewicht zu stapeln."

    r "Sie haben Recht, Doc."

    b "Außerdem ist das der Zweck des Kodex, das Wissen aus unserer Vergangenheit
    wiederzuerlangen, egal, was die älteren Führer wollen. Ziel ist es doch die Unwissenheit
    über unsere Geschichte und ehemalige Technologien auszulöschen, damit wir nach einer besseren
    Zukunft streben können."

    r "Ja, ja, die edle Vision"

    b "Rex, mein Junge. Für die nächste Mission wirst du ins Jahr 2024 transportiert.
    An einen Ort namens Estinien Applied University of Technology"

    r "Moment. Anfang 2000? Sie sagten doch, jeder Moment zwischen 1999 und 2500 sei
    aufgrund der Zeitfeld-Interferenz tabu?"

    b "Ja, ja, ich weiß. Die Spiral-Termporal-Field-Theroie meines Vaters. Das ist aber der
    Hauptgrund, warum wir fast nichts über die Informatik wissen."

    b "Aber sieh doch, aufgrund ihrer Vergangenheit glauben wir Zugang zu diesem zeitlichen
    Feld gefunden zu haben."

    r "Ein Hoch auf die Wissenschaft!"

    b "Die Wissenschaft ist wirklich wunderbar."

    scene zeitmaschine

    b "Siehst du Rex, das Zeitfeld wirkt wie ein Schild um die Jahre 1999 und 2500. Wir haben
    aber rausgefunden, dass wir diese Barriere durchdringen können. Dafür müssen wir uns nur
    als Objekt dieser Zeit verkleiden und unsere wahre Zeitsignatur verbergen."

    b "Um es kurz zu machen: Wenn das Zeitfeld irgendwie deine wahre Zeitsignatur kennt, dann
    werden Sie gewaltsam in die Vergangenheit oder Zukunft geschleudert."

    b "Hier das wichtigste. Das Temporal Cloaking Device. Du musst nur diese Taste drücken,
    und auf 2024 einstellen. Die Zeitmaschine wird dich in das Jahr befördern und
    sich selbst tarnen"

    #Music missing

    scene 2024

    r "Ist das?"

    b "Ja, das ist es tatsächlich, ein Ort, den die meisten Menschen meiden, perfekt,
    um eine Zeitmaschine zu verstecken"
    




    play music bm3

    scene milstart
    
    a "Willkommen zum heutigen Thema: Heapsort!"

    show announcer at right with dissolve

    a "Heapsort ist ein effizienter, vergleichsbasierter Sortieralgorithmus, der uns hilft, eine Liste von Zahlen in aufsteigender Reihenfolge zu ordnen."
    a "Er basiert auf einer speziellen Datenstruktur, dem sogenannten Heap, und unterscheidet sich dadurch von anderen Algorithmen wie Quicksort oder Mergesort."
    a "Lasst uns zuerst klären, was ein Heap eigentlich ist und wie er funktioniert."

    show announcer at left with move

    show cont1 at right with dissolve

    c "[name_a], was genau ist ein Heap? Ich habe den Begriff schon gehört, aber wie sieht so eine Struktur eigentlich aus?"

    a "Gute Frage,  [name_c] ! Ein Heap ist eine spezielle Art binärer Baum, der eine feste Struktur einhält: Jeder Elternknoten ist größer als seine Kindknoten. Das bedeutet, dass der größte Wert im Baum immer an der Spitze, also an der Wurzel, steht."
    a "Wir nennen diese Struktur einen Max-Heap. Das ist wichtig, weil wir beim Heapsort genau diese Max-Heap-Eigenschaft nutzen, um das größte Element im Baum zu identifizieren und an die richtige Stelle im Array zu bringen."
    a  "Verstanden?"

    show cont1 at right with dissolve

    c "Ja, das hilft schon mal! Aber wie genau können wir diesen Heap dann für die Sortierung verwenden?"

    a "Sehr gute Frage! Der Max-Heap gibt uns die Möglichkeit, in jedem Schritt das größte verbleibende Element schnell zu finden und an die richtige Position im Array zu setzen."
    a "Ich werde den Ablauf des Heapsort-Algorithmus Schritt für Schritt erklären, damit ihr seht, wie das funktioniert."

    show cont1 at right with vpunch

    a "Schritt 1: Aufbau des Max-Heaps."
    a "Der erste Schritt beim Heapsort besteht darin, das Eingabearray – also die Liste der zu sortierenden Zahlen – in einen Max-Heap umzuwandeln."
    a  "Das bedeutet, dass wir die Elemente so anordnen, dass der größte Wert an der Wurzel steht und die Max-Heap-Eigenschaft für alle Eltern-Kind-Beziehungen gilt."

    c  "Und wie genau machen wir das? Ist das nicht aufwendig?"

    a  "Gute Beobachtung, [name_c]! Um das Array in einen Max-Heap umzuwandeln, verwenden wir eine Methode namens 'Heapify'. Die Heapify-Prozedur überprüft jeden Knoten und stellt sicher, dass die Max-Heap-Eigenschaft für diesen Knoten und seine Kinder erfüllt ist."
    a  "Wir arbeiten uns dabei von unten nach oben durch den Baum – beginnend bei den Knoten, die Kinder haben, und bewegen uns schrittweise zur Wurzel. Das ermöglicht uns, die Max-Heap-Eigenschaft für den gesamten Baum zu garantieren, ohne alles neu zu ordnen."

# Visualisierung Anzeigen (ungeordneter Heap)
    a "Hier seht ihr ein Beispiel eines Arrays vor dem Heapify-Prozess. Die Zahlen sind noch ungeordnet."
    a "Nach dem Heapify-Prozess sieht der Baum jedoch so aus:"
#Visualisierung Anzeigen (geordneter Heap)
    show cont1 at right with vpunch
    c  "Okay, jetzt verstehe ich, wie der Max-Heap aussieht! Aber was machen wir dann damit?"

    a  "Sehr gut, [name_c]. Das bringt uns zu Schritt 2."
    a "Schritt 2: Tauschen und neu aufbauen."

    a "Da der größte Wert nun an der Wurzel steht, tauschen wir ihn mit dem letzten Element des Arrays."
    a "Dadurch bringen wir das größte Element an die richtige Position im Array."
    a "Nachdem wir diesen Tausch durchgeführt haben, reduzieren wir die Größe des Heaps um eins, weil das größte Element jetzt sortiert und fest an seiner Position ist."

    c  "Und was passiert dann mit dem Heap? Ist er dann nicht kaputt?"

    a  "Genau, [name_c]! Nach dem Tausch kann die Max-Heap-Eigenschaft tatsächlich verletzt sein. Deshalb wenden wir die Heapify-Prozedur erneut auf die Wurzel an, um den Heap zu reparieren und sicherzustellen, dass die Max-Heap-Eigenschaft wiederhergestellt wird."

#Visualisierung Anzeigen (Heapify vorher)
    a "Hier tauschen wir das Wurzelelement mit dem letzten Element."
    a "Da die Max-Heap-Eigenschaft dadurch verletzt wurde, wenden wir Heapify auf den Wurzelknoten an, um die Struktur zu reparieren."
#Visualisierung Anzeigen(Heapify nachher)

    a "Nach dem erneuten Aufrufen von Heapify sieht der Heap wieder korrekt aus, und wir können den nächsten Schritt fortsetzen."
    a "Schritt 3: Wiederholen, bis das gesamte Array sortiert ist."
    a "Wir wiederholen den Prozess – das Wurzelelement mit dem letzten Element tauschen, die Heapgröße reduzieren und Heapify auf die Wurzel anwenden – bis das gesamte Array sortiert ist."
    a "Am Ende ist das Array vollständig sortiert, und wir haben die Zahlen in aufsteigender Reihenfolge angeordnet."
#Visualisierung Anzeigen (vollständige Sortierung der Liste)
    c  "Wow, das ist echt clever! Aber warum ist Heapsort eigentlich so effizient?"

    a  "Gute Frage, [name_c]! Der Heapsort-Algorithmus hat im besten, durchschnittlichen und schlechtesten Fall eine Zeitkomplexität von O(n log n), was bedeutet, dass er auch bei großen Datenmengen effizient bleibt."
    a  "Im Gegensatz zu einigen anderen Algorithmen benötigt Heapsort außerdem nur eine konstante Menge an zusätzlichem Speicherplatz, da der gesamte Sortiervorgang direkt im Eingabearray durchgeführt wird. Das nennt man in-situ-Sortierung."

    c  "Das klingt ziemlich nützlich! Gibt es Nachteile im Vergleich zu anderen Algorithmen?"

    a  "Ja, tatsächlich. Ein Nachteil von Heapsort ist, dass er keine stabile Sortierung bietet. Das bedeutet, dass gleiche Werte ihre relative Reihenfolge im Array verlieren können."
    a  "Außerdem ist Heapsort keine Divide-and-Conquer-Methode wie Quicksort oder Mergesort. Heapsort teilt das Array nicht in kleinere Teile auf, sondern arbeitet durch das kontinuierliche Wiederherstellen der Heap-Struktur, um die Sortierung zu erreichen."

#Abschluss Monolog (Begleitete Simulation)



    label intro:
        scene backcont
        show announcer at right with dissolve

        a "Im Laufe der Übung könnt ihr die einzelnen Schritte mit den Pfeiltasten durchlaufen, um genau zu beobachten, wie der Heap sich bei jedem Schritt verändert."
        a "Ich werde bei jedem Schritt erklären, warum wir ihn durchführen und was im Hintergrund passiert."
        a "Lasst uns also in die Simulation einsteigen und Heapsort in Aktion sehen!"

# Potenzielle Simulation an einem Beispiel. 
        a "Jetzt solltet ihr genügend wissen zu dem Heapsort-Algorithmus gesammelt haben, um euch den Kontrollfragen zu stellen."
        

    label q1:
        call lifecount
        a "Kommen wir zur ersten Frage!"
        a "Was ist die Hauptidee hinter dem Heapsort-Algorithmus?"

        menu:
            "Den Eingabedatensatz in einen geordneten Baum umzuwandeln, um das größte Element schnell zu finden.":
                a "Ja genau, der Eingabedatensatz wird in einen geordneten Baum umgewandelt, um das größte Element schnell zu finden."
                jump win1

            "Den Eingabedatensatz in kleinere Teile aufzuteilen und diese unabhängig zu sortieren.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal."
                $ life_counter -= 1
                if life_counter > 0:
                    jump q1
                else: 
                    jump game_over

            "Jedes Element mit jedem anderen zu vergleichen und in aufsteigender Reihenfolge anzuordnen.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal."
                $ life_counter -= 1
                if life_counter > 0:
                    jump q1
                else: 
                    jump game_over

            "Eine Sortierung durch wiederholtes Vergleichen benachbarter Elemente.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal."
                $ life_counter -= 1
                if life_counter > 0:
                    jump q1
                else: 
                    jump game_over

            "Ich brauche einen Hinweis!":
                a "Hast du mir überhaupt zugehört?"
                jump q1
    return

    label win1:
        jump q2

    label q2:
        scene backcont
        show announcer at right with dissolve
        call lifecount
        a "Welche Aussage beschreibt die Max-Heap-Eigenschaft korrekt?"

        menu:
            "Jeder Kindknoten hat einen größeren Wert als sein Elternknoten.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal."
                $ life_counter -= 1
                if life_counter > 0:
                    jump q2
                else: 
                    jump game_over
    
            "Jeder Elternknoten hat einen größeren Wert als seine Kindknoten.":
                a "Ja genau jeder Elternknoten hat einen größeren Wert als seine Kindknoten."
                jump q3

            "Die Knoten sind in zufälliger Reihenfolge angeordnet.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal."
                $ life_counter -= 1
                if life_counter > 0:
                    jump q2
                else: 
                    jump game_over
            
            "Der linke Kindknoten ist immer kleiner als der rechte Kindknoten.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal."
                $ life_counter -= 1
                if life_counter > 0:
                    jump q2
                else: 
                    jump game_over

            "Ich brauche einen Hinweis!":
                a "Hast du mir überhaupt zugehört?"
                jump q2
    return
        



    label q3:
        a "Wie lautet die Zeitkomplexität des Heapsort-Algorithmus im besten, durchschnittlichen und schlechtesten Fall?"

        menu:
            "O(n)":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal."
                $ life_counter -= 1
                if life_counter > 0:
                    jump q3
                else: 
                    jump game_over
            
            "O(n log (n))":
                a "Ja genau die Zeitkomplexität beträgt immer O(n log (n))."
                jump q4
            
            "O(n^2)":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal."
                $ life_counter -= 1
                if life_counter > 0:
                    jump q3
                else: 
                    jump game_over
            
            "O(log n)":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal."
                $ life_counter -= 1
                if life_counter > 0:
                    jump q3
                else: 
                    jump game_over
            
            "Ich brauche einen Hinweis!":
                a "Hast du mir überhaupt zugehört?"
                jump q3
    return
            
    label q4:
        a "Welche Aufgabe erfüllt die Heapify-Prozedur im Heapsort-Algorithmus?"

        menu:

            "Sie vertauscht das größte und kleinste Element im Array.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q4
                else: 
                    jump game_over

            "Sie vertauscht das größte und kleinste Element im Array.":
                a "Ja genau die Heapify-Prozedur überprüft und stellt sicher, dass die Max-Heap-Eigenschaft eines Knotens und seinen Kinder gewahrt bleibt."
                jump q5
            
            "Sie teilt das Array in kleinere Unterarrays auf.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q4
                else: 
                    jump game_over
            
            "Sie entfernt das kleinste Element aus dem Heap.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q4
                else: 
                    jump game_over
            
            "Ich brauche einen Hinweis!":
                a "Hast du mir überhaupt zugehört?"
                jump q4
    return

    label q5:
        a "Schritte des Heapsort-Algorithmus"

        menu:

            "Aufbau eines Max-Heaps aus dem Eingabearray.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q5
                else: 
                    jump game_over
            
            "Aufteilen des Arrays in mehrere Teilbäume.":
                a "Ja genau, das Aufteilen des Arrays in mehrere Teilbäume ist kein Teil des Algorithmus."
                jump q6
            
            "Vertauschen des größten Elements mit dem letzten Element des Heaps.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q5
                else: 
                    jump game_over
            
            "Wiederholtes Anwenden von Heapify nach jedem Tausch.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q5
                else: 
                    jump game_over
            
            "Ich brauche einen Hinweis!":
                a "Hast du mir überhaupt zugehört?"
                jump q5
    return
    
    label q6:
        a "Welchen Speicherbedarf hat der Heapsort-Algorithmus?"

        menu:

            "O(n) zusätzlicher Speicher":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q6
                else: 
                    jump game_over
            
            "O(n^2) zusätzlicher Speicher":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q6
                else: 
                    jump game_over

            "O(1) zusätzlicher Speicher":
                a "Ja genau, das Aufteilen des Arrays in mehrere Teilbäume ist kein Teil des Algorithmus."
                jump q7
            
            "O(log n) zusätzlicher Speicher":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q6
                else: 
                    jump game_over

            "Ich brauche einen Hinweis!":
                a "Hast du mir überhaupt zugehört?"
                jump q6
    return

    label q7:
        a "Wann ist es sinnvoll, Heapsort gegenüber Quicksort zu verwenden?"

        menu:

            "Wenn der Speicherverbrauch minimiert werden muss.":
                a "Ja genau, man sollte Heapsort verwenden, wenn der Speicherverbrauch minimiert werden muss."
                jump q8
            
            "Wenn die Daten bereits fast sortiert sind.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q7
                else: 
                    jump game_over

            "Wenn eine stabile Sortierung notwendig ist.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q7
                else: 
                    jump game_over
            
            "Wenn die Eingabegröße klein ist.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q7
                else: 
                    jump game_over

            "Ich brauche einen Hinweis!":
                a "Hast du mir überhaupt zugehört?"
                jump q7
    return

    label q8:
        a "Was ist die richtige Reihenfolge der folgenden Schritte im Heapsort-Algorithmus?"
        a " 1. Vertausche das Wurzelelement mit dem letzten Element des Heaps.
            2. Baue einen Max-Heap aus dem Eingabearray auf.
            3. Wende die Heapify-Prozedur an, um die Max-Heap-Eigenschaft wiederherzustellen.
            4. Reduziere die Heapgröße um eins. "

        menu:

            "2 → 1 → 4 → 3":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q8
                else: 
                    jump game_over
            
            "1 → 2 → 3 → 4":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q8
                else: 
                    jump game_over

            "2 → 1 → 3 → 4":
                a "Ja genau, genau das ist die richtige Reihenfolge."
                jump q9a

            "3 → 2 → 1 → 4":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q8
                else: 
                    jump game_over
            
            "Ich brauche einen Hinweis!":
                a "Hast du mir überhaupt zugehört?"
                jump q8
    return
        
    label q9a:
        a "Welche der folgenden Aussagen ist richtig?"

        menu:

            "Heapsort benötigt in der Regel weniger Speicher als Quicksort.":
                a "Ja genau, Heapsort benötigt in der Regel weniger Speicher als Quicksort."
                jump q9b
            
            "Quicksort ist stabil, Heapsort jedoch nicht.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q9a
                else: 
                    jump game_over
            
            "Heapsort ist im Durchschnitt schneller als Quicksort.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q9a
                else: 
                    jump game_over
            
            "Quicksort hat eine schlechtere Zeitkomplexität als Heapsort im schlechtesten Fall.":
                a "Ja genau, Heapsort hat eine schlechtere Zeitkomplexität als Heapsort im schlechtesten Fall."
                jump q9c

            "Ich brauche einen Hinweis!":
                a "Hast du mir überhaupt zugehört?"
                jump q9a
    return

    label q9b:
        a "Welche Aussage ist wahr?"

        menu:

            "Quicksort ist stabil, Heapsort jedoch nicht.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q9a
                else: 
                    jump game_over
            
            "Heapsort ist im Durchschnitt schneller als Quicksort.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q9a
                else: 
                    jump game_over

            "Quicksort hat eine schlechtere Zeitkomplexität als Heapsort im schlechtesten Fall.":
                a "Ja genau, Heapsort hat eine schlechtere Zeitkomplexität als Heapsort im schlechtesten Fall."
                jump q9c

            "Ich brauche einen Hinweis!":
                a "Hast du mir überhaupt zugehört?"
                jump q9b
    return
        
    label q9c:
        a "Welche Aussage stimmt noch?"

        menu:

            "Heapsort benötigt in der Regel weniger Speicher als Quicksort.":
                a "Ja genau, Heapsort benötigt in der Regel weniger Speicher als Quicksort ."
                jump q10

            "Quicksort ist stabil, Heapsort jedoch nicht.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q9a
                else: 
                    jump game_over

            "Heapsort ist im Durchschnitt schneller als Quicksort.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q9a
                else: 
                    jump game_over

            "Ich brauche einen Hinweis!":
                a "Hast du mir überhaupt zugehört?"
                jump q9c
    return

    label q10:
        a "Welcher Fehler kann zu einer fehlerhaften Sortierung bei Heapsort führen?"

        menu:

            "Das Vertauschen des größten Elements mit dem ersten Element statt mit dem letzten.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q10
                else: 
                    jump game_over

            "Das Nicht-Anwenden von Heapify nach dem Tausch der Wurzel.":
                a "Ja genau, das Nicht-Anwenden von Heapify nach dem Tausch der Wurzel, kann zu einer Fehlerhaften Sortierung führen."
                jump win_game

            "Das Vertauschen der Kindknoten im Heap während des Heapify-Prozesses.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q10
                else: 
                    jump game_over
            
            "Das erneute Aufbauen des Heaps nach jedem Sortierschritt.":
                a "Nein, dass ich leider nicht richtig. Versuch es nochmal"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q10
                else: 
                    jump game_over

            "Ich brauche einen Hinweis!":
                a "Hast du mir überhaupt zugehört?"
                jump q10
    return

    label lifecount:
        if life_counter == 3:
            show three at right with dissolve
        elif life_counter == 2:
            show two at right with dissolve
        elif life_counter == 1:
            show one at right with dissolve
        else:
            show zero at right with dissolve
        return

    label hint_counter:
        if hint_counter == 3:
            show 
    

    label game_over:
    
    scene milstart
    show announcer at right with dissolve
    a "game over"

    show cont1 at left with vpunch
    c "aww"
    
    jump over_screen

    label win_game:
    
        scene milstart
        show announcer at right with dissolve
        a "you win"

        show cont1 at left with dissolve
        c "yay"
    jump over_screen

    label over_screen:
        a "So ends the class"

    return
