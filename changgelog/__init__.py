import sys
import time
import winsound


def 取频率(x, c1=440): 
    对应 = [0, 2, 4, 5, 7, 9, 11]
    a = x % 7
    b = x // 7
    return int(c1 * 2**(对应[a]/12+b))


def bind(steam):
    q = steam.write
    def 歌(s):
        for x in s:
            o = ord(x)
            q(x)
            steam.flush()
            if x in ',./;\'"[]-=<>?:{}_+ ':
                winsound.Beep(取频率(-5), 100)
            winsound.Beep(取频率(o%14), 100+(o>127)*50)
    steam.write = 歌
