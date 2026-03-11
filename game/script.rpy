# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("[bk_name]", who_color="#7d593a")

define pov = Character("[player_name]")

define slow_move = MoveTransition(1.2)

transform midleft:
    xalign 0.1 # 0.0 = far left, 0.5 = center, 1.0 = far right
    yalign 1.0 # keep them aligned to the bottom

transform midright:
    xalign 0.9
    yalign 1.0

transform mug_offset:
    xoffset 120
    yoffset 64

transform napkin_offset:
    xoffset -120
    yoffset 180

layeredimage drink:
    always:
        Null(width=650, height=480) # a bit larger than the max size of all mug based items
    at transform:
        xanchor 0.5
        yanchor 1.0

    group tray: # what's defined first is in the background
        attribute milk:
            "tray_milk.png"

    group plate:
        attribute plate:
            "mug_plate.png"

    group liquid:
        at mug_offset
        xoffset 25
        yoffset 11
        attribute berry_tea:
            "liquid_berry_tea.png"
        attribute black_tea:
            "liquid_black_tea.png"
        attribute camomille_tea:
            "liquid_camomille_tea.png"
        attribute coffee:
            "liquid_coffee.png"
        attribute ginger_tea:
            "liquid_ginger_tea.png"
        attribute green_tea:
            "liquid_green_tea.png"
        attribute hot_chocolate:
            "liquid_hot_chocolate.png"
        attribute matcha:
            "liquid_matcha.png"
        attribute peppermint_tea:
            "liquid_peppermint_tea.png"

    group container:
        at mug_offset
        attribute mug default:
            "mug.png"
        attribute cup:
            yoffset -5
            "cup.png"

    group tray_foreground:
        attribute milk:
            "tray_milk_foreground.png"

    group addons_foreground: # note: within a group you can't show more than one attribute at once
        at mug_offset
        xoffset 25
        attribute cream:
            yoffset -49
            "cream.png"
        attribute marshmallows:
            yoffset 10
            "marshmallows.png"
        attribute cream_marshmallows:
            yoffset -65
            "cream_marshmallows.png"

    group napkin:
        at napkin_offset
        attribute napkin:
            "napkin.png"

    group sugar:
        attribute sugar:
            "mug_sugar.png"
        attribute sugar_stick:
            at napkin_offset
            "cup_sugar.png"

    group creamer:
        at napkin_offset
        attribute creamer:
            "creamer.png"

    group cookie:
        attribute cookie: # we always show the cookie with the plate, but in the foreground
            "mug_cookie.png"
        attribute cup_cookie:
            at napkin_offset
            "cup_cookie.png"

    group tea_bag:
        at mug_offset
        xoffset 180
        yoffset 46
        attribute berry_tea: # same attribute name as the tea liquid means it gets shown together (but this one in the foreground)
            "teabag_berry.png"
        attribute black_tea:
            "teabag_black.png"
        attribute camomille_tea:
            "teabag_camomille.png"
        attribute ginger_tea:
            "teabag_ginger.png"
        attribute green_tea:
            "teabag_green.png"
        attribute peppermint_tea:
            "teabag_peppermint.png"

transform mug_position:
    xalign 0.5
    yalign 0.93

transform cup_position:
    mug_position
    xoffset 0
    yoffset -165

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bar

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show barkeeper neutral at midright
    $ menu_flipped = True

    $ bk_name = "Barkeeper"
    $ player_name = "You"
    "One day in the life of a little lofi bunny, you make your way to the Loffee coffee shop."
    "In search of some nice ambient background with calming music, you notice that something changed..."
    "The self-serve coffee place has gained a new employee!"
    "From across the room you see them working on orders and loading and unloading the dishwasher."

    window show
    $ descriptor_text = "Hmmm.... they look "
    jump menu_bk_age

menu menu_bk_age:
    "[descriptor_text]"

    "old":
        $ bk_age = "old"
        $ followup_text = "old enough to own the place."
        jump age_chosen

    "young":
        $ bk_age = "young"
        $ followup_text = "young enough that this might be their first job."
        jump age_chosen

    "middle aged":
        $ bk_age = "middle"
        $ followup_text = "like they've been barkeeping for a few years."
        jump age_chosen

