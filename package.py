



class Package:

    def __init__(self):
        self.width = 0
        self.height = 0
        self.length = 0
        self.mass = 0
        self.volume = 0


def get_double(val: str):
    try:
        return float(val)
    except:
        return None


def parse_package(line: str):

    tokens = line.split(',')

    if len(tokens) != 4:
        return None
    
    # assume line is Width,Height,Length,Mass

    package = Package()

    package.width = get_double(tokens[0])
    package.height = get_double(tokens[1])
    package.length = get_double(tokens[2])
    package.mass = get_double(tokens[3])

    for val in [package.width, package.height, package.length, package.mass]:
        if val is None:
            return None 
        
        if val <= 0:
            return None
    
    package.volume = package.length * package.width * package.height

    return package

