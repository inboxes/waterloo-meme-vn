# images
image waterlooair = "waterlooair.jpg"
image feridun = "feridun.png"
image ga = "gooseass.png"
image eyebrow = "eyebrow.png"
image uwp = "uwp.png"
image rch = "rch.jpg"
image phathat = "phathat.jpg"
image paninos = "paninos.jpg"
image goosegf = "goosegf.png"
image feels = "feels.png"
image mc = "mc.jpg"
image dasani = "dasani.png"
image ut = "ut.jpg"
image utstudent = "utstudent.png"
image memelord = "memelord.png"
image broad = "broad.jpg"
image fuck = "fuck.png"
image feriduncart = "feriduncart.png"
image feridunback = "feridunbackground.jpg"
image pan = "startscene.jpg"
image thesaviour = "thesaviour.png"
image eyebrow_battle = im.FactorScale("eyebrow.png", 0.4)
image player_battle = im.FactorScale(im.Flip("Angra.png", horizontal=True), 1.2)
image lecture = "lecture.jpg"
image battleground = "battleground.jpg"
image playerfull = "playerhealthfull.png"
image playerempty = "playerhealthempty.png"
image goosehealth = "goosehealth.png"
image dorm = "dorm.jpg"
# characters    
define f = Character('Feridun Hamdullahpur',color="#9400d3")
define ga = Character('/u/SseCn8jx',color="#18b5ef")
define eb = Character('Eyebrow Goose',color="#d0bd3b")
define ut = Character('UofT Student',color="#002f65")
define gs = Character('Sergeant Goose',color="#fc1409")
#use m for the username

# opening sequence
label splashscreen:
play sound "intro.ogg"
scene black
with Pause(1)

show text "{color=#ffffff}{size=+30}From Enghack...{/size}{/color}" with dissolve
with Pause(2)
hide text with dissolve
with Pause(1)

show text "{color=#ffffff}{size=+30}Type-Meme presents...{/size}{/color}" with dissolve
with Pause(2)
hide text with dissolve
with Pause(1)

show text "{color=#ffffff}{size=+30}The Bamboozle{/size}{/color}" with dissolve
with Pause(2)
hide text with dissolve
with Pause(1)

$ renpy.movie_cutscene('intro.webm')

return


#username input
label start:
    scene waterlooair with dissolve
    show feriduncart with dissolve
    f "Why hello!"
    f "Welcome to the University of Waterloo!"
    f "Innovation starts here."
    f "What is INNOVATION you ask?"
    f "INNOVATION is...{w} disruptive."
    f "I'm sure you will learn of it soon enough once you have spent enough time here."
    f "Now what was your name again?"
    
    "Strange...{w} You can't seem to remember your name."
    
    $ player_name = renpy.input("What is your name?")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="Newbie"
        
    hide feriduncart with dissolve
        
    show thesaviour from bottom with dissolve
    gs "Welcome to Waterloo %(player_name)s!"
    gs "You will soon learn to Thank Mr.Goose."
    gs "I will be your guide."
    
    $ points = 0
    
    $ m = DynamicCharacter('player_name',color="#9309fd") #defining the user name
    stop sound fadeout(2.0)
    jump introshot
    
#intro pan
label introshot:
    #PROLOGUE
    scene black with dissolve
    show text "{color=#ffffff}{size=+30}Prologue\nWaking Memories{/size}{/color}" with Pause(1)
    hide text with dissolve
    scene black with dissolve
    play music "scene.ogg"
    scene startscene at Pan((0, 0), (580,0), 15.0)
    
    show text "{color=#ffc600}{size=+30}You look upon the apocalyptic future that is 2017.{/size}{/color}"
    with Pause (2)
    hide text with dissolve
    with Pause (1)

    show text "{color=#ffc600}{size=+30}It was not always this way.{/size}{/color}"
    with Pause (2)
    hide text with dissolve
    with Pause (1)
    
    show text "{color=#ffc600}{size=+30}You recall a time before WaterlooWorks.{/size}{/color}"
    with Pause (2)
    hide text with dissolve
    with Pause (1)

    show text "{color=#ffc600}{size=+30}You were just a mere first year student,{/size}{/color}"
    with Pause (2)
    hide text with dissolve
    with Pause (1)
    
    show text "{color=#ffc600}{size=+30}unaware of the sacrifices that were to be made.{/size}{/color}"
    with Pause (2)
    hide text with dissolve
    with Pause (1)
    
    stop music fadeout 2.0
    jump startgame
    
