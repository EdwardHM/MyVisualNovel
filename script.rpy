# Declare Images
image bg apartmentKitchen = "YumeBackgroundsPackOne/Small_Apartment_Kitchen.png"
image bg apartmentOutside = "YumeBackgroundsPackOne/Apartment_Exterior.png"
image bg apartmentStairs = "YumeBackgroundsPackOne/Outdoor_Stairs.png"
image bg trainTunnel = "YumeBackgroundsPackOne/Train_Tunnel.png"
image bg restaurant = "YumeBackgroundsPackOne/Restaurant_B.png"

# Aiko Sprite
image Aiko casual smile = "Aiko/Casual/Aiko_Smile.png"
image Aiko casual shout = "Aiko/Casual/Aiko_Shout.png"
image Aiko casual frown = "Aiko/Casual/Aiko_Frown.png"
image Aiko casual smile blush = "Aiko/Casual/Aiko_Smile_Blush.png"
image Aiko casual shout blush = "Aiko/Casual/Aiko_Shout_Blush.png"
image Aiko casual frown blush = "Aiko/Casual/Aiko_Frown_Blush.png"
image Aiko winter pony smile = "Aiko/WinterUniform/Pony/Aiko_WinterUni_Pony_Smile.png"
image Aiko winter pony shout = "Aiko/WinterUniform/Pony/Aiko_WinterUni_Pony_Shout.png"
image Aiko winter pony frown = "Aiko/WinterUniform/Pony/Aiko_WinterUni_Pony_Frown.png"
image Aiko winter pony smile blush = "Aiko/WinterUniform/Pony/Aiko_WinterUni_Pony_Smile_Blush.png"
image Aiko winter pony shout blush = "Aiko/WinterUniform/Pony/Aiko_WinterUni_Pony_Shout_Blush.png"
image Aiko winter pony frown blush = "Aiko/WinterUniform/Pony/Aiko_WinterUni_Pony_Frown_Blush.png"

# Sora sprite
image Sora casual smile = "Sora/Casual/Sora_casual_smile.png"
image Sora casual open = "Sora/Casual/Sora_casual_open.png"
image Sora casual frown ="Sora/Casual/Sora_casual_frown.png"
image Sora winter smile = "Sora/winter/Sora_winteruni_smile.png"
image Sora winter open = "Sora/winter/Sora_winteruni_open.png"
image Sora winter frown = "Sora/winter/Sora_winteruni_frown.png"
image Sora winter smile blush = "Sora/winter/Sora_winteruni_smile_blush.png"
image Sora winter open blush = "Sora/winter/Sora_winteruni_open_blush.png"
image Sora winter frown blush = "Sora/winter/Sora_winteruni_blush.png"

# Miki Sprite
image Miki casual sidetail smile = "Miki/Casual/Sidetail/Miki_Casual_Sidetail_Smile.png"
image Miki casual sidetail frown = "Miki/Casual/Sidetail/Miki_Casual_Sidetail_Frown.png"
image Miki casual sidetail open = "Miki/Casual/Sidetail/Miki_Casual_Sidetail_Open.png"
image Miki casual sidetail smile blush = "Miki/Casual/Sidetail/Miki_Casual_Sidetail_Smile_Blush.png"
image Miki casual sidetail frown blush = "Miki/Casual/Sidetail/Miki_Casual_Sidetail_Frown_Blush.png"
image Miki casual sidetail open blush = "Miki/Casual/Sidetail/Miki_Casual_Sidetail_Open_Blush.png"
image Miki winter sidetail smile = "Miki/Winter_Uniform/Sidetail/Miki_WinterUni_SideTail_Smile.png"
image Miki winter sidetail frown = "Miki/Winter_Uniform/Sidetail/Miki_WinterUni_SideTail_Frown.png"
image Miki winter sidetail open = "Miki/Winter_Uniform/Sidetail/Miki_WinterUni_SideTail_Open.png"
image Miki winter sidetail smile blush = "Miki/Winter_Uniform/Sidetail/Miki_WinterUni_SideTail_Smile_Blush.png"
image Miki winter sidetail frown blush = "Miki/Winter_Uniform/Sidetail/Miki_WinterUni_SideTail_Frown_Blush.png"
image Miki winter sidetail open blush = "Miki/Winter_Uniform/Sidetail/Miki_WinterUni_SideTail_Open_Blush.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Aiko = Character("Aiko", color= "#FF2F1A")
define Miho = Character("Miho", color= "#1B0B2C")
define Miki = Character("Miki", color= "#00FF38")
define Sora = Character("Sora", color= "#0219A7")
define unknown = Character("????", color="#656565")
define unknownAiko = Character("Aiko ?", color= "#FF2F1A")
define unknownSora = Character("Sora ?", color= "#0219A7")
define AikoSora = Character("Aiko (Sora)", color= "#0219A7")
define SoraAiko = Character("Sora (Aiko)", color= "#FF2F1A")
define SoraAndAiko = Character(" Sora & Aiko", color="#5C0485")
# The game starts here.

