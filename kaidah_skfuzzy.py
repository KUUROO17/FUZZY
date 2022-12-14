import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Generate universe variables
#   * Quality and service on subjective ranges [0, 10]
#   * Tip has a range of [0, 25] in units of percentage points
population = np.arange(0, 150, 1)
density = np.arange(0, 25, 1)
area = np.arange(0, 200, 1)
growth = np.arange(0, 3, 1)
percentage = np.arange(0, 20, 1)
pokok  = np.arange(0, 10, 1)

# Generate fuzzy membership functions
#kaidah population
pop_lo = fuzz.trapmf(population, [0, 0, 10, 34])
pop_md = fuzz.trimf(population, [10, 34, 140])
pop_hi = fuzz.trapmf(population, [0, 0, 34, 140])
#kaidah density
dens_lo = fuzz.trapmf(density, [0, 0, 0.2, 4])
dens_md = fuzz.trimf(density, [0.2, 4, 23])
dens_hi = fuzz.trapmf(density, [0, 0, 4, 23])
#kaidah area
area_lo = fuzz.trapmf(area, [0, 0, 5, 58])
area_md = fuzz.trimf(area, [0.01, 58, 170])
area_hi = fuzz.trapmf(area, [0, 0, 58, 170])
#kaidah growth
grow_lo = fuzz.trapmf(growth, [0, 0, 0.01, 1])
grow_md = fuzz.trimf(growth, [0.1, 1, 1.8])
grow_hi = fuzz.trapmf(growth, [0, 0, 1, 1.8])
#kaidah percentage
per_lo = fuzz.trapmf(percentage, [0, 0, 0.1, 6])
per_md = fuzz.trimf(percentage, [0.1, 6, 17])
per_hi = fuzz.trapmf(percentage, [0, 0, 6, 17])
#kaidah pokok
pokok_lo = fuzz.trapmf(pokok, [0, 0, 2, 5])
pokok_md = fuzz.trimf(pokok, [2, 5, 8])
pokok_hi = fuzz.trapmf(pokok, [0, 0, 5, 8])



# kaidah 1
fig, (ax0, ax1, ax2, ax3 ) = plt.subplots(nrows=4, figsize=(8, 9))

ax0.plot(population, pop_hi, 'b', linewidth=1.5, label='tinggi')
ax0.set_title('2022 populaton')
ax0.legend()

ax1.plot(area, area_hi, 'r', linewidth=1.5, label='besar')
ax1.set_title('area')
ax1.legend()

ax2.plot(growth, grow_hi, 'g', linewidth=1.5, label='besar')
ax2.set_title('growth rate')
ax2.legend()

ax3.plot(pokok, pokok_hi, 'r', linewidth=1.5, label='besar')
ax3.set_title('harga pokok')
ax3.legend()


# kaidah 2
fig, (ax0, ax1, ax2, ax3 ) = plt.subplots(nrows=4, figsize=(8, 9))

ax0.plot(population, pop_md, 'b', linewidth=1.5, label='menengah')
ax0.set_title('2022 populaton')
ax0.legend()

ax1.plot(area, area_hi, 'r', linewidth=1.5, label='besar')
ax1.set_title('area')
ax1.legend()

ax2.plot(growth, grow_md, 'g', linewidth=1.5, label='menengah')
ax2.set_title('growth rate')
ax2.legend()

ax3.plot(pokok, pokok_md, 'r', linewidth=1.5, label='standart')
ax3.set_title('harga pokok')
ax3.legend()

# kaidah 3
fig, (ax0, ax1, ax2, ax3 ) = plt.subplots(nrows=4, figsize=(8, 9))

ax0.plot(population, pop_lo, 'b', linewidth=1.5, label='rendah')
ax0.set_title('2022 populaton')
ax0.legend()

ax1.plot(density, dens_hi, 'r', linewidth=1.5, label='padat')
ax1.set_title('density')
ax1.legend()

ax2.plot(percentage, per_lo, 'g', linewidth=1.5, label='besar')
ax2.set_title('percentage')
ax2.legend()

ax3.plot(pokok, pokok_hi, 'r', linewidth=1.5, label='besar')
ax3.set_title('harga pokok')
ax3.legend()


# kaidah 4
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9)) 

ax0.plot(population, pop_lo, 'b', linewidth=1.5, label='rendah')
ax0.set_title('2022 populaton')
ax0.legend()

ax1.plot(density, dens_hi, 'r', linewidth=1.5, label='cukup padat')
ax1.set_title('density')
ax1.legend()

ax2.plot(pokok, pokok_md, 'r', linewidth=1.5, label='standart')
ax2.set_title('harga pokok')
ax2.legend()



# kaidah 5
fig, (ax0, ax1, ax2, ax3 ) = plt.subplots(nrows=4, figsize=(8, 9))

ax0.plot(density, dens_hi, 'b', linewidth=1.5, label='sangat padat')
ax0.set_title('density')
ax0.legend()

ax1.plot(growth, grow_hi, 'r', linewidth=1.5, label='besar')
ax1.set_title('growth rate')
ax1.legend()

ax2.plot(area, area_hi, 'g', linewidth=1.5, label='besar')
ax2.set_title('area')
ax2.legend()

ax3.plot(pokok, pokok_hi, 'r', linewidth=1.5, label='tinggi')
ax3.set_title('harga pokok')
ax3.legend()



# kaidah 6
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9)) 

ax0.plot(density, dens_lo, 'b', linewidth=1.5, label='cukup padat')
ax0.set_title('density')
ax0.legend()

ax1.plot(growth, grow_md, 'r', linewidth=1.5, label='sedang')
ax1.set_title('growth rate')
ax1.legend()

ax2.plot(pokok, pokok_md, 'r', linewidth=1.5, label='standart')
ax2.set_title('harga pokok')
ax2.legend()



# kaidah 7
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9)) 

ax0.plot(growth, grow_lo, 'b', linewidth=1.5, label='rendah')
ax0.set_title('growth rate')
ax0.legend()

ax1.plot(density, dens_hi, 'r', linewidth=1.5, label='sangat padat')
ax1.set_title('density')
ax1.legend()

ax2.plot(pokok, pokok_md, 'r', linewidth=1.5, label='standart')
ax2.set_title('harga pokok')
ax2.legend()



# kaidah 6
fig, (ax0, ax1, ax2, ax3, ax4) = plt.subplots(nrows=5, figsize=(8, 9)) 

ax0.plot(population, pop_hi, 'b', linewidth=1.5, label='tinggi')
ax0.set_title('2022 populaton')
ax0.legend()

ax1.plot(area, area_hi, 'r', linewidth=1.5, label='besar')
ax1.set_title('area')
ax1.legend()

ax2.plot(growth, grow_hi, 'r', linewidth=1.5, label='besar')
ax2.set_title('growth rate')
ax2.legend()

ax3.plot(density, dens_hi, 'r', linewidth=1.5, label='sangat padat')
ax3.set_title('density/km2')
ax3.legend()

ax4.plot(percentage, per_hi, 'r', linewidth=1.5, label='naik')
ax4.set_title('world population percentage')
ax4.legend()

plt.tight_layout()
plt.show()