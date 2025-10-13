# The Laws of Thermodynamics

The laws of thermodynamics are the fundamental principles which govern how energy moves and changes form
in all physical systems. They describe the relationships between relevant physical quantities: heat, work,
temperature, entropy and energy; and set the absolute limits on what processes are physically possible. 

Unconventionally for physics, these laws are enumerated starting from zero - a consequence of the order
in which these laws were discovered. The zeroth law was formulated after the first and second laws had 
already been established, but was recognised as being even more fundamental and thus allotted the position
of zero to reflect its logical precedence. 

Together, the four laws of thermodynamics form a complete framework for understanding all sorts of thermal
processes, ranging from combustion and refrigeration to the study of particle motion in materials. 

## The Zeroth Law 

The Zeroth Law of Thermodynamics establishes the concept of thermal equilibrium and forms a basis for the
definition of temperature. It states:
    
*"If system A is in thermal equilibrium with system B, and system B is in thermal equilibrium with
system C, then systems A and C are also in thermal equilibrium."*

Or in plain English: "if two systems are in thermal equilibrium with a third system, then they are in
thermal equilibrium with each other." This law allows us to define the quantity 'temperature' as a common
property that determines whether systems are in equilibrium with each other. Systems in thermal equilibrium
have the same temperature and do not exchange any energy in the form of heat.

## The First Law

The First Law of Thermodynamics is a statement of energy conservation within thermal processes. It states:

*"Energy cannot be created or destroyed, only transformed from one form to another."*

When energy passes into or out of a system (as work, heat or matter), the system's internal energy changes
in accordance to the conservation of energy; such that, in an externally isolated system, the sum of all
forms of energy must remain constant:

$$\Delta U = Q_{add} - W_{by},$$ 

where:
- $\Delta U$ = The change in the system's internal energy.
- $Q_{add}$ = The heat that is added to the system, a negative value corresponds to heat lost.
- $W_{by}$ = The work done by the system, i.e. macroscopic influences on the environment driven by forces.

Alternatively we can set $Q_{out} = - Q_{add}$ as heat subtracted from the system, and/or $W_{on} = -W_{by}$ as work 
done on the system, which allows us to alternatively define the first law by:

$$\Delta U = W_{on} - Q_{out}$$.

### 1st Law - Example 1 - Compressing a balloon

You squash an inflated ballon, decreasing its volume; the process is carried out fast enough as to not add additional 
heat to the system (i.e. $Q_{add} = Q_{out} = 0$). What are the implications for the system's internal energy?

We can use the first law to discern what happens. By compressing the balloon, we are doing work on the system, such that
$W_{on}$ is positive (and thus $W_{by}$ is negative.) The first law states that:

$$
\Delta U = Q_{add} - W_{by} = 0 + W_{on} = W_{on} 
$$

Hence, the internal energy will increase linearly in proportion to the work we've applied to the system via compression. 
The internal energy of a system is directly proportional to temperature, so a positive $\Delta U$ corresponds to an 
increase in the system's temperature.

### 1st Law - Example 2 - Inflating a balloon

Consider the opposite of the previous example. In this hypothetical scenario, a balloon with a fixed amount of matter
within increases in size, sufficiently quickly such that again $Q_{add} = Q_{out} = 0$. In this case, the expansion of 
the balloon's surface forcibly moves nearby air molecules outside the balloon, to make space for its new volume. 
Therefore, the work done by the balloon is positive, $W_{by} > 0$. 

$$\Delta U = Q_{add} - W_{by} = 0 + W_{by} = -W_{by}$$


## The Second Law

The Second Law of Thermodynamics introduces the concept of *entropy*, a measure of disorder or the variety of manners 
energy can be equivalently distributed in a system. The law states:

*"In a natural thermodynamic process, the total entropies of an isolated system can never decrease."*

In equation form, this law is expressed as:

$$\Delta S_{closed} \geq 0,$$

where *S* quantifies entropy.

In other words, whilst energy is conserved (in abidance to the First law), it becomes increasingly dispersed or 
unavailable for performing work. Heat naturally flows from warmer to cooler environments, but not the other way around.
This law explains why perpetual motion machines are not possible, and why time appears to have a direction - towards 
increased entropy.

### 2nd Law - Example 1 - Melting ice in a warm room.

When you place an ice cube into a warm room, heat flows spontaneously from the air (the hotter body) into the ice
(the colder body). The consequently melts as it absorbs this energy.

Although the melting ice itself becomes more disordered as it replaces its crystalline structure with a fluid arrangement,
increasing its entropy, the air loses some heat and slightly decreases its own entropy. Nonetheless, the system's total
entropy, (ice + room) increases overall. The process is irreversible: the melted water will never spontaneously refreeze 
whilst the room remains warm. This one-way flow of energy helps illustrate the "arrow of time" implied by the second law.

## The Third Law

The Third Law of Thermodynamics describes the behaviour of a system's entropy as its temperature approaches the lowest
possible value, absolute zero (0 K). It states:

*"A system's entropy approaches a constant value as its temperature approaches absolute zero."*

At absolute zero temperature, the system will be in a state of minimal thermal energy, commonly referred to as a 'ground'
state. The constant value (not necessarily zero) of the entropy at this level is called the residual entropy of the 
system. This entropy can only be exactly zero if there is only one configuration the system can take at this level. 

Leaning briefly into statistical mechanics lens of thermodynamics, the entropy of a system is related to the number of 
possible microstates the system can be in, according to Boltzmann's principle:

$$S = k_B \ ln(\Omega),$$

where $S$ is the entropy of the system, $k_B$ is the Boltzmann constant and $\Omega$ is the number of possible 
microstates. In scenarios where at absolute zero, there is only one microstate possible, we have:

$$S = k_B \ ln(\Omega) = k_B \ ln(1) = k_B * 0 = 0.$$