label start:

    play music "audio/1_Menu_Master.ogg"
    scene bg apartmentKitchen with fade

    "Friday, 12 September 20xx"

    play sound "audio/effect/backpack_zipping.mp3"
    show Sora winter smile at truecenter with dissolve:
        xzoom 0.5 yzoom 0.5

    unknown "*Fiuuhhh* And with that I'm done packing all what I need."
    Sora "(My name is Sora, seventeen years old. I'm just an average highschool boy you can see everywhere)."
    Sora "I'm so exicted with this field trip, even I barely to sleep last nigth."
    Sora "(Thats right, today until this Sunday, my school held field trip to X City)."
    Sora "Oh look at the time, it already 08.00 AM ! I must hurry go to school before 09.00 AM, or I'm gonna late for the field trip."

    menu:
        Sora "(What should I do ?)"

        "Check my travel bag and surrounding.":
            jump travelBag

        "Okay I'm ready to go !":
            jump goOutside

label travelBag:

    hide Sora winter smile with dissolve
    play sound "audio/effect/backpack_zipping.mp3"
    Sora "(I open may travel bag and check all the thing inside the bag to make sure I bring all I need for this field trip)."
    Sora "Hmm... Ok, I think everything is already in the bag."
    play sound "audio/effect/backpack_zipping.mp3"
    Sora "(I close my travel bag and then check my surrounding to make sure I already turn off the stove and any other electronic appliances)."
    Sora "(Everything looks fine)."
    jump goOutside

label goOutside:

    show Sora winter smile at truecenter with dissolve:
        xzoom 0.5 yzoom 0.5
    Sora "Okay, full speed to the school !"

    play sound "audio/effect/door_open.mp3"
    scene black
    Sora "(I leave my apartment. I always walk to go to school, and it takes around thirty minutes from my apartment)."
    Sora "(I make sure to go early this time because I need to carry this travel bag, which is more heavier than my school bag)."
    play sound "audio/effect/door_closing.mp3"
    scene bg apartmentOutside with fade
    show Sora winter open at truecenter with dissolve:
        xzoom 0.5 yzoom 0.5
    Sora "(Oh... !)"

    hide Sora winter open with dissolve
    show Aiko winter pony smile at truecenter with dissolve:
        xzoom 0.5 yzoom 0.5
    unknown "(hum hum hum~~~♪♫)"

    Sora "(The girl name who humming right now is Aiko. Her room is next to me in this apartment)."
    Sora "(To be exactly my room is not really \"side by side\" with her. Our room is separated by stairs that connect first floor and second floor where our room is)."
    Sora "(She is also my classmate at class 2-B. Really a lot of coincidences, right !?)."

    hide Aiko winter pony smile with dissolve
    menu:
        Sora "(Should I greet her ?)."
        "Ignore Her":
            jump ignoreHer
        "Good Morning Aiko !":
            jump goodMorning

