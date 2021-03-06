"""
A factory needs an iterable object to keep track of employee working hours for each day.
Each employee has a string name and a tuple containing start work and end work time (use format you like).
Iterating the object will return tuple with name and hours worked that day for each employee
1) 40p: Definition
    a) 10p: Class with constructor that receives the date in the format you desire (representing the day)
    b) 10p: Create method to add worker start time
         - if start time has already been added a custom exception inheriting ValueError (exception: WorkStartError)
         exception will be raised with message indicating employee name and existing start time
    c) 10p: Create method to add worker end time
         - if end time has already been added a custom exception inheriting ValueError (exception: WorkEndError)
         exception will be raised with message indicating employee name and existing end time
    c) 10p: Iterating the object will return tuple with name and time worked that day for each employee
2) 40p: Execution:
    a) 10p: Create instance of class with date format you selected.
    b) 10p: Add start of work for the following employees:
        - Joe: 09:01:20 - start time
        - Ana: 09:03:15 - start time
        - Tim: 09:04:25 - start time
        - Tim: 09:04:30 - start time - treat this exception
    c) 10p: Add end of work for the following employees:
        - Joe: 16:01:20 - end time
        - Ana: 18:04:15 - end time
        - Tim: 18:05:25 - end time
        - Tim: 18:05:30 - end time - treat this exception
    d) 10p: Iterate the created object and save each value on a new line in a file
3) 20p: Documenting:
   a) 5p: type hints for all arguments (optional for returned values)
   a) 5p: module documentation
   b) 5p: class documentation for all classes
   c) 5p: method documentation for all methods
"""

import datetime

# Class with constructor that receives the date in the format you desire
class Test1:
  def __init__(self, date):
    date = datetime.datetime(2020, 5, 17)
    self.date = date

  # Create method to add worker start time
  def add_start_time(self, start_time, times):
    times.append((start_time, ""))


  def add_worker(self, name_list, name):
    name_list.append(name)

  # Create method to add worker end time
  def add_end_time(self, end_time, times):
     times.append(("", end_time))

# Defining possible errors

class Error(Exception):
  """Base class for other exceptions"""
  pass


class WorkStartError(Error):
  """Raised if start time has already been added """
  pass


class WorkEndError(Error):
  """Raised if end time has already been added """
  pass


# Creating lists
name_list = []
times = []

# Checking for errors
Test1.add_worker("Joe", name_list)
try:
  Test1.add_start_time("09:01:20", )
except WorkStartError:
  pass

try:
  Test1.add_end_time("16:01:20", times)
except WorkEndError:
  pass


Test1.add_worker("Ana", name_list)
try:
  Test1.add_start_time("09:03:15", times)
except WorkStartError:
  pass

try:
  Test1.add_end_time("18:04:15", times)
except WorkEndError:
  pass


Test1.add_worker("Tim", name_list)
try:
  Test1.add_start_time("09:04:25", times)
except WorkStartError:
  pass

try:
  Test1.add_end_time("18:05:25", times)
except WorkEndError:
  pass


Test1.add_worker("Tim", name_list)
try:
  Test1.add_start_time("09:04:30", times)
except WorkStartError:
  pass

try:
  Test1.add_end_time("18:05:30", times)
except WorkEndError:
  pass

f = open("Test.txt", "w")

f.write(name_list,times)

f.close()
