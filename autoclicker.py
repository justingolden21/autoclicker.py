import pyautogui as gui, time

gui.FAILSAFE = True

# get position:
# user enters number of seconds to wait before getting position
# prog then gets position and alerts user
#
# click mouse
# user enters position
# user enters left, right, double click (nah)
# user enters number of clicks
# user enters interval
# 
# hold mouse
# user enters position
# user enters left, right, or double click (nah)
# user enters number of seconds
# 
# keep looping through options until user clicks exit

# emergency kill program?
# add keys too
# error check for coords off screen ir non int, too large
# remember prev coords
#two input boxes in one prompt for x y
#help button (top left is 0,0), how to use prog, can hit enter key instead of ok, move to corner of screen to fail safe exit prog
#quick run option where you hover position then click at that position
#export prog with libraries
#typewriter mode too
#tell them how to autokill program
#remember previous instruction and do that option?
#option to autoclick wihtout moving mouse to coords


while True:

    result = gui.confirm(text='Select an option:', title='Autoclicker', buttons=['Get Position', 'Click Mouse', 'Hold Mouse', 'Exit'])
    print(result)
    if result == 'Exit' or result == None:
        break

    if result == 'Get Position':
        result = gui.prompt('Wait how many seconds before getting position?')
        print(result)
        if result == None:
            continue
        time.sleep(int(result) )
        pos = gui.position()
        print(pos.x)
        gui.confirm(text='Mouse Position was ' + str(pos.x) + ',' + str(pos.y), buttons=['Ok'])

    if result == 'Click Mouse':
        x = gui.prompt('Enter X position')
        if x == None:
            continue
        y = gui.prompt('Enter Y position')
        if y == None:
            continue
        num_clicks = gui.prompt('Enter number of clicks')
        if num_clicks == None:
            continue
        click_interval = gui.prompt('Enter click interval in seconds')
        if click_interval == None:
            continue
        init_delay = gui.prompt('Enter number of seconds to wait before starting')
        if init_delay == None:
            continue
        time.sleep(float(init_delay) )
        gui.click(int(x), int(y), int(num_clicks), float(click_interval) )

    if result == 'Hold Mouse':
        x = gui.prompt('Enter X position')
        if x == None:
            continue
        y = gui.prompt('Enter Y position')
        if y == None:
            continue
        num_sec = gui.prompt('Enter number of seconds to hold mouse')
        if num_sec == None:
            continue
        init_delay = gui.prompt('Enter number of seconds to wait before starting')
        if init_delay == None:
            continue
        time.sleep(init_delay)
        gui.moveTo(int(x), int(y) )
        gui.mouseDown()
        time.sleep(float(init_delay) )
        gui.mouseUp()






print('Program Terminated')