label ignoreHer:

    Sora "(Well I don't have a duty to greet her every morning right)."
    Sora "(I pretending not hear her humming and just walk to the stairs)"

    show Aiko winter pony smile at truecenter with dissolve:
        xzoom 0.5 yzoom 0.5

    Aiko "Good morning Sora. The weather looks nice today."
    Sora "(Well I can't really ignoring you, if you greet me now....)."

    show Aiko winter pony smile at right with easeinright:
        xzoom 0.5 yzoom 0.5
    show Sora winter smile at truecenter with dissolve:
        xzoom 0.5 yzoom 0.5
    show Sora winter smile at left with  easeinleft:
        xzoom 0.5 yzoom 0.5

    Sora "Oh Aiko.... Good morning."

    show Aiko winter pony frown at right:
        xzoom 0.5 yzoom 0.5

    Aiko "Your sound seems like not enthusiams about field trip today. Are you feeling well ?"

    show Sora winter open at left:
        xzoom 0.5 yzoom 0.5

    Sora "What ! No no, I'm so excited about today field trip. Even I barerly sleep last night, because waiting for today come."

    show Aiko winter pony smile at right:
        xzoom 0.5 yzoom 0.5

    Aiko "Fufu... Well you sounds like a kid now."
    Aiko "I hope you don't collapse when doing the field trip activities today, because lack of sleep."

    show Sora winter smile at left:
        xzoom 0.5 yzoom 0.5

    Sora "Haha.... I won't"
    jump exictedToo

label goodMorning:

    show Sora winter smile at truecenter with dissolve:
        xzoom 0.5 yzoom 0.5

    Sora "Yo Aiko, good morning !"

    show Sora winter smile at left with  easeinleft:
        xzoom 0.5 yzoom 0.5
    show Aiko winter pony smile at truecenter with dissolve:
        xzoom 0.5 yzoom 0.5
    show Aiko winter pony smile at right with easeinright:
        xzoom 0.5 yzoom 0.5

    Aiko "Good morning too Sora. It's looks like the weather will be good for field trip today"
    Sora "Yeah, I think the weather is good too. I hope the weather will be nice everyday for our field trip."
    Aiko "Fufu... Looks like you are so full of energy for this field trip."
    Sora "Hahaha yeah! Im so exicted for this field trip."
    jump exictedToo

label exictedToo:

    Aiko "Well I can't wait for this field trip too, so I know how excited you feel."
    Sora "(I see a big suitcase beside her)."
    Sora "Is that all your thing inside that suitcase you gonna bring for this field trip ?"
    Aiko "Yup that's right. It easier to bring using a suitcase, also compared to boys I think what girls need to bring is quite a lot and suitcase has a lot capacity too."
    Sora "Well I can imagine that. All I need just inside this travel bag."
    Aiko "Alright then should we walk to school together now ?"
    Sora "Yeah lets go."

    play sound "audio/effect/Rolling_suitcase by Aurelon.mp3"

    Sora "(I lead the way to downstairs, and behind me Aiko drag her suitcase down the stairs)."
    Sora "Do you need some help with that ? I think the suitcase should be lifted, not being dragged down the stairs if you don't want damage the suitcase."
    Aiko "Ah.. It's fine I can handle this."
    Sora "(Then Aiko tried to lift the suitcase while down the stairs)."
    Sora "Watch your step ok !"

    show Aiko winter pony frown:
        xzoom 0.5 yzoom 0.5

    Aiko "Hnngg... Yeah I will."

    hide Aiko winter pony frown with dissolve
    hide Sora winter smile with dissolve

    menu:
        Sora "(The suitcase look like quiet heavy should I help her ?)."

        "Just let her.":
            jump letHer

        "Help her.":
            jump helpHer

label letHer:
    Sora "(She already said she will be fine, so I think she can handle it. Do your best Aiko)."
    Sora "(I continue to walk to downstairs, but...)."

    show Aiko winter pony shout at truecenter with dissolve:
        xzoom 0.5 yzoom 0.5
    show Aiko winter pony shout at truecenter with hpunch:
        xzoom 0.5 yzoom 0.5

    Aiko "Kyaa....!!"

    show Aiko winter pony shout at right with easeinright:
        xzoom 0.5 yzoom 0.5
    show Sora winter open at truecenter with dissolve:
        xzoom 0.5 yzoom 0.5
    show Sora winter open at left with easeinleft:
        xzoom 0.5 yzoom 0.5
    Sora "(I turned my body to look behind because that shriek)"
    Sora "Oiii.....!"
    jump bothUnconscious

