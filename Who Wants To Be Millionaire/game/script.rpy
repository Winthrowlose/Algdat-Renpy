# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Contestant", color="#03f0fc")
define a = Character("Announcer", color="#bbc400")

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

label intro:
    scene backcont
    show announcer at right with dissolve

    a "Our first contestant of the night is X"

    show cont1 at left with dissolve

    a "Good Evening X, Please introduce yourself to the audience"
    c "Hello my name is X and i like waffles and winning"
    a "very poggers of you X, shall we get into the first question"

label q1:
    c "What energy drink did Logan Paul and KSI make?"
    
    menu:
        "Prime":
            c "THAT'S CORRECT"
            jump q2
        "Gatorade":
            c "Do they look like gators?"
        "Liquid Cryptoscam":
            c "God, we wish!"
        "Wedang Jahe"
            c "Goblok!"
    jump q1

label q2:
    c "congratz"

    return
