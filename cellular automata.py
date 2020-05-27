# -*- coding: utf-8 -*-
"""
Evolution of cellular automata, Rule 90
"""

import numpy as np
from PIL import Image

rule_90 =np.array([False, True, False, True, True, False, True, False])
# Regel wie sich Zustand bei bestimmter Konfiguration von sich und seinen Nachbarn ändert
# False = 0, True = 1, 000 ->0, 001 -> 1, 010 -> 0 ...

evolution_steps = 500
vector_size = 150

state =np.random.choice([True, False], size = vector_size)

#print(state[1:10])
result = np.zeros(shape=(evolution_steps, vector_size), dtype = bool)

for i in range(evolution_steps):
    
    state = rule_90[ np.roll(state,-1)+2*state+4*np.roll(state,+1)]
    result[i] =state
    
pict = Image.fromarray(result)
pict.save("evolution.png")
