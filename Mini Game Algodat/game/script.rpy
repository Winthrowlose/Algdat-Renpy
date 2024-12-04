# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rex")
define b = Character("Bolt")
default life_counter1 = 3


# The game starts here.

label start:
    show rex
    scene tmnow #time machine outside 2024
    r "lets go home"
    scene timemachine01 #time machine inside scene
    # boom sound effect
    scene timemachine02 
    r "um... bolt, you might want to take a loot at this"
    b "great scotts... the heapsortinator is broken, you have to fix it"
    r "cringe but ok"
    r "i guess i gotta look on the heapsortinator"
    b "sort it based on max heap"

    label mg1:
        call lifecount2
        scene mg1 #minigame scrambled
        b "put the stuff on a heaptree"
        scene mg2 #minigame heaptree
        b "now do the steps for heapify"

        menu:
            "6 to 0":
                scene mg60 #minigame heaptree 6 to 0
                #play explosion sound effect
                b "i don't think that's right, careful now"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg1
                else: 
                    jump game_over
    
            "1 to 3":
                scene mg13 #minigame heaptree 1 to 3
                #play explosion sound effect
                b "i don't think that's right, careful now"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg1
                else: 
                    jump game_over

            "7 to 0":
                scene mg70 #minigame heaptree 7 to 0
                #play correct ding"
                b "that seems right me boi"
                jump mg2

            "This seems correct already":
                #play explosion sound effect
                b "i don't think that's right, careful now"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg1
                else: 
                    jump game_over
    return

    label mg2:
        call lifecount2
        b "what's next"

        menu:
            "6 to 7":
                scene mg76 #minigame heaptree 7 to 6
                #play explosion sound effect
                b "i don't think that's right, careful now"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg2
                else: 
                    jump game_over
    
            "3 to 1":
                scene mg31 #minigame heaptree 3 to 1
                #play explosion sound effect
                b "i don't think that's right, careful now"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg2
                else: 
                    jump game_over

            "3 to 7":
                scene mg37 #minigame heaptree 3 to 7
                #play correct ding"
                b "that seems right me boi"
                jump mg3

            "This seems correct already":
                #play explosion sound effect
                b "i don't think that's right, careful now"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg2
                else:
                    jump game_over
    return

    label mg3:
        call lifecount2
        b "what's next"

        menu:
            "3 to 0":
                scene mg03 #minigame heaptree 0 to 3
                #play explosion sound effect
                b "i don't think that's right, careful now"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg3
                else: 
                    jump game_over
    
            " 1 to 7":
                scene mg31 #minigame heaptree 1 to 7
                #play explosion sound effect
                b "i don't think that's right, careful now"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg3
                else: 
                    jump game_over

            "6 to 3":
                scene mg63 #minigame heaptree 6 to 3
                #play correct ding"
                b "that seems right me boi"
                jump mg4

            "This seems correct already":
                #play explosion sound effect
                b "i don't think that's right, careful now"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg3
                else: 
                    jump game_over
    return

    label mg4:
        call lifecount2
        b "what's next"

        menu:
            "1 to 7":
                scene mg17 #minigame heaptree 1 to 7
                #play explosion sound effect
                b "i don't think that's right, careful now"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg4
                else: 
                    jump game_over
    
            "3 to 6":
                scene mg36 #minigame heaptree 3 to 6
                #play explosion sound effect
                b "i don't think that's right, careful now"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg4
                else: 
                    jump game_over

            "6 to 7":
                #play explosion sound effect
                scene mg67 #minigame heaptree 6 to 7
                b "i don't think that's right, careful now"
                $ life_counter1 -= 1
                if life_counter1 > 0:
                    jump mg4
                else: 
                    jump game_over

            "This seems correct already":
                #play correct ding"
                b "that seems right me boi"
                jump victory        
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

    label victory:
        b "it works"
        r "i'm home"


    return
