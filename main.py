#pgzero
import random

WIDTH = 600 # Ширина окна
HEIGHT = 400 # Высота окна

TITLE = "Стрела света" # Заголовок окна игры
FPS = 30 # Количество кадров в секунду

#объектs
sdragon = Actor('sdragon2', (300, 200))
menu = Actor('bonus', (300, 100))
archer = Actor('archer2', (300, 200))
floor = Actor('floor2')
cont = Actor('bonus', (300, 300))
back = Actor('bonus', (300, 300))
archer.health = 50

#переменные
mode = 'menu'
win = 0
#отрисовка
def draw():
    if mode == 'game':
        screen.fill("#2f3542")
        floor.draw()
        archer.draw()
        screen.draw.text(archer.health, center=(500, 370), color = 'green', fontsize = 20)
        screen.draw.text('HP:', center=(450, 370), color = 'green', fontsize = 20)
        for i in range(len(enemies)):
            enemies[i].draw()
            screen.draw.text(enemies[i].health, center=(enemies[i].x - 30, enemies[i].y - 40), color = 'green', fontsize = 20)
            screen.draw.text(enemies[i].attack, center=(enemies[i].x + 10, enemies[i].y - 40), color = 'red', fontsize = 20)
        for i in range(len(arrows)):
            arrows[i].draw()
        for i in range(len(arrowsr)):
            arrowsr[i].draw()
    elif mode == 'menu':
        screen.fill('black')
        menu.draw()
        cont.draw()
        screen.draw.text('Играть', center = (300, 90), color = 'black', fontsize = 30)
        screen.draw.text('Управление', center = (300, 290), color = 'black', fontsize = 30)
    elif mode == 'control':
        screen.fill('black')
        screen.draw.text('WASD - движение', center=(290, 100), color = 'white', fontsize = 20)
        screen.draw.text('Левый клик мыши - атака', center=(290, 200), color = 'white', fontsize = 20)
        back.draw()
        screen.draw.text('Вернуться', center = (300, 290), color = 'black', fontsize = 30)
    elif mode == "end":
        screen.fill("black")
        sdragon.draw()
        screen.draw.text("Поражение!", center=(WIDTH/2, HEIGHT/2), color = 'white', fontsize = 46)
        screen.draw.text("Нажмите Пробел для перезапуска", center=(WIDTH/2, 300), color = 'white', fontsize = 20)
    elif mode == 'win':
        screen.fill("black")
        sdragon.draw()
        screen.draw.text("Победа!", center=(WIDTH/2, HEIGHT/2), color = 'white', fontsize = 46)
        screen.draw.text("Нажмите Пробел для перезапуска", center=(WIDTH/2, 300), color = 'white', fontsize = 20)
    elif mode == 'level_2':
        screen.fill("#2f3542")
        floor.draw()
        archer.draw()
        screen.draw.text(archer.health, center=(500, 370), color = 'green', fontsize = 20)
        screen.draw.text('HP:', center=(450, 370), color = 'green', fontsize = 20)
        for i in range(len(enemies)):
            enemies[i].draw()
            screen.draw.text(enemies[i].health, center=(enemies[i].x - 30, enemies[i].y - 40), color = 'green', fontsize = 20)
            screen.draw.text(enemies[i].attack, center=(enemies[i].x + 10, enemies[i].y - 40), color = 'red', fontsize = 20)
        for i in range(len(arrows)):
            arrows[i].draw()
        for i in range(len(arrowsr)):
            arrowsr[i].draw()
    elif mode == 'level_3':
        screen.fill("#2f3542")
        floor.draw()
        archer.draw()
        screen.draw.text(archer.health, center=(500, 370), color = 'green', fontsize = 20)
        screen.draw.text('HP:', center=(450, 370), color = 'green', fontsize = 20)
        for i in range(len(enemies)):
            enemies[i].draw()
            screen.draw.text(enemies[i].health, center=(enemies[i].x - 30, enemies[i].y - 40), color = 'green', fontsize = 20)
            screen.draw.text(enemies[i].attack, center=(enemies[i].x + 10, enemies[i].y - 40), color = 'red', fontsize = 20)
        for i in range(len(arrows)):
            arrows[i].draw()
        for i in range(len(arrowsr)):
            arrowsr[i].draw()
        
