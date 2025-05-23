from enum import Enum

BULKY_VOLUME = 1000000
BULKY_DIMENSION = 150
HEAVY_MASS = 20

class Stack(Enum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"


def is_heavy(mass: float) -> bool:
    """Determine if a package is heavy"""
    if mass <= 0:
        raise Exception(f"invalid package mass {mass}")
    return mass >= HEAVY_MASS

def is_bulky(width: float, height: float, length: float) -> bool:
    """Determine if a package is bulky"""
    for dim in [width, height, length]:
        if dim <= 0:
            raise Exception(f"invalid package dimension {dim}")

    for dim in [width, height, length]:
        if dim >= BULKY_DIMENSION:
            return True
    return width * height * length >= BULKY_VOLUME

def sort(width: float, height: float, length: float, mass: float) -> str:
    """Given a package's dimensions and weight, determine its stack."""

    bulky = is_bulky(width, height, length)
    heavy = is_heavy(mass)

    if not bulky and not heavy:
        return Stack.STANDARD.value 
    elif bulky and heavy:
        return Stack.REJECTED.value 
    else:
        return Stack.SPECIAL.value 


