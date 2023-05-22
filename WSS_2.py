#2023-05-17
#This code, the calculate_wall_shear_stress function takes the pipe diameter, fluid velocity, fluid density, and fluid viscosity as input parameters.
                #****************************************#
                # WALL SHEAR STREESS CALCULATION IN PIPE #
                #****************************************#  
import math

def calculate_wall_shear_stress(diameter, velocity, density, viscosity):
    # Calculate Reynolds number
    reynolds_number = (density * velocity * diameter) / viscosity

    # Calculate friction factor using Moody's diagram or another method
    friction_factor = calculate_friction_factor(reynolds_number)

    # Calculate wall shear stress using the Darcy-Weisbach equation
    wall_shear_stress = 0.5 * friction_factor * density * velocity**2

    return wall_shear_stress

def calculate_friction_factor(reynolds_number):
    print("Reynolds Number=", reynolds_number)
    
    # Calculate friction factor using Moody's diagram or another method
    # This is just a simple example using the Colebrook equation

    epsilon = 1e-6  # Roughness height of the pipe
    f = 0.02  # Initial guess for friction factor

    while True:
        # Colebrook equation
        left = -2 * math.log10((epsilon / (3.7 * diameter)) + (2.51 / (reynolds_number * math.sqrt(f))))
        right = 1 / math.sqrt(f)

        error = left - right

        if abs(error) < 1e-6:
            break

        # Newton's method to solve the equation
        derivative = (1 / (f * math.sqrt(f))) + (1.25 / (reynolds_number * (math.sqrt(f) + (epsilon / (3.7 * diameter)))))
        f = f - error / derivative

    return f

# Example
diameter = 0.01  # Pipe diameter in meters
velocity = 1  # Fluid velocity in meters per second
density = 1000  # Fluid density in kilograms per cubic meter
viscosity = 0.001  # Fluid viscosity in Pascal-seconds

wall_shear_stress = calculate_wall_shear_stress(diameter, velocity, density, viscosity)
print("Diameter=", diameter)
print("Velocity=", velocity)
print("Density=", density)
print("Viscocity=", viscosity)
print()
print("Wall shear stress=", wall_shear_stress)


