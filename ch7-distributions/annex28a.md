# Annex 2.8.A: Black-Body Radiation and Statistical Distribution at Thermal Equilibrium

JEP - complementary teaching material  
M. Ferrera  
March 2026  

---

## Introduction

Thermal radiation is one of the fundamental mechanisms by which energy is transferred in nature. Unlike conduction and convection, radiation does not require a material medium and can propagate through empty space. Every body at a finite temperature emits electromagnetic radiation as a consequence of microscopic atomic and molecular transitions.

Thermal fluctuations continuously excite and de-excite the internal energy levels of atoms and molecules, leading to the spontaneous emission of photons. Because these microscopic processes occur in a very large number of particles, the resulting radiation is described statistically and gives rise to what is known as thermal radiation.

---

## Black Body Concept

An important idealization used to study thermal radiation is the black body. A black body is defined as an object that absorbs all incident radiation independently of wavelength and direction.

(fig:blackbody)=
```{figure} images/blackbody_cavity.png
:width: 60%
:align: center
Practical realization of a black body using a cavity with a small aperture.
```

A practical realization consists of a cavity with a small aperture. Radiation entering the hole undergoes many reflections inside the cavity. At each reflection, part of the radiation is absorbed by the walls. After many reflections, essentially all incoming radiation is absorbed, making the cavity an excellent approximation of a black body.

Inside the cavity, radiation repeatedly interacts with the walls. Photons are absorbed and re-emitted, and after many such processes, the system reaches thermal equilibrium. The radiation field inside the cavity depends only on temperature and not on the material.

---

## Kirchhoff’s Law of Thermal Radiation

Let:
- a(ν): absorptivity at frequency ν
- E(ν, T): emitted spectral power
- E_bb(ν, T): black-body emission

Kirchhoff’s law states:

```{math}
\frac{E(\nu, T)}{a(\nu)} = E_{\text{bb}}(\nu, T)
```

This implies:
- Good absorbers are good emitters
- A perfect absorber (a(ν) = 1) emits maximally:

```{math}
E(\nu, T) = E_{\text{bb}}(\nu, T)
```

---

## Determination of the Black-Body Spectrum

Kirchhoff’s law does not determine the spectral shape. Experimental observations revealed a universal curve depending only on temperature.

### Planck’s Theory

Max Planck proposed that energy is quantized:

```{math}
E_n = n h \nu
```

Average energy per oscillator:

```{math}
\langle E \rangle = \frac{h\nu}{e^{h\nu / k_B T} - 1}
```

Spectral energy density:

```{math}
u(\nu, T) = \frac{8\pi h \nu^3}{c^3} \frac{1}{e^{h\nu / k_B T} - 1}
```

---

## Physical Interpretation

The spectrum arises from two competing effects:

- Number of modes increases with frequency (∝ ν²)
- Occupation probability decreases exponentially

This produces a peak in the spectrum.

(fig:bb_spectrum)=
```{figure} images/blackbody_spectrum.png
:width: 70%
:align: center
Spectral distribution of black-body radiation at different temperatures.
```

As temperature increases:
- Total emitted radiation increases
- Peak shifts to higher frequencies

---

## Review Questions

1. Why can thermal radiation propagate through empty space while conduction and convection cannot?
2. Why does the cavity model behave like a black body?
3. What does thermal equilibrium inside the cavity mean?
4. Why must a perfect absorber be a perfect emitter?
5. Explain the terms in Kirchhoff’s law.
6. Describe trends in the spectrum as temperature increases.
7. Why does emitted radiation depend only on temperature?
8. What happens if incoming photon flux increases?
9. (Bonus) Why is emission independent of cavity material?

---

## Statistical Distributions in Thermal Equilibrium

Thermodynamics describes macroscopic properties arising from many particles. Statistical mechanics determines how particles occupy energy states.

### Maxwell–Boltzmann Distribution

Applicable to classical systems:

```{math}
f(E) \propto e^{-E / k_B T}
```

- Higher energy states are less populated
- Applies to dilute gases

---

### Fermi–Dirac Distribution

Applies to fermions (e.g., electrons):

```{math}
f(E) = \frac{1}{e^{(E - \mu)/k_B T} + 1}
```

- Obeys Pauli exclusion principle
- Important in solids

(fig:distributions)=
```{figure} images/distributions.png
:width: 70%
:align: center
Comparison of Maxwell–Boltzmann and Fermi–Dirac distributions.
```

---

## Tutorial: Relative Intensity of Spectral Lines

Two energy levels E1, E2:

```{math}
\frac{N_2}{N_1} = e^{-(E_2 - E_1)/k_B T}
```

Given:
- E2 − E1 = 0.20 eV
- T = 3000 K
- kB = 8.617 × 10⁻⁵ eV/K

---

### Solution

```{math}
\frac{I_2}{I_1} = \frac{N_2}{N_1}
```

```{math}
\frac{E_2 - E_1}{k_B T} = \frac{0.20}{(8.617 \times 10^{-5})(3000)} \approx 0.77
```

```{math}
\frac{I_2}{I_1} = e^{-0.77} \approx 0.46
```

Result:
The higher-energy spectral line has ~46% of the intensity of the lower one.