# What is a pertubation?

A pertubation is a temporary change in the environment that causes a pronounced
change on a biological system. Pertubations are also known as **disturbances**.

# Why do we care?

Pertubations are a useful way to understand a biological system. First,
sometimes pertubations happen naturally in an environment, so it may be useful
to examine what happpens in that case. Second, pertubations can be used to
control a genetic circuit. For instance, an increase in IPTG can be used to
synchronize repressilators.

# How do we model pertubations in Tellurium?

For our purposes, a pertubation temporarily changes a parameter in the model.
We can do this in tellurium by simulating our model in separate parts.

```python
# Simulate the model as normal for the time period before the pertubation
# In this case it is from time 0 to 24 hours
prepertubation = r.simulate(0, 24, 1000)

# Modify a field to change the conditions, then simulate during the pertubation
r.variable = NEW_VALUE
pertubation = r.simulate(24, 32, 1000)

# If desired, return the variable to its original state and simulate after the pertubation
r.variable = OLD_VALUE
postpertubation = r.simulate(32, 48, 1000)

# Finally, merge together before, after, and during the pertubation into a single result
# (There are several functions that can do this, but this is an easy one)
result = numpy.vstack((prepertubation, pertubation, postpertubation));
```

When graphed, the result is this:
![](images/pertubation-example.png "An example pertubation using a repressilator as a base")

You can find an example with code in the file [toggleSwitch.py](toggleSwitch.py) in this directory.

