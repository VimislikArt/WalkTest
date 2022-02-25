##======================================================================
#                               UNIVERSAL CALLS FOR AREAS!
##======================================================================

#screen that allows mouse location pulls
screen hallway_checkMouse():
    if standWalk==0:
        key "mousedown_1" action Jump("hallway_checkDist")

# Extrapolates Location information from mouse input, and applies to area variables.
label hallway_checkDist:
    # Pulling mouse click position
    $ mX=renpy.get_mouse_pos()[0]
    $ mY=renpy.get_mouse_pos()[1]

    # sX represents the "true" position of the character
    # against the full background
    if mX >= sX:
        $ sX_add = (mX-sX)
        $ sX_coord = sX_coord + sX_add
    else:
        $ sX_add = (sX-mX)
        $ sX_coord = sX_coord - sX_add

    # Sets the speed of the character
    $ bmX_speed = sX_add

    if mY > maxY:
        $ mY = maxY
    if mY < minY:
        $ mY = minY

    # Sets maximum coordinates
    if location == "Market_Chapter1" and sX_coord < (-4*mY) + 2800:
        if mX < sX:
            $ mY = 562
            $ sX_coord = 432
        #else:
        #    jump Market_Chapter1_mod_continue
        #$ sX_coord = (-4*mY) + 2700 #(-4*mY) + 2600 #2800

    if sX_coord <= 0:
        $ sX_coord = 0
    if sX_coord >= max_bg_dimension:
        $ sX_coord = max_bg_dimension

    # Once the character reaches the center of the screen,
    # the character stays at position X, until it hits the last
    # half screen length of the background
    if sX_coord < Xcenter:
        $ Xmove = sX_coord
        if mX < sX and bmX < 0:
            $ bmX = 0

    elif sX_coord >= Xcenter and sX_coord <= Xcenter_right:
        $ Xmove = Xcenter
        if mX >= Xcenter:
            $ bmX=bsX-(mX-Xcenter)
        if mX < Xcenter:
            $ bmX=bsX+(Xcenter-mX)

    else:
        $ bmX = max_bsX
        $ Xmove = mX

    if bmX <= max_bsX:
        $ bmX=max_bsX
    if bmX >= min_bsX:
        $ bmX=min_bsX

    # Establishes fake Z coordinates of character
    # (Shrinks character as they walk towards the horizon)
    $ mZ_fractdist = (mY-minY) / (Zdist*1.0)
    $ mZ_bg1_yzoomadjust = 1.0 - mZ_fractdist
    $ mZ = (mZ_fractdist*Zratio) + 1.0

    # Activates the correct character direction while walking,
    # sets a walking speed when the character moves a short distance

    if mX >= sX:
        $ direction = right
        if bmX_speed > 200:
            show gamerwalk run_right
            jump run_directory
        else:
            call ypos_speedlimit from _call_ypos_speedlimit
            show gamerwalk walk_right_chapter4
            jump walk_directory

    else:
        $ direction = left
        if bmX_speed > 200:
            show gamerwalk run_left
            jump run_directory
        else:
            call ypos_speedlimit from _call_ypos_speedlimit_1
            show gamerwalk walk_left_chapter4
            jump walk_directory

# Reduces speed based on y positioning
label ypos_speedlimit:
    # This keeps the character from jumping too fast
    # forward and back when they don't move a long
    # distance along X
    if sY >= mY:
        if (sY-mY) > 200:
            $ bmX_speed=(sY-mY)*1.8
    else:
        if (mY-sY) > 200:
            $ bmX_speed=(mY-sY)*1.8
    return

label universal_postmovement_calibration:
    hide pointclick
    $ sX=Xmove
    $ sY=mY
    $ sZ=mZ
    $ bsX=bmX
    return

# Use this when entering area from another area
label new_scene_placement:
    # sX represents the "true" position of the character
    # against the full background
    if mX >= sX:
        $ sX_add = (mX-sX)
        $ sX_coord = sX_coord + sX_add
    else:
        $ sX_add = (sX-mX)
        $ sX_coord = sX_coord - sX_add

    # Sets the speed of the character
    $ bmX_speed = sX_add

    # Once the character reaches the center of the screen,
    # the character stays at position X, until it hits the last
    # half screen length of the background
    if sX_coord < Xcenter:
        $ Xmove = sX_coord
        if mX < sX and bmX < 0:
            $ bmX = 0

    elif sX_coord >= Xcenter and sX_coord <= Xcenter_right:
        $ Xmove = Xcenter
        if mX >= Xcenter:
            $ bmX=bsX-(mX-Xcenter)
        if mX < Xcenter:
            $ bmX=bsX+(Xcenter-mX)

    else:
        $ bmX = max_bsX
        $ Xmove = mX

    if bmX <= max_bsX:
        $ bmX=max_bsX
    if bmX >= min_bsX:
        $ bmX=min_bsX

    # Establishes fake Z coordinates of character
    # (Shrinks character as they walk towards the horizon)
    $ mZ_fractdist = (mY-minY) / (Zdist*1.0)
    $ mZ_bg1_yzoomadjust = 1.0 - mZ_fractdist
    $ mZ = (mZ_fractdist*Zratio) + 1.0

    return

# Checks the various clickable areas
label areacheck:
    if location == "test":
        call hallway_test_areacheck
    elif location == "Market_Chapter1":
        call Market_Chapter1_test_areacheck
    elif location == "Residence_Chapter1":
        call Residence_Chapter1_test_areacheck
    return

