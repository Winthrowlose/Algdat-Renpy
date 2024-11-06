# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("[name_c]", color="#03f0fc")
define a = Character("[name_a]", color="#bbc400")
default life_counter = 3
default name_a = "Announcer"
default name_c = "Contestant"
# The game starts here.

label start:

    play music bm3

    scene milstart
    
    a "Willkommen zum heutigen Thema: Heapsort!"

    show announcer at right with dissolve

    a "Heapsort ist ein effizienter, vergleichsbasierter Sortieralgorithmus, der uns hilft, eine Liste von Zahlen in aufsteigender Reihenfolge zu ordnen."
    a "Er basiert auf einer speziellen Datenstruktur, dem sogenannten Heap, und unterscheidet sich dadurch von anderen Algorithmen wie Quicksort oder Mergesort."
    a "Lasst uns zuerst klären, was ein Heap eigentlich ist und wie er funktioniert."

    show announcer at left with move

    show cont1 at right with dissolve

    c "Lehrer, was genau ist ein Heap? Ich habe den Begriff schon gehört, aber wie sieht so eine Struktur eigentlich aus?"

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
        a "Frage 1: Grundlagen von Heapsort "
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
    return

    label win1:
        scene 100d
        show announcer at right with dissolve
        jump q2

    label q2:
        scene backcont
        show announcer at right with dissolve
        call lifecount
        a "Welche Aussage beschreibt die Max-Heap-Eigenschaft korrekt?"

        menu:
            "Jeder Kindknoten hat einen größeren Wert als sein Elternknoten.":
                a "fuckin idiot"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q2
                else: 
                    jump game_over
    
            "Jeder Elternknoten hat einen größeren Wert als seine Kindknoten.":
                a "Goood"
                jump q3

            "Die Knoten sind in zufälliger Reihenfolge angeordnet.":
                a "STOP"
                a "FUCKING DIE"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q2
                else: 
                    jump game_over
            
            "Der linke Kindknoten ist immer kleiner als der rechte Kindknoten.":
                a "STOP"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q2
                else: 
                    jump game_over
    return
        



    label q3:
        a "Wie lautet die Zeitkomplexität des Heapsort-Algorithmus im besten, durchschnittlichen und schlechtesten Fall?"

        menu:
            "O(n)":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q3
                else: 
                    jump game_over
            
            "O(n log (n))":
                a "gooood"
                jump q4
            
            "O(n^2)":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q3
                else: 
                    jump game_over
            
            "O(log n)":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q3
                else: 
                    jump game_over
    return
            
    label q4:
        a "Welche Aufgabe erfüllt die Heapify-Prozedur im Heapsort-Algorithmus?"

        menu:

            "Sie vertauscht das größte und kleinste Element im Array.":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q4
                else: 
                    jump game_over

            "Sie vertauscht das größte und kleinste Element im Array.":
                a "gooood"
                jump q5
            
            "Sie teilt das Array in kleinere Unterarrays auf.":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q4
                else: 
                    jump game_over
            
            "Sie entfernt das kleinste Element aus dem Heap.":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q4
                else: 
                    jump game_over
    return

    label q5:
        a "Schritte des Heapsort-Algorithmus"

        menu:

            "Aufbau eines Max-Heaps aus dem Eingabearray.":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q5
                else: 
                    jump game_over
            
            "Aufteilen des Arrays in mehrere Teilbäume.":
                a "aa"
                jump q6
            
            "Vertauschen des größten Elements mit dem letzten Element des Heaps.":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q5
                else: 
                    jump game_over
            
            "Wiederholtes Anwenden von Heapify nach jedem Tausch.":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q5
                else: 
                    jump game_over
    
    label q6:
        a "Welchen Speicherbedarf hat der Heapsort-Algorithmus?"

        menu:

            "O(n) zusätzlicher Speicher":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q6
                else: 
                    jump game_over
            
            "O(n^2) zusätzlicher Speicher":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q6
                else: 
                    jump game_over

            "O(1) zusätzlicher Speicher":
                a "aa"
                jump q7
            
            "O(log n) zusätzlicher Speicher":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q6
                else: 
                    jump game_over
    return

    label q7:
        a "Wann ist es sinnvoll, Heapsort gegenüber Quicksort zu verwenden?"

        menu:

            "Wenn der Speicherverbrauch minimiert werden muss.":
                a "aa"
                jump q8
            
            "Wenn die Daten bereits fast sortiert sind.":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q7
                else: 
                    jump game_over

            "Wenn eine stabile Sortierung notwendig ist.":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q7
                else: 
                    jump game_over
            
            "Wenn die Eingabegröße klein ist.":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q7
                else: 
                    jump game_over
    return

    label q8:
        a "Was ist die richtige Reihenfolge der folgenden Schritte im Heapsort-Algorithmus?"
        a " 1. Vertausche das Wurzelelement mit dem letzten Element des Heaps.
            2. Baue einen Max-Heap aus dem Eingabearray auf.
            3. Wende die Heapify-Prozedur an, um die Max-Heap-Eigenschaft wiederherzustellen.
            4. Reduziere die Heapgröße um eins. "

        menu:

            "2 → 1 → 4 → 3":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q8
                else: 
                    jump game_over
            
            "1 → 2 → 3 → 4":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q8
                else: 
                    jump game_over

            "2 → 1 → 3 → 4":
                a "aa"
                jump q9a

            "3 → 2 → 1 → 4":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q8
                else: 
                    jump game_over
    return
        
    label q9a:
        a "Welche der folgenden Aussagen ist richtig im Vergleich von Heapsort und Quicksort?"

        menu:

            "Heapsort benötigt in der Regel weniger Speicher als Quicksort.":
                a "aa"
                jump q9b
            
            "Quicksort ist stabil, Heapsort jedoch nicht.":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q9a
                else: 
                    jump game_over
            
            "Heapsort ist im Durchschnitt schneller als Quicksort.":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q9a
                else: 
                    jump game_over
            
            "Quicksort hat eine schlechtere Zeitkomplexität als Heapsort im schlechtesten Fall.":
                a "aa"
                jump q9c
    return

    label q9b:
        a "True, which else is true?"

        menu:

            "Quicksort ist stabil, Heapsort jedoch nicht.":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q9a
                else: 
                    jump game_over
            
            "Heapsort ist im Durchschnitt schneller als Quicksort.":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q9a
                else: 
                    jump game_over

            "Quicksort hat eine schlechtere Zeitkomplexität als Heapsort im schlechtesten Fall.":
                a "aa"
                jump q10
    return
        
    label q9c:
        a "True, which else is true?"

        menu:

            "Heapsort benötigt in der Regel weniger Speicher als Quicksort.":
                a "aa"
                jump q10

            "Quicksort ist stabil, Heapsort jedoch nicht.":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q9a
                else: 
                    jump game_over

            "Heapsort ist im Durchschnitt schneller als Quicksort.":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q9a
                else: 
                    jump game_over
    return

    label q10:
        a "Welcher Fehler kann zu einer fehlerhaften Sortierung bei Heapsort führen?"

        menu:

            "Das Vertauschen des größten Elements mit dem ersten Element statt mit dem letzten.":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q10
                else: 
                    jump game_over

            "Das Nicht-Anwenden von Heapify nach dem Tausch der Wurzel.":
                a "aa"
                jump win_game

            "Das Vertauschen der Kindknoten im Heap während des Heapify-Prozesses.":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q10
                else: 
                    jump game_over
            
            "Das erneute Aufbauen des Heaps nach jedem Sortierschritt.":
                a "aa"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q10
                else: 
                    jump game_over
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
