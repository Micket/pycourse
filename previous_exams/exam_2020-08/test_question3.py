breast100m = Event("100m breaststroke", "s")
print(breast100m)
breast50m = Event("50m breaststroke", "s")
result = Result(breast100m, 67.16, "2020-04-12", "KM 2020 Valhallabadet")
print(result)

my_results = Results("p24", "Emil Berg")
my_results.add_result(result)

result = Result(breast50m, 32.05, "2020-04-13", "KM 2020 Valhallabadet")
my_results.add_result(result)

result = Result(breast100m, 69.41, "2020-06-27", "Simiaden 2020 Borås Arena")
my_results.add_result(result)

result = Result(breast100m, 66.94, "2020-07-05", "Bredsimmet 2020 Alingsås")
my_results.add_result(result)

print(my_results)

print()

print(my_results.best_result(breast100m))
