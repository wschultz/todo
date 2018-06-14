#!/usr/bin/env python3

import collections
import datetime
import json

Todo = collections.namedtuple('Todo', 'desc time status priority')
todos = dict()


def initialize():
  '''This should run at the start of the program, it will look for a JSON file and
  load it into a dict that contains a key as the descripter and a value in the
  form of a namedtuple
  '''
  try:
    with open('todo.json') as file:
      todos = json.load(file)
      for key, value in todos.items():
        todos[key] = Todo(*value)

    if type(todos) is not dict:
      todos = dict()

  except:
    todos = dict()

  return(todos)


def add_todo(label, desc, time, status, priority):
  ''' Here's where we add a new ToDo into the dict
  '''
  todos[label] = Todo(desc=desc, time=time, status=status, priority=priority)
  save_file()

  return(todos)


def delete_todo(todo):
  '''Here's where we delete the items that no longer are required
  '''
  del todos[todo]
  save_file()

  return(todos)


def save_file():
  with open('todo.json', 'w') as outfile:
      json.dump(todos, outfile)


if __name__ == "__main__":

  todos = initialize()

  loop = True
  while loop:
    print ("""
    1. List current To-Do's
    2. Add a To-Do
    3. Delete a To-Do
    4. Exit/Quit
    """)

    loop = input("What would you like to do? ")
    if loop == "1":
      try:
        print("\nHere's a list of current To-Do's\n")
        if todos == {}:
          print("It doesn't appear that we've got any yet, let's get to work!")
        else:
          num_priorities = collections.defaultdict(int)
          for key, value in todos.items():
            desc, time, status, priority = value
            num_priorities[priority] += 1
            print("\n* Label is: {}\n  Description: {}\n  Created on: {}\n  Status is: {}\n  Priority is: {}".format(key, *value))

          for k,v in num_priorities.items():
            if v > 1:
              print("\n   the priority {} shows up {} times".format(k, v))

          mylist = []

          for k,v in num_priorities.items():
            mylist.append(k)

          mylist.sort()
          mynewlist = range(mylist[0], mylist[-1])
          myothernewlist = []

          for num in mynewlist:
            if num not in mylist:
              myothernewlist.append(num)

          print("\nThe following priorities don't exist: " + ' '.join(str(e) for e in myothernewlist))



      except Exception as e:
        print(e)

    elif loop == "2":
      print("\nOkay, let's add a to-do in the format of label, description, status, priority\n")
      try:
        label    = input("What is the label? ")
        desc     = input("What is the description? ")
        status   = input("What is the status? ")
        priority = int(input("What is the priority? "))
        time     = str(datetime.datetime.now())
        if label in todos.keys():
          print("\nSorry, that label already exists... Please try again...")
        else:
          add_todo(label, desc, time, status, priority)

      except Exception as e:
        print("\nThis field needs to be a number, the actual error is " + str(e) + "please report that error to your friendly neighborhood sytem administrator")
        loop == True

    elif loop == "3":
      delete_me = input("\n Okay, let's delete a to-do... what's the label? ")
      if delete_me not in todos.keys():
        print("\nThat label doesn't seem to exist, are you sure that's correct?\n")
      else:
        delete_todo(delete_me)

    elif loop == "4":
      print("\n Have a nice day!\n")
      loop = False

    else:
      print("\n Not Valid Choice Try again\n")
      loop = True
