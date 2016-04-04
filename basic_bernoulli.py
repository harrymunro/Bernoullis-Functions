def bernoulli_constant(pressure, density, velocity, elevation, gravity):
    return pressure + 0.5 * density * velocity**2 + density * gravity * elevation
  
def bernoulli_pressure(constant, density, velocity, elevation, gravity):
    return constant - 0.5 * density * velocity**2 - density * gravity * elevation
  
def bernoulli_density(constant, pressure, velocity, elevation, gravity):
    return (constant - pressure) / (0.5 * velocity**2 + gravity * elevation)
  
def bernoulli_velocity(constant, density, pressure, elevation, gravity):
    return ((constant - pressure - density * gravity * elevation) / (0.5 * density))**0.5
  
def bernoulli_elevation(constant, pressure, density, velocity, gravity):
    return (constant - 0.5 * density * velocity**2 - pressure) / (density * gravity)
    
def bernoulli_gravity(constant, pressure, density, velocity, elevation):
    return (constant - 0.5 * density * velocity**2 - pressure) / (density * elevation)
