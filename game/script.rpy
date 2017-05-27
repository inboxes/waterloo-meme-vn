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
# characters    
define f = Character('Feridun Hamdullahpur',color="#9400d3")
define ga = Character('/u/SseCn8jx',color="#18b5ef")
define eb = Character('Eyebrow Goose',color="#d0bd3b")
define ut = Character('UofT Student',color="#002f65")
define gs = Character('The Saviour',color="#fc1409")
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

show text "{color=#ffffff}{size=+30}The Dream Meme Team presents...{/size}{/color}" with dissolve
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
    "Life at university means a new start."
    "And..."
    "You seem to have forgot your name."
    
    $ player_name = renpy.input("What is your name?")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="Mr.Goose"
        
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

    
    play music "begin.ogg"
    scene waterlooair with dissolve
    "You have just arrived at Waterloo."
    "You are part of the select few who have been selected to join the new engineering program."
    "With UWaterloo's rising popularity, there has been an increased need to innovate more creamy memes."
    "Meme Engineering is only in its first year of infancy and you have been one of ten people selected to participate in this new program."
    "You are too poor to afford MKV air conditioning so you head towards the UWP dorms."
    
    scene uwp with dissolve
    ##play sound footstepgravel
    m "There is goose crap everywhere, dragging your luggage through the gravel road, trying to avoid much of the crap on the ground as possible."
    
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
    
    scene uwp with dissolve
    
    menu:
        "Fight":
            $ points += 1
            jump fightgoose
            
        "Flight":
            jump flightgoose


label fightgoose:
    
    scene uwp with dissolve
    show eyebrow with dissolve
    
    "You flap your arms in the air and chase after the goose."
    m "1v1 me REEEEEEEEEEEEE!"
    
    play sound "honk.ogg"
    scene waterlooair with dissolve
    
    "You did not win against the goose."
    "You die knowing that these large water fowl are too dangerous to fight."
    "Rip"
    
    jump startgame


label flightgoose:
    
    scene uwp with dissolve
    show eyebrow with dissolve
    
    "You are wise in avoiding the goose."
    m "Man I'm tired."
    "You are tired despite doing literally nothing other than deciding whether or not you want to fight a goose."
    "You head to your dorm and rest the night."
    
    scene uwp with dissolve
    
    "You are well rested."
    "You begin heading towards your first lecture."
    
    scene rch with dissolve
    
    "The rusty figure of RCH looms over you."
    m "Wait,{w} this is literally a bombshelter."
    "You must wait until >=19 years of exp before you can actually go the the Bombshelter."
    "You descened down the stairs of RCH"
    ##play sound footstepstairs
    ##scene lecture with dissolve
    
    
    scene mc with dissolve
    
    "One particular day after you leave your Linear Algebra tutorial, you feel thirsty and the desire to use the washroom."
    "Upon arriving at the washroom, you find a half-empty water bottle on the seat of the toilet."
   
    show dasani with dissolve
    
    "You move the water bottle and use the toilet."
    "You are rather thirsty."
    
    menu:
        
        "Drink":
            $ points += 1
            jump drink
            
        "Bidet":
            jump bidet
          
          
label drink:
    
    scene mc with dissolve
    show dasani with dissolve
    
    "???"
    "Why?"
    "Someone used that water bottle as a bidet you know."
    "Didn't anyone teach you to not drink a half-empty water bottle that you found in a bathroom stall?"
    "Go use it as a bidet instead."
    "I know we have a shortage of female students.."
    "but damn you thirsty."
    "Narrator just broke the forth wall."
    
    jump bidet


label bidet:
    
    scene mc with dissolve
    show dasani with dissolve
    
    "You use the half empty water bottle as a bidet."
    "Your anus has never felt so refreshed."
    "Your anus is no longer hurting from all the ass-rape you have suffered since coming here."
    
    jump coop


label coop:
    
    scene uwp with dissolve
    
    "You head home to apply to co-op"
    "Cali or bust you say"
    "You apply to only the dankest Cali jobs at the pig 4, who wouldn't want you, you have that dank high school mark."
    
    jump before_midterms
    
    
label before_midterms:
    
    scene waterlooair with dissolve
    
    "~Time skip to before midterms~"
    "..."
    "You have still not been interviewed yet."
    "You put your resume on /r/uwaterloo but everyone just says its shit."
    "Feels bad man."
    
    scene uwp with dissolve
    
    "You are famished after staying up two nights to study for your midterms. You have been eating nothing but Soylent for the past week."
    "You require real food."
    "You head to the plaza in search of food."
    
    jump phathatpaninos


label phathatpaninos:
    
    menu:
        
        "Paninos":
            jump paninos
            
        "Phat Hat":
            $ points += 1
            jump phathat