#Start of the Game
label startgame:

    #CHAPTER 1
    scene black with dissolve
    show text "{color=#ffffff}{size=+30}Chapter 1\nA Frightening Sight{/size}{/color}" with Pause(1)
    hide text with dissolve
    scene black with dissolve

    play music "begin.ogg"
    scene waterlooair with dissolve
    "You have just arrived at Waterloo."
    "You are part of the select few who have been selected to join the new engineering program."
    "With UWaterloo's rising popularity, there has been an increased need to innovate more creamy memes."
    "Meme Engineering is only in its first year of infancy and you have been one of ten people selected to participate in this new program."
    "You are too poor to afford MKV air conditioning so you head towards the UWP dorms."
    
    scene uwp with dissolve
    play sound "footstepgravel.ogg"
    "You drag your luggage through the gravel road, trying to avoid much of the crap on the ground as possible."
    m "There is goose shit everywhere!"
    
    show eyebrow with dissolve
    "Along the way, you are stopped by a goose with eyebrows."
    "The goose raises its eyebrow."
    
    play sound "honk.ogg"
    
    eb "Honk"
    m "Wait..."
    m "Is this the goose that has shat all over the road?"
    m "My luggage will not die in vain."
    "You decide if you want to fight this goose and claim vengeance for your luggage."
    
    jump fightflight
    
    
    
label fightflight:
    
    play music "Battle! (Wild Pokémon) (Pokémon Ruby & Sapphire).mp3"
    scene black with pixellate
    scene black with squares
    scene battleground with dissolve
    show eyebrow_battle at Position(xpos = 0.73, xanchor=0.5, ypos=0.45, yanchor=0.5)with moveinright
    show goosehealth with moveinright
    show player_battle at Position(xpos = 0.25, xanchor=0.5, ypos=0.6, yanchor=0.5)with moveinleft
    show playerfull with moveinleft
    
    "A wild Goose has appeared!"
    $ pkmn_easter = 0
    
    menu battle:
        "Fight":
            jump fightgoose
        "P*km*n":
            "What's a Pokerman? Never heard of them. Maybe you should pick a real choice."
            $ pkmn_easter += 1
            #unlocks special scene later
            jump battle
        "Bag":
            "You find only pencils and pens"
            "You're not in Kanto anymore. The wild Goose isn't a digital monster."
            jump battle
        "Run":
            "You run away with your hands covering your head."
            "Got away safely"
            hide eyebrow
            hide player_battle with moveoutleft
            jump flightgoose
    
label fightgoose:
    
    "You flap your arms in the air and chase after the goose."
    m "1v1 me REEEEEEEEEEEEE!"
    
    menu moves:
        "Tackle":
            "You charge at the goose like a maniac."
            "You miss."
            "Mr.Goose used honk."
            play sound "honk.ogg"
            with hpunch
            "It's super effective."
            hide player_battle with moveoutbottom
        "Roll Pencil":
            "You roll a pencil to determine more choices."
            "This is not a multiple choice exam."
            "Mr.Goose used honk."
            play sound "honk.ogg"
            with hpunch
            "It's super effective."
            hide player_battle with moveoutbottom
        "Screech":
            #animate
            "You try to screech to lower the goose's defences, but it failed"
            #animate
            "The wild Goose used laugh."
            with hpunch
            play sound "honk.ogg"
            "It was super effective!"
            "You realize how pathetic you sound and start to cry."
            hide player_battle with moveoutbottom
        "Hyper Beam":
            "Your mouth is agap as you charge up.{w} You let out a burp."
            "You realize humans can't actually use hyper beam.{w}Obviously."
            "Mr.Goose used honk."
            play sound "honk.ogg"
            with hpunch
            "It's super effective."
            hide player_battle with moveoutbottom
            #animate goose attacking
    
    show playerempty with dissolve
    "You have fainted"
    stop music fadeout 1.0
    scene waterlooair with dissolve
    
    "You did not win against the goose."
    "You die knowing that these large water fowl are too dangerous to fight."
    "Rip"
    
    jump fightflight