label walk_directory:
    if location == "test":
        jump hallway_walk
    elif location == "Market_Chapter1":
        jump Market_Chapter1_walk
    elif location == "Residence_Chapter1":
        jump Residence_Chapter1_walk
    return

label run_directory:
    if location == "test":
        jump hallway_run
    elif location == "Market_Chapter1":
        jump Market_Chapter1_run
    elif location == "Residence_Chapter1":
        jump Residence_Chapter1_run
    return

##======================================================================
#                               TEST AREA
##======================================================================
label hallway:
    # Sets initial coordinates of the character
    # Z determines the base size
    $ location = "test"
    $ direction = right
    $ sX=640
    $ sY=500
    $ sZ=1.0
    $ sX_coord=sX

    # Sets maximum dimensions for the available walking space
    $ minX=0
    $ maxX=1280
    $ minY=500
    $ maxY=850
    $ Zdist=maxY-minY

    # Sets values for the size of the background
    $ bmX=0
    $ bsX=0
    $ Xcenter=640
    $ max_bg_dimension=2560
    $ Xcenter_right = (max_bg_dimension-640)
    $ max_bsX=(-(max_bg_dimension))+1280
    #$ max_bsX=-1280
    $ min_bsX=0

    # This determines the smallest the character will get as it goes back
    $ Zratio=0.5

    # Change runspeed to make the character move faster or slower
    $ runspeed=320.0
    $ walkspeed=runspeed/2.0

    show back1:
        xpos 0
    show bg grey onlayer master:
        subpixel True xpos None ypos 478
    #call clickeffect_parse
    show gamerwalk idle_left_chapter4:
        xanchor char_xanchor yanchor char_yanchor xpos sX ypos sY
    show front1:
        xpos 0

    show screen hallway_checkMouse

label hallway_stand:

    if direction == right:
        show gamerwalk idle_right_chapter4:
            xanchor char_xanchor yanchor char_yanchor ypos sY zoom sZ
    elif direction == left:
        show gamerwalk idle_left_chapter4:
            xanchor char_xanchor yanchor char_yanchor ypos sY zoom sZ

    #checks to see if character ran into an interactable area
    call areacheck from _call_areacheck

    #resets character back if area check conditions are called
    if direction == right:
        show gamerwalk idle_right_chapter4:
            xanchor char_xanchor yanchor char_yanchor ypos sY zoom sZ
    elif direction == left:
        show gamerwalk idle_left_chapter4:
            xanchor char_xanchor yanchor char_yanchor ypos sY zoom sZ

    $ standWalk=0

    $ renpy.pause(hard=True)

label hallway_walk:
    $ standWalk=1

    show pointclick click behind gamerwalk:
        xanchor 0.5 yanchor 0.5 ypos mY xpos mX
        linear bmX_speed/200.0 xpos Xmove

    show gamerwalk:
        ypos sY zoom sZ
        linear bmX_speed/200.0 ypos mY zoom mZ xpos Xmove
    show back1:
        linear bmX_speed/200.0 xpos bmX
    show front1:
        linear bmX_speed/200.0 xpos bmX

    $ renpy.pause(bmX_speed/200.0, hard=True)
    call universal_postmovement_calibration
    jump hallway_stand

label hallway_run:
    $ standWalk=1

    show pointclick click behind gamerwalk:
        xanchor 0.5 yanchor 0.5 ypos mY xpos mX
        linear bmX_speed/500.0 xpos Xmove

    show gamerwalk:
        ypos sY zoom sZ
        linear bmX_speed/500.0 ypos mY zoom mZ xpos Xmove

    show back1:
        linear bmX_speed/600.0 xpos bmX
    show front1:
        linear bmX_speed/600.0 xpos bmX

    $ renpy.pause(bmX_speed/600.0, hard=True)
    call universal_postmovement_calibration
    if direction == right:
        show gamerwalk stop_right_chapter4:
            xanchor char_xanchor yanchor char_yanchor ypos sY zoom sZ
    elif direction == left:
        show gamerwalk stop_left_chapter4:
            xanchor char_xanchor yanchor char_yanchor ypos sY zoom sZ

    $ renpy.pause(0.1, hard=True)

    jump hallway_stand

label hallway_test_areacheck:
    if sX_coord > 1000 and sX_coord < 1200:
        if sY == 500:
            if direction == right:
                show gamerwalk idle_right_chapter4_pause:
                    blur 5
            elif direction == left:
                show gamerwalk idle_left_chapter4_pause:
                    blur 5
            show blackout:
                alpha 0.5
            call gradient_gamer from _call_gradient_gamer_5
            show back1:
                blur 5
            show bg:
                blur 5
            show front1:
                blur 5
            show gamerconvo question onlayer master:
                subpixel True xpos 0.0 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.91 rotate None
                ease 0.2 xpos 0.75
            show wordballoon1:
                subpixel True xpos 0.09 ypos 0.61 xanchor None yanchor None zoom 0.6 rotate None
            a "{color=000}Wait, this looks like this is outside the testing area...  I can't leave here...{/color}"
            show gamerconvo question:
                ease 0.2 xpos 0.0
            $ renpy.pause(0.2)
            hide gamerconvo
            show gamerwalk:
                blur 0
            show back1:
                blur 0
            show front1:
                blur 0
            call gradient_gone
            show bg:
                blur 0
            hide wordballoon1
            hide blackout
    return