label age_chosen:
    "[descriptor_text]{fast}[followup_text]"
    $ descriptor_text = "In the way they move, they seem "

menu menu_bk_age_done:
    "[descriptor_text]"

    "nonchalant":
        $ bk_demeanor = "nonchalant"
        $ followup_text = "confident and nonchalant in their abilities to run this place. You can see them wink at another customer after giving them their drink."
        $ bk_action_text = "gives you a smile."
        show barkeeper wink
        jump character_chosen

    "calm":
        $ bk_demeanor = "calm"
        $ followup_text = "calm and collected, while they prepare a hot drink for someone. They seem so much at peace that it radiates across the whole cafe."
        $ bk_action_text = "gives you a nod to acknowledge your presence."
        show barkeeper neutral
        jump character_chosen

    "nervous":
        $ bk_demeanor = "nervous"
        $ followup_text = "nervous, almost anxious, as if they feared getting the orders wrong. Their movements are just a tad too fast, but you have to say it's a bit endearing."
        $ bk_action_text = "jumps a little, then blushes."
        show barkeeper shocked
        jump character_chosen

label character_chosen:
    "[descriptor_text]{fast}[followup_text]"
    show barkeeper neutral

    "You decide to step across the room to the bar."

    "As you lean against the bar table, the barkeeper notices you and [bk_action_text]"
    if bk_demeanor == "nonchalant":
        show barkeeper smile
    elif bk_demeanor == "calm":
        show barkeeper slightsmile
    else:
        show barkeeper shockblush


    b "I'll be with you in a second!"
    if bk_demeanor == "nervous":
        show barkeeper blush
    else:
        show barkeeper neutral

    pov "No hurries!"
    if bk_demeanor == "nervous":
        show barkeeper modestblush
    else:
        show barkeeper lookdown

    "You wait for them to wrap up their current order before they come over to you."

    if bk_demeanor == "nervous":
        show barkeeper blush at midleft with slow_move
    else:
        show barkeeper neutral at midleft with slow_move
    $ menu_flipped = False

    jump menu_select_drink