label flightgoose:
    stop music fadeout 2.0
    scene uwp with dissolve
    show eyebrow with dissolve
    
    "You are wise in avoiding the goose."
    hide eyebrow with dissolve
    m "Man I'm tired."
    "You are tired despite doing literally nothing other than deciding whether or not you want to fight a goose."
    "You head to your dorm and rest the night."
    scene dorm with dissolve
    m "Ahh...{w} so comfortable."
    m "The mattress might be a rock but I feel like I could get used to sleeping here."
    "Little did you know that you won't be getting much sleep."
    "Your dorm is already a mess."
    jump firstlecture

label firstlecture:
    
    scene black
    scene dorm with dissolve
    
    "You are well rested."
    "You begin heading towards your first lecture."
    
    scene rch with dissolve
    
    "The rusty figure of RCH looms over you."
    m "Wait,{w} this is literally a bombshelter."
    "You must wait until >=19 years of exp before you can actually go the the Bombshelter."
    "You descened down the stairs of RCH"
    play sound "footstepstairs.ogg"
    scene lecture with dissolve
    m "Wow!{w} Lectures are going to be so fun!"
    "Little did you know that you would skip most of your lectures in the not so distant future."
    
    scene mc with dissolve
    
    "One particular day after you leave your Linear Algebra tutorial..."
    m "Let me use the washroom real quick."
   
    show dasani with dissolve
    m "Wait,{w} why is there a half-empty water bottle here?"
    m "Guess I'll just move it"
    play sound "flush.ogg"
    m "Hmm...{w} I am rather thirsty..."
    m "I just spent my entire meal plan at Timmy's the other day..."
    m "Should I risk the drink?"
    
    menu:
        
        "Drink":
            jump drink
            
        "Stay thirsty":
            jump thirst
          
          
label drink:
    
    scene mc with dissolve
    show dasani at right with dissolve
    show thesaviour at left with dissolve
    
    gs"???"
    gs"Why?"
    gs"Didn't anyone teach you to not drink a half-empty water bottle that you found in a bathroom stall?"
    gs"Why are you so thirsty?{w} In both sense of the word."
    
    scene waterlooair with dissolve
    "You die of E.Coli that you contracted from the water bottle."
    "Don't drink random half-empty water bottles that you find in bathroom stalls in the future."
    
    jump firstlecture


label thirst:
    
    scene mc with dissolve
    show dasani with dissolve
    
    m "Drinking a half-empty water bottle that I found in the middle of nowhere is not worth."
    hide dasani with dissolve
    show thesaviour with dissolve
    gs "Good call."
    gs "You've been thirsty for this long,{w} being thirsty for a little bit longer won't hurt."
    
    jump coop


label coop:
    
    #CHAPTER 2
    scene black with dissolve
    show text "{color=#ffffff}{size=+30}Chapter 2\nWaterloo (Doesn't) Work{/size}{/color}" with Pause(1)
    hide text with dissolve
    scene black with dissolve

    scene uwp with dissolve
    "You head home to apply to co-op"
    scene dorm with dissolve
    m "Cali or bust"
    "You apply to only the dankest Cali jobs."
    m "I got those side projects.{w} I learned html from code academy.{w} Easy Web Dev co-op for Google."
    
    jump before_midterms

label before_midterms:
    #Chapter 3
    scene black with dissolve
    show text "{color=#ffffff}{size=+30}Chapter 3\nCHE 102{/size}{/color}" with Pause(1)
    hide text with dissolve
    scene black with dissolve
    
    scene waterlooair with dissolve
    
    "~Time skip to before midterms~"
    show thesaviour with dissolve
    gs "..."
    gs "You have still not been interviewed yet."
    m "Feels bad man."
    
    scene dorm with dissolve
    
    "You are famished after staying up two nights to study for your midterms. You have been eating nothing but Soylent for the past week."
    m "Food..."
    m "I miss that high calorie high sodium taste."
    "You head to the plaza in search of food."
    
    menu:
        
        "Paninos":
            jump paninos
            
        "Paninos":
            jump paninos
        
        "Paninos":
            jump paninos
        
        "Paninos or bust":
            jump paninos


