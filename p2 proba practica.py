from datetime import datetime


class WorkStartError(ValueError):
    pass


class WorkEndError(ValueError):
    pass


class TimeIter:
    """Iterator for starting hours by name"""

    def __init__(self, start_working_time: list):
        self.start_working_time = start_working_time

    def __iter__(self):
        return self

    def __next__(self):
        if not self.start_working_time:
            raise StopIteration
        else:
            return self.start_working_time.pop(0)


class TimeKeeper:
    """keeps track of starting times"""
    ledger = {}

    def __init__(self, date: list):
        self.date = date

    def __iter__(self):
        result = []
        for name, start_work_time in self.ledger.items():
            result.append((name, start_work_time))
        return TimeIter(result)

    def start_work_time(self, name: str, start_work_time: list):
        """add start time"""
        if self.ledger.get(name, None):
            raise WorkStartError(f'{name} already started work')
        self.ledger[name] = [datetime(*self.date, *start_work_time)]

    def remove_from_factory(self, name: str):
        """remove from factory and raise the error"""
        if self.ledger.get(name) is None:
            raise WorkEndError(f'{name} is not in the factory {datetime.now()}')
        self.ledger.pop(name)


timer = TimeKeeper([2021, 3, 4])

# add start time
timer.start_work_time('Joe', [9, 1, 20])
timer.start_work_time('Ana', [9, 3, 15])
timer.start_work_time('Tim', [9, 4, 25])
try:
    timer.start_work_time('Tim', [9, 4, 30])
except WorkStartError as e:
    print(e)
# print the values in a file
with open('timer.log', 'w') as file:
    for data in timer:
        file.write(f'{data[0]}: {data[1]}\n')
# remove from the factory
timer.remove_from_factory('Joe')
timer.remove_from_factory('Ana')
timer.remove_from_factory('Tim')
try:
    timer.remove_from_factory('Tim')
except WorkEndError as e:
    print(e)
