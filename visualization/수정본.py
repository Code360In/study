# matplotlib tools 여러 그래프 그리기
plt.plot([0,100,100,0,0,100,50,0,100],[0,0,100,100,0,100,130,100,0])
plt.axis([-10,110,-10,140])
plt.show()

fig, ax = plt.subplots()
ax.plot([0,100,100,0,0,100,50,0,100],[0,0,100,100,0,100,130,100,0])
ax.set_xlim(-10,110)
ax.set_ylim(-10,140)
plt.show()

plt.plot([0, 100, 100, 0, 0], [0, 0, 100, 100, 0], "r-", [0, 100, 50, 0, 100], [0, 100, 130, 100, 0], "g--")
plt.axis([-10, 110, -10, 140])
plt.show()

plt.plot([0, 100, 100, 0, 0], [0, 0, 100, 100, 0], "r-")
plt.plot([0, 100, 50, 0, 100], [0, 100, 130, 100, 0], "g--")
plt.axis([-10, 110, -10, 140])

# pyplot
## version1
x = np.linspace(-1.4,1.4,30)
plt.plot(x,x,'g--', x,x**2, 'r:', x,x**3, 'b^')
plt.show()

## version2
fig,ax = plt.subplots()
x = linspace(-1.4,1.4,30)
ax.plot(x,x,'g--')
ax.plot(x,x**2,'r:')
ax.plot(x,x**3,'b^')
plt.show()

# Line2D
x = np.linspace(-1.4,1.4,30)
line1, line2, line3 = plt.plot(x,x,'g--',x,x**2,'r:',x,x**3,'b^')
line1,set_linewidth(3.0)
line1.set_dash_capstyle('round')
line3.set_alpha(0.2)
plt.show()

#
x = np.linspace(-1.4, 1.4, 30)
fig, ax = plt.subplots()
line1 = ax.plot(x, x, 'g--', linewidth=3, dash_capstyle='round')
line2 = ax.plot(x, x**2, 'r:')
line3 = ax.plot(x, x**3, 'b^', alpha=0.2)
plt.show()

# 여러개의 그림
## subplot
x = np.linspace(-1.4, 1.4, 30)

# subplot(2,2,1)은 subplot(221)로 축약
plt.subplot(2, 2, 1)  # 좌측 상단
plt.plot(x, x)
plt.subplot(2, 2, 2)  #  우측 상단
plt.plot(x, x**2)
plt.subplot(2, 2, 3)  #  좌측 하단
plt.plot(x, x**3)
plt.subplot(2, 2, 4)  #  우측 하단
plt.plot(x, x**4)
plt.show()

## fig,ax
x = np.linspace(-1.4, 1.4, 30)
fig, ax = plt.subplots(2, 2) 
ax[0, 0].plot(x, x)       #  좌측 상단
ax[0, 1].plot(x, x**2)   #  우측 상단
ax[1, 0].plot(x, x**3)   #  좌측 하단
ax[1, 1].plot(x, x**4)   #  우측 하단
plt.show()

## grid
grid = plt.GridSpec(2, 2)  # 2행 2열 크기의 격?자를 준비합니다.

ax1 = plt.subplot(grid[0, 0])  # 좌측 상단
ax2 = plt.subplot(grid[0, 1])  # 우측 상단
ax3 = plt.subplot(grid[1, 0:]) # 2행 *1*열의 두 번째 부분 그래프 = 하단
                               # 범위를 [1, 0:]으로 설정하여 2행 전체를 지정함.
ax1.plot(x, x)
ax2.plot(x, x**2)
ax3.plot(x, x**3)
plt.show()

##
fig, ax = plt.subplots()

ax.plot(x, x**2, "b-")
ax.plot(px, py, "ro")

ax.text(0, 1.5, "Square function\n$y = x^2$", fontsize=20, color='blue', horizontalalignment="center") # horizontalalignment(수평정렬)
ax.text(px - 0.08, py, "Beautiful point", ha="right", weight="heavy")
ax.text(px, py, "x = %0.2f\ny = %0.2f"%(px, py), rotation=50, color='gray')

plt.show()

