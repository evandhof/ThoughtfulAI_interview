
from package import Package, parse_package
from sort import sort_package, Stack

if __name__ == "__main__":

    input = "/home/evan/Desktop/Thoughtful AI Interview/input.csv"

    with open(input, 'r') as f:
        lines = f.readlines()
    
    packages = []
    for line in lines:
        packages.append(parse_package(line))

    packages = [package for package in packages if package is not None]
    
    print(f"Num packages: {len(packages)}")

    stacks = [sort_package(package) for package in packages]

    standard = [package for package, stack in zip(packages, stacks) if stack == Stack.STANDARD.value]
    special = [package for package, stack in zip(packages, stacks) if stack == Stack.SPECIAL.value]
    rejected = [package for package, stack in zip(packages, stacks) if stack == Stack.REJECTED.value]

    stacks = [(standard, "standard"), (special, "special"), (rejected, "rejected")]

    for stack, name in stacks:
        print(f"Statistics for stack {name}:")
        print(f"{len(stack)} packages is {len(stack) / len(packages) * 100}% of total packages")

        # avg, min, max for mass and volume
        min_mass = min([package.mass for package in stack])
        max_mass = max([package.mass for package in stack])
        avg_mass = sum([package.mass for package in stack]) / len(stack)

        min_volume = min([package.volume for package in stack])
        max_volume = max([package.volume for package in stack])
        avg_volume = sum([package.volume for package in stack]) / len(stack)

        print(f"min mass: {min_mass} units. max mass: {max_mass} units. avg mass: {avg_mass} units.")
        print(f"min volume: {min_volume} units. max volume: {max_volume} units. avg volume: {avg_volume} units.")
        print("")