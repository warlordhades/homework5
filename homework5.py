import pgzrun

WIDTH = 600
HEIGHT = 400

left_click_actor = Actor('alien')
right_click_actor = Actor('hero')

def draw():
    screen.clear()
    left_click_actor.draw()
    right_click_actor.draw()

def on_mouse_down(pos, button):
    if button == mouse.RIGHT:
        right_click_actor.pos = pos

        
    elif button == mouse.LEFT:
        left_click_actor.pos = pos

pgzrun.go()
