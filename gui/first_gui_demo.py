import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# 创建 Tkinter 窗口
root = tk.Tk()
root.title("饼图示例")

# 数据准备
labels = ['Python', 'C++', 'Java', 'JavaScript']
sizes = [40, 25, 20, 15]

# 创建饼图
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# 保持饼图为圆形
ax.axis('equal')

# 将图表嵌入 Tkinter 窗口
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# 显示 Tkinter 窗口
root.mainloop()
