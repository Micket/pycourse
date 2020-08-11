from __future__ import annotations


class Event(object):
    def __init__(self, name: str, unit: str, lower_is_better = True):
        self.name = name
        self.unit = unit
        self.lower_is_better = lower_is_better

    def __repr__(self) -> str:
        return f"{self.name}"

    #def __hash__(self):
    #    return hash(self.name)


class Result(object):
    def __init__(self, event: Event, result: float or int, date: str, venue: str):
        self.event = event
        self.result = result
        self.date = date
        self.venue = venue

    def __repr__(self) -> str:
        return f'Event: {self.event}, Result: {self.result}{self.event.unit} ({self.date} at "{self.venue}")'


class Results(object):
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.results = dict()

    def add_result(self, result: Result):
        if result.event in self.results:
            self.results[result.event].append(result)
        else:
            self.results[result.event] = [result]

    def best_result(self, event: Event) -> Result:
        if not event in self.results:
            raise ValueError

        first = True
        for result in self.results[event]:
            if first:
                best = result
                first = False
                continue
            if (event.lower_is_better and result.result < best.result) or \
                    (not event.lower_is_better and result.result > best.result):
                best = result
                
        return best

    def __repr__(self) -> str:
        s = f'Results for "{self.name}"'
        for event, results in self.results.items():
            s += "\n" + str(event) + ":"
            for result in results:
                s += "\n  " + str(result)
        return s


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