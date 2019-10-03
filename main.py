# -*- coding: utf-8 -*-
from automator import Automator
from target import TargetType

if __name__ == '__main__':
    # 声明货物要移动到的建筑 ID 。
    targets = {
        # TargetType.Chair: 1,
        # TargetType.Box: 1,
        # TargetType.Cotton: 7,
        # TargetType.Dogfood: 2,
        # TargetType.Sofa: 3,
        # TargetType.Plant: 3,
        # TargetType.Microphone: 4,
        # TargetType.Shoes: 5,
        # TargetType.Chicken: 6,
        # TargetType.Bottle: 4,
        # TargetType.Vegetable: 5,
        # TargetType.Food: 8,
        # TargetType.Book: 5,
        # TargetType.Bag: 6,
        # TargetType.Wood: 7,
        # TargetType.Oil: 8,
        # # TargetType.Food: 8,
        # TargetType.Iron: 8,
        # TargetType.Grass:9,
        # TargetType.Tool: 8,
        # TargetType.Quilt: 9,
    }

    goodInstMap = {
        TargetType.Shoes: 'shangmao',
        # TargetType.Bag:  '',
        # TargetType.Book:  '',
        # TargetType.Bottle:  '',
        # TargetType.Box:  '',
        # TargetType.Chair:  '',
        # TargetType.Chicken:  '',
        # TargetType.Coal:  '',
        # TargetType.Computer:  '',
        TargetType.Cotton: 'fangzhichang',
        TargetType.Dogfood: 'huayuanyangfang',
        TargetType.Food:  'shipinchang',
        # TargetType.Grass:  '',
        # TargetType.Honor:  '',
        # TargetType.Iron:  '',
        TargetType.Microphone: 'meiti',
        # TargetType.Oil:  '',
        # TargetType.Plant:  '',
        # TargetType.Quilt:  '',
        # TargetType.Screw:  '',
        # TargetType.Sofa:  '',
        TargetType.Tool:  'qiejixie',
        # TargetType.Tree:  '',
        # TargetType.Vegetable:  '',
        # TargetType.Wood: '', 
        TargetType.chenshan: 'fuzhuang',
        TargetType.xiangzi: 'xiaoxinggongyu',
        TargetType.tanzi: 'fuxinggongguan'
    }

    location2shop = {
        'xiaoxinggongyu': 1,
        'huayuanyangfang': 2,
        'fuxinggongguan': 3,
        'fuzhuang': 4,
        'shangmao': 5,
        'meiti': 6,
        'fangzhichang': 7,
        'shipinchang': 8,
        'qiejixie': 9,
        '': 1
    }

    for key in goodInstMap:
        targets[key] = location2shop[goodInstMap[key]]

    #print(targets)

    # 连接 adb ，MuMu 模拟器默认 adb 控制链接为 127.0.0.1:7555 。
    instance = Automator('127.0.0.1:7555', targets)

    # 启动脚本。
    instance.start()
