from util import *
from const import const

CHAPTER_NUM = 7  # 几-几
CHAPTER_NUM2 = 2  # 几-几
CHAPTER_X, CHAPTER_Y = 476, 250  # 几-几的坐标

# if __name__ == '__main__':
def main():
    time.sleep(2)
    print('困难'+str(CHAPTER_NUM)+'-'+str(CHAPTER_NUM2)+'脚本开始')

    # 进入困难第CHAPTER_NUM章界面
    const.chapterProcess(CHAPTER_NUM, 'H')

    # 每日困难3次
    for i in range(3):
        const.intoStageProcess(CHAPTER_X, CHAPTER_Y)
        const.goBossProcess()
    const.backMainProcess()
    return
