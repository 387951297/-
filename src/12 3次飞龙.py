from util import *
from const import const

path = const.publicPath() + 'beacon/'

def main():
    time.sleep(2)
    util.logOut(__file__,'3次飞龙 开始')

    #返回主页面
    const.backMainProcess()
    #进入出击界面
    x , y = const.picLoop(const.publicPath() + 'bmp/weigh anchor.jpg')
    util.click(x,y)
    x , y = const.picLoop(path + 'operation.jpg')
    util.click(x,y)
    x , y = const.picLoop(path + 'ash.jpg')
    time.sleep(2)
    util.click(x,y)
    x , y = const.picLoop(path + 'beacon list.jpg')
    util.click(x,y)
    for n in range(3):
        util.logOut(__file__,'------------一把开始-----------')
        x , y = const.picLoop(path + 'batile start.jpg')
        util.click(x,y)
        x , y = const.picLoop(path + 'weigh anchor.jpg')
        util.click(x,y)
        x , y = const.picLoop(const.publicPath() + 'bmp/get_items.bmp')
        util.click(x,y)
        x , y = const.picLoop(path + 'ok.jpg')
        util.click(x,y)
        util.logOut(__file__,'------------一把结束-----------')
    #返回主页面
    const.backMainProcess()
