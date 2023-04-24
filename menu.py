import pygame
import pygame_menu
from pygame_menu import themes

pygame.init()

WIDTH = 1500
HEIGHT = 1000
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

#VALUES = [PAPER, ROCK, SCISSORS, SIZES]
VALUES = [5, 5, 5, 50, 0]

def set_value(value, id):

    
    obj_id = value[0][1]
    
    
    if obj_id == 1:
        VALUES[0] = int(value[0][0])

    elif obj_id == 2:
        VALUES[1] = int(value[0][0])

    elif obj_id == 3:
       VALUES[2] = int(value[0][0])

    elif obj_id == 4:
        txt = value[0][0]

        if txt == 'Small':
        
            VALUES[3] = 30

        elif txt == 'Medium':
        
            VALUES[3] = 50
            
        elif txt == 'Big':
        
            VALUES[3] = 70
    
    elif obj_id == 5:
        txt = value[0][0]

        if txt == 'Slow':
        
            VALUES[4] = 1
            
        elif txt == 'Fast':
        
            VALUES[4] = 5
        elif txt == 'Very Fast':
        
            VALUES[4] = 10
    

#main menu starter 
def start_main_menu():
    mainmenu._open(loading)
    pygame.time.set_timer(update_loading, 5)

#menu to set amount and sizes
def settings_menu():
    mainmenu._open(settings)
 

mainmenu = pygame_menu.Menu('Welcome', WIDTH, HEIGHT, theme=themes.THEME_DARK)
mainmenu.add.button('Play', settings_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)
 

settings = pygame_menu.Menu('Play', WIDTH, HEIGHT, theme=themes.THEME_DARK)
settings.add.selector('Rock :', [('5', 2), ('10', 2), ('15', 2), ('20', 2), ('25', 2), ('50', 2)], onchange=set_value)
settings.add.selector('Paper :', [('5', 1), ('10', 1), ('15', 1), ('20', 1), ('25', 1), ('50', 1)], onchange=set_value)
settings.add.selector('Scissors :', [('5', 3), ('10', 3), ('15', 3), ('20', 3), ('25', 3), ('50', 3)], onchange=set_value)
settings.add.selector('Size :', [('Small', 4), ('Medium', 4), ('Big', 4)], onchange=set_value)
settings.add.selector('Speed :', [('Random', 5), ('Slow', 5), ('Fast', 5), ('Very Fast', 5)], onchange=set_value)
settings.add.button('Play', start_main_menu)
 

#creates a loading animation
loading = pygame_menu.Menu('Loading...', WIDTH, HEIGHT, theme=themes.THEME_DARK,)
loading.add.progress_bar("", progressbar_id = "1", default=0, width = 1000, )
update_loading = pygame.USEREVENT + 0

#arrow to get back
arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (15, 15))

# music usage
musicOne = pygame.mixer.Sound('audio1.mp3')
musicOne.set_volume(0.1)


def startMenu(winner):
    
    #text to show the winner
    text_surface = pygame.font.Font('freesansbold.ttf', 60).render(f'Winner is {winner}', True, (255, 255, 255, 180))
    text_width, text_height = text_surface.get_size()
    text_x = (WIDTH - text_width) // 2
    text_y = 200
    
    while True:

        musicOne.play()

        events = pygame.event.get()

        for event in events:
            
            #this is for loading, every loop it increments the loading status by one and
            #then redirects to game when 100 hits
            #stops the music and also sends values for object amounts and size
            #for game file
            if event.type == update_loading:
                
                progress = loading.get_widget("1")
                progress.set_value(progress.get_value() + 1)
   
                if progress.get_value() == 100:

                    pygame.time.set_timer(update_loading, 0)
                    progress.set_value(0)
                    mainmenu.full_reset()
                    musicOne.stop()
                    return VALUES

            #helps to close the play menu
            if event.type == pygame.KEYDOWN and  event.key == pygame.K_ESCAPE:
                settings.full_reset()
                       
                    
            if event.type == pygame.QUIT:
                exit()
        
        #draws the main menu and arrow
        if mainmenu.is_enabled():

            mainmenu.update(events)
            mainmenu.draw(WINDOW)

            if (mainmenu.get_current().get_selected_widget()):
                arrow.draw(WINDOW, mainmenu.get_current().get_selected_widget())
        
            if len(winner) > 0:
                WINDOW.blit(text_surface, (text_x, text_y ))

        pygame.display.update()

    


