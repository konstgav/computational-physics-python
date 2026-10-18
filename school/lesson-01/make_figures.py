"""Рисунки для слайдов занятия 1. Запуск: python make_figures.py (из папки lesson-01)."""
import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, 'img')
DATA = os.path.join(HERE, '..', '..', 'data')
os.makedirs(IMG, exist_ok=True)

plt.rcParams.update({'font.size': 13, 'figure.dpi': 120})
e = 1.602176634e-19  # Кл


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(IMG, name))
    plt.close(fig)


# Плохой и хороший график
t = np.linspace(0, 2, 50)
y = 20 * t - 9.8 * t**2 / 2
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4))
a1.plot(t, y)
a1.set_title('Плохо')
a2.plot(t, y, label='$y = v_0 t - gt^2/2$')
a2.set_xlabel('$t$, с')
a2.set_ylabel('$y$, м')
a2.set_title('Хорошо')
a2.grid(alpha=0.3)
a2.legend()
save(fig, 'bad-good-plot.png')

# Логистическое отображение
r = np.linspace(2.5, 4.0, 2000)
x = 0.5 * np.ones_like(r)
for _ in range(500):
    x = r * x * (1 - x)
rs, xs = [], []
for _ in range(200):
    x = r * x * (1 - x)
    rs.append(r)
    xs.append(x)
fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(np.concatenate(rs), np.concatenate(xs), ',k', alpha=0.3)
ax.set_xlabel('$r$')
ax.set_ylabel('$x$')
ax.set_title('$x_{n+1} = r\\,x_n(1-x_n)$')
save(fig, 'logistic.png')

# Милликен: МНК с отклонениями
nu, U = np.loadtxt(os.path.join(DATA, 'millikan.txt'), unpack=True)
k, b = np.polyfit(nu, U, 1)
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(nu / 1e14, U, 'o', ms=8, label='данные Милликена')
nn = np.linspace(4.5e14, 12.5e14, 2)
ax.plot(nn / 1e14, k * nn + b, label=f'$U = k\\nu + b$,  $h = ek = {e * k * 1e34:.2f}\\cdot 10^{{-34}}$ Дж·с')
for xi, yi in zip(nu, U):
    ax.vlines(xi / 1e14, yi, k * xi + b, colors='r', lw=1)
ax.set_xlabel('$\\nu$, $10^{14}$ Гц')
ax.set_ylabel('$U_з$, В')
ax.grid(alpha=0.3)
ax.legend()
save(fig, 'millikan.png')

# Эффект Рунге
f = lambda x: 1 / (1 + 25 * x**2)
xn = np.linspace(-1, 1, 11)
xx = np.linspace(-1, 1, 500)
p = np.polyfit(xn, f(xn), len(xn) - 1)
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(xx, f(xx), 'k', lw=2, label='функция')
ax.plot(xx, np.polyval(p, xx), label='полином 10-й степени')
ax.plot(xx, CubicSpline(xn, f(xn))(xx), '--', label='кубический сплайн')
ax.plot(xn, f(xn), 'o', color='k')
ax.set_ylim(-0.5, 2)
ax.grid(alpha=0.3)
ax.legend()
save(fig, 'runge.png')

print('Рисунки сохранены в', IMG)