label helpHer:
    Sora "(It's not fine just let her struggle lifting that suitcase)."

    show Sora winter open at truecenter with dissolve:
        xzoom 0.5 yzoom 0.5

    Sora "Hey Aiko just let me......"

    show Sora winter open at left with easeinleft:
        xzoom 0.5 yzoom 0.5

    show Aiko winter pony shout at truecenter with dissolve:
        xzoom 0.5 yzoom 0.5

    show Aiko winter pony shout at right with easeinright:
        xzoom 0.5 yzoom 0.5

    show Aiko winter pony shout at right with hpunch:
        xzoom 0.5 yzoom 0.5

    Aiko "Kyaa....!!"
    Sora "Watch out.!"
    jump bothUnconscious

label bothUnconscious:

    stop music fadeout 1.0
    show Aiko winter pony shout at left with moveinleft:
        xzoom 0.5 yzoom 0.5

    scene bg apartmentOutside with hpunch
    play sound "audio/effect/object_falls.mp3"
    scene black
    "................."
    "........."
    "*Ughhh............*"
    "(My head...*Ugh !* It's hurt... especially around the forehead)."
    "Hey... can you get up already, I can't move."

    play sound "audio/effect/Clothing_rustling_2 by toiledejouy84.mp3"

    "(Oh right I need to get up first for now)."
    "(I feel a bit dizzy)."

    scene bg apartmentStairs with fade

    show Aiko winter pony frown at truecenter with dissolve:
        xzoom 0.5 yzoom 0.5

    Aiko "*Ugh...* My Head."

    show Aiko winter pony shout at truecenter:
        xzoom 0.5 yzoom 0.5

    Aiko "I already told you to be careful right ! Look what you did now."

    show Aiko winter pony shout at right with easeinright:
        xzoom 0.5 yzoom 0.5
    show Sora winter frown at truecenter with dissolve:
        xzoom 0.5 yzoom 0.5
    show Sora winter frown at left with easeinleft:
        xzoom 0.5 yzoom 0.5

    Sora "*Ouch....* I'm so sorry Sora."

    show Aiko winter pony frown at right:
        xzoom 0.5 yzoom 0.5

    Aiko "Huh !"

    show Sora winter open at left:
        xzoom 0.5 yzoom 0.5

    Sora "Hmm.... !?"

    show Aiko winter shout at right:
        xzoom 0.5 yzoom 0.5

    Aiko "Why I can see my own body ?"
    Sora "Isn't that... Me !?"

    play music "audio/A weird thing by Chiro.mp3"

    SoraAndAiko "EEEEHHHHH.....!!!!"
    SoraAndAiko "WHAT'S HAPPENING NOW!"
    SoraAndAiko "......."

    show Sora winter frown at left:
        xzoom 0.5 yzoom 0.5

    unknownSora "For now take a deep breath and calm our mind ok."
    unknownAiko "How can you so calm in this situation !?"

    show Sora winter open at left:
        xzoom 0.5 yzoom 0.5
    unknownSora "*Inhale....* *Exhale....* *Inhale....* *Exhale....*"

    show Sora winter smile at left:
        xzoom 0.5 yzoom 0.5
    unknownSora "So now who currently inside {color=#FFF700} \"My Body\" {/color} is Sora right."


    SoraAiko "What a pointless question, ofcourse {color=#FFF700} \"I'm Sora\" {/color} !"

    show Sora winter frown at left:
        xzoom 0.5 yzoom 0.5

    AikoSora "So we really did switch body, and this happen because I falling from the stairs...."
    AikoSora "I never thought such a thing could happen."

    show Aiko winter pony frown at right:
        xzoom 0.5 yzoom 0.5

    SoraAiko "Believe it or not, but it actually happen."
    SoraAiko "Hey how about my {color=#FFF700}\"My Body\"{/color}, is there any injured ?"

    show Sora winter smile at left:
        xzoom 0.5 yzoom 0.5

    AikoSora "Nope, I think there is no fatal injury thanks to your travel bag. {color=#FFF700} \"Your Head\"{/color} landed on the travel bag."
    SoraAiko "*Fiuhh...* that's make one less problem for me."
    SoraAiko "And now what should we do ?"
    AikoSora "Hmmm... We should act normal for now I think."

    show Aiko winter pony shout at right:
        xzoom 0.5 yzoom 0.5

    SoraAiko "And what do you mean by \"normal\"?"
    AikoSora "Like I said, pretend like nothing happen. From now you act like you are {color=#FFF700}\"Me\"{/color}, and I will act like how Sora is."

    show Aiko winter pony frown at right:
        xzoom 0.5 yzoom 0.5

    SoraAiko "(I don't get it how she can think like that....)."
    SoraAiko "It's not easy to act like someone casually you know that. Also I don't really know how you act when I'm not around."

    show Sora winter frown at left:
        xzoom 0.5 yzoom 0.5

    AikoSora "Well that same for me too, but you should act based on how you see me everyday, I think that's enough for now."
    SoraAiko "How can you so confident about that...."

    show Sora winter smile at left:
        xzoom 0.5 yzoom 0.5

    AikoSora "Well hang in there and let's do our best ok."
    SoraAiko "Good grief, why it must happen today......"

    hide Aiko winter pony frown with dissolve
    hide Sora winter smile with dissolve

    SoraAiko "(I took the cellphone out of Aiko skirt pocket, oh ! I mean {color=#FFF700}my skirt pocket{/color} and look at the screen to check what time it is)"

    show Aiko winter pony shout at truecenter with dissolve:
        xzoom 0.5 yzoom 0.5

    SoraAiko "Oh crap it's already 08.25 AM ! We must hurry if we don't want left behind for the field trip."
    hide Aiko with dissolve

    SoraAiko "(I took my travel bag and already dash to school)."

    show Sora winter frown at truecenter with dissolve:
        xzoom 0.5 yzoom 0.5

    AikoSora "Wait a second Sora !"

    show Sora winter frown at left with easeinleft:
        xzoom 0.5 yzoom 0.5

    show Aiko winter pony shout at truecenter with dissolve:
        xzoom 0.5 yzoom 0.5
    show Aiko winter pony shout at right with easeinright:
        xzoom 0.5 yzoom 0.5

    SoraAiko "What now ! If we don't hurry."
    AikoSora "It will be strange if you bring your travel bag now, remember right now you are {color=#FFF700}\"Me\"{/color} so you should bring the suitcase."
    SoraAiko "Ok then I will bring that suitcase ! Let's moving now !"

    show Sora winter smile at left:
        xzoom 0.5 yzoom 0.5

    AikoSora "Fufu... shall we go now."

    scene black
    play sound "audio/effect/Running by Juandamb.mp3"
    "[<<< To Be Continue...]"
    stop music fadeout 1.0



# label Ready:
#     show Miki casual sidetail smile at right with dissolve:
#         xzoom 0.5 yzoom 0.5
#
#     Miki "Great ! now into the next scene"
#
#     scene bg trainTunnel with fade
#     show Aiko casual smile at left with dissolve:
#         xzoom -0.5 yzoom 0.5
#     Aiko "Change Scene Success"
#
#     "[Good End]"
#
#     return
#
# label End:
#     show Aiko casual frown at left with dissolve:
#         xzoom -1 yzoom 0.5 rotate 180
#     Miki "Oh..... To bad, well whenever you ready just tell me ok !"
#     Aiko "We will waiting for you"
#
#     scene black
#     "You never know when you ready ! You shoul just do it !"
#     "[BAD END]"
#     # This ends the game.
#
#     return
