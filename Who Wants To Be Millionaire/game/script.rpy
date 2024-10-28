# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Contestant", color="#03f0fc")
define a = Character("Announcer", color="#bbc400")
default life_counter = 3
# The game starts here.

label start:


    scene milstart
    
    a "Welcome, everyone, to Information is Money! The game where knowledge is power... and that power turns into cash!"

    show announcer at right with dissolve

    a "Tonight, our contestants will face a mountain of questions, each one worth more than the last"
    a "With every right answer, they'll climb higher, earning more and more cash... but every wrong answer brings them closer to losing it all."
    a "In this game, it’s not just what you know – it’s how much you're willing to risk!"

    show announcer at left with move

    a "Who will conquer the questions, outsmart the odds, and walk away with a fortune? It’s time to find out! Let’s play Information is Money!"

    call lifecount

    label intro:
        scene backcont
        show announcer at right with dissolve

        a "Our first contestant of the night is X"

        show cont1 at left with dissolve

        a "Good Evening X, Please introduce yourself to the audience"
        c "Hello my name is X and i like waffles and winning"
        a "very poggers of you X, shall we get into the first question"
    
    


    label q1:
        a "What energy drink did Logan Paul and KSI make?"

        menu:
            "Prime":
                a "THAT'S CORRECT"
                    jump q2
            "Gatorade":
                a "Do they look like gators?"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q1
                else: 
                    jump game_over
            "Liquid Cryptoscam":
                a "God, we wish!"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q1
                else: 
                    jump game_over
            "Wedang Jahe":
                a "Goblok!"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q1
                else: 
                    jump game_over

    label q2:
        scene 100d
        show announcer at right with dissolve
        a "congratz u got the first one right"
        a "u get 100 bucks"
        a "Next question"
        a "Did you Know?"

        menu:
            "No, I don't":
                a "fuckin idiot"
                $ life_counter -= 1
                if life_counter > 0:
                    jump q1
                else: 
                    jump game_over
    
            "Yes, I do":
                a "Goood"
                jump q3

            "That in terms of Pokemon and Human....":
                a "STOP"
                a "FUCKING DIE"
                jump game_over
        



    label q3:
    a "Good anakin, Good"





    label lifecount:
        if life_counter == 3:
            show three at right with dissolve
        elif life_counter == 2:
            show two at right with vpunch
        elif life_counter == 1:
            show one at right with vpunch
        else:
            show zero at right with vpunch
        return
    

    label game_over:
    
    scene milstart
    show announcer at right with dissolve
    a "game over mfker"

    show cont1 at left with vpunch
    c "dogshit game fr"

    return
