# -*- coding: utf-8 -*-

from target import TargetType
from cv import UIMatcher
import uiautomator2 as u2
import time


def TIME():
    """
    时间输出工具函数。
    """
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


class Automator:
    def __init__(self, device, targets):
        """
        device: 如果是 USB 连接，则为 adb devices 的返回结果；如果是模拟器，则为模拟器的控制 URL 。
        """
        self.d = u2.connect(device)
        self.targets = targets
        self.count = 0
        
        # 开启 trainMode 即可实现每次搬运货物前自动启动应用，搬运后关闭应用，如此反复。
        # 由于启动需等待 40s ，所以默认是不开启 trainMode 的。
        self.trainMode = True
        self.harvestCount = 0

    def just_online(self):
        interval = 120
        while True:
            self.d.click(1, 1919)
            time.sleep(interval)
            self.d.click(490, 1825)
            time.sleep(interval)

    def online_upgrade(self, arr):
        self.d.app_start("com.tencent.jgm")
        time.sleep(10)
        self.d.click(1, 1919)
        time.sleep(2)
        # 1: (294, 1184),
        # 2: (551, 1061),
        # 3: (807, 961),
        # 4: (275, 935),
        # 5: (535, 810),
        # 6: (799, 687),
        # 7: (304, 681),
        # 8: (541, 568),
        # 9: (787, 447)
        while True:
            try:
                self.d.swipe(1, 1, 2, 2)
                time.sleep(2)
                self.complete_city_task(0)
                for i in range(180):
                    time.sleep(1)
                    self.d.click(807, 961)
                    if i%5 == 0:
                        self.d.click(294, 1184)
                        self.d.click(551, 1061)
                        self.d.click(275, 935)
                        self.d.click(535, 810)
                        self.d.click(799, 687)
                        self.d.click(304, 681)
                        self.d.click(541, 568)
                        self.d.click(787, 447)
                # self._swipe()
                time.sleep(2)
                self._upgrade_arr(arr, 3)
                # time.sleep(60)
            except Exception as e:
                print(e)
    def complete_city_task(self, i):
        # complete task
        time.sleep(2)
        print(i, "start complete task")
        print(i, "open task")
        self.d.click(170, 1608)
        time.sleep(2)
        print(i, "complete task")
        self.d.click(545, 1545)
        time.sleep(2)
        print(i, "quit task")
        self.d.click(10,10)
        time.sleep(2)

    def start(self):
        """
        启动脚本，请确保已进入游戏页面。
        """
        while True:
            try:
                # 由于此处鲁棒性在我本地测试不怎么好，所以个人推荐关闭 trainMode （一家之言）。 
                if self.trainMode:
                    self.d.app_start("com.tencent.jgm")
                    self.isHarvest = False
                    for i in range(28):
                        time.sleep(1)
                        if i%5 == 0:
                            self.d.click(275, 935)
                            self.d.click(551, 1061)
                            self.d.click(535, 810)
                        if (i+1)%19 == 0:
                            self.d.click(294, 1184)
                            self.d.click(807, 961)
                            self.d.click(799, 687)
                            self.d.click(304, 681)
                            self.d.click(541, 568)
                            self.d.click(787, 447)
                            self.complete_city_task(i)
                    self.d.click(1, 1919)

                self.d.click(1,1)
                time.sleep(1)
                # 获取当前屏幕快照
                screen = self.d.screenshot(format="opencv")
                is_empty = self._is_empty_train(screen)
                if is_empty and self.trainMode != True:
                    print(TIME(), 'train not found , swip and continue')
                    # self._swipe()
                    # time.sleep(12)
                    for i in range(12):
                        time.sleep(1)
                        if i%5 == 0:
                            self.d.click(275, 935)
                            self.d.click(551, 1061)
                            self.d.click(535, 810)
                        if i%11 == 0:
                            self.d.click(294, 1184)
                            self.d.click(807, 961)
                            self.d.click(799, 687)
                            self.d.click(304, 681)
                            self.d.click(541, 568)
                            self.d.click(787, 447)
                    continue
                print('is_empty_train', is_empty)
                if is_empty and self.trainMode:
                    self.d.app_stop("com.tencent.jgm")
                    time.sleep(2)
                    continue

                # 判断是否出现货物。
                count = 0
                for target in self.targets.keys():
                    if self._match_target(screen, target):
                        count = count + 1
                        print(count)
                    if count == 3:
                        print("3 times found, break..")
                        break

                print("at last")
                print(count)

                # 滑屏拾币
                self._swipe()
                
                # 取消注释下一行，即可实现对特定建筑的升级
                # self._upgrade(5, 10)
                # time.sleep(1)
                # self._upgrade(8, 10)
                # time.sleep(1)

                # 开启 trainMode 后，会输出当前货物的搬运成果，随后关闭应用。
                if self.trainMode:
                    self.count = self.count + 1
                    if self.isHarvest:
                        self.harvestCount = self.harvestCount + 1
                        print(TIME(), "get！", self.harvestCount/self.count)
                    else:
                        print(TIME(), "not get...", self.harvestCount/self.count)
                    self.d.app_stop("com.tencent.jgm")
                    time.sleep(2)
                
                # time.sleep(18)
            except Exception as e:
                print(e)

    def _swipe(self):
        """
        滑动屏幕，收割金币。
        """
        for i in range(3):
            # 横向滑动，共 3 次。
            sx, sy = self._get_position(i * 3 + 1)
            ex, ey = self._get_position(i * 3 + 3)
            self.d.swipe(sx, sy, ex, ey)

    def _upgrade(self, id, count):
        """
        升级指定建筑。
        """
        self.d.click(1000, 1100)
        time.sleep(2)
        sx, sy = self._get_position(id)
        self.d.click(sx, sy)
        time.sleep(2)
        for i in range(count):
            self.d.click(875, 1750)
            # time.sleep(0.)
        time.sleep(2)
        self.d.click(1000, 1100)
        time.sleep(2)

    def _upgrade_arr(self, arr, count):
        """
        升级指定建筑。
        """
        self.d.click(1000, 1100)
        time.sleep(2)
        for id in arr:
            sx, sy = self._get_position(id)
            self.d.click(sx, sy)
            time.sleep(2)
            for i in range(count):
                self.d.click(875, 1750)
            time.sleep(1)
        time.sleep(2)
        self.d.click(1000, 1100)
        time.sleep(2)

    @staticmethod
    def _get_position(key):
        """
        获取指定建筑的屏幕位置。
        """
        positions = {
            1: (294, 1184),
            2: (551, 1061),
            3: (807, 961),
            4: (275, 935),
            5: (535, 810),
            6: (799, 687),
            7: (304, 681),
            8: (541, 568),
            9: (787, 447)
        }
        return positions.get(key)

    def _get_target_position(self, target):
        """
        获取货物要移动到的屏幕位置。
        """
        return self._get_position(self.targets.get(target))

    def _is_empty_train(self, screen):
        result = UIMatcher.match(screen, TargetType.empty_train)
        if result is None:
            return False
        return True
        

    def _match_target(self, screen, target):
        """
        探测货物，并搬运货物。
        """
        # 由于 OpenCV 的模板匹配有时会智障，故我们探测次数实现冗余。
        counter = 5
        while counter != 0:
            counter = counter - 1

            # 使用 OpenCV 探测货物。
            result = UIMatcher.match(screen, target)

            # 若无探测到，终止对该货物的探测。
            # 实现冗余的原因：返回的货物屏幕位置与实际位置存在偏差，导致移动失效
            if result is None:
                return False

            # 在 trainMode 下设置搬运成果。
            if self.trainMode:
                self.isHarvest = True

            sx, sy = result
            # 获取货物目的地的屏幕位置。
            ex, ey = self._get_target_position(target)
            # 搬运货物。
            self.d.swipe(sx, sy, ex, ey)
            print("swipe ...")
        print("found!")
        return True

    def collect_red_pack(self, scale, count):
        self.d.app_start("com.tencent.jgm")
        self.d.click(1, 1919)
        time.sleep(2)
        self.d.click(490, 1825)
        for i in range(count*3):
            time.sleep(0.5)
            print(i)
            if 0 == scale:
                self.d.click(205, 706)
                time.sleep(0.5)
                self.d.click(540, 355)
            if 1 == scale:
                self.d.click(547, 708)
                time.sleep(0.5)
                self.d.click(540, 355)
            if 2 == scale:
                self.d.click(876,687)
                time.sleep(0.5)
                self.d.click(540, 355)

    def collect_photo(self, count):
        # self.d.app_start("com.tencent.jgm")
        # self.d.click(1, 1919)
        # time.sleep(2)
        # self.d.click(490, 1825)
        for i in range(count):
            self.d.click(547, 1407)
            time.sleep(3)
            self.d.click(540, 355)
            print(i)
            time.sleep(1)

            # if i % 10 == 0:
            #     self.d.click(1, 1919)
            #     time.sleep(3)
            #     self.d.click(490, 1825)
        time.sleep(2)
        self.d.click(1, 1919)
        time.sleep(2)