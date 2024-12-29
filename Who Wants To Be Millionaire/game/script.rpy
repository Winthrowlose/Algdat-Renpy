# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define x = Character("", color = "#eb3200")
define r = Character("Rex", color ="#eb3000")
define b = Character("Bolt", color="#03f0fc")
define T = Character("TM-510")
define p = Character("[name_p]")
default life_counter1 = 3
default life_counter = 3
default name_a = "Lehrer"
default name_c = "Mitschüler"
default name_p = "???"
default hint_counter = 3
transform half_size: 
    zoom 0.5 #adjust as required
transform quater_size:
    zoom 0.25 #adjust as required
transform tiny: 
    zoom 0.1 #adjust as required
# The game starts here.

label start:
    menu: 
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
                    renpy.say(x,"[arr]")
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
                        renpy.say(x,"[arr]")
                def heapSort(arr):
                    n = len(arr)
                    for i in range(n // 2, -1, -1):
                        heapify(arr, n, i)
                    for i in range(n - 1, 0, -1):
                        (arr[i], arr[0]) = (arr[0], arr[i]) # swap
                        heapify(arr, i, 0)
                arr = [n1, n2, n3, n4, n5, n6, ]
                heapSort(arr)
                renpy.say(x,"[arr]")
                n = len(arr)

            return
        "normal":
            menu :              #scuffed version of translation , replace with renpy translation feature -E
                "Deutsch":
                    jump D_start
                
                "English" :
                    jump E_start
    
    #Storyline
label D_start :
    scene black

    x "Wissen beruht nicht nur auf Wahrheit, sondern auch auf Irrtum. - Carl Jung"
    
    scene future #idk what picture

    x "Jahr 3670"
    x "Bevölkerung {color=#f00}25%%{/color}"

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
    scene command center 3670
    
    #picture missing

    show rex at half_size, right with dissolve

    r "Was zur Hölle? Ein Wecker so früh nach der gestrigen Aufgabe?
    Der Arzt ist diese Woche absolut in Höchstform."

    b "Rex an die Kommandozentrale, Rex an die Kommandozentrale! Wir haben endlich
    Informationen für den Sortieralgorithmus gefunden, den wir brauchen."

    scene command center 3670

    show bolt at half_size, left with dissolve
    
    b "Ah, da bist du ja, komm mein Junge. Wir haben Arbeit zu erledigen."

    show rex at half_size, right
    with dissolve
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


    b "Siehst du Rex, das Zeitfeld wirkt wie ein Schild um die Jahre 1999 und 2500. Wir haben
    aber rausgefunden, dass wir diese Barriere durchdringen können. Dafür müssen wir uns nur
    als Objekt dieser Zeit verkleiden und unsere wahre Zeitsignatur verbergen."

    b "Um es kurz zu machen: Wenn das Zeitfeld irgendwie deine wahre Zeitsignatur kennt, dann
    werden Sie gewaltsam in die Vergangenheit oder Zukunft geschleudert."

    b "Hier das wichtigste. Das Temporal Cloaking Device. Du musst nur diese Taste drücken,
    und auf 2024 einstellen. Die Zeitmaschine wird dich in das Jahr befördern und
    sich selbst tarnen"

    #Music missing

    scene time_machine_outside
    show rex at quater_size, left with dissolve

    r "Ist das?"    #Rex Soyface pointing 

    b "Ja, das ist es tatsächlich, ein Ort, den die meisten Menschen meiden, perfekt,
    um eine Zeitmaschine zu verstecken"

    r "Okay, los geht's! Basierend auf dem, was der Arzt gesagt hat, müssen wir nur
    die Zeit auswählen, die wir brauchen. Plus/Minus eine Woche. "

    r "Lass uns den 02.08.2024 daraus machen und dann müssen wir nur noch das Temporal
    Cloaking Device auf 2024 stellen, kurz bevor wir ankommen."

    b "Okay, Rex, alles sieht gut aus und scheint in Ordnung zu sein. Viel Glück bei deiner
    Mission und vergiss nicht, dein Tarngerät einzuschalten."  

    hide rex
    show rex_happy at half_size,left with dissolve 

    r "Wird gemacht, Doc!"

    x "Und damit verlässt Doctor Bolt Spiral die TM510 und Rex setzt seinen Weg fort."
    hide rex_happy

    scene timemachine 
    show rex at half_size,left 

    x "Etwa eine Stunde nach Beginn der Reise..."

    r "Sie haben viel Arbeit in dieses neue Modell gesteckt. Sie haben die Austattung definitiv
    verbessert. Ich könnte hier sogar..."

    r "...hier sogar"

    r "...schlafen"

    hide rex

    x "Und so kam es auch, Rex schlief während der Reise durch Raum und Zeit ein."

    #Alarmgeräusche

    x "Zielort nähert sich. Tarnvorrichtung akiviert!"

    show rex at half_size, right with dissolve

    r "Mist, ich muss eingeschlafen sein. Ich habe vergessen meine Tarnung zu aktivieren."
    
    r "Anscheinend gibt es aber eine automatische Funktion, danke Doc!"

    scene time_machine_outside_past_02
    show rex at right,tiny with dissolve

    r "Moment mal, der Doc hat diese Autofunktion nie erwähnt, ist die überhaupt sicher?"

    x "Rex drückt die Taste für die Tarnfunktion"

    x "Manuelle Übersteuerung erkannt! Tarnfunktion abgeschaltet. Zeitreise wird beendet."

    #Alarm Zeitmaschine, Absturz dieser

    #Bolt nur als Hologramm

    b "Was ist los, Rex? Ich empfange eine kritische Störung."

    r "Die Zeitmaschine ist abgestürzt!"

    b "Mit dir ist es immer ein Abenteuer oder? Bleib wo du bist. Ich werde den Schaden
    analysieren und sehen was ich tun kann."

    r "Naja wenigstens ist die Landschaft nicht schlecht. Sachsen, was? Ich war hier noch nie."

    r "Und was soll ich tun während ich warte?"

    b "Rex, ich hab gute und schlechte Neuigkeiten."

    b "Zuerst die schlechten. Es wird wohl eine Weile dauern, bis die Maschine repariert ist."

    b "Nimm bitte dein Kommunikationsgerät mit!"

    r "Und die guten Nachrichten?"

    b "Du befindest dich genau in der Mitte deines Ziels. Jetzt liegt es nur an ihnen,
    mehr über Heapsort zu lernen."

    r "Ok,Ok. Zuerst muss ich mir neue Kleidung suchen. Dieser Overall ist nicht besonders unaufällig. das wasser hilf auch nich dabei."

    b "Wasser ?"

    hide rex
    show rex_angry at right,tiny

    r "Ja , Wasser , ich bin auf einer Insel in einem Teich"

    b "Nun , mein vorschlag ist das schwimmen"

    r "wollte ich gerade tun !"

    hide rex_angry with dissolve

    x "Rex schwimmt durch den Teich und beginnt seine suche"

    #SCENE 4 :

    scene clothing_store

    show rex_angry at half_size , right with dissolve

    x "Rex betritt zitternd einen Kleidungsladen in seinem nassen Overall. Nervös sucht er nach passender und stylischer Kleidung."
    x  "Er stößt auf einen großen, imposanten Mann mit einem ordentlich gestutzten Bart und einer schwarzen Tweedjacke. Der Mann zieht eine Augenbraue hoch und mustert Rex von oben bis unten."
    hide rex_angry 
    show rex at half_size , right 
    show professor at half_size, left with dissolve
    p "Ich habe dich hier noch nie zuvor gesehen . Bist du einer der neuen Studenten?"
    r "Uh, Ja... sowas in die richtung."
    p "Haben wir us verlaufen? Keine Angst , das passiert selbst den besten. sag mal , das ist aber ein sehr interessantes outfit das du da trägst."
    hide professor
    x "Rexs Kommunikationsgerät fängt plötzlich an zu brummen . ein Hologram von Bolt erscheint."
    show bolt at half_size, left with dissolve
    b "Rex! das ist er , das ist der Professor!"
    $ name_p = "Professor"
    hide rex
    show rex_angry at half_size , right
    r  "Dok, nicht so laut!"
    b "Oh, richtig. Ahem. Folge ihm, Rex! Er ist der Schlüssel zum Heapsort wissen!"
    hide bolt
    show professor  at half_size, left with dissolve
    hide rex_angry
    show rex at half_size , right

    r  "Nett sie kennen zu lernen , aber ich muss jetzt los"
    x "Rex versucht ungeschickt dem Professor zu folgen."
    hide rex
    show rex_sithlord at half_size , right with dissolve
    p "Moment mal, Junge! Wozu die Eile?"

    hide rex_sithlord
    show rex at half_size , right with dissolve

    r "Ich .. uh.. "
    p  "falls du das 13.15 Seminar suchst kannst du mir einfach folgen ."

    r "roger roger!"

    p " Professor Black ist der Name. Remington Black."
    $ name_p = "Professor Black"


#Scene 5: Classroom shenanigans
    scene classroom
    show rex at half_size, left with dissolve
    show professor at half_size, right with dissolve


    x "Rex Folgt Professor Black in eine große vorlesungshalle voller gelangweilter Studenten."
    x "Rex setzt sich in der letzten reihe um unauffällig zu bleiben . Professor Black lauft energetisch zum pult und beginnt seine vorlesung."
    p "Guten morgen herren und damen! in der heutigen vorlesung befassen wir uns mit der spannenden welt der Algorithmen, Heapsort um genauer zu sein"
    x "Rex gähn und seine blick wandert duch den raum. Plötzlich ertönt Bolts stimme in seinem Ohr."
    hide professor with dissolve
    b "Rex! Aufpassen! Gleich kommt Heapsort!"
    show professor at half_size, right with dissolve
    x "Rex richtet sich abrupt auf und Fokusiert seinen Blick auf Black."
    p "Heapsort ist ein effizienter Algorithmus, der auf der Heap-Datenstruktur basiert..."
    x  "Professor Black beginnt, den Algorithmus im Detail zu erklären. Rex kritzelt wütend auf sein Tablet."
    b "Ja! Ja! Das ist der Schlüssel zur Reparatur von TM-510! Rex, mein Junge, hör gut zu und mach dir Notizen, wie du es schon unzählige Male getan hast, und komm zurück zu unserer guten alten Zeit..."
    r "...Doc? Doc!... Verdammt noch mal! Das muss das Wasser sein, das das Kommunikationsgerät stört!"

#explenation heapsort

    scene classroom
    show professor at right , half_size with dissolve

    p "Zunächst sollten wir klären, was ein Heap überhaupt ist."

    p "Ein Heap ist eine Art binärer Baum – eine Struktur, in der jeder Elternknoten zwei Kindknoten hat."

    p "Besonders interessant für uns ist der sogenannte Max-Heap."

    p "In einem Max-Heap gilt die Regel: Jeder Elternknoten ist größer als seine beiden Kindknoten. "

    p "Das bedeutet, dass der größte Wert im Baum immer an der Spitze – der Wurzel – zu finden ist. "

    p "Warum nutzen wir diesen Heap? Nun, die Max-Heap-Eigenschaft ermöglicht es uns, in jedem Schritt das größte verbleibende Element schnell zu finden. "

    p "Das ist der Schlüssel zu Heapsort. "

    show professor at left ,half_size with move

    p "Schauen wir uns die drei Schritte von Heapsort an. "

    p "Schritt 1: Aufbau eines Max-Heaps "
    p "Der erste Schritt besteht darin, das Eingabearray in einen Max-Heap umzuwandeln. Dafür verwenden wir eine Methode namens Heapify. "

    p "Stellen Sie sich vor, wir überprüfen jeden Knoten und stellen sicher, dass die Max-Heap-Eigenschaft erfüllt ist. "

    p "Falls ein Elternknoten kleiner ist als eines seiner Kinder, vertauschen wir die beiden und setzen die Überprüfung fort."

    p "Wir arbeiten uns dabei von unten nach oben durch den Baum. Warum? "

    p "Weil ein Problem bei den unteren Knoten sofort Auswirkungen auf die darüberliegenden hat. Indem wir von unten beginnen, stellen wir sicher, dass die Struktur stabil bleibt."
   
#schritt 2
    p "Schritt 2: Tauschen und Neuaufbau "
    p "Sobald wir einen Max-Heap haben, können wir mit dem Sortieren beginnen. "

    p "Das größte Element – das Wurzelelement – wird mit dem letzten Element des Arrays getauscht. "

    p "Dadurch bringen wir das größte Element an die richtige Position. "

    p "Aber Achtung: Nach dem Tausch ist die Max-Heap-Eigenschaft verletzt. Deshalb wenden wir Heapify erneut an, diesmal auf den verkleinerten Heap, um die Struktur zu reparieren. "


    p "Schritt 2: Tauschen und Neuaufbau "
    p "Sobald wir einen Max-Heap haben, können wir mit dem Sortieren beginnen. "

    p "Das größte Element – das Wurzelelement – wird mit dem letzten Element des Arrays getauscht. "

    p "Dadurch bringen wir das größte Element an die richtige Position. "

    p "Aber Achtung: Nach dem Tausch ist die Max-Heap-Eigenschaft verletzt. Deshalb wenden wir Heapify erneut an, diesmal auf den verkleinerten Heap, um die Struktur zu reparieren. "

#schritt 3
    p "Schritt 3: Wiederholen bis zur vollständigen Sortierung "
    p "Diesen Prozess – Tauschen, Reparieren und Verkleinern des Heaps – wiederholen wir so lange, bis alle Elemente sortiert sind. "

    p "Am Ende erhalten wir eine Liste in aufsteigender Reihenfolge. "

    p "Vielleicht fragen Sie sich, warum Heapsort eine gute Wahl ist. Nun, Heapsort hat im besten, durchschnittlichen und schlechtesten Fall eine Zeitkomplexität von O(n log n). "

    p "Das liegt daran, dass jeder Schritt – sei es der Aufbau des Heaps oder das Heapify – proportional zur Höhe des Baums arbeitet, was logarithmisch wächst. "

    p "Ein weiterer Vorteil von Heapsort ist, dass er nur eine konstante Menge an zusätzlichem Speicherplatz benötigt. "

    p "Der gesamte Sortiervorgang erfolgt direkt im Eingabearray. Dies nennt man in-situ-Sortierung, und es unterscheidet Heapsort von vielen anderen Algorithmen wie Mergesort. "

    p "Aber nichts ist perfekt. Heapsort hat auch Schwächen. "

    p "Eine davon ist, dass der Algorithmus nicht stabil ist. Das bedeutet, dass gleiche Werte ihre relative Reihenfolge verlieren können. "

    p "Außerdem ist Heapsort keine Divide-and-Conquer-Methode wie Quicksort oder Mergesort. "

    p "Statt das Array in kleinere Teile zu zerlegen, arbeiten wir direkt mit der Heap-Struktur. "

    p "Zusammengefasst: Heapsort basiert auf drei Schritten – dem Aufbau eines Max-Heaps, dem Tauschen des größten Elements und dem Wiederherstellen der Max-Heap-Eigenschaft, bis das Array vollständig sortiert ist. "

    p "Mit diesem Wissen sollten Sie in der Lage sein, Heapsort eigenständig zu implementieren und seine Effizienz zu verstehen. "

    p "Aber denken Sie daran, der Schlüssel liegt im Verständnis der Max-Heap-Eigenschaft und der korrekten Anwendung von Heapify. "





#Abschluss Monolog (Begleitete Simulation)


    show professor_happy at left ,half_size with move
    x "Professor Black schließt seine Vorlesung mit einem breiten Grinsen ab."
    p  "...und damit ist die heutige Vorlesung über Sortieralgorithmen beendet. "
    p  "Sie mögen jetzt nicht besonders nützlich erscheinen... "
    p  "aber du wirst den Tag erleben, an dem du dieses Wissen brauchst, "
    p  "sei es in deiner Programmierkarriere, beim Entwickeln von Programmen als Hobby... "
    p  "(mit einem subtilen Grinsen und einem Seitenblick auf Rex)... oder bei der Rettung der Menschheit."
    x "Professor Black verlässt den Vorlesungssaal, während die Studenten zusammenpacken, um zu gehen."


# Scene 6 : Heapsort to the rescue

    scene time_machine_outside_past
    show rex at tiny, right with dissolve
    # Rex stands before the TM-510
    r "Okay, der Doc hat gesagt, dass Heapsort der Schlüssel ist... mal sehen, ob ich das nicht herausfinden kann."
    x "Rex nähert sich der Zeitmaschine. Er legt seine Hand auf das Bedienfeld, das sich mit einem Zischen öffnet und eine schwindelerregende Anzahl von futuristisch aussehenden Schaltkreisen und Schalttafeln offenbart."
    x "Rexs Augen scannen die komplizierten Abläufe, bis sie auf einem Abschnitt mit der Aufschrift 'Manuelle Zeitfeld überbrückung' landen."
    r "Bingo. Sieht so aus, als würde hier die Magie passieren." 
    jump minigame
# jump to interactive heapsort from here
    #English Version------------------------------------------------


label E_start :
    scene black

    x "Knowledge rests not upon truth alone, but upon error also. - Carl Jung"

    x "Year 3670"
    x "Population {color=#f00}25%%{/color}"

    x "What was left of the humatity's greatest achievements were long-forgotten memories
    in rubble and ash."

    x "Some blamed the hubris of humans, thinking we could have it all only to realize the only 
    ones between us and everything we wanted was our kin."

    x "Others blamed the machines."

    x "Bearing the sins of those responsible for terrible weapons of mass destruction, mankind
    put their technologies to the fire."

    x "And in doing so, sealed the fate of mankind to live in a second dark age where pursuit of 
    knowledge is heresy."

    x "But in a tale as old as human history itself, there are those who renounce the grip of 
    ignorance on their neck."

    #cut to rex waking up from sleep in the Command Center 3670 due to an alarm

    scene command center 3670 # should we add an alarm here ? -E
    show rex at half_size , right with dissolve
    show bolt at half_size , left with dissolve
    r "What the hell? An alarm this early after yesterday's task? The doctor is absolutely on fire 
    this week"

    b "Rex to the command center, Rex to the command center. We've finally 
    tracked the information for the sorting algorithm we need."

    b "Ah, there you are, my boy. Come, we have work to do."

    r "Morning, Doc, I thought we've cracked sorting with the information you had me steal 
    yesterday from Goldsteine and von Neumann in 1948."

    b "That, rex, was a detailed description and analysis of Merge sort, what we need to find 
    here today, is Heapsort, one might say, a relative of Merge sort, yet unique in so many different ways."

    r "That’s cool and all Doc, but do we really need to understand all Sorting algorithms? 
    Isn't what we have now enough?"

    b "Rex my dear boy, The different Sorting Algorithms have their own practical functions. 
    Our good comrades down in provisions could use a better way of stacking the food 
    crates by their weight, hm?"

    r "I mean, I guess you're right Doc."

    b "Besides that’s what the Codex was built around, the retrieval of knowledge from our past despite what the 
    Elder Leaders want, to erase ignorance of our history and technology so that we may strive for a better future."

    r "Yeah, yeah, The Noble Vision."

    b "Rex my boy, For your next mission you will be transported back to 2024, specifically to a place called the 
    Estinien Applied University of Technology."

    r "Wait, the early 2000? But you said every moment in between 1999 and 2120 is a no go due to the temporal field 
    caused by the interference with the..."

    b "Yes yes, i know, the Spiral Temporal Field theory, its all my father could talk about, and the main reason why we're 
    left with scraps when it comes to learning about the basics of Informatics."

    b "But, look, due to your past excursions we think we’ve found a way with which to pierce the temporal field of the time."

    r " Yo, Hell yeah Doc, Science!"

    b "Yes Rex, Science, truly wonderful, isn't it."

    #in front of the time maschine

    scene time_machine_outside
    show rex at half_size , right with dissolve
    show bolt at half_size , left with dissolve
    b "You see rex, The Temporal field acts like a shield around the temporal space between 1999 and 2500, as you know. Well the way 
    we've found that might allow us through this field is to disguise yourself as an object from that time, 
    masking our true Temporal Signature."

    r "And what would happen if it knows our true Temporal Signature doc?"

    b "well, think of it like this, what would happen if you were to somehow change the magnetic field of a positively charged magnet 
    to negative while its sticking to another negatively charged magnet?"

    b " in short, if the Temporal Field somehow knows that your and the time machine's true Temporal Signature, you'd be violently 
    flung into the past or future."

    scene timemachine
    show rex at half_size , right with dissolve
    show bolt at half_size , left with dissolve

    b "I'd like to Introduce you to TM-510, the 510th iteration of the Time Machine."

    b "In here rex, you can see the controls of the time machine. But as that's the 
    basic controls that you already know anyway i won't explain too much"

    b "The most important thing is here, the Temporal Cloaking Device, It is currently deactivated but all you need to do is press 
    this button and set this to “2024” and it would change your temporal signature to 2024 while also changing the outward appearance 
    of the time machine to look like something from its time."

    scene time_machine_outside
    show rex at half_size , right with dissolve
    show bolt at half_size , left with dissolve

    r "Is that?"

    b "Bolt: Yes, indeed it is, a place where people avoid most of the time, 
    perfect to disguise a time machine."

    scene timemachine
    show rex at half_size , right with dissolve
    show bolt at half_size , left with dissolve

    r "Alright, lets get going. Based on what the doc said, all we gotta do is 
    to select the time we are going to give or take a week."

    r "Let's make that 02.08.2024 and then all we have to do is to set the 
    Temporal Cloaking Device to 2024 too right before we arrive."

    b "Okay rex, all looks good, and everything seems to be in order. Good luck on your mission and remember, don't 
    forget to turn your Temporal Cloaking Device a bit of time before entering the Spiral Temporal Field."

    r "Will do, Doc!"

    x "And with that, Doctor Bolt Spiral departs the TM510 and Rex goes on his way."

    x "Around an hour into the journey..."

    r "They did a lot of work on this new model of the Time Machine, They certainly upgraded the amenities, 
    I mean, it's so comfortable, i might..."

    r "even be able to..."

    r "to sleep...here..."

    x "Approaching Spiral Temporal Field! Warning! Warning! Cloaking Device Engaged!"

    r "OH NO, i must've fallen asleep and forgot to turn on the Cloaking Device, Thank god 
    for the auto Cloak function!"

    r "Wait a minute... the professor never mentioned an auto-function! Is this even safe?"

    r "Eh, better safe than sorry."

    x "Warning! Manual override detected. Shutting down the cloak function. Terminating time travel."

    b "Rex! What's happening? I'm picking up a critical malfunction!"

    r "Doc? Yeah, we've got a bit of a situation here. Seems I accidentally turned off the cloak thingy, 
    and we had a rough landing. The Time Machine's busted."

    b "Rex, Rex... Always an adventure with you, isn't it? Stay put, I'll analyze 
    the damage and see what I can do."

    r "Well, at least the scenery's not bad. Saxony, huh? Never been here before."

    r "Now, what to do while I wait..."

    b "Rex, I have good news and bad news."

    r "Hit me with it, Doc."

    b "Bad news first. It's going to take a while to figure out how to fix TM-510 remotely. 
    You'll need to bring your comms device with you."

    r "Explore? But I don't know where I am!"

    b "hat's the good news, my dear boy! You're smack dab in the middle of our destination, 
    chronologically speaking. Now it's up to you to find where."

    r "Alright, alright. But first, I need to find some clothes. This jumpsuit isn't exactly going to blend in….. Not to mention the water."

    b "Water?"

    r "Yes, Water. I landed on an island… in a lake."

    b "Well, then, I suppose you better start swimming"

    r "I was about to!"

    x "Rex then reluctantly swims across the lake to begin his search."

    #SCENE 4 :

    scene clothing_store

    show rex at half_size , right with dissolve

    x "Rex, shivering slightly in his damp jumpsuit, steps into a clothing store. He awkwardly browses the racks, trying to find something that fits both the current fashion and his unusual physique."
    x "He bumps into a tall, imposing man with a neatly trimmed beard and a black tweed jacket. The man raises an eyebrow, looking Rex up and down."
    show professor at half_size, left with dissolve
    p "Well, well, haven't seen you around here before. You one of the new students?"
    r "Uh, yeah... something like that."
    p "Bit lost, are we? Don't worry, happens to the best of us. Say, that's quite the... interesting outfit you've got there."
    hide professor
    x "Rex's comms device suddenly starts buzzing. A holographic image of Bolt pops up."
    show bolt at half_size, left with dissolve
    b "Rex! That's him! That's the professor!"
    $ name_p = "Professor"
    r  "Doc, not so loud!"
    b "Oh, right. Ahem. Follow him, Rex! He's the key to Heapsort knowledge!"
    hide bolt
    show professor  at half_size, left with dissolve

    r  "Well, uh, nice to meet you, Professor... I, uh, gotta run!"
    x "Rex clumsily tries to follow the professor."
    p "Hold on there, Buster! What's the rush?"

    r "I.. uh.. "
    p  "if you’re lost for the 13.15 seminar, then you’ve met the right person, come."

    r "Aye aye, sir!"

    p "That’s Professor Black to you. Remington Black."
    $ name_p = "Professor Black"


#Scene 5: Classroom shenanigans
    scene classroom
    show rex at half_size, left with dissolve
    show professor at half_size, right with dissolve


    x "Rex follows Professor Black into a large lecture hall, packed with students who are tapping away on their tablets, looking bored. Rex slides into a seat in the back row, trying to blend in. Professor Black strides energetically to the lectern and begins his lecture in a booming voice."
    p "Good morning, ladies and gentlemen! Today, we'll be delving into the fascinating world of sorting algorithms..."
    x "Rex yawns and lets his gaze wander around the room. Suddenly, Bolt's voice rings in his ear."
    hide professor with dissolve
    b "Rex! Pay attention! Here comes Heapsort!"
    show professor at half_size, right with dissolve
    x "Rex sits up abruptly and fixes Professor Black with a focused stare."

#heapsort explain here

    scene classroom

    show professor at right , half_size with dissolve

    p "Heapsort is an efficient, comparison-based sorting algorithm that helps us organise a list of numbers in ascending order."
    p "It is based on a special data structure, the so-called heap, and thus differs from other algorithms such as Quicksort or Mergesort."
    p "First, let's clarify what a heap actually is and how it works."

    show professor at left ,half_size with move

    show rex at right, half_size with dissolve

    r "[name_p], What exactly is a heap? I've heard the term before, but what does such a structure actually look like?"

    p "Good question, Rex! A heap is a special type of binary tree that maintains a fixed structure: each parent node is larger than its child nodes. This means that the largest value in the tree is always at the top, at the root."
    p "We call this structure a max heap. This is important because we use exactly this max heap property when heapsorting to identify the largest element in the tree and to put it in the correct place in the array."
    p  "Got it?"

    show rex at right ,half_size with dissolve

    r "Yes, that helps! But how exactly can we use this heap for sorting?"

    p "Very good question! The max heap gives us the opportunity to quickly find the largest remaining element at each step and place it in the correct position in the array."
    p "I'll explain the process of the heapsort algorithm step by step so that you can see how it works."

    show rex at right , half_size with vpunch

    p "Step 1: Construct the max heaps."
    p "The first step in heapsort is to convert the input array – that is, the list of numbers to be sorted – into a max heap."
    p  "This means that we arrange the elements so that the largest value is at the root and the max heap property applies to all parent-child relationships."

    r  "And how exactly do we do that? Isn't it costly?"

    p  "Good observation, Rex! To convert the array to a max heap, we use a method called “heapify”. The heapify procedure checks each node and ensures that the max heap property is satisfied for that node and its children."
    p  "We work our way up through the tree from the bottom, starting with the nodes that have children, and gradually move towards the root. This enables us to guarantee the max heap property for the entire tree without resorting to a complete reordering."

# Visualisierung Anzeigen (ungeordneter Heap)
    p "Here you can see an example of an array before the heapify process. The numbers are still in disorder."
    p "After the heapify process, however, the tree looks like this:"
#Visualisierung Anzeigen (geordneter Heap)
    show rex at right ,half_size with vpunch
    r  "Okay, now I understand what the max heap looks like! But what do we do with it?"

    p  "Very good, Rex. That brings us to step 2."
    p "Step 2: Swap and rebuild."

    p "Since the largest value is now at the root, we swap it with the last element of the array."
    p "This is how we bring the largest element to the correct position in the array."
    p "After we have made this swap, we reduce the size of the heap by one, because the largest element is now sorted and firmly in its position."

    r  "And what happens to the heap then? Isn't it broken then?"

    p  "Exactly, Rex! After the swap, the max heap property may actually be violated. Therefore, we reapply the heapify procedure to the root to repair the heap and ensure that the max heap property is restored."

#Visualisierung Anzeigen (Heapify vorher)
    p "Here we swap the root element with the last element."
    p "Since the max heap property has been violated, we apply Heapify to the root node to repair the structure."
#Visualisierung Anzeigen(Heapify nachher)

    p "After rerunning Heapify, the heap looks correct again and we can continue to the next step."
    p "Step 3: Repeat until the entire array is sorted."
    p "We repeat the process – swapping the root element with the last element, reducing the heap size and applying Heapify to the root – until the entire array is sorted."
    p "At the end, the array is completely sorted, and we have arranged the numbers in ascending order."
#Visualisierung Anzeigen (vollständige Sortierung der Liste)
    r  "Wow, that's really clever! But why is Heapsort so efficient?"

    p  "Good question, Rex! The heapsort algorithm has a time complexity of O(n log n) in the best, average and worst case, which means that it remains efficient even with large amounts of data."
    p  "Unlike some other algorithms, Heapsort also only requires a constant amount of additional memory, since the entire sorting process is carried out directly in the input array. This is called in-situ sorting."

    r  "That sounds pretty useful! Are there any disadvantages compared to other algorithms?"

    p  "Yes, indeed. One disadvantage of heapsort is that it does not provide stable sorting. This means that equal values can lose their relative order in the array."
    p  "Furthermore, heapsort is not a divide-and-conquer method like quicksort or mergesort. Heapsort does not divide the array into smaller parts, but works by continuously restoring the heap structure to achieve the sorting."

#Abschluss Monolog (Begleitete Simulation) Syncing....

    
    x "Professor Black begins to explain the algorithm in detail. Rex scribbles furiously on his tablet."
    b "Yes! Yes! This is the key to fixing TM-510! Rex, my boy, listen carefully and take notes like you've done countless times before, and get back to our good old time ma-" 
    r "...Doc? Doc!... Dammit! Must be the water messing with the comms device!"
    x "Professor Black wraps up his lecture with a broad grin."
    p "...and that concludes today's lecture on sorting algorithms. They may not seem particularly useful now... but you'll see the day when you need this knowledge, whether it be in your programming career, developing programs as a hobby (with a subtle smirk and a side glance at Rex)... or saving humanity."
    x "Professor Black exits the lecture hall as the students start packing up to leave."


# Scene 6 : Heapsort to the rescue

    scene time_machine_outside_past
    show rex at half_size, right with dissolve
    # Rex stands before the TM-510
    r "Okay, Doc mentioned something about Heapsort being the key...let me see if I can't figure that out."  
    x "Rex approaches the Time Machine. He places his hand on the control panel, and it slides open with a hiss, revealing a dizzying array of futuristic-looking circuits and panels."
    x "Rex's eyes scan the intricate workings until they land on a section labeled 'Manual Temporal Field Override'."
    r "Bingo. Looks like this is where the magic happens." 
    jump minigame



    # Scene 7 : Too far into the future


#Jahr 5000. Die Zeitmaschine landet in einer verwüsteten Landschaft. Rex steigt aus und sieht gigantische Maschinen und eine unheimlich stille Umgebung.

#Rex Purplewoman: (erschrocken) "Was… was ist hier passiert? Das ist nicht 3670!"

#TM-510 (Automatische Stimme): "Fehler bei der Zielzeit. Angekommen: Jahr 5000."

#Bolt Spiral: (erscheint als Hologramm) "Rex, was hast du getan?! Du bist zu weit in die Zukunft gereist! Unsere Berechnungen zeigen, dass die Menschheit in dieser Zeit vollständig durch Maschinen ersetzt wurde."

#Rex Purplewoman: "Das kann nicht wahr sein. Alles ist… so leer. Und diese Maschinen, sie sehen aus, als wären sie lebendig."

#(Plötzlich beginnt eine der Maschinen sich zu bewegen und nähert sich Rex.)

#TM-510: "Warnung: Unbekannte Entität erkannt. Empfehle sofortige Rückkehr zur Zeitmaschine."

#Bolt Spiral: "Rex, du musst sofort die Zeitmaschine reaktivieren! Die Maschinen in dieser Zeit könnten feindlich sein!"

#Rex Purplewoman: (rennt zurück zur Zeitmaschine) "Ich hasse es, wenn du recht hast, Doc! Los geht's, TM-510, bring mich hier raus!"

    #Scene 7: Too Far back in the past

#Jahr 65 Millionen v. Chr. Die Zeitmaschine landet in einem dichten Dschungel. Rex tritt vorsichtig heraus und hört seltsame Geräusche.

#Rex Purplewoman: (sich umblickend) "Okay, das hier sieht definitiv nicht nach Sachsen aus. Oder nach 3670. Wo bin ich?!"

#TM-510 (Automatische Stimme): "Fehler bei der Zielzeit. Angekommen: Jahr 65.000.000 v. Chr."

#Rex Purplewoman: (panisch) "Was?! Das ist die Kreidezeit! Ich bin bei den Dinosauriern gelandet!"

#(Ein lautes Brüllen ertönt in der Ferne, und der Boden bebt leicht.)

#Bolt Spiral: (erscheint als Hologramm) "Rex! Was hast du gemacht?! Du bist in der Kreidezeit! Wir haben keine Daten darüber, wie lange du hier sicher bleiben kannst!"

#Rex Purplewoman: (nervös) "Oh, keine Sorge, Doc, ich bin sicher, die Dinosaurier sind freundlich. Oder… auch nicht?"

#(Ein riesiger Tyrannosaurus Rex tritt in Sichtweite und richtet seinen Blick auf Rex.)

#Bolt Spiral: "Rex, steig sofort zurück in die Zeitmaschine! Und vergiss nicht, die Koordinaten zu korrigieren!"

#Rex Purplewoman: (rennt zur Zeitmaschine) "Wusste ich doch, dass das schiefgeht! TM-510, bring mich hier raus, bevor ich auf der Speisekarte lande!"

#(Die Zeitmaschine startet im letzten Moment, und der T-Rex bleibt verwirrt zurück.)



#Scene 8: Happy Ending



#Die Zeitreise hat geklappt (Zurück in die richtige Zeit)

#Szene: Ankunft in der Kommandozentrale im Jahr 3670. Rex steigt aus der Zeitmaschine aus.

#Bolt Spiral: "Rex! Du hast es geschafft! Die TM-510 zeigt die korrekten Koordinaten an – willkommen zurück in 3670."

#Rex Purplewoman: (springt erleichtert aus der Zeitmaschine) "Puh, ich dachte, das würde schiefgehen. Aber hey, Heapsort hat mich gerettet!"



# Scene 7 : Too far into the future


#Jahr 5000. Die Zeitmaschine landet in einer verwüsteten Landschaft. Rex steigt aus und sieht gigantische Maschinen und eine unheimlich stille Umgebung.

#Rex Purplewoman: (erschrocken) "Was… was ist hier passiert? Das ist nicht 3670!"

#TM-510 (Automatische Stimme): "Fehler bei der Zielzeit. Angekommen: Jahr 5000."

#Bolt Spiral: (erscheint als Hologramm) "Rex, was hast du getan?! Du bist zu weit in die Zukunft gereist! Unsere Berechnungen zeigen, dass die Menschheit in dieser Zeit vollständig durch Maschinen ersetzt wurde."

#Rex Purplewoman: "Das kann nicht wahr sein. Alles ist… so leer. Und diese Maschinen, sie sehen aus, als wären sie lebendig."

#(Plötzlich beginnt eine der Maschinen sich zu bewegen und nähert sich Rex.)

#TM-510: "Warnung: Unbekannte Entität erkannt. Empfehle sofortige Rückkehr zur Zeitmaschine."

#Bolt Spiral: "Rex, du musst sofort die Zeitmaschine reaktivieren! Die Maschinen in dieser Zeit könnten feindlich sein!"

#Rex Purplewoman: (rennt zurück zur Zeitmaschine) "Ich hasse es, wenn du recht hast, Doc! Los geht's, TM-510, bring mich hier raus!"

    #Scene 7: Too Far back in the past

#Jahr 65 Millionen v. Chr. Die Zeitmaschine landet in einem dichten Dschungel. Rex tritt vorsichtig heraus und hört seltsame Geräusche.

#Rex Purplewoman: (sich umblickend) "Okay, das hier sieht definitiv nicht nach Sachsen aus. Oder nach 3670. Wo bin ich?!"

#TM-510 (Automatische Stimme): "Fehler bei der Zielzeit. Angekommen: Jahr 65.000.000 v. Chr."

#Rex Purplewoman: (panisch) "Was?! Das ist die Kreidezeit! Ich bin bei den Dinosauriern gelandet!"

#(Ein lautes Brüllen ertönt in der Ferne, und der Boden bebt leicht.)

#Bolt Spiral: (erscheint als Hologramm) "Rex! Was hast du gemacht?! Du bist in der Kreidezeit! Wir haben keine Daten darüber, wie lange du hier sicher bleiben kannst!"

#Rex Purplewoman: (nervös) "Oh, keine Sorge, Doc, ich bin sicher, die Dinosaurier sind freundlich. Oder… auch nicht?"

#(Ein riesiger Tyrannosaurus Rex tritt in Sichtweite und richtet seinen Blick auf Rex.)

#Bolt Spiral: "Rex, steig sofort zurück in die Zeitmaschine! Und vergiss nicht, die Koordinaten zu korrigieren!"

#Rex Purplewoman: (rennt zur Zeitmaschine) "Wusste ich doch, dass das schiefgeht! TM-510, bring mich hier raus, bevor ich auf der Speisekarte lande!"

#(Die Zeitmaschine startet im letzten Moment, und der T-Rex bleibt verwirrt zurück.)



#Scene 8: Happy Ending



#Die Zeitreise hat geklappt (Zurück in die richtige Zeit)

#Szene: Ankunft in der Kommandozentrale im Jahr 3670. Rex steigt aus der Zeitmaschine aus.

#Bolt Spiral: "Rex! Du hast es geschafft! Die TM-510 zeigt die korrekten Koordinaten an – willkommen zurück in 3670."

#Rex Purplewoman: (springt erleichtert aus der Zeitmaschine) "Puh, ich dachte, das würde schiefgehen. Aber hey, Heapsort hat mich gerettet!"



# Scene 7 : Too far into the future


#Jahr 5000. Die Zeitmaschine landet in einer verwüsteten Landschaft. Rex steigt aus und sieht gigantische Maschinen und eine unheimlich stille Umgebung.

#Rex Purplewoman: (erschrocken) "Was… was ist hier passiert? Das ist nicht 3670!"

#TM-510 (Automatische Stimme): "Fehler bei der Zielzeit. Angekommen: Jahr 5000."

#Bolt Spiral: (erscheint als Hologramm) "Rex, was hast du getan?! Du bist zu weit in die Zukunft gereist! Unsere Berechnungen zeigen, dass die Menschheit in dieser Zeit vollständig durch Maschinen ersetzt wurde."

#Rex Purplewoman: "Das kann nicht wahr sein. Alles ist… so leer. Und diese Maschinen, sie sehen aus, als wären sie lebendig."

#(Plötzlich beginnt eine der Maschinen sich zu bewegen und nähert sich Rex.)

#TM-510: "Warnung: Unbekannte Entität erkannt. Empfehle sofortige Rückkehr zur Zeitmaschine."

#Bolt Spiral: "Rex, du musst sofort die Zeitmaschine reaktivieren! Die Maschinen in dieser Zeit könnten feindlich sein!"

#Rex Purplewoman: (rennt zurück zur Zeitmaschine) "Ich hasse es, wenn du recht hast, Doc! Los geht's, TM-510, bring mich hier raus!"

    #Scene 7: Too Far back in the past

#Jahr 65 Millionen v. Chr. Die Zeitmaschine landet in einem dichten Dschungel. Rex tritt vorsichtig heraus und hört seltsame Geräusche.

#Rex Purplewoman: (sich umblickend) "Okay, das hier sieht definitiv nicht nach Sachsen aus. Oder nach 3670. Wo bin ich?!"

#TM-510 (Automatische Stimme): "Fehler bei der Zielzeit. Angekommen: Jahr 65.000.000 v. Chr."

#Rex Purplewoman: (panisch) "Was?! Das ist die Kreidezeit! Ich bin bei den Dinosauriern gelandet!"

#(Ein lautes Brüllen ertönt in der Ferne, und der Boden bebt leicht.)

#Bolt Spiral: (erscheint als Hologramm) "Rex! Was hast du gemacht?! Du bist in der Kreidezeit! Wir haben keine Daten darüber, wie lange du hier sicher bleiben kannst!"

#Rex Purplewoman: (nervös) "Oh, keine Sorge, Doc, ich bin sicher, die Dinosaurier sind freundlich. Oder… auch nicht?"

#(Ein riesiger Tyrannosaurus Rex tritt in Sichtweite und richtet seinen Blick auf Rex.)

#Bolt Spiral: "Rex, steig sofort zurück in die Zeitmaschine! Und vergiss nicht, die Koordinaten zu korrigieren!"

#Rex Purplewoman: (rennt zur Zeitmaschine) "Wusste ich doch, dass das schiefgeht! TM-510, bring mich hier raus, bevor ich auf der Speisekarte lande!"

#(Die Zeitmaschine startet im letzten Moment, und der T-Rex bleibt verwirrt zurück.)



#Scene 8: Happy Ending



#Die Zeitreise hat geklappt (Zurück in die richtige Zeit)

#Szene: Ankunft in der Kommandozentrale im Jahr 3670. Rex steigt aus der Zeitmaschine aus.

#Bolt Spiral: "Rex! Du hast es geschafft! Die TM-510 zeigt die korrekten Koordinaten an – willkommen zurück in 3670."

#Rex Purplewoman: (springt erleichtert aus der Zeitmaschine) "Puh, ich dachte, das würde schiefgehen. Aber hey, Heapsort hat mich gerettet!"




# Scene 7 : Too far into the future


#Jahr 5000. Die Zeitmaschine landet in einer verwüsteten Landschaft. Rex steigt aus und sieht gigantische Maschinen und eine unheimlich stille Umgebung.

#Rex Purplewoman: (erschrocken) "Was… was ist hier passiert? Das ist nicht 3670!"

#TM-510 (Automatische Stimme): "Fehler bei der Zielzeit. Angekommen: Jahr 5000."

#Bolt Spiral: (erscheint als Hologramm) "Rex, was hast du getan?! Du bist zu weit in die Zukunft gereist! Unsere Berechnungen zeigen, dass die Menschheit in dieser Zeit vollständig durch Maschinen ersetzt wurde."

#Rex Purplewoman: "Das kann nicht wahr sein. Alles ist… so leer. Und diese Maschinen, sie sehen aus, als wären sie lebendig."

#(Plötzlich beginnt eine der Maschinen sich zu bewegen und nähert sich Rex.)

#TM-510: "Warnung: Unbekannte Entität erkannt. Empfehle sofortige Rückkehr zur Zeitmaschine."

#Bolt Spiral: "Rex, du musst sofort die Zeitmaschine reaktivieren! Die Maschinen in dieser Zeit könnten feindlich sein!"

#Rex Purplewoman: (rennt zurück zur Zeitmaschine) "Ich hasse es, wenn du recht hast, Doc! Los geht's, TM-510, bring mich hier raus!"

    #Scene 7: Too Far back in the past

#Jahr 65 Millionen v. Chr. Die Zeitmaschine landet in einem dichten Dschungel. Rex tritt vorsichtig heraus und hört seltsame Geräusche.

#Rex Purplewoman: (sich umblickend) "Okay, das hier sieht definitiv nicht nach Sachsen aus. Oder nach 3670. Wo bin ich?!"

#TM-510 (Automatische Stimme): "Fehler bei der Zielzeit. Angekommen: Jahr 65.000.000 v. Chr."

#Rex Purplewoman: (panisch) "Was?! Das ist die Kreidezeit! Ich bin bei den Dinosauriern gelandet!"

#(Ein lautes Brüllen ertönt in der Ferne, und der Boden bebt leicht.)

#Bolt Spiral: (erscheint als Hologramm) "Rex! Was hast du gemacht?! Du bist in der Kreidezeit! Wir haben keine Daten darüber, wie lange du hier sicher bleiben kannst!"

#Rex Purplewoman: (nervös) "Oh, keine Sorge, Doc, ich bin sicher, die Dinosaurier sind freundlich. Oder… auch nicht?"

#(Ein riesiger Tyrannosaurus Rex tritt in Sichtweite und richtet seinen Blick auf Rex.)

#Bolt Spiral: "Rex, steig sofort zurück in die Zeitmaschine! Und vergiss nicht, die Koordinaten zu korrigieren!"

#Rex Purplewoman: (rennt zur Zeitmaschine) "Wusste ich doch, dass das schiefgeht! TM-510, bring mich hier raus, bevor ich auf der Speisekarte lande!"

#(Die Zeitmaschine startet im letzten Moment, und der T-Rex bleibt verwirrt zurück.)



#Scene 8: Happy Ending



#Die Zeitreise hat geklappt (Zurück in die richtige Zeit)

#Szene: Ankunft in der Kommandozentrale im Jahr 3670. Rex steigt aus der Zeitmaschine aus.

#Bolt Spiral: "Rex! Du hast es geschafft! Die TM-510 zeigt die korrekten Koordinaten an – willkommen zurück in 3670."

#Rex Purplewoman: (springt erleichtert aus der Zeitmaschine) "Puh, ich dachte, das würde schiefgehen. Aber hey, Heapsort hat mich gerettet!"


#Bolt Spiral: (lacht) "Heapsort und deine Fähigkeit, sich anzupassen. Das Wissen, das du zurückgebracht hast, wird der Schlüssel zur Wiederherstellung unseres Fortschritts sein."

#Rex Purplewoman: "Na ja, ich hatte meine Zweifel, ob ich das hinbekomme. Aber es hat sich gelohnt. Also, was jetzt?"

#Bolt Spiral: "Jetzt, mein Junge, werden wir das Wissen über Heapsort analysieren und in die Codex-Datenbank aufnehmen. Du hast Geschichte geschrieben, Rex!"

#Rex Purplewoman: "Ich? Ein Held? Na, wenn das so ist… können wir jetzt endlich eine Pause machen? Ich brauche ein Sandwich."

#Bolt Spiral: (lachend) "Natürlich. Aber mach dich darauf gefasst, dass die nächste Mission bald beginnt. Wissen ruht nie!"



label game_over:
    jump expression renpy.random.choice(("game_over_0","game_over_1"))

label game_over_0:
    scene game_over_future
# Scene 7 : Too far into the future
    show rex  at right , half_size with dissolve
    #Jahr 5000. Die Zeitmaschine landet in einer verwüsteten Landschaft. Rex steigt aus und sieht gigantische Maschinen und eine unheimlich stille Umgebung.

    r  "Was… was ist hier passiert? Das ist nicht 3670!"

    T   "Fehler bei der Zielzeit. Angekommen: Jahr 5000."

    show rex_sithlord  at right , half_size with dissolve

    b  "Rex, was hast du getan?! Du bist zu weit in die Zukunft gereist! Unsere Berechnungen zeigen, dass die Menschheit in dieser Zeit vollständig durch Maschinen ersetzt wurde."

    r "Das kann nicht wahr sein. Alles ist… so leer. Und diese Maschinen, sie sehen aus, als wären sie lebendig."

    x "(Plötzlich beginnt eine der Maschinen sich zu bewegen und nähert sich Rex.)"

    T "Warnung: Unbekannte Entität erkannt. Empfehle sofortige Rückkehr zur Zeitmaschine."

    b "Rex, du musst sofort die Zeitmaschine reaktivieren! Die Maschinen in dieser Zeit könnten feindlich sein!"

    r  "Ich hasse es, wenn du recht hast, Doc! Los geht's, TM-510, bring mich hier raus!"

return
label game_over_1:

#Scene 7: Too Far back in the past
    scene game_over_past
    show rex  at right , half_size with dissolve

    r"Okay, das hier sieht definitiv nicht nach Sachsen aus. Oder nach 3670. Wo bin ich?!"

    T "Fehler bei der Zielzeit. Angekommen: Jahr 65.000.000 v. Chr."

    r  "Was?! Das ist die Kreidezeit! Ich bin bei den Dinosauriern gelandet!"

    x   "(Ein lautes Brüllen ertönt in der Ferne, und der Boden bebt leicht.)"

    b "Rex! Was hast du gemacht?! Du bist in der Kreidezeit! Wir haben keine Daten darüber, wie lange du hier sicher bleiben kannst!"

    r "Oh, keine Sorge, Doc, ich bin sicher, die Dinosaurier sind freundlich. Oder… auch nicht?"

    x   "(Ein riesiger Tyrannosaurus Rex tritt in Sichtweite und richtet seinen Blick auf Rex.)"

    b   "Rex, steig sofort zurück in die Zeitmaschine! Und vergiss nicht, die Koordinaten zu korrigieren!"

    r   "Wusste ich doch, dass das schiefgeht! TM-510, bring mich hier raus, bevor ich auf der Speisekarte lande!"

    x   "(Die Zeitmaschine startet im letzten Moment, und der T-Rex bleibt verwirrt zurück.)"

return

#Scene 8: Happy Ending

label victory :

    x "Die Zeitreise hat geklappt "
    scene command center 3670
    show rex at right , half_size with dissolve

    b  "Rex! Du hast es geschafft! Die TM-510 zeigt die korrekten Koordinaten an – willkommen zurück in 3670."

    x "Rex (springt erleichtert aus der Zeitmaschine)"
    r "Puh, ich dachte, das würde schiefgehen. Aber hey, Heapsort hat mich gerettet!"

    b  "Heapsort und deine Fähigkeit, sich anzupassen. Das Wissen, das du zurückgebracht hast, wird der Schlüssel zur Wiederherstellung unseres Fortschritts sein."

    r "Na ja, ich hatte meine Zweifel, ob ich das hinbekomme. Aber es hat sich gelohnt. Also, was jetzt?"

    b "Jetzt, mein Junge, werden wir das Wissen über Heapsort analysieren und in die Codex-Datenbank aufnehmen. Du hast Geschichte geschrieben, Rex!"

    r "Ich? Ein Held? Na, wenn das so ist… können wir jetzt endlich eine Pause machen? Ich brauche ein Sandwich."

    b "Natürlich. Aber mach dich darauf gefasst, dass die nächste Mission bald beginnt. Wissen ruht nie!"

    return
    #Scene 7: Too Far back in the past

#Jahr 65 Millionen v. Chr. Die Zeitmaschine landet in einem dichten Dschungel. Rex tritt vorsichtig heraus und hört seltsame Geräusche.

#Rex Purplewoman: (sich umblickend) "Okay, das hier sieht definitiv nicht nach Sachsen aus. Oder nach 3670. Wo bin ich?!"

#TM-510 (Automatische Stimme): "Fehler bei der Zielzeit. Angekommen: Jahr 65.000.000 v. Chr."

#Rex Purplewoman: (panisch) "Was?! Das ist die Kreidezeit! Ich bin bei den Dinosauriern gelandet!"

#(Ein lautes Brüllen ertönt in der Ferne, und der Boden bebt leicht.)

#Bolt Spiral: (erscheint als Hologramm) "Rex! Was hast du gemacht?! Du bist in der Kreidezeit! Wir haben keine Daten darüber, wie lange du hier sicher bleiben kannst!"

#Rex Purplewoman: (nervös) "Oh, keine Sorge, Doc, ich bin sicher, die Dinosaurier sind freundlich. Oder… auch nicht?"

#(Ein riesiger Tyrannosaurus Rex tritt in Sichtweite und richtet seinen Blick auf Rex.)

#Bolt Spiral: "Rex, steig sofort zurück in die Zeitmaschine! Und vergiss nicht, die Koordinaten zu korrigieren!"

#Rex Purplewoman: (rennt zur Zeitmaschine) "Wusste ich doch, dass das schiefgeht! TM-510, bring mich hier raus, bevor ich auf der Speisekarte lande!"

#(Die Zeitmaschine startet im letzten Moment, und der T-Rex bleibt verwirrt zurück.)


label minigame:
    show rex
    scene time_machine_outside_past_02 #time machine outside 2024
    r "auf nach Hause"
    scene timemachine #time machine inside scene
    # boom sound effect
    scene timemachine02_alarm
    r "um... Bolt, du solltest dir das mal anschauen"
    b "mein Gott... der Heapsortinator ist kaputt , du musst ihn reparieren"
    r "dann muss ich wohl den Heapsortinator überprüfen "
    b "sortiere es mit Maxheap !"


    scene mg1 #minigame scrambled
    b "Setze die Zahlen auf einen Heap-Baum!"
    scene mg2 #minigame heaptree
    b "Gut , danach noch das Heapify"
    label mg1:
        scene mg70
        call lifecount2 from _call_lifecount2
        menu:
            "6 to 7":
                scene mg67
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg1
                else: 
                    jump game_over
            #"1 to 3":
                #scene mg13_n #minigame heaptree 1 to 3
                #play explosion sound effect

            #"1 to 3":
                #scene mg13_n #minigame heaptree 1 to 3
                #play explosion sound effect
                #b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                #$ life_counter1 -= 1
                #if life_counter1 > 0:
                #    jump mg1
                #else: 
                #    jump game_over

            "7 to 0":
                scene mg70_n #minigame heaptree 7 to 0
                #play correct ding"
                b "Das klappt !"
                jump mg2

            "Es sieht schon korrekt aus.":
                #play explosion sound effect

                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg1
                else: 
                    jump game_over

            #"1 to 3":
                #scene mg13_n #minigame heaptree 1 to 3
                #play explosion sound effect
                #b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                #$ life_counter1 -= 1
                #if life_counter1 > 0:
                #    jump mg1
                #else: 
                #    jump game_over


            "7 to 0":
                scene mg70_n #minigame heaptree 7 to 0
                #play correct ding"
                b "Das klappt !"
                jump mg2

            "Es sieht schon korrekt aus.":
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg1
                else: 
                    jump game_over

    return

    label mg2:
        call lifecount2 from _call_lifecount2_1
        b "Und dann ... ?"

        menu:
            "6 to 7":

                #scene mg76_n #minigame heaptree 7 to 6

                scene mg67 #minigame heaptree 6 to 7


                scene mg67 #minigame heaptree 6 to 7

                scene mg67 #minigame heaptree 6 to 7

                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg2
                else: 
                    jump game_over
    

            "3 to 1":
                #scene mg31_n #minigame heaptree 3 to 1
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg2
                else: 
                    jump game_over

            #"3 to 1":
            #    scene mg31 #minigame heaptree 3 to 1
            #    #play explosion sound effect
            #   b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
            #    $ life_counter1 -= 1
            #    if life_counter1 > 0:
            #        jump mg2
            #    else: 
            #        jump game_over


            "3 to 7":
                scene mg37_n #minigame heaptree 3 to 7
                #play correct ding"
                b "Das klappt !"
                jump mg3

            "Es sieht schon korrekt aus.":
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg2
                else:
                    jump game_over
    return

    label mg3:
        call lifecount2 from _call_lifecount2_2
        b "Und dann ... ?"

        menu:

            #"3 to 0":
                #scene mg03_n #minigame heaptree 0 to 3

            "6 to 3":
                scene mg63_n #minigame heaptree 6 to 3
                #play correct ding"
                b "Das klappt !"
                jump mg4

            "3 to 0":
                scene mg03 #minigame heaptree 0 to 3

                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg3
                else: 
                    jump game_over
    
            " 1 to 7":

                #scene mg17_n #minigame heaptree 1 to 7

                scene mg17 #minigame heaptree 1 to 7

                scene mg17 #minigame heaptree 1 to 7

                scene mg17 #minigame heaptree 1 to 7

                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg3
                else: 
                    jump game_over


            "6 to 3":
                scene mg63_n #minigame heaptree 6 to 3
                #play correct ding"
                b "Das klappt !"
                jump mg4

            "Es sieht schon korrekt aus.":
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg3
                else: 
                    jump game_over

    return

    label mg4:
        call lifecount2 from _call_lifecount2_3
        b "Und dann ... ?"

        menu:
            "1 to 7":

                #scene mg17 #minigame heaptree 1 to 7
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg4
                else: 
                    jump game_over
    
            "3 to 6":
                #scene mg36 #minigame heaptree 3 to 6
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg4
                else: 
                    jump game_over

            "0 to 7":
                scene mg07_n #minigame heaptree 0 to 7
                b "Das klappt !"
                jump mg5   

            "Es sieht schon korrekt aus.":
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg4
                else: 
                    jump game_over          
    return

    label mg5:
        call lifecount2 from _call_lifecount2_4
        b "Und dann ... ?"
        menu:
            "0 to 1":
                #scene mg01w #minigame heaptree 1 to 0
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg5
                else: 
                    jump game_over
    
            "7 to 6":
                #scene mg76_n #minigame heaptree 7 to 6
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg5
                else: 
                    jump game_over

            "0 to 6":
                scene mg06_n #minigame heaptree 0 to 6
                b "Das klappt !"
                jump mg6   

            "Es sieht schon korrekt aus.":
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg5
                else: 
                    jump game_over          
    return

    label mg6:
        call lifecount2 from _call_lifecount2_5
        b "Und dann ... ?"
        menu:
            "7 to 0":
                #scene mg70w #minigame heaptree 1 to 0
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg6
                else: 
                    jump game_over
    
            "1 to 6":
                #scene mg16w #minigame heaptree 7 to 6
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg6
                else: 
                    jump game_over

            "0 to 3":
                scene mg03_n #minigame heaptree 0 to 3
                b "Das klappt !"
                jump mg7   

            "Es sieht schon korrekt aus.":
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg6
                else: 
                    jump game_over          
    return

    label mg7:
        call lifecount2 from _call_lifecount2_6
        b "Und dann ... ?"
        menu:
            "1 to 6":
                #scene mg16_n #minigame heaptree 1 to 6
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg7
                else: 
                    jump game_over
    
            "7 to 3":
                #scene mg73_n #minigame heaptree 3 to 7
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg7
                else: 
                    jump game_over

            "0 to 6":
                scene mg062_n #minigame heaptree 0 to 
                b "Das klappt !"
                jump mg8   

            "Es sieht schon korrekt aus.":
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg7
                else: 
                    jump game_over          
    return

    label mg8:
        call lifecount2 from _call_lifecount2_7
        b "Und dann ... ?"
        menu:
            "1 to 0":
                #scene mg10_n #minigame heaptree 1 to 0
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg8
                else: 
                    jump game_over
    
            "6 to 1":
                #scene mg61_n #minigame heaptree 6 to 1
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg8
                else: 
                    jump game_over

            "0 to 3":
                scene mg032_n #minigame heaptree 0 to 
                b "Das klappt !"
                jump mg9   

            "Es sieht schon korrekt aus.":
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg8
                else: 
                    jump game_over          
    return

    label mg9:
        call lifecount2 from _call_lifecount2_8
        b "Und dann ... ?"
        menu:
            "6 to 0":
                #scene mg60w #minigame heaptree 1 to 0
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg9
                else: 
                    jump game_over
    
            "7 to 0":
                #scene mg70w2 #minigame heaptree 7 to 6
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg9
                else: 
                    jump game_over

            "1 to 3":
                scene mg13_n #minigame heaptree 0 to 
                b "Das klappt !"
                jump mg10   

            "Es sieht schon korrekt aus.":
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg5
                else: 
                    jump game_over          
    return

    label mg10:
        call lifecount2 from _call_lifecount2_9
        b "Und dann ... ?"
        menu:
            "6 to 7":
                #scene mg67w2 #minigame heaptree 1 to 0
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg10
                else: 
                    jump game_over
    
            "3 to 1":
                #scene mg31w #minigame heaptree 7 to 6
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg10
                else: 
                    jump game_over

            "0 to 1":
                scene mg01_n #minigame heaptree 0 to 
                b "Das klappt !"
                jump mg11   

            "Es sieht schon korrekt aus.":
                #play explosion sound effect
                b "Ich glaube, das ist nicht ganz richtig, Junge. Versuch es noch einmal"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg10
                else: 
                    jump game_over          
    return

    label mg11:
        call lifecount2 from _call_lifecount2_10
        r "Das korrekte Arry ist ..."
        menu:
            "7, 6, 3, 1, 0":
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg11
                else: 
                    jump game_over
    
            "6, 1, 0, 3, 7":
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg11
                else: 
                    jump game_over

            "0, 1, 3, 6, 7":
                jump victory   

            "7, 6, 1, 3, 0":
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg11
                else: 
                    jump game_over          
    return

    label lifecount2:
            if life_counter1 == 3:
                show three at right with dissolve
            elif life_counter1 == 2:
                show two at right with dissolve
            elif life_counter1 == 1:
                show one at right with dissolve
            else:
                show zero at right with dissolve
            return


    return