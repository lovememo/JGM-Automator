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
        # TargetType.Shoes: 'shangmao',
        # TargetType.Bag:  '',
        # TargetType.Book:  '',
        # TargetType.Bottle:  '',
        # TargetType.Box:  '',
        # TargetType.Chair:  '',
        TargetType.Chicken:  'minshizhai',
        # TargetType.Coal:  'dianchang',
        # TargetType.Computer:  'rencaigongyu',
        # TargetType.Cotton: 'fangzhichang',
        # TargetType.Dogfood: 'huayuanyangfang',
        # TargetType.Food:  'shipinchang',
        # TargetType.Grass:  '',
        # TargetType.Honor:  '',
        # TargetType.Iron:  '',
        TargetType.Microphone: 'meiti',
        TargetType.Oil:  'renminshiyou',
        # TargetType.Plant:  '',
        # TargetType.Quilt:  '',
        # TargetType.Screw:  '',
        # TargetType.Sofa:  '',
        TargetType.Tool:  'qiejixie',
        # TargetType.Tree:  '',
        # TargetType.Vegetable:  '',
        # TargetType.Wood: '', 
        # TargetType.chenshan: 'fuzhuang',
        # TargetType.xiangzi: 'xiaoxinggongyu',
        TargetType.tanzi: 'fuxinggongguan'
    }

    location2shop = {
        'xiaoxinggongyu': 2,
        'rencaigongyu': 3,
        'fuxinggongguan': 3,
        'shangmao': 5,
        'minshizhai': 5,
        'meiti': 6,
        'dianchang': 8,
        'renminshiyou': 8,
        'qiejixie': 9,
        '': 9
    }

   
    for key in goodInstMap:
        targets[key] = location2shop[goodInstMap[key]]

    #print(targets)

    # 连接 adb ，MuMu 模拟器默认 adb 控制链接为 127.0.0.1:7555 。
    instance = Automator('127.0.0.1:7555', targets)

    # upgrade_arr = [3, 5, 6]
    # upgrade_arr = [1,2,3,4,5,6,7,8,9]
    # upgrade_arr = [5]
    upgrade_arr = []
    onlineLayout = ['中式小楼', '人才公寓', '空中别墅',
                    '服装店',   '图书城',   '学校',
                    '纺织厂',    '造纸厂',  '电厂']
    
    
    # 启动脚本。
    #火车脚本
    # instance.start()
    #红包收集 0-小红包 1-中红包 2-大红包
    instance.collect_red_pack(0)
    #相册收集
    # instance.collect_photo(100)
    #在线挂机升级建筑
    # instance.online_upgrade(upgrade_arr)
    # instance.just_online()