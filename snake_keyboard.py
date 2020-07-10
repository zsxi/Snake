import pygame
import sys
import random
import time
import csv

from pygame.locals import *  # 从pygame模块导入常用的函数和常量

# 定义颜色变量
black_colour = pygame.Color(30, 30, 30)
white_colour = pygame.Color(255, 255, 255)
red_colour = pygame.Color(255, 0, 0)
grey_colour = pygame.Color(150, 150, 150)
yellow_color = pygame.Color(255,224,141)
# 窗口大小
screenLength = 640
screenHeight = 480
# 前进速度控制
game_speed = 8
s_num = 0 # 数量
data_list = []
# 分数
score = 0

# 是否结束游戏
GameOver_state = 0
def game_init():
    global game_speed
    global s_num
    global score
    global data_list

    game_speed = 8
    s_num = 0
    score = 0
    data_list = []

# 定义游戏结束函数
def GameOver(gamesurface, time_start, time_end):
    global score
    global data_list
    global s_num
    # 时间和分数数据的写入
    t = time.strftime('%H:%M:%S', time.localtime(time.time()))
    time_cost = "{:.2f}".format(time_end - time_start)
    final_score = str(score)
    data = [t, time_cost, final_score, s_num, "effective", data_list] # test为测试， effective 为实验
    with open("data/keyboard_data.csv", 'a+') as f:
        csv_write = csv.writer(f)

        csv_write.writerow(data)


    # print('time cost', time_end - time_start, 's')

    # 设置提示字体的格式
    GameOver_font = pygame.font.Font(r"fonts/abc.ttf", 120)
    score_display_font = pygame.font.Font(r"fonts/abc.ttf", 60)
    score_display_colour = score_display_font.render(u'分数：%d' % score, True, yellow_color)
    # 设置提示字体的颜色
    GameOver_colour = GameOver_font.render('Game Over', True, yellow_color)
    # 设置提示位置
    GameOver_location = GameOver_colour.get_rect()
    GameOver_location.midtop = (screenLength/2, 10)
    # 绑定以上设置到句柄
    gamesurface.blit(GameOver_colour, GameOver_location)
    gamesurface.blit(score_display_colour, (screenHeight/2, 240) )
    # 提示运行信息
    pygame.display.flip()

    # 初始化
    game_init()

    # 休眠5秒
    time.sleep(3)

    # 退出游戏
    #pygame.quit()
    # 退出程序
    #sys.exit()

