import pyautogui as pa
import time
import pyperclip
import PIL


# time.sleep(1)

# 鼠标移动 (2560 * 1600)
# pa.moveTo(1, 1, 0.2)

# 鼠标偏移
# pa.move(100, 100, 0.2)

# 获取分辨率
# x, y = pa.size()
# print(x,y)

# 获取鼠标位置
# x, y = pa.position()
# while True:
#   x1, y1 = pa.position()
#   if x1 != x or y1 != y:
#       x, y = x1, y1
#       print(x, y)

# 鼠标点击
# pa.click(100, 100, 3, 1, 'right', 1) 位置 次数 间隔时间 鼠标键(默认左键) 鼠标移动时间
# pa.click()

# 鼠标按住、抬起(默认左键)
# pa.mouseDown()
# time.sleep(3)
# pa.mouseUp ()

# 鼠标滑轮滚动
# pa.scroll() 负往下， 正往上 滚轮一次在一百多

# 键盘输入(不支持中文)
# pa.write('fda', 1)

# 按键输入、次数、间隔
# pa.press('enter', 2, 0.5)

# 组合按键
# pa.hotkey('ctrl', 'v')

# 中文输出 pyperclip.copy(传入字符串)
# a = '有'
# pyperclip.copy(a)
# pa.hotkey('ctrl', 'v')

# 按键按住、抬起
# pa.keyDown('shift')
# pa.press('s')
# pa.keyUp('shift')

#截屏(文件名, 截取范围)
# pa.screenshot('1.png')

# 消息框、输入框
# pa.alert('的', 'd', 'ok') (内容、标题、按钮)
# pa.prompt('的', 'd', 'w')(内容、标题、默认文本)