label menu_select_drink:
    if bk_demeanor == "nonchalant":
        show barkeeper slightsmile
        $ bk_text = "Now, what can I get for you, dear?"
    elif bk_demeanor == "calm":
        show barkeeper slightsmile
        $ bk_text = "What can I get for you?"
    else:
        show barkeeper shockblush
        $ bk_text = "Uh, what can I get? For you, I mean? Anything you want from the menu?"

    $ drink_addons = []
    menu:
        b "[bk_text]"

        "Coffee":
            pov "Just a coffee, thank you!"
            if bk_demeanor == "nervous":
                show barkeeper shocked
            else:
                show barkeeper neutral

            $ drink_type = "coffee"
            $ drink_name = "hot coffee"
            menu:
                b "Any sugar or milk with that?"
                "Just milk":
                    pov "Just some milk please!"
                    $ drink_name += " with milk and no sugar"
                    $ drink_addons.append("milk")
                "Sugar only":
                    pov "I'll take my coffee black, but with sugar please!"
                    $ drink_name += " with sugar, no milk"
                    $ drink_addons.append("sugar")
                "Both":
                    pov "Both, please!"
                    $ drink_name += " with sugar and milk"
                    $ drink_addons.append("sugar")
                    $ drink_addons.append("milk")
                "None":
                    pov "I'll have it black, no sugar, thank you!"
                    $ drink_name += " black, no milk, no sugar, all natural"

            jump menu_to_go

        "Hot chocolate":
            pov "I'd love a hot chocolate!"
            if bk_demeanor == "nervous":
                show barkeeper shocked
            else:
                show barkeeper neutral

            $ drink_type = "hot chocolate"
            $ drink_name = "hot chocolate"
            menu:
                b "Would you like some whipped cream or marshmallows on top?"
                "Yes, both":
                    pov "Sure, why not?"
                    $ drink_name += " with marshmallows and cream"
                    $ drink_addons.append("cream")
                    $ drink_addons.append("marshmallows")
                "Just cream":
                    pov "Just some cream, please."
                    $ drink_name += " with cream"
                    $ drink_addons.append("cream")
                "Marshmallows please":
                    pov "I'd love to have some marshmallows, but please no cream!"
                    $ drink_name += " with marshmallows"
                    $ drink_addons.append("marshmallows")
                "No":
                    pov "No, thank you. Just the hot chocolate will do!"
                    b "Fair enough!"
            jump menu_to_go
        "Tea":
            pov "A nice hot cup of tea please!"
            if bk_demeanor == "nervous":
                show barkeeper shocked
            else:
                show barkeeper neutral

            $ drink_type = "tea"
            menu:
                b "What kind of tea are you looking for? We have black, green, forest berries, ginger, peppermint or camomille."
                "Black tea":
                    pov "Hm, I'll go for a black tea please."
                    $ drink_name = "black tea"
                    menu:
                        b "Any sugar or milk with that?"
                        "Just milk":
                            pov "Just some milk please!"
                            $ drink_name += " with milk"
                            $ drink_addons.append("milk")
                        "Sugar only":
                            pov "Oh, no milk please, but some sugar is good!"
                            $ drink_name += " with sugar"
                            $ drink_addons.append("sugar")

                        "Both":
                            pov "Both, please!"
                            $ drink_name += " with sugar and milk"
                            $ drink_addons.append("sugar")
                            $ drink_addons.append("milk")
                        "None":
                            pov "No, thank you!"
                            $ drink_name += " no milk, no sugar, all natural"
                "Green tea":
                    pov "I feel like a green tea would be nice."
                    $ drink_name = "green tea"
                "Forest berries":
                    pov "Forest berries sounds perfect right now."
                    $ drink_name = "berry tea"
                "Ginger":
                    pov "I haven't had ginger tea in a while, so why not?"
                    $ drink_name = "ginger tea"
                "Peppermint":
                    pov "Oh! Peppermint sounds lovely, I'll have that!"
                    $ drink_name = "peppermint tea"
                "Camomille":
                    pov "I think I'll have a camomille tea."
                    $ drink_name = "camomille tea"

            if drink_name != "black tea":
                menu:
                    b "Would you like some sugar with that?"
                    "Yes":
                        pov "Yes, please."
                        $ drink_addons.append("sugar")
                    "No":
                        pov "No thanks, no sugar for me!"

            jump menu_to_go
        "Matcha":
            pov "Do you serve matcha here?"
            b "Yes, matcha milk tea is on our menu!"
            pov "Perfect! Then I'd like one please."
            $ drink_type = "matcha"
            $ drink_name = "matcha milk tea"
            menu:
                b "Would you like some sugar with that?"
                "Yes":
                    pov "Yes, please."
                    $ drink_addons.append("sugar")
                "No":
                    pov "No thanks, no sugar for me!"
            jump menu_to_go

label menu_to_go:
    menu:
        b "And is that to sit in, or to go?"
        "Sit in":
            pov "I'll drink it here, please."
            $ drink_container = "mug"
        "To go":
            pov "I'll have it to go, please."
            $ drink_container = "cup"

    if bk_demeanor == "nonchalant":
        show barkeeper smile
        b "Sure, one [drink_name], just for you, coming up in a second!"
        "The barkeeper flashes you another smile and saunters off to get a [drink_container] from the shelf."
    elif bk_demeanor == "calm":
        show barkeeper slightsmile
        b "Alright, let me get that for you."
        "The barkeeper walks over to the shelf to grab a [drink_container] and then starts preparing your [drink_type]."
    else:
        show barkeeper modestblush
        b "Perfect! I'll get that for you any second now!"
        "As the barkeeper walks to the machine, you hear them mumble your order to themselves."

    show barkeeper turnedaway at midright with slow_move
    $ menu_flipped = True

    jump menus_smalltalk