label phathat:
    
    scene phathat with dissolve
    
    "You forgot that Phathat is actually a money laundering service."
    "There is no food here and you starve."
    "You head to Paninos instead."
    
    jump paninos


label paninos:
    
    scene paninos with dissolve
    
    "You eat the food before you with haste."
    "You are filled up and leave."
    
    scene uwp with dissolve
    
    "You ponder about life as you walk back towards your dorm."
    "'Why no gf?'"
    
    play sound "honk.ogg"
    
    "You hear a honk and turn around."
    
    show goosegf with dissolve
    
    "Even the goose from before has a gf."
    
    hide goosegf with dissolve
    show feels with dissolve
    
    "At least you aren't in 4B ECE."
    
    jump after_midterms


label after_midterms:
    
    scene waterlooair with dissolve
    
    "..."
    "Midterms are over"
    "You are failing three of your classes."
    "Your 99 in high school did not help."
    "You still have no co-op."
    "You have busted"
    "(¬‿¬)"
    "The pressure is on."
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
    
    hide feridun 
    scene uwp with dissolve
    
    "You go to resume critiques and go to extra help sessions."
    "You apply to every damn co-op you can."
    "Your meme game intensifies."
    
    jump finals
    

label finals:
    
    scene waterlooair with dissolve
    
    "It is exam season"
    "You head to Toronto to catch up with your high-school friends because you sure haven't made any friends here"
    
    scene ut with dissolve
    
    "You can feel the normie atmosphere coming from everyone walking the campus"
    
    stop music fadeout 1.0
    show utstudent with dissolve
    
    "A UofT student walks up to you."
    
    ut "UofT has better memes than Waterloo"
    
    play sound "hype.ogg" fadein 2.0

    "(╯°□°)╯ ┻━┻"
    "You become triggered"
    
    menu:
        
        "Declare meme war":
                jump memewar
                
        "Settle for peace":
                $ points += 1
                jump peace


label peace:
    
    scene ut with dissolve
    
    "Don't be a pussy, we will never lose to these normal fags when it comes to a meme war"
    "You have been conscripted into the meme war"
    
    jump memewar


label memewar:
    
    scene ut with dissolve
    
    "You have cast away all reason and have started making memes in the middle of exam season."
    "The war is fierce."
    "UofT lead by /u/fattittyfucker creates one Spongebob meme after another"
    "You see the food truck meme rising in popularity."
    "When all is looking bleak, one man appears to end it all."
    "Suddenly /u/SseCn8jx appears."

    show fuck with dissolve
    ga "'Fuck it, if this post receives 2000 upvotes I will tattoo a goose on my ass.'"
    
    stop sound fadeout 1.0
    
    $ renpy.movie_cutscene("staynight.webm")
    
    scene ut with dissolve
    show utstudent at left with dissolve
    show ga at right with dissolve
    play sound "nani.ogg"
    
    ut "NANI?BAKANA? How do you guys shitpost so hard in the middle of exam season?"
    
    show feridun with dissolve
    
    f "Fools."
    f "You think you can stop the disruptive power of /r/uwaterloo?"
    f "The last time something dropped this hot it ended WWII."
    
    hide feridun
    hide ut student
    hide ga
    
    scene uwp with dissolve
    
    "You return to school knowing that you participated in such a historic event."
    "You study for exams."
    "Who are you kidding, you brows reddit all day."
    "You apply lube to your anus in expectation of the ass-rape to come."
    "( ͡° ͜ʖ ͡°)"
    
    
    scene waterlooair with dissolve
    play sound "shrek.ogg"
    
    "You managed to pass your exams and boost your average up."
    "You found a dank co-op"
    "You have a GF now"
    "Life is great"
    "..."
    "You really thought that could happen at Waterloo?"
    "(☞*∀*)☞"
    "You barely make it past first year"
    "You have a co-op painting fences."
    "Still single as ever"
    "You have however discovered something within you."
    "You have cast away your earthly desires of wanting human companionship and the need for sleep"
    "Your level of autism and degeneracy greatly increases"
    
    show memelord with dissolve
    
    "You have evolved into a memelord!"
    "You head-off into the work term with renewed vigor"
    "You can't wait to graduate and escape from this shit-hole"
    
    jump ending
    
label ending:
    
    if points >= 4:
        "Wait what's this?"
        jump broad
    else:
        jump credits
    
label broad:
    scene broad with dissolve
    "Congrats"
    "You actually managed to fuck up so hard that you unlocked this easter egg"
    "You had a 1/16 chance to get this easter egg based on your choices."
    "That's it"
    "Just some internet points"
    "Why do you do this to yourself?"
    "Broad is love Broad is life"
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

