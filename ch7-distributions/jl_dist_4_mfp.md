# Mean Free Path

The **mean free path** is the average distance travelled by a particle between collisions.

## Given (at ambient pressure)

- Ambient pressure:  
  $$101325 \, \text{Pa} = 1013 \, \text{hPa}$$

- Number density:  
  $$N_v = 2.7 \times 10^{25} \, \text{molecules/m}^3$$

- Mean free path:  
  $$\lambda \approx 68 \, \text{nm}$$

This means that out of $$2.7 \times 10^{25}$$ molecules in a cubic meter, each molecule travels on average only $$68 \, \text{nm}$$ before colliding with another molecule.

---

## High Vacuum

In high vacuum:
$$
P < 10^{-7} \, \text{Pa}
$$

The mean free path becomes:
$$
\lambda \sim 10^5 \, \text{km}
$$

---

## Collision Model

Treat molecules as spheres of diameter $$d$$.

Equivalent view:
- A point particle moving
- Other particles expanded to diameter $$2d$$

A particle moving with velocity $$v$$ sweeps out a cylindrical volume:

$$
\text{Collision volume} = \pi d^2 \, v t
$$

---

## Mean Free Path Derivation

Mean free path:
$$
\lambda = \frac{\text{distance travelled}}{\text{number of collisions}}
$$

Distance travelled:
$$
vt
$$

Number of collisions:
$$
\pi d^2 \, vt \, N_v
$$

So:
$$
\lambda = \frac{vt}{\pi d^2 \, vt \, N_v}
$$

$$
\lambda = \frac{1}{\pi d^2 N_v}
$$

More accurately:
$$
\lambda = \frac{1}{\sqrt{2} \, \pi d^2 N_v}
$$

---

## Example

At temperature $$20^\circ \text{C}$$ (i.e. $$T = 293 \, \text{K}$$), for nitrogen gas:

- Pressure:
  $$
  P = 10^5 \, \text{Pa}
  $$

- Molecular diameter:
  $$
  d = 2 \times 10^{-10} \, \text{m}
  $$

### Step 1: Number Density

Using:
$$
N_v = \frac{P}{k_B T}
$$

$$
N_v = \frac{1 \times 10^5}{1.38 \times 10^{-23} \times 293}
$$

$$
N_v \approx 2.5 \times 10^{25} \, \text{molecules/m}^3
$$

---

### Step 2: Mean Free Path

$$
\lambda = \frac{1}{\sqrt{2} \, \pi (2 \times 10^{-10})^2 \times 2.5 \times 10^{25}}
$$

$$
\lambda \approx 2.25 \times 10^{-7} \, \text{m}
$$

$$
\lambda \approx 225 \, \text{nm}
$$