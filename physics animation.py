import numpy as np
from math import pi

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
# plt.style.use('seaborn-pastel')

markersize = 25
tam = 1
y_0 = tam
fig, ax = plt.subplots(dpi = 150)
ax.set_xlim(0, y_0)
ax.set_ylim(0, y_0)

scale = ax.transData.get_matrix()[0, 0]
radius = np.sqrt(markersize) / 2 / scale * 0.72
line, = ax.plot([], [], 'ko', markersize = markersize)

fps = 60

g = 9.80665
m = 1
r = 0.8
x = y_0 / 2

y = y_0
center = y + radius
e_pot = m * g * y_0
e_cin = 0
e_cin2 = 0
e_total = e_pot + e_cin
v_y = 0
v_x = 1
sinal1 = True
sinal2 = True
t = 0
last_t = 0

def imprime(value):
    return str(round(value, 2))

def init():
    return line,

def update(frame):
    global y_0
    global x

    global y
    global center
    global e_pot
    global e_cin
    global e_cin2
    global e_total
    global v_y
    global v_x
    global sinal1
    global sinal2
    global t
    global last_t

    t = (frame / fps) - last_t

    if sinal1:
        y -= v_y * 1 / 60
        v_y = g * t
    else:
        y += v_y * 1 / 60
        v_y -= (g / fps)

    if sinal2:
        x -= v_x * 1 / 60
    else:
        x += v_x * 1 / 60

    center = y + radius
    e_pot = m * g * y
    e_cin = e_total - e_pot

    if e_pot <= 0 and sinal1:
        sinal1 = False
        y_0 *= r ** 2
        v_y *= r
        e_cin *= r ** 2
        e_total *= r ** 2

    if v_y <= 0 and not sinal1:
        sinal1 = True
        last_t = frame / fps

    if x <= 0 and sinal2:
        sinal2 = False
    if x >= tam and not sinal2:
        sinal2 = True

    print('Time: ' + imprime(t + last_t) + ' s')
    print('y = ' + imprime(y) + ' m')
    print('e_pot = ' + imprime(e_pot) + ' J')
    print('e_cin = ' + imprime(e_cin) + ' J')
    print('e_total = ' + imprime(e_total) + ' J')
    print('v_y = ' + imprime(v_y) + ' m/s')
    print('v_x = ' + imprime(v_x) + ' m/s')
    print()
    line.set_data(x, y)
    # line.set_data(tam / 2, tam / 2)
    return line,

ani = FuncAnimation(fig, update, init_func = init, frames = fps * 10, interval = 1000 / fps, blit = True)
# ani = FuncAnimation(fig, update, init_func = init, frames = 600, interval = 16.667)

# ani.save('animation.gif', writer='imagemagick')

# plt.hlines(tam * r ** (2 ** 1), 0, tam)
# plt.hlines(tam * r ** (2 ** 2), 0, tam)
# plt.hlines(tam * r ** (2 ** 3), 0, tam)
# plt.hlines(tam * r ** (2 ** 4), 0, tam)
# plt.hlines(tam * r ** (2 ** 5), 0, tam)
# plt.hlines(tam * r ** (2 ** 6), 0, tam)

plt.show()