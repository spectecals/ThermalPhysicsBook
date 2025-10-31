{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a33600ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from matplotlib.patches import Arc\n",
    "lw = 1.5\n",
    "plt.rcParams['lines.linewidth'] = lw\n",
    "plt.rcParams['patch.linewidth'] = lw\n",
    "plt.rcParams['font.size'] = 14\n",
    "plt.rcParams['figure.figsize'] = (5, 4)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c1712c81",
   "metadata": {},
   "source": [
    "**Molecular model of an ideal gas**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1d7c3836",
   "metadata": {},
   "source": [
    "[[Figure of 3D cube with internal gas particle hitting wall]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0cd31991",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 500x400 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax = plt.subplots()\n",
    "lw = 1.5\n",
    "ax.set_xlim(-1.5, 2.5)\n",
    "ax.set_ylim(0, 2)\n",
    "ax.set_axis_off()\n",
    "\n",
    "x0 = 0\n",
    "y0 = 0\n",
    "x1 = 2\n",
    "y1 = 1\n",
    "y2 = 2\n",
    "x2 = -1\n",
    "\n",
    "# V1\n",
    "ax.annotate(\n",
    "    \"\",\n",
    "    xy=(x1/2, y1/2),\n",
    "    xytext=(x0, y0),\n",
    "    arrowprops=dict(arrowstyle=\"->\", shrinkA=0, shrinkB=0)\n",
    ")\n",
    "ax.plot([x1/2, x1], [y1/2, y1], c='k')\n",
    "\n",
    "# Vx\n",
    "ax.annotate(\n",
    "    \"\",\n",
    "    xy=(x1/2, y0),\n",
    "    xytext=(x0, y0),\n",
    "    arrowprops=dict(arrowstyle=\"->\", shrinkA=0, shrinkB=0)\n",
    ")\n",
    "\n",
    "# H\n",
    "ax.plot([x0, x1], [y1, y1], c='k')\n",
    "\n",
    "# -Vx\n",
    "ax.annotate(\n",
    "    \"\",\n",
    "    xy=(x2, y2),\n",
    "    xytext=(x0, y2),\n",
    "    arrowprops=dict(arrowstyle=\"->\", shrinkA=0, shrinkB=0)\n",
    ")\n",
    "\n",
    "# -V\n",
    "ax.annotate(\n",
    "    \"\",\n",
    "    xy=(x1 * .4, y2 * .8),\n",
    "    xytext=(x1, y1),\n",
    "    arrowprops=dict(arrowstyle=\"->\", shrinkA=0, shrinkB=0)\n",
    ")\n",
    "ax.plot([x1/2, y0], [x1 * .75, y2], c='k')\n",
    "\n",
    "ax.plot([x1, y2], [x0, y2], c='k')\n",
    "\n",
    "# Center of the angle (vertex)\n",
    "xc, yc = 2, 1\n",
    "\n",
    "# Angle span (degrees)\n",
    "theta1 = -26.565\n",
    "theta2 = 0\n",
    "radius = -1.0        # visual radius of the angle arc\n",
    "\n",
    "# Draw arc\n",
    "arc = Arc((xc, yc), 2*radius, 2*radius, angle=0, theta1=theta1, theta2=theta2, linewidth=1.5)\n",
    "ax.add_patch(arc)\n",
    "\n",
    "# Label angle (manually positioned along the arc)\n",
    "label_angle = np.deg2rad((theta1 + theta2) / 2)\n",
    "ax.text(\n",
    "    xc + radius * 0.7 * np.cos(label_angle),\n",
    "    yc - radius * 0.7 * np.sin(label_angle),\n",
    "    r\"$\\theta_i$\",\n",
    "    ha=\"center\",\n",
    "    va=\"center\",\n",
    ")\n",
    "\n",
    "# Draw arc\n",
    "arc = Arc((xc, yc), 2*radius, 2*radius, angle=0, theta1=theta1 + 26.565, theta2=theta2 + 26.565, linewidth=1.5)\n",
    "ax.add_patch(arc)\n",
    "\n",
    "# Label angle (manually positioned along the arc)\n",
    "label_angle = np.deg2rad((theta1 + theta2) / 2)\n",
    "ax.text(\n",
    "    xc + radius * 0.7 * np.cos(label_angle),\n",
    "    yc + radius * 0.7 * np.sin(label_angle),\n",
    "    r\"$\\theta_r$\",\n",
    "    ha=\"center\",\n",
    "    va=\"center\",\n",
    "\n",
    ")\n",
    "\n",
    "ax.text(\n",
    "    x0 - .5, y2 - .2,\n",
    "    r\"$V_x$\",\n",
    "\n",
    ")\n",
    "\n",
    "ax.text(\n",
    "    x1 / 3, y0 + 0.1,\n",
    "    r\"$V_x$\",\n",
    "\n",
    ")\n",
    "\n",
    "ax.text(\n",
    "    x1 / 3, y1 / 2,\n",
    "    r\"$V$\",\n",
    "\n",
    ")\n",
    "\n",
    "y_vals = np.linspace(0, 2, 15)  # number of hash marks; increase for denser hatching\n",
    "for y in y_vals:\n",
    "    x0, y0 = 2, y\n",
    "    x1, y1 = 2.1, y + 0.1  # small 45° segment\n",
    "    ax.plot([x0, x1], [y0, y1], linewidth=1, c='k')\n",
    "\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "da2312ce",
   "metadata": {},
   "source": [
    "The change in momentum is given by\n",
    "$$\\Delta p_x = -2mv_x = F\\Delta t,$$\n",
    "$$F_1 = \\frac{-2m_x}{\\Delta t}, \\qquad d = v_x t, \\qquad \\Delta t = \\frac{2d}{v_x},$$\n",
    "$$F_1 = \\frac{-2mv_x v_x}{2d}, \\qquad F_1 = \\frac{-m{v_x}^2}{d},$$\n",
    "$$F_{molecule} = -F_{wall}, \\qquad F_{wall} = \\frac{mv_x^2}{d}, \\qquad \\longleftarrow \\text{from 1 particle}$$\n",
    "$$F_{total} = \\frac{m}{d}(v_{x_1}^2 + v_{x_2}^2 + \\ldots) = \\frac{Nm}{d}\\left(\\bar v_x^2\\right), \\qquad \\text{where } N = \\text{number of molecules}\\qquad\\bm{(1)}$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6d3d8a7d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 500x400 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax = plt.subplots()\n",
    "ax.plot([0, 1, 1, 0], [0, 0, 1, 0], c='k')\n",
    "ax.set_axis_off()\n",
    "ax.text(.5, -.12, 'x')\n",
    "ax.text(1.03, .5, 'y')\n",
    "ax.text(.44, .58, 'z')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b1e2b09f",
   "metadata": {},
   "source": [
    "$$z^2 = x^2 + y^2,$$\n",
    "$$v^2 = v_x^2 + v_y^2 + v_z^2,$$\n",
    "$$\\bar v^2 = \\bar v_x^2 + \\bar v_y^2 + \\bar v_z^2,$$\n",
    "$$\\bar v^2 = 3\\bar v_x^2,$$\n",
    "$$\\text{from } \\bm{(1)}, \\qquad \\frac{Nm}{d}\\left(\\bar v_x^2\\right) = \\frac{N}{3}\\left(\\frac{m\\bar v^2}{d}\\right)$$"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3079a3fc",
   "metadata": {},
   "source": [
    "$$P = \\frac{F}{A} = \\frac{F}{d^2}$$\n",
    "$$\\frac{F}{d^2} = \\frac{1}{3}\\left(\\frac{N}{d^3}m\\bar v^2\\right) = \\frac{1}{3}\\left(\\frac{N}{V}m\\bar v^2\\right)$$\n",
    "$$E_k = \\frac{1}{2}mv^2$$\n",
    "$$P=\\frac{2}{3}\\left(\\frac{N}{V}\\right)\\left(\\frac{1}{2}m\\bar v^2\\right)$$\n",
    "Pressure is proportional to the number of molecules per unit volume $(\\frac{N}{V})$ times the average translational kinetic energy, $\\frac{1}{2}m\\bar v^2$."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "77798664",
   "metadata": {},
   "source": [
    "**Ideal gas law**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d922bab3",
   "metadata": {},
   "source": [
    "$$PV = nRT, \\qquad R = N_A k_B$$\n",
    "$$nR =nN_A k_B$$\n",
    "$$PV = Nk_B T, \\qquad nR = Nk_B $$\n",
    "$$PV = \\frac{2}{3}N\\left(\\frac{1}{2}m\\bar v^2\\right) = Nk_B T$$\n",
    "$$\\frac{1}{2}m\\bar v^2 = \\frac{3}{2}k_B T$$\n",
    "$$\\bar v^2 = 3\\bar v_x^2, \\qquad \\text{so we have:}$$\n",
    "$$\\frac{1}{2}m\\bar v_x^2 = \\frac{1}{2}k_B T$$\n",
    "This gives us the theory of equipartition.\n",
    "Every degree of freedom contributes $\\frac{1}{2}k_B T$ of energy.\n",
    "\n",
    "How much is $\\frac{1}{2}k_B T$ at room temp?\n",
    "$$\\frac{1}{2}k_B T = \\frac{1}{2} * 1.38*10^{-23} * 293 = 2.02*10^{-21}J$$\n",
    "A tiny quantity of energy.\n",
    "The total energy associated with the translation of molecules is\n",
    "$$E_{trans} = \\frac{1}{2}m\\bar v^2 * N = 3 * N * \\frac{1}{2}k_B T$$\n",
    "$$3 * N * \\frac{1}{2}k_B T = \\frac{3}{2}Nk_B T \\qquad \\text{(3 degrees of freedom for an ideal gas)}$$\n",
    "$$\\frac{3}{2}Nk_B T = \\frac{3}{2}nRT$$\n",
    "$$E_{trans} = U = \\text{internal energy}$$\n",
    "$$U=\\frac{3}{2}nRT$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e5b5f6b8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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h4eHh+mxxx5Tr/fBBx+YAgICTO+++27x1991112munXrmnr06GGaP3++adq0aSZfX1/TAw88YOrYsaPpp59+Ms2ePdtUu3Zt9X2bTZ8+vfh7/Pzzz00LFiww9erVS30/6enp6jHyfXXo0MHUqlUr0w8//GBauHChafDgwaaIiAhTRkaGeszx48fV88h9Tz75pGnZsmWmdevWqc/JuGfOnKl+zvK9tG3b1nT99dcXj0G+V/na5557Tt2Wi+XY8vLyih8rt+U++ZxZo0aNTPXq1TNdd911amxysWbMrsqWLGBY6WnPXC2s3mtrMhUUmNyFBFFEROWBNWyYe/xItm/fboqOjlb/P9SoUUO9Wb/55pvFYVKahIu8Cb766qumdu3alQmrt99+u/i+P//8U903adKk4vv27dun7lu+fLn6+K+//lIfb968ucRrtG/f3vToo49WOO7y3pzl66KiokwPPfRQice+8847prCwMFNubm5xWHl7e5tOnz5d/JhRo0ap59uyZUvxff/5z3/U85V+TQlrs/Pnz6tg/fDDD9XHErilgzYzM1OFowSnZVj9+9//NlUmPz/ftHr1avXvIgFtJl8rr1PVz6OisJKL5eOsGbOrsiULuAyop5bDAN8QIO00cHId3EWdOlo5u8VKVxmLFlV9QrErkCWnAwcOYO7cubj//vuRlpaG5557DgMGDEBBwcX+kdOmTUO7du3UEpEsvb344os4cuRImeeT5SMzWTYU8lyl75PlR7F8+XI0adJEjUOWreQirytfU3p5rSqHDh1CTEwMbrnlluLnksvAgQPVMtepU6eKH9uqVSu17Gg5Lll6k2U9y/tiY2PLHL+74YYbim/Xrl0bvXv3xuaitWP5fnr27In69esXv76Pj4+6r/T3M6ycih9ZhrzqqqsQEhICLy8v9OvXT73+0aNHYS/XXHONem4zW8bszhhWevL2A9qNdJtzriwNHVr1ViEvvQQsXQqXJwEkRRVTp05Vb4pSbbZhwwb8/vvv6vM///wzHnzwQYwYMQILFizApk2b8OyzzyInJ6fMc8mbrJm84VV034WiTcUkRI4fP64C0PLyySefqOCxhTyXkHCyfK6u0tkYKPF8lmMyj6u8+8zhaUmO65T+OC4urngMctyu9PcjP7fS30/dunVLfCw/h+HDh6sAnDFjhvo3+OWXX0r8vOyh9Ova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",
      "text/plain": [
       "<Figure size 500x400 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "p_ax = np.linspace(0, 10, 1001)[1:-1]\n",
    "v_ax = np.linspace(0, 10, 1001)[1:-1]\n",
    "\n",
    "fig, ax = plt.subplots()\n",
    "\n",
    "ax.set_xticks([])\n",
    "ax.set_yticks([])\n",
    "\n",
    "ax.set_ylabel('P', labelpad=10, rotation=0)\n",
    "ax.set_xlabel('V')\n",
    "\n",
    "ax.set_ylim(0, 100)\n",
    "ax.set_xlim(0, 0.5)\n",
    "\n",
    "ax.plot(v_ax, v_ax[::-1] / p_ax, label=r'PV$\\propto T_1$')\n",
    "ax.plot(v_ax, v_ax[::-1] * 0.5 / p_ax, label=r'PV$\\propto T_2$')\n",
    "ax.annotate('', xy=(v_ax[900], p_ax[100]),\n",
    "            xytext=(v_ax[900], p_ax[100]),\n",
    "            bbox=dict(boxstyle=\"circle\", fill=False))\n",
    "a=15\n",
    "ax.plot(v_ax[a:a+20], (v_ax[::-1] / p_ax)[a:a+20], lw=5, c='b')\n",
    "ax.annotate('Same temperature,\\nsame internal energy',\n",
    "            [.25, 50],\n",
    "            [.25, 50], size = plt.rcParams['font.size'] * 3 / 4)\n",
    "ax.annotate('',\n",
    "            [.19, 55],\n",
    "            [.24, 55],\n",
    "            arrowprops=dict(arrowstyle=\"->\")\n",
    "            )\n",
    "ax.annotate('',\n",
    "            [.3, 34],\n",
    "            [.3, 48],\n",
    "            arrowprops=dict(arrowstyle=\"->\")\n",
    "            )\n",
    "ax.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "68c3c5f5",
   "metadata": {},
   "source": [
    "**Example**\n",
    "\n",
    "By relating the total translational energy of one mole ($N_A$ particles) to the total kinetic energy, estimate the speed of the atoms in an ideal gas at $25^\\circ \\mathrm{C}$ with mass $=6.64*10^{-27}$ kg.\n",
    "\n",
    "$$\\text{Translational energy} = \\text{total kinetic energy,}$$\n",
    "$$\\frac{\\!3}{\\!2}nRT =  \\!3\\left(\\frac{1}{\\!2}mv^2\\right) * N_A$$\n",
    "$$v^2 = \\frac{nRT}{mN_A}$$\n",
    "$$v=\\sqrt{\\frac{1*8.31*297}{6.64*10^{-27}}*6.02*10^{-23}}$$\n",
    "$$=780\\text{ms}^{-1}$$\n",
    "**Assumptions**\n",
    "1. N is large, V of each is negligible\n",
    "2. Newtonian mechanics\n",
    "3. Elastic collision (no loss of kinetic enrgy)\n",
    "4. Negligible forces between molecules\n",
    "5. All particles identical."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
