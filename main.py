
# Possible buckets for packages
STANDARD_PACKAGE: str = "STANDARD" # Not bulky or heavy
SPECIAL_PACKAGE: str = "SPECIAL" # Either havy or bulky
REJECTED_PACKAGE: str = "REJECTED" # Both heavy and bulky

# Global constants for package dimensions
MAXIMUM_MASS: float = 20.0 # Maximum mass in kg
MAXIMUM_VOLUME_PER_PACKAGE: float = 1_000_000.0 # Maximum volume in cubic cm

# Error messages
ERROR_DIMENSIONS: str = "Dimensions and mass must be greater than zero."
ERROR_INPUT_TYPE: str = "Dimensions and mass must be a number."

"""
Checks if a package's mass exceeds the predefined maximum mass.

Args:
    mass (float): The mass of the package in kilograms.

Returns:
    bool: True if the package is heavy (mass >= MAXIMUM_MASS), False otherwise.
"""
def isHeavy(mass: float) -> bool:
    return mass >= MAXIMUM_MASS

"""
Checks if a package is bulky based on its dimensions or volume.
A package is considered bulky if any single dimension (width, height, or length)
is 150 cm or more, or if its total volume is 1,000,000 cubic cm or more.

Args:
    width (float): The width of the package in centimeters.
    height (float): The height of the package in centimeters.
    length (float): The length of the package in centimeters.

Returns:
    bool: True if the package is bulky, False otherwise.
"""
def isBulky(width: float, height: float, length: float) -> bool:
    if width >= 150 or height >= 150 or length >= 150:
        return True

    volume: float = width * height * length

    return volume >= MAXIMUM_VOLUME_PER_PACKAGE

"""
Sorts a package into one of three categories: STANDARD, SPECIAL, or REJECTED,
based on its dimensions (width, height, length) and mass.

Args:
    width (float): The width of the package in centimeters.
    height (float): The height of the package in centimeters.
    length (float): The length of the package in centimeters.
    mass (float): The mass of the package in kilograms.

Returns:
    str: The category of the package (STANDARD_PACKAGE, SPECIAL_PACKAGE, or REJECTED_PACKAGE).

Raises:
    ValueError: If any dimension or mass is not a number, or if any dimension
                or mass is less than or equal to zero.
"""
def sort(width: float, height: float, length: float, mass: float) -> str:
    # Make sure all values are numbers and greater than zero
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)) or not isinstance(length, (int, float)) or not isinstance(mass, (int, float)):
        raise ValueError(ERROR_INPUT_TYPE)
    elif width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError(ERROR_DIMENSIONS)
    
    tooHeavy: bool = isHeavy(mass)
    tooLarge: bool = isBulky(width, height, length)

    if tooHeavy and tooLarge:
        return REJECTED_PACKAGE
    elif tooHeavy or tooLarge:
        return SPECIAL_PACKAGE
    else:
        return STANDARD_PACKAGE
