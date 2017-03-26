# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init: 
    # images
    image waterlooair = "waterlooair.jpg"
    image feridun = "feridun.png"
    image gooseass = "gooseass.png"
    image eyebrow = "eyebrow.png"
    # characters
    define f = Character('Feridun Hamdullahpur',color="#9400d3")
    define ga = Character('u/SseCn8jx',color="#18b5ef")
    define eb = Character('Eyebrow Goose',color="#d0bd3b")

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene waterlooair
    "You have just arrived at Waterloo."
    "You are part of the select few who have been selected to join the new engineering program"
    "With r/uwaterloo's rising popularity, there has been an increased need to innovate more creamy memes"
    "Meme Engineering is only in its first year of infancy and you have been one of ten people selected to participate in this new program"
    
    show gooseass at left
    show feridun at right

    # These display lines of dialogue.

    "Hello, world."

    f "You've created a new Ren'Py game."

    ga "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
