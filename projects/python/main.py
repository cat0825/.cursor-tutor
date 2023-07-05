#####################
# Welcome to Cursor #
#####################

'''
Step 1: Try generating with Cmd+K or Ctrl+K on a new line. Ask for CLI-based game of TicTacToe.

Step 2: Hit Cmd+L or Ctrl+L and ask the chat what the code does. 
   - Then, try running the code

Step 3: Try highlighting all the code with your mouse, then hit Cmd+k or Ctrl+K. 
   - Instruct it to change the game in some way (e.g. add colors, add a start screen, make it 4x4 instead of 3x3)

Step 4: To try out cursor on your own projects, go to the file menu (top left) and open a folder.
'''



# 这是一个简单的数学建模问题：求解一个线性方程
# 例如，我们有以下的线性方程：2x + 3y = 12
# 我们的目标是找到满足这个方程的x和y的值

# 导入需要的库
import numpy as np

# 定义系数矩阵和常数向量
A = np.array([[2, 3]])
b = np.array([12])

# 使用numpy的linalg.solve函数来求解
x = np.linalg.lstsq(A, b, rcond=None)[0]
print('解为：', x)