def game(ftpsClock):
    global game_speed
    global s_num
    global score
    global data_list

    # 创建一个窗口
    gamesurface = pygame.display.set_mode((screenLength, screenHeight))
    # 设置窗口的标题
    pygame.display.set_caption('贪吃蛇 v1.0')
    # 初始化变量
    # 初始化贪吃蛇的起始位置
    snakeposition = [100, 100]
    # 初始化贪吃蛇的长度
    snakelength = [[100, 100], [80, 100], [60, 100]]
    # 初始化目标方块的位置
    square_purpose = [300, 300]
    # 初始化一个数来判断目标方块是否存在
    square_position = 1
    # 初始化方向，用来使贪吃蛇移动
    derection = "right"
    change_derection = derection

    Snake_font = pygame.font.Font(r"fonts/abc.ttf", 120)
    keyboard_font = pygame.font.Font(r"fonts/abc.ttf", 62)
    Snake_colour = Snake_font.render(u'贪吃蛇', True, yellow_color)
    keyboard_color = keyboard_font.render(u'键盘版', True, grey_colour)
    gamesurface.blit(keyboard_color, (screenLength / 2,120))
    Snake_location = Snake_colour.get_rect()
    Snake_location.midtop = (screenLength / 2, 15)

    gamesurface.blit(Snake_colour, Snake_location)
    start = pygame.image.load("images/start.jpg").convert_alpha() # 200 * 80

    gamesurface.blit(start, (screenLength / 2 - 100, screenHeight / 2 - 40))
    pygame.display.update()
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == QUIT:
                # 接收到退出事件后，退出程序
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 检测鼠标点击事件
                mouse_x, mouse_y = pygame.mouse.get_pos()  # get_pos()返回一个单击时鼠标的xy坐标
                active = False
    time.sleep(0.5)
    time_start = time.time()
    while True:

        # 检测按键等pygame事件
        for event in pygame.event.get():
            if event.type == QUIT:
                # 接收到退出事件后，退出程序
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # 判断键盘事件,用w,s,a,d来表示上下左右
                if event.key == K_RIGHT or event.key == ord('d'):
                    change_derection = "right"
                if event.key == K_LEFT or event.key == ord('a'):
                    change_derection = "left"
                if event.key == K_UP or event.key == ord('w'):
                    change_derection = "up"
                if event.key == K_DOWN or event.key == ord('s'):
                    change_derection = "down"
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

                data_list.append(change_derection)

        # 判断移动的方向是否相反
        if change_derection == 'left' and not derection == 'right':
            derection = change_derection
        if change_derection == 'right' and not derection == 'left':
            derection = change_derection
        if change_derection == 'up' and not derection == 'down':
            derection = change_derection
        if change_derection == 'down' and not derection == 'up':
            derection = change_derection
        # 根据方向，改变坐标
        if derection == 'left':
            snakeposition[0] -= 20
        if derection == 'right':
            snakeposition[0] += 20
        if derection == 'up':
            snakeposition[1] -= 20
        if derection == 'down':
            snakeposition[1] += 20
        # 增加蛇的长度
        snakelength.insert(0, list(snakeposition))
        # 判断是否吃掉目标方块
        if snakeposition[0] == square_purpose[0] and snakeposition[1] == square_purpose[1]:
            square_position = 0
            score = score + game_speed
            s_num = s_num + 1
            if s_num % 5 == 0:
                game_speed = game_speed + 1

        else:
            snakelength.pop()
        # 重新生成目标方块
        if square_position == 0:
            # 随机生成x,y,扩大二十倍，在窗口范围内
            x = random.randrange(1, screenLength / 20)
            y = random.randrange(1, screenHeight / 20)
            while [int(x * 20), int(y * 20)] in snakelength:
                x = random.randrange(1, screenLength / 20)
                y = random.randrange(1, screenHeight / 20)
            square_purpose = [int(x * 20), int(y * 20)]
            square_position = 1
        # 绘制pygame显示层
        gamesurface.fill(black_colour)
        for position in snakelength:
            pygame.draw.rect(gamesurface, white_colour, Rect(position[0], position[1], 20, 20))
            pygame.draw.rect(gamesurface, red_colour, Rect(square_purpose[0], square_purpose[1], 20, 20))
        score_font = pygame.font.Font('fonts/abc.ttf', 24)
        # gamesurface = score_font.render(u'当前得分', True, [255, 255, 255])
        # 刷新pygame显示层
        gamesurface.blit(score_font.render(u'当前得分：%d' % score, True, [255, 255, 255]), [20, 20])
        pygame.display.flip()

        # 判断是否死亡
        if snakeposition[0] < 0 or snakeposition[0] > screenLength:
            time_end = time.time()
            GameOver(gamesurface, time_start, time_end)
            GameOver_state = 1
            return
        if snakeposition[1] < 0 or snakeposition[1] > screenHeight:
            time_end = time.time()
            GameOver(gamesurface, time_start, time_end)
            GameOver_state = 1
            return
        for snakebody in snakelength[1:]:
            if snakeposition[0] == snakebody[0] and snakeposition[1] == snakebody[1]:
                time_end = time.time()
                GameOver(gamesurface, time_start, time_end)
                GameOver_state = 1
                return
        # 控制游戏速度

        speed = pygame.font.Font(r"fonts/abc.ttf", 16)
        speed_text = speed.render(str(game_speed), True, grey_colour)
        gamesurface.blit(speed_text, (20, 20))
        ftpsClock.tick(game_speed)

# 定义主函数
def main():
    # 初始化pygame，为使用硬件做准备
    pygame.init()
    pygame.time.Clock()
    ftpsClock = pygame.time.Clock()
    while GameOver_state == 0:
        game(ftpsClock)
        if GameOver_state == 1:
            GameOver_state == 0
            game(ftpsClock)



if __name__ == "__main__":
    main()
