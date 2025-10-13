# Heat & Temperature

As humans, we all have an intuitive notion of what heat is. When we place our hands around a mug of hot coffee, we feel them
warm up as heat flows into our skin. Whereas when we instead hold an ice cube, we feel our hands becoming colder;
this time it is not because "coldness" flows into them, but because heat is leaving our hands and flowing into the ice.

These simple experience help illustrate a fundamental natural law of physics: **heat always flows from regions of higher
temperature to regions of lower temperature**, unless we actively intervene with the heat exchange process. 

We define *heat* as thermal energy that is in transit. It is neither a substance, nor something an object "contains"; it
refers specifically to the transfer of energy between bodies because of a temperature difference. 

In this course, we adopt the sign convention:
- Heat added is positive (Q_{add} > 0)
- Heat removed is negative (Q_{add} < 0)

Because heat quantifies an energy transfer, it is measured in Joules ($J$) within the SI system (*Système international d'unités*).
The rate of heat transfer is measured in Watts ($W$), where $1 W = 1 J \cdotp s^{-1}$.

### Points about the definition & analogies

There *are* circumstances where heat appears to move "backwards" - from cold to hot environments - but only in cases where
external work is being done. The textbook example of this is the humble refrigerator. When you place food at room temperature
inside, the refrigerator's compressor expends electrical energy to extract heat from the warmer food and release it via the 
cooler coils located at the back of the fridge. Ever noticed how warm the back of the fridge is? Reversing the natural 
direction of heat flow always requires an energy input, in this case, electricity. 

The phrase "in transit" is crucial to understanding heat. An object possesses internal energy, but not a "quantity of heat."
Heat only has meaning when it is being transferred between systems. To visualise this, picture your cold hands on a brisk
winter day. You can increase their temperature in two ways:

1. By adding heat - Placing your hands nearby a warmer system (e.g. a fire) allows energy to flow from the hotter environment
your cooler skin, consistent with the second law of thermodynamics.

2. by doing work - rubbing your hands together converts mechanical energy (from your muscles, powered by food calories)
into internal energy, thereby increasing your temperature.

In both cases the hands end up warmer, yet only in the first case did heat flow into them. The point of the example is to
illustrate that heat and work are both *modes of energy transfer* and not forms of stored energy. 

## Temperature: A Measure of Thermal State

Whilst heat describes energy in motion, temperature describes the state of a system in terms of how energetically its 
constituent particles are moving on average. At the microscopic level, temperature reflects the mean kinetic energy of 
atoms and molecules. The faster they move or vibrate, the higher the temperature. When two systems are brought into
contact, energy will flow as heat until their temperatures become equal. Once this happens, they are said to be in thermal
equilibrium. This is the content of the Zeroth Law of Thermodynamics, which allows temperature to serve as a consistent
and measurable quantity.

A thermometer works on this principle: it is a small system designed to come into equilibrium with its surroundings, and
its expansion or resistance then acts as a readable measure of that equilibrium temperature.

## Specific Heat - Connecting Heat & Temperature

Suppose we apply heat to a material through some thermodynamic process. If no phase change occurs (e.g. liquid -> gas), 
this increased internal energy will increase the average molecular motion and hence increase the temperature. 
Empirically, the temperature change $\Delta T$ is found to be proportional to the amount of heat (Q_{add}) added, but 
inversely proportional to the mass ($m$) of the object being heated, empirically we can write this relationship as:

$$Q_{add} = m c \Delta T$$,

where c is the *specific heat capacity*, a material property which measures how much heat is required to raise the temperature
of an object, depending on its mass. More generically, we write:

$$Q_{add} = m \int_{T_{initial}}^{T_{final}} c dT$$.

Substances with a high specific heat capacity (such as water) require large amounts of energy to change temperature, which 
is why water takes a lot of energy to boil; whereas metals, which have lower specific het capacities warm up and cool down
quickly. Recall when you've placed your hand on a cold metal pipe, and shortly after it warms nearly to the temperature
of your hand. 

## Latent Heat - Heat changes the phase of matter

Adding heat will not always raise the temperature of an object. During a phase change, such as: *melting* a solid into a liquid,
*freezing* a liquid into a solid, or *boiling* a liquid into a gas, the supplied heat energy goes into rearranging the 
molecular structure rather than increasing the average particle speed.

We define *latent heat* as the heat required to change the phase of a given mass of substance. For example, at 0 $\degrees C$,
ice absorbs heat from its surroundings until it melts into liquid water. That absorbed energy is the *latent heat of fusion*.
Similarly, at 100 $\degrees C$, water absorbs heat to become a vapour - the *latent heat of vapourisation*.

## Summary

- Temperature measures the average kinetic energy of particles; it defines the thermal state of a body.

- Heat is thermal energy in transit, describing energy that is transferred due to a temperature difference.

- Specific heat capacity links the amount of heat supplied/extracted to the temperature increase/reduction of a substance.

- Latent heat quantifies energy absorbed or released during a phase change, when the temperature remains constant.