## 
fig, ax = plt.subplots()
ax.plot(x, x**2, px, py, "ro")
ax.annotate("Beautiful point", xy=(px, py), xytext=(px-1.3,py+0.5),    # 관심있는 부분의 위치를 지정하고, 텍스트의 위치를 지정 및 화살표 추가속성
                           color="green", weight="heavy", fontsize=14,
                           arrowprops={"facecolor": "lightgreen"})
plt.show()

fig, ax = plt.subplots()
ax.plot(x, x**2)
ax.plot(px, py, "ro")

bbox_props = dict(boxstyle="rarrow,pad=0.3", ec="b", lw=2, fc="lightblue") 
ax.text(px-0.2, py, "Beautiful point", bbox=bbox_props, ha="right")

bbox_props = dict(boxstyle="round4,pad=1,rounding_size=0.2", ec="black", fc="#EEEEFF", lw=5)
ax.text(0, 1.5, "Square function\n$y = x^2$", fontsize=20, color='black', ha="center", bbox=bbox_props)

plt.show()

## 범례
x = np.linspace(-1.4, 1.4, 50)

fig, ax = plt.subplots()

ax.plot(x, x**2, "r--", label="Square function")
ax.plot(x, x**3, "g-", label="Cube function")
ax.legend(loc="best")
ax.grid(True)
plt.show()


## scatter
fig, ax = plt.subplots()

for color in ['red', 'green', 'blue']:
    n = 100
    x, y = rand(2, n)
    scale = 500.0 * rand(n) ** 5
    ax.scatter(x, y, s=scale, c=color, alpha=0.3, edgecolors='blue')

ax.grid(True)

plt.show()

## 일반
from numpy.random import randn

# Axis를 인자로 전달하여 함수 연산과 시각화를 수행합니다.
def plot_line(axis, slope, intercept, **kargs):
    xmin, xmax = axis.get_xlim()
    axis.plot([xmin, xmax], [xmin*slope+intercept, xmax*slope+intercept], **kargs)

x = randn(1000)
y = 0.5*x + 5 + randn(1000)*2

fig, ax = plt.subplots()

ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-5, 15)
ax.scatter(x, y, alpha=0.2)
ax.plot(1, 0, "ro")
ax.vlines(1, -5, 0, color="red")
ax.hlines(0, -2.5, 1, color="red")
plot_line(axis=ax, slope=0.5, intercept=5, color="magenta")  
ax.grid(True)
plt.show()

## 히스토그램
data1 = np.random.randn(400)
data2 = np.random.randn(500) + 3
data3 = np.random.randn(450) + 6
data4a = np.random.randn(200) + 9
data4b = np.random.randn(100) + 10

fig, ax = plt.subplots()
ax.hist(data1, bins=5, color='g', alpha=0.75, label='bar hist') # default histtype='bar'
ax.hist(data2, color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
ax.hist(data3, color='r', histtype='step', label='step hist')
ax.hist((data4a, data4b), color=('r','m'), alpha=0.55, histtype='barstacked', label=('barstacked a', 'barstacked b'))

ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
ax.legend()
ax.grid(True)
plt.show()

## 애니메이션
import matplotlib.animation as animation
matplotlib.rc('animation', html='jshtml')

x = np.linspace(-1, 1, 100)
y = np.sin(x**2*25)
data = np.array([x, y])

fig, ax = plt.subplots()

line, = ax.plot([], [], "r-") # start with an empty plot
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.plot([-0.5, 0.5], [0, 0], "b-", [0, 0], [-0.5, 0.5], "b-", 0, 0, "ro")
ax.grid(True)
ax.set_title("Marvelous animation")

# this function will be called at every iteration
def update_line(num, data, line):
    line.set_data(data[..., :num] + np.random.rand(2, num) / 25)  # we only plot the first `num` data points.
    return line,

line_ani = animation.FuncAnimation(fig, update_line, frames=100, fargs=(data, line), interval=67)
plt.close()
line_ani

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
line_ani.save('my_wiggly_animation.mp4', writer=writer)

#  결측치 제거
from random import randint

x = np.arange(10, dtype='float')    # 예제 데이터 만들기
for i in range(3):   # 예제 데이터에 랜덤으로 결측치 3개 심기
    idx = randint(0, 9)
    x[idx] = np.nan

print(x)

idxnan = np.where(np.isnan(x))[0]
print(idxnan)

x1 = np.delete(x, idxnan)
print(x1)
