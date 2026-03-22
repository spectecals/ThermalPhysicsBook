We know that the pressure decreases as a function of altitude.
But by how much?

            ↑ h
            |
        (sketch: surface with “polar bear”)

---

Number density is number per unit volume

$$
N_v = \frac{N}{V}
$$

Ideal gas law:

$$
\begin{aligned}
PV &= nRT \\
   &= k_B N T
\end{aligned}
$$

So:

$$
\frac{N}{V} = \frac{P}{k_B T} = N_v
$$

Hence:

$$
P = N_v k_B T
$$

That says pressure is proportional to number per unit volume times temperature.

---

Consider a thin slice of atmosphere (area $A$, thickness $dh$)

Top force:
$$
F_{\text{top}} = (P + dP)A
$$

Bottom force:
$$
F_{\text{bottom}} = PA
$$

Weight:
$$
F = mg = N m g
$$

Forces are all balanced:

$$
\begin{aligned}
PA &= Nmg + (P + dP)A \\
PA &= Nmg + PA + dP\,A
\end{aligned}
$$

Rearranging:

$$
\begin{aligned}
- dP\,A &= Nmg \\
- dP\,A &= N_v (A\,dh)\, m g \\
- dP &= N_v m g\, dh
\end{aligned}
$$

Using:

$$
N_v = \frac{P}{k_B T}
$$

We get:

$$
dP = - \frac{P}{k_B T} m g\, dh
$$

---

Separate variables:

$$
\int \frac{dP}{P} = - \int \frac{m g}{k_B T}\, dh
$$

Integrate:

$$
\ln\left(\frac{P_f}{P_i}\right)
=
- \frac{m g}{k_B T}(h_f - h_i)
$$

Hence:

$$
P_f = P_i \, e^{-\frac{m g}{k_B T}(h_f - h_i)}
$$

---

Let:

$$
h_i = h_0 \quad \text{(sea level)}, \qquad P_i = P_0
$$

$$
h_f = h
$$

Then:

$$
P = P_0 \, e^{-\frac{m g}{k_B T}(h - h_0)}
$$

Define:

$$
h' = h - h_0
$$

Final form:

$$
P = P_0 \, e^{-\frac{m g h'}{k_B T}}
$$

---

(Graph: pressure vs height, exponential decay)

---

Example

What’s the pressure on top of Everest?

Assume no change in temperature ($0^\circ$C)  
Take average molecular mass:

$$
m \approx 4.8 \times 10^{-26}\ \text{kg}
$$

Formula:

$$
P = P_0 e^{-\frac{m g h'}{k_B T}}
$$

Compute exponent:

$$
\begin{aligned}
\frac{m g h'}{k_B T}
&=
\frac{(4.8 \times 10^{-26})(9.8)(8848)}
     {(1.38 \times 10^{-23})(273)} \\
&\approx 1.11
\end{aligned}
$$

So:

$$
\begin{aligned}
P &= P_0 e^{-1.11} \\
  &= 1\ \text{atm} \times 0.33 \\
  &= 0.33\ \text{atm}
\end{aligned}
$$

---

What about Ben Nevis?

$$
\begin{aligned}
P &= 1\ \text{atm} \times
e^{-\frac{(4.8 \times 10^{-26})(9.8)(1544)}
         {(1.38 \times 10^{-23})(273)}} \\
&\approx 0.84\ \text{atm}
\end{aligned}
$$

---

(Final sketch: pressure vs height with markers for Ben Nevis and Everest)