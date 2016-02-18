import argparse
from scipy.special import comb

# CLI interface
def int_or_float(string: str) -> int:
	try:
		value = int(string)
	except ValueError:
		value = float(string)
	return value

parser = argparse.ArgumentParser(description='Genetic drift statictics tool')
parser.add_argument('population_size', type=int)
parser.add_argument('initial_frequency', type=int_or_float)
args = parser.parse_args()


# Wright-Fisher Drift model

def wright_fisher(population: int, initial: int, final: int) -> float:
	frequency = initial / population
	return comb(population, final, exact=True) \
	  * (frequency)**final \
	  * (1 - frequency)**(population - final)

def wright_fisher_generation(population: int, initial: int) -> list:
	return [wright_fisher(population,initial,x) for x in range(population+1)]


# Main

if args.initial_frequency is float:
	args.initial_frequency = round(args.population_size * args.initial_frequency)

print(wright_fisher_generation(args.population_size, args.initial_frequency))
