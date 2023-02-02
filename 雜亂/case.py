TOP = 0
RIGHT = "你好"
LEFT = 2
UP = 3
DOWN = 4

action = RIGHT

match action:
    case 0:
        print('播放停止動畫')
    case "你好":
        print('播放向右動畫')
    case 2:
        print('播放向左動畫')
    case 3:
        print('播放向上動畫')
    case 4:
        print('播放向下動畫')
    case _:
        print('不支援此動作')