label menus_smalltalk:
    menu:
        pov "So..."
        "How did you come across this place?":
            show barkeeper sweatsmile
            b "Oh you know, one day I was there, the other day I was here, I kinda just happened upon the job. But I like it here!"
            show barkeeper turnedaway
            pov "I see...? In any case, I'm glad you like it!"
            show barkeeper neutral
        "How do you like this place?":
            show barkeeper smile
            b "I like it a lot. The people here are all so nice!"
            show barkeeper turnedaway
            pov "I'm glad to hear that!"
            show barkeeper neutral

    menu:
        b "How about you? What are you up to today?"
        "Work":
            show barkeeper turnedaway
            pov "I've got some work to do, so I should get some focus hours in today."
            b "Oh, good luck with that, I hope you can get a lot done today!"
            $ bye_text = "Best of luck with your work today!"
        "Studying":
            show barkeeper turnedaway
            pov "I've got a lot of studying to do, so I'm gonna try my best at that!"
            b "Oh, good luck with that! I hope you'll make good progress on it today!"
            $ bye_text = "Good luck with your studies today!"
        "Reading":
            show barkeeper turnedaway
            pov "I've got some stuff I wanna read today."
            menu:
                b "That sounds nice. I hope your reading material is interesting!"
                "It is!":
                    pov "Yeah, I've long been looking forward to this, it'll be good!"
                    b "I'm glad to hear that!"
                    $ bye_text = "Have a wonderful time reading your book!"
                "Not really...":
                    pov "Actually it's a rather dry book, but I kinda have to get through it."
                    b "Aw, best of luck with it though. You got this!"
                    $ bye_text = "Good luck with that reading you gotta do today!"
        "Chatting with friends":
            show barkeeper turnedaway
            pov "I'm gonna meet up with a few friends and just hang out and catch up. It'll be good!"
            b "That sounds like a lot of fun!"
            $ bye_text = "I hope you have an amazing time with your friends!"
        "Nothing":
            show barkeeper turnedaway
            pov "Oh nothing, really. Just grabbing a drink and seeing where to go from there!"
            b "That sounds relaxing! I hope you find something nice to spend your time with today!"
            $ bye_text = "I hope you have a lovely day!"

    show barkeeper slightsmile
    jump drink_done

label drink_done:
    show barkeeper at midleft with slow_move
    $ menu_flipped = False

    if drink_container == "cup":
        show drink cup at cup_position
    else:
        show drink mug at mug_position

    if drink_type == "tea":
        if drink_name.startswith("green"):
            show drink green_tea
        elif drink_name.startswith("black"):
            show drink black_tea
        elif drink_name.startswith("berry"):
            show drink berry_tea
        elif drink_name.startswith("camomille"):
            show drink camomille_tea
        elif drink_name.startswith("peppermint"):
            show drink peppermint_tea
        elif drink_name.startswith("ginger"):
            show drink ginger_tea
    elif drink_type == "coffee":
        show drink coffee
    elif drink_type == "matcha":
        show drink matcha
    else:
        show drink hot_chocolate

    "The barkeeper brings over your [drink_container] of [drink_type]."
    if ("cream" in drink_addons or "marshmallows" in drink_addons):
        show barkeeper lookdown
        "You observe them adding "
        if "cream" in drink_addons:
            show drink cream
            if "marshmallows" in drink_addons:
                extend "a generous amount of whipped cream "
                show drink -cream cream_marshmallows
                extend "and a good handful of mini-marshmallows {nw}"
            else:
                extend "a generous amount of whipped cream {nw}"
        else:
            extend "a good handful of mini-marshmallows {nw}"
            show drink marshmallows
        extend "to your drink."
    if drink_container == "cup":
        show barkeeper lookdown
        show drink napkin
        "As they add a napkin, a wooden stirrer"
        if "sugar" in drink_addons:
            show drink sugar_stick
            extend ", a bag of cane sugar"
        if "milk" in drink_addons:
            show drink creamer
            extend ", a small milk creamer"
        show drink cup_cookie
    else:
        show barkeeper lookdown
        show drink plate
        "As they set the mug on a small plate and adorn it with a spoon"
        if "sugar" in drink_addons:
            show drink sugar
            extend ", two cubes of sugar"
        if "milk" in drink_addons:
            show drink milk
            extend ', a little beaker with milk'
        show drink cookie

    extend " and a cookie, you decide to continue the small talk."
    jump smalltalk2

