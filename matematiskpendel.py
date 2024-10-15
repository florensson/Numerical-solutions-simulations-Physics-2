#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:44:33 2024

@author: fredriklorensson
"""
# testa gärna att ändra tidspann på rad 31 och 32

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Fysikaliska konstanter
g = 9.81  # Tyngdaccelerationen i m/s^2
L = 1.0   # Pendellängden i meter

# Funktion som representerar pendelns ekvationer
def pendulum(t, y):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -(g / L) * np.sin(theta)
    return [dtheta_dt, domega_dt]

# Initialtillstånd: initial vinkel och vinkelhastighet
theta0 = np.radians(60)  # 60 graders utslag
omega0 = 0.0             # Pendeln är i vila initialt
initial_conditions = [theta0, omega0]

# Tidsspann för lösningen
t_span = (0, 10)  # Från 0 till 10 sekunder
t_eval = np.linspace(0, 10, 10000)  # Tidssteg för utvärdering

# Lös ekvationerna numeriskt
solution = solve_ivp(pendulum, t_span, initial_conditions, t_eval=t_eval)

# Extrahera lösningen
theta = solution.y[0]
omega = solution.y[1]

# Plotta resultateter
plt.plot(t_eval, np.degrees(theta))  # Omvandla från radianer till grader för plotten
plt.title('Pendelns rörelse med stora utslag')
plt.xlabel('Tid [s]')
plt.ylabel('Vinkel [grader]')
plt.grid(True)
plt.show()
