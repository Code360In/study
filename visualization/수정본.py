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
