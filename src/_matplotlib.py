import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker


# Set up
def setup_rc():
    SMALL = 8
    MEDIUM = 10
    BIGGER = 12

    plt.rc('font', size=SMALL, weight='bold')
    plt.rc('axes', titlesize=SMALL)
    plt.rc('axes', labelsize=MEDIUM)
    plt.rc('xtick', labelsize=SMALL, color='black', direction='out', alignment="center")
    plt.rc('ytick', labelsize=SMALL, color='black', direction='out')
    plt.rc('legend', loc='best', fontsize='medium')
    plt.rc('figure', titlesize=BIGGER)
    plt.rc('grid', linestyle="-", color='grey', lw=0.5)
    plt.rc('lines', linewidth=2)
    plt.rc('savefig', dpi=300)
    plt.rc('figure', figsize=(5, 5))
    plt.rc("tight_layout")

    # Style Reference
    # print(plt.style.available)
    plt.style.use('default')

# setup_rc()
# plt.rcdefaults()


# Simple template
x = np.linspace(0, 10, 10)
y = x * 2

fig, axs = plt.subplots()
axs.plot(x, y, 'b')
axs.set_xlabel('x')
axs.set_ylabel('y')
axs.set_title('title')
# plt.show()


# Iterate through axes
fig, axs = plt.subplots(nrows=1, ncols=2, dpi=100)
for ax in axs:
    ax.plot(x, y, 'b')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')
# plt.show()


# Subplot example
fig, ax = plt.subplots(3, 2)
plt.subplot(2, 2, 1)
plt.plot(x, y)

plt.subplot(2, 2, 2)
plt.plot(x, y)

plt.subplot(2, 2, 3)
plt.plot(x, y)

plt.subplot(2, 2, 4)
plt.plot(x, y)


# All together
fig, axs = plt.subplots(1, 2, figsize=(8, 4))

axs[0].plot(x, x ** 2, x, x, marker="|", linestyle="--")

# Labels
axs[0].set_title("My title")
axs[0].set_xlabel('x label')
axs[0].set_ylabel('y label')
axs[0].xaxis.labelpad = 0
axs[0].yaxis.labelpad = 0
axs[0].legend("My legend", loc='best')

# Axes
axs[0].set_xlim(0, 5)
axs[0].set_ylim(2, 20)
axs[0].spines['bottom'].set_color('blue')
axs[0].spines['top'].set_color('blue')
axs[0].spines['left'].set_color('red')
axs[0].spines['left'].set_linewidth(2)
axs[0].set_yscale("log")
axs[0].yaxis.set_ticks_position('left')
axs[0].set_xticks([1, 2, 3, 4, 5])
axs[0].set_xticklabels(
    ["oneone", "twotwo", "threethree", "fourfour", "fivefive"],
    rotation=45)
ax2 = axs[0].twinx()
ax2.plot(x, x*2, lw=2, color="red")

# Grid
axs[0].grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
axs[0].yaxis.grid(True, color='b', ls='--')

# Draw
axs[0].axhline(0.1)
axs[0].axvline(0.1)
axs[0].axhspan(0.1, ymax=-0)
axs[0].axvspan(0.1, xmax=-0)
axs[0].text(2, 10, r"$y=x^3$", fontsize=10, color="green")
axs[0].annotate("XXX", xy=(12, 1))
axs[0].arrow(0, 0, 12, 0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')

# Second subplot
axs[1].plot(x, x ** 2, x, x)
axs[1].set_title("Normal scale")

# Options on figure
plt.tight_layout()
plt.figtext(0.1, 0, "caption", wrap=True, horizontalalignment='right', fontsize=10)
fig.savefig("matplotlib.png", dpi=300, transparent=True)
plt.show()


# More options
# https://matplotlib.org/api/axes_api.html?

fig, axs = plt.subplots(1, 1, figsize=(5, 5))
axs.scatter(x, y)

# Labels
axs.set_xlabel("x label")
axs.set_ylabel("y label")
axs.vlines(1, ymin=0, ymax=1)
axs.hlines(1, xmin=0, xmax=10)
axs.legend(x, loc='best')

# Grid
ax.grid(True)

# Axes
axs.yaxis.grid(True, color='b', ls='--')
axs.xaxis.grid(True)
sec_ax = axs.secondary_xaxis(0.2, functions=(lambda x: x*2, lambda x: x)) # float or 'top'
sec_ax = axs.secondary_yaxis('right', functions=(lambda x: x*2, lambda x: x))
axs.set(xlim=(-1, 20), ylim=(-2, 1.5))
axs.set_frame_on(False) # outer frame
axs.set_axisbelow(True)
axs.xaxis.labelpad = 10
axs.yaxis.labelpad = 10
axs.set_xscale('linear')
axs.set_yscale('linear')
axs.set_xticks([1, 2])
axs.set_xticklabels(['1', '2'])
axs.set_yticks([2, 3, 4, 5])
axs.set_yticklabels([r'$\alpha$', r'$\beta$', r'$\gamma$', r'$\delta$'])
axs.minorticks_on()

# Draw
axs.annotate("XXX", xy=(12,1))
axs.text(0.15, 0.2, r"$y=x^2$", fontsize=20, color="blue")
axs.arrow(0, 0, 12, 0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')
axs.axhline(0.1)
axs.axvline(0.1)
axs.axhspan(0.1, ymax=-0)
axs.axvspan(0.1, xmax=-0)
axs.set_facecolor('#eafff5')

# Ticks
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1, 1))
axs.yaxis.set_major_formatter(formatter)

# axs.invert_xaxis()
# axs.get_xlabel()
# axs.cla()
plt.show()
