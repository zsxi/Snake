# Snake
python实现贪吃蛇，键盘操作和鼠标操作

## 贪吃蛇 v1.0 键盘版/鼠标版

开发环境：Windows 10 / python 3.6.8 / pyCharm 2018.2.4
所用到的库： pygame, sys, random, time, csv

一、snake_keyboard.py 为键盘版
    启动方式：cmd 进入sourse文件夹 运行python snake_keyboard.py
    玩法：键盘上、下、左、右 或 W A S D控制蛇的运动
    规则：点击开始游戏后即开始，当蛇的头部碰壁或碰到自己的身体即游戏结束。游戏初始速度为8，分数计算方式为没吃一个方块加上速度值的分数。score = score + speed。同时，每吃掉五个方块速度加一。

二、snake_mouse.py 为鼠标版
    启动方式：cmd 进入sourse文件夹 运行python snake_mouse.py
    玩法：当蛇朝着一个方向移动时，点击相对头部的位置来改变方向，例如：当蛇向上运动时，点击头部左侧即向左转，点击右侧向右转。
    规则：点击开始游戏后即开始，当蛇的头部碰壁或碰到自己的身体即游戏结束。游戏初始速度为8，分数计算方式为没吃一个方块加上速度值的分数。score = score + speed。同时，每吃掉五个方块速度加一。

