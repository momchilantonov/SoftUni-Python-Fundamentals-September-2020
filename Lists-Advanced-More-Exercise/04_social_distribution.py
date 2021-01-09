population = [int(el) for el in input().split(", ")]
minimum_wealth = int(input())


def distribution_possibility(pop, min_wealth):
    if sum(pop) >= len(pop) * min_wealth:
        possible = True
        return possible
    else:
        possible = False
        return possible


def wealthiest_check(pop):
    wealthiest = max(pop)
    return pop.index(wealthiest)


def population_status(p, pop, min_wealth, index_mw):
    if pop[p] < min_wealth:
        cur_dif = min_wealth-pop[p]
        pop[p] += cur_dif
        pop[index_mw] -= cur_dif
        return pop
    else:
        return pop


def main():
    if distribution_possibility(population, minimum_wealth):
        for person in range(len(population)):
            population_status(person, population, minimum_wealth, wealthiest_check(population))
        print(population)
    else:
        print("No equal distribution possible")


main()