label smalltalk2:
    show barkeeper slightsmile
    "The barkeeper serves you your [drink_type]."
    b "There you go, one [drink_name] for you!"
    show barkeeper neutral
    pov "Thank you so much!"
    pov "Oh by the way, I don't think I caught your name!"

    if bk_demeanor == "nonchalant":
        show barkeeper smile
        b "You can call me anything you want, dear, I don't mind."
    elif bk_demeanor == "calm":
        show barkeeper blushsmile
        b "My name's not that important. Please call me whatever you want."
    else:
        show barkeeper sweatsmile
        b "Oh, I don't think my name is that important. Just call me anything."

    $ names_asked = []
    $ can_type_name = False
    $ name1_asked = False
    $ name2_asked = False
    $ name3_asked = False
    $ knows_name_bruno = False
    jump menu_name_select

label menu_name_select:
    show barkeeper neutral

    menu:
        pov "['H' if can_type_name else 'Then h']ow about..."
        "Preston?" if bk_age == "old" and not name1_asked:
            $ name1_asked = True
            $ names_asked.append("Preston")
            if bk_demeanor == "nonchalant":
                show barkeeper blushsmile
                b "That's a good name! Preston - I like it. It suits me! Feel free to call me that, if you want."
                $ bk_name = "Preston"
                jump name_suggestion_done
            elif bk_demeanor == "calm":
                show barkeeper sweatsmile
                b "Oh no, please. Preston sounds a bit too dramatic, don't you think?"
            else:
                show barkeeper shocksweat
                b "I'm not sure about that one... It sounds rather pompuous, don't you think?"
            jump menu_name_select
        "Bartholomew?" if bk_age == "old" and not name2_asked:
            $ name2_asked = True
            $ names_asked.append("Bartholomew")
            if bk_demeanor == "nonchalant":
                show barkeeper sweatsmile
                b "Oh please, that name sounds way too stiff. Not like me at all!"
            elif bk_demeanor == "calm":
                show barkeeper blush
                b "Bartholomew? Now that's a name I could get behind. Quite suitable indeed. I like it."
                $ bk_name = "Bartholomew"
                jump name_suggestion_done
            else:
                show barkeeper sweatsmile
                b "Oh no, no, Bartholomew... That's uhh - that sounds so composed. Not like me at all! Maybe something else...?"
            jump menu_name_select
        "Minnow?" if bk_age == "old" and not name3_asked:
            $ name3_asked = True
            $ names_asked.append("Minnow")
            if bk_demeanor == "nonchalant":
                show barkeeper sweatsmile
                b "Minnow? No, that'd be too cute for me. I'd love to meet a Minnow though, I'm sure they'd be lovely!"
            elif bk_demeanor == "calm":
                show barkeeper slightsmile
                b "Hmm, I like the name, but I don't think it fits. But thank you for suggesting it."
            else:
                show barkeeper shockblush
                b "Minnow? Oh! Minnow! I like it! It's perfect! Thank you!"
                $ bk_name = "Minnow"
                jump name_suggestion_done
            jump menu_name_select

        "Leon?" if bk_age == "middle" and not name1_asked:
            $ name1_asked = True
            $ names_asked.append("Leon")
            if bk_demeanor == "nonchalant":
                show barkeeper blushsmile
                b "That's a cool name! Leon - I like it, it's strong and charming, just like me. Call me Leon, if you want!"
                $ bk_name = "Leon"
                jump name_suggestion_done
            elif bk_demeanor == "calm":
                show barkeeper sweatsmile
                b "Leon? I feel like that sounds a bit too wild for me, don't you think?"
            else:
                show barkeeper shockblush
                b "Leon's a cool name, but it sounds a bit too... strong for me? I don't know..."
            jump menu_name_select
        "Alexander?" if bk_age == "middle" and not name2_asked:
            $ name2_asked = True
            $ names_asked.append("Alexander")
            if bk_demeanor == "nonchalant":
                show barkeeper smile
                b "I know an Alexander, good guy. Not a name for me, though, I think. But thanks for the suggestion!"
            elif bk_demeanor == "calm":
                show barkeeper blush
                b "Hmm, I like the name! It suits me! Alexander. Yep, that's good. You can call me that!"
                $ bk_name = "Alexander"
                jump name_suggestion_done
            else:
                show barkeeper sweatsmile
                b "Alexander? That sounds so confident... I like the name, but I don't think it's for me."
            jump menu_name_select
        "Ponty?" if bk_age == "middle" and not name3_asked:
            $ name3_asked = True
            $ names_asked.append("Ponty")
            if bk_demeanor == "nonchalant":
                show barkeeper sweatsmile
                b "Ponty? Do I look like I'm so adorable? No, no, I don't think it fits me. Way too cute of a name for me!"
            elif bk_demeanor == "calm":
                show barkeeper slightsmile
                b "Ponty is a nice name, but I don't think it fits me."
            else:
                show barkeeper shockblush
                b "Oh, I like that name! It sounds perfect for me! Ponty. Yes, Ponty it is! Thank you!"
                $ bk_name = "Ponty"
                jump name_suggestion_done
            jump menu_name_select

        "Maurice?" if bk_age == "young" and not name1_asked:
            $ name1_asked = True
            $ names_asked.append("Maurice")
            if bk_demeanor == "nonchalant":
                show barkeeper blushsmile
                b "Maurice? I dig that name! A lot! You can call me Maurice, if you want!"
                $ bk_name = "Maurice"
                jump name_suggestion_done
            elif bk_demeanor == "calm":
                show barkeeper sweatsmile
                b "Hmm, that name's kinda cool, but I don't vibe with it. But thanks for the suggestion!"
            else:
                show barkeeper shocksweat
                b "Maurice? Hmm, no... That's a much too cool name for me."
            jump menu_name_select
        "Casey?" if bk_age == "young" and not name2_asked:
            $ name2_asked = True
            $ names_asked.append("Casey")
            if bk_demeanor == "nonchalant":
                show barkeeper smile
                b "Casey is a neat name, but I feel like it doesn't suit me. Do you have any other ideas?"
            elif bk_demeanor == "calm":
                show barkeeper blush
                b "Casey? That's got a nice ring to it. I like it! Call me Casey, if you want!"
                $ bk_name = "Casey"
                jump name_suggestion_done
            else:
                show barkeeper sweatsmile
                b "Casey is a nice name. But it sounds like someone who's way more composed than me, if you get what I mean?"
            jump menu_name_select
        "Noel?" if bk_age == "young" and not name3_asked:
            $ name3_asked = True
            $ names_asked.append("Noel")
            if bk_demeanor == "nonchalant":
                show barkeeper sweatsmile
                b "Mmmh no, Noel doesn't fit my vibe. Nice name, but like, not for me."
            elif bk_demeanor == "calm":
                show barkeeper slightsmile
                b "Noel is a lovely name, but I think it's for someone who's softer-spoken than me. Do you have any other suggestions?"
            else:
                show barkeeper shockblush
                b "Ohh, Noel? I like it! I think that's a good fit! You can call me Noel, if you want!"
                $ bk_name = "Noel"
                jump name_suggestion_done
            jump menu_name_select
        "...(Type a name)..." if can_type_name:
            $ new_name = renpy.input("Suggest a name for the barkeeper:", length=32).strip()
            if new_name:
                if new_name in names_asked:
                    show barkeeper sweatsmile
                    b "I think you've suggested that one before."
                    jump menu_name_select
                elif new_name == "Bruno":
                    $ knows_name_bruno = True
                    show barkeeper shocked
                    menu:
                        b "Wait, how did you guess that?"
                        "What?":
                            pov "Guess {i}what{/i}? Is Bruno your actual name?"
                            b "It is, in fact!"
                            pov "No way! That's actually insane!"
                        "I just knew":
                            pov "That Bruno is your real name?"
                            b "Yes."
                            pov "I just knew. Instinctively!"
                            b "Wow!"
                            pov "Actually, a friend told me."
                            show barkeeper sweatsmile
                            b "I suspected as much. Word goes around in lofi town, doesn't it?"
                            pov "Yeah."
                    jump menu_choose_bruno_or_not

                $ names_asked.append(new_name)
                $ random = renpy.random.randint(0, 4)
                if random == 0 or random == 1:
                    show barkeeper smile
                    menu:
                        b "You're right, this name fits me much better. You can choose what you want to call me, [bk_name] or [new_name]."
                        "[bk_name]":
                            pov "Nah, I was joking. Let's stick with [bk_name]."
                            show barkeeper sweatsmile
                            b "Sure, whatever."
                            jump name_done
                        "[new_name]":
                            pov "Yeah, I like [new_name] better too!"
                            $ bk_name = new_name
                            show barkeeper blushsmile
                            b "Then [new_name] it is."
                            jump name_done
                        "Try another name":
                            pov "No, hang on, I can come up with something even better."
                            show barkeeper shockblush
                            b "Okay, I'm curious!"
                            jump menu_name_select
                elif random == 2:
                    show barkeeper sweatsmile
                    b "I don't know. I don't think this one's as good as [bk_name]. Can you think of another one?"
                    jump menu_name_select
                elif random == 3:
                    show barkeeper sweatsmile
                    b "I... am not sure that one suits me. I think I prefer [bk_name]. But you could try coming up with something else?"
                    jump menu_name_select
                else:
                    show barkeeper sweatsmile
                    b "Nice suggestion, but I don't think that fits me. Do you have any other suggestions?"
                    jump menu_name_select
        "Stick with [bk_name]" if can_type_name:
            pov "Well, I think [bk_name] is the best I can come up with. It suits you!"
            show barkeeper blushsmile
            b "It does! I like it!"
            jump name_done