label paninos:
    
    scene paninos with dissolve
    
    "You eat the food before you with haste."
    m "Thank Paninos for nourishment." 
    "You are filled up and leave."
    
    scene uwp with dissolve
    
    "You ponder about life as you walk back towards your dorm."
    m "Why am I so lonely"
    
    play sound "honk.ogg"
    
    "You hear a honk and turn around."
    
    show goosegf with dissolve
    
    "Even the goose from before has a friend."
    
    hide goosegf with dissolve
    show feels with dissolve
    
    m "Feels Bad Man"
    
    jump after_midterms


label after_midterms:
    #CHAPTER 4
    scene black with dissolve
    show text "{color=#ffffff}{size=+30}Chapter 4\nEarly Aftermath{/size}{/color}" with Pause(1)
    hide text with dissolve
    scene black with dissolve
    
    scene waterlooair with dissolve
    
    "..."
    "Midterms are over"
    "You are failing three of your classes."
    "Your 99 in high school did not help."
    "You still have no co-op."
    "You have busted"
    "(¬‿¬)"
    "The pressure is on."
    play sound "hypesong.ogg" fadein(3)
    "You receive an email one day asking you to meet a councillor about your grades."

    scene feridunback with dissolve
    show feriduncart with dissolve
    
    "You see Feridun himself in the flesh."
    "You must be dreaming."
    
    f "Do not worry young one, if you fall, simply innovate harder."
    f "Finals are worth more than midterms."
    f "There is always continuous round."
    f "Work hard and make me proud."
    
    "Feridun is love, Feridun is life."
    
    hide feridun with dissolve
    scene uwp with dissolve
    
    "You go to resume critiques and extra help sessions."
    "You apply to more co-ops."
    "Your meme game intensifies."
    stop sound fadeout(2)
    
    jump finals
    

label finals:
    "You thought you still had two weeks but lmao, finals came faster than yourself."
    show thesaviour with dissolve
    gs "Don't worry. A person only needs a maximum of 48 hours to learn a course anyways.{w} It is a fact.{w} Proven by science."
    "You did the math. You have 3 hours of lecturs a week. A term is 12 weeks. That's only 36 hours in total. Mr.Goose is right again. You thank him for his guidance."
    "You went back to your room and opened up your laptop.{w} Two familiar icons appeared in front of your eyes."
    
    menu: 
        "Play League.":
            "What? You can't choose studying? {w} Of course not. If you could choose that you would have done it 12 weeks ago."
            "You play one game and get recked. You rage quit and begin studying."
        "Play Overwatch.":
            "What? You can't choose studying? {w} Of course not. If you could choose that you would have done it 12 weeks ago."
            "You misses all your shots. You rage quit and begin studying."
    
    "You begin studying."
    "..."
    "..."
    "..."
    "2 hours passed. {w} It is the 50th time you read over the first paragraph in your notes." 
    "You still don't get it."
    show thesaviour with dissolve
    gs "Search it on YouTube."
    "You search for a tutuorial on Youtube."
    ".......{w}......"
    "7 hours passed."
    "During this time, you have mastered 3 ways of communicating with Zebras, 5 secret recipies for the perfect Congo Cuisine, and 2 ways of making your personal spacecraft."
    "You also finally understands the first paragraph in your notes."
    "It has already darkened out side."
    menu:
        "Keep studying.":
            "You keep studying."
            "..."
            "Two days passed."
            "You are too exhausted.{w} The world darkenes before your eyes."
    
    ## need new ending
    jump ending
    
label ending:
    
    if points >= 4:
        "Wait what's this?"
        jump broad
    else:
        jump credits

    # This ends the game.

label credits: 
    
    scene waterlooair with dissolve
    
    "I'm the narrator and I like to chase geese around."
    "I wouldn't recommend it though, sometimes they chase back."
    "Thanks for playing the game"
    "I didn't know wtf I was doing half the time, but hey it worked out"
    "Special thanks to Laggy for letting me use his amazing videos, my game would have been complete shit without them."
    "All content belong to their respectful owners. Sources can be found in the About tab in the main menu."
    stop sound fadeout 1.0

    return

