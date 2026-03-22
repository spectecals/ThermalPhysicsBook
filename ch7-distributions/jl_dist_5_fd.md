# Statistical Mechanics & Quantum Statistics

## Classical vs Quantum Description

So far we have dealt with molecules which are considered **indistinguishable**.  
This is because their wavelength is much greater than their de Broglie wavelength:

$$
\lambda \gg \lambda_{dB}
$$

Thus:
- Classical picture → particles are distinguishable
- Quantum picture → particles are indistinguishable

This is not true for electrons, which are an example of **fermions**.  
Photons would be examples of **bosons**.

---

## Particle Types

| Particle Type | Examples            | Statistics            | Principle |
|--------------|--------------------|----------------------|-----------|
| Fermions     | Electrons          | Fermi–Dirac          | Pauli     |
| Bosons       | Photons            | Bose–Einstein        | No Pauli  |

- **Pauli exclusion principle**: Two or more identical fermions cannot occupy the same quantum state at the same time.

---

## Energy Levels in Atoms

Energy levels are discrete.

Example:
- $$n = 1,2,3,4$$
- Orbitals: s, p, d, ...

Electrons occupy the lowest available energy level first.

This is in contrast to photons, which can all occupy the same energy level.

---

## Pressure and Temperature

At absolute zero:

$$
T = 0 \, \text{K}
$$

Pressure in a gas:

$$
P = \frac{2}{3} \left(\frac{N}{V}\right) \left\langle E \right\rangle
$$

where:
- $$\langle E \rangle$$ = average kinetic energy
- molecules slow down as temperature decreases

---

## Maxwell–Boltzmann Distribution

Distribution of molecular velocities:

- At higher temperature → broader distribution
- At lower temperature → narrower distribution

All energy states are accessible.

---

## Boltzmann Distribution

Probability that a particle has energy $$E_i$$:

$$
p(E_i) = \frac{e^{-E_i / k_B T}}{\sum_j e^{-E_j / k_B T}}
$$

---

### At Absolute Zero

As $$T \to 0$$:

$$
p(E_i) = \frac{e^{-E_i / k_B T}}{\text{const}}
$$

For $$E_i > 0$$:
$$
p(E_i) \to 0
$$

For $$E_i = 0$$:
$$
p(E_i) \to 1
$$

So all particles occupy the ground state.

---

## Atomic Bonding

When two hydrogen atoms are brought together:

- Their wavefunctions combine
- Energy levels split
- A **bond** forms

---

## Solids and Bands

In metals (e.g. copper):

- Many atoms → many closely spaced energy levels
- These form **bands**

Example:
- Conduction band
- Valence band

Energy gap:
$$
E_g \sim 2\text{–}3 \, \text{eV}
$$

Thermal energy at room temperature:

$$
k_B T \approx 0.03 \, \text{eV}
$$

This is small compared to the band gap.

Electrons in the conduction band are free to move → electrical conduction.

---

## Fermi–Dirac Distribution

Probability of occupation:

$$
p(E_i) = \frac{1}{e^{(E_i - E_F)/k_B T} + 1}
$$

where:
- $$E_F$$ = Fermi energy

---

### Limits

As $$T \to 0$$:

- If $$E_i > E_F$$:
  $$
  p(E_i) \to 0
  $$

- If $$E_i < E_F$$:
  $$
  p(E_i) \to 1
  $$

- At $$E_i = E_F$$:
  $$
  p(E_i) = \frac{1}{2}
  $$

---

## Summary

- Classical particles → distinguishable → Maxwell–Boltzmann
- Fermions → Fermi–Dirac → obey Pauli exclusion
- Bosons → Bose–Einstein → no restriction
- At low temperatures, quantum effects dominate