label name_suggestion_done:
    show barkeeper smile
    pov "Oh wow, I didn't actually expect you to like the name I chose."
    show barkeeper shockblush
    menu:
        b "Why, did you have more suggestions in mind?"
        "Keep the name [bk_name].":
            show barkeeper blushsmile
            pov "No, I think [bk_name] is great."
            b "It is indeed!"
            jump name_done
        "Change the name":
            show barkeeper modestblush
            pov "Let me come up with something else."
            b "Alright, try me!"
            $ can_type_name = True
            jump menu_name_select

label name_done:
    show barkeeper blushsmile
    pov "Thank you for the [drink_type], [bk_name]. It was a pleasure!"
    b "Likewise! Nice to meet you ...! "
    show barkeeper shockblush
    extend "Now I only need {i}your{/i} name."
    show barkeeper blush
    pov "Oh, I'm..."
    $ pov_name = ''
    while not pov_name:
        $ pov_name = renpy.input("Enter your name:", length=32).strip();
    pov "Oh, I'm {fast}[pov_name]."
    if bk_name == 'Bruno' or knows_name_bruno:
        show barkeeper smile
        b "Nice to meet you, [pov_name]."
        pov "Nice to meet you too, [bk_name]."
        jump end
    else:
        show barkeeper smile
        b "Nice to meet you, [pov_name]."
        show barkeeper wink
        extend " I'm Bruno."
        show barkeeper smile
        pov "Wait... what? I thought ..."
        show barkeeper wink
        jump menu_choose_bruno_or_not


menu menu_choose_bruno_or_not:
    b "But you can keep calling me [bk_name] if you want."
    "Use Bruno":
        show barkeeper smile
        pov "No, I think it's more respectful to call you Bruno. But the name choosing was fun!"
        $ bk_name = "Bruno"
        b "That works for me!"
        jump end
    "Use [bk_name]":
        show barkeeper smile
        pov "If that's alright, I'll stick with [bk_name]. It'll be funny to explain that to anyone else."
        show barkeeper blushsmile
        b "Go ahead! I'm sure it will!"
        jump end

label end:
    show barkeeper neutral
    "You see someone else walk up to the bar and decide to not keep [bk_name] busy for longer."
    pov "Alright, I should get going. See you around, [bk_name]!"
    show barkeeper blushsmile
    b "Bye [pov_name]! [bye_text]"
    pov "Thanks! Have a nice one!"
    if drink_container == "cup":
        "You make your way out of the coffee shop with your hot cup in your hands and a smile on your face."
    else:
        "Smiling, you make your way to a table in the coffee shop, carefully balancing your tray with your drink."
    "And you know it'll be a good day."

    # This ends the game.
    return