#отрисовка врагов
enemies = []
def enemy_spawn():
    for i in range(5):
        x = random.randint(1, 10) * 50
        y = random.randint(1, 3) * 70
        enemy = Actor("skeleton", topleft = (x, y))
        enemy.health = random.randint(10, 20)
        enemy.attack = random.randint(5, 10)
        enemies.append(enemy)
enemy_spawn()

#отрисовка стрел
arrowsr = []
arrows = []

#конец
def victory():
    global mode, win
    if (enemies == [] and archer.health > 0) and mode == 'game':
        mode = "level_2"
        win += 1
        for i in range(5):
            if mode == 'level_2':
                x = random.randint(1, 10) * 50
                y = random.randint(1, 3) * 70
                enemy = Actor("shadow2", topleft = (x, y))
                enemy.health = random.randint(15, 25)
                enemy.attack = random.randint(5, 10)
                enemies.append(enemy)
                
    if (enemies == [] and archer.health > 0) and mode == 'level_2':
        mode = "level_3"
        win += 1
        for i in range(5):
            if mode == 'level_3':
                x = random.randint(1, 10) * 50
                y = random.randint(1, 3) * 70
                enemy = Actor("monster", topleft = (x, y))
                enemy.health = random.randint(25, 35)
                enemy.attack = random.randint(15, 20)
                enemies.append(enemy)
                
    if (enemies == [] and archer.health > 0) and mode == 'level_3':
        mode = 'win'
        
    elif archer.health <= 0:
        mode = "end"
        win = -1
        
#управление
def on_key_down(key):
    global mode, enemies
    if (keyboard.left or keyboard.a) and archer.x > 50:
        archer.x -= 50
        archer.image = 'archerl2'
    elif (keyboard.right or keyboard.d) and archer.x < 550:
        archer.x += 50
        archer.image = 'archer2'
    elif (keyboard.up or keyboard.w) and archer.y > 50:
        archer.y -= 50
    elif (keyboard.down or keyboard.s) and archer.y < 350:
        archer.y += 50
    num = archer.collidelist(enemies)
    if num != -1:
        archer.health -= enemies[num].attack
    elif keyboard.space and (mode == 'end' or mode == 'win'):
        archer.health = 50
        enemies = []
        mode = 'game'
        enemy_spawn()

def update(dt):
    victory()
    if not (mode == 'menu' or mode == 'control'):
        for i in range(len(arrows)):
            if arrows[i].x < 0:
                arrows.pop(i)
                break
            else:
                arrows[i].x -= 20
        for i in range(len(arrowsr)):
            if arrowsr[i].x > 600:
                arrowsr.pop(i)
                break
            else:
                arrowsr[i].x += 20
        for i in range(len(enemies)):
            for j in range(len(arrows)):
                if arrows[j].colliderect(enemies[i]):
                    enemies[i].health -= 5
                    arrows.pop(j)
                    if enemies[i].health <= 0:
                        enemies.pop(i)
            for j in range(len(arrowsr)):
                if arrowsr[j].colliderect(enemies[i]):
                    enemies[i].health -= 5
                    arrowsr.pop(j)
                    if enemies[i].health <= 0:
                        enemies.pop(i)
        
#атака
def on_mouse_down(button, pos):
    global mode, arrowr, arrow
    if (button == mouse.LEFT and archer.image == 'archerl2') and not (mode == 'menu' or mode == 'control'):
        arrow = Actor('arrow3')
        arrow.pos = archer.pos
        arrows.append(arrow)
    elif (button == mouse.LEFT and archer.image == 'archer2') and not (mode == 'menu' or mode == 'control'):
        arrowr = Actor('arrowr3')
        arrowr.pos = archer.pos
        arrowsr.append(arrowr)
    elif menu.collidepoint(pos) and mode == 'menu' and button == mouse.LEFT:
        mode = 'game'
    elif cont.collidepoint(pos) and mode == 'menu' and button == mouse.LEFT:
        mode = 'control'
    elif back.collidepoint(pos) and mode == 'control' and button == mouse.LEFT:
        mode = 'menu'
