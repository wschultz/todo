#!/usr/bin/env python3

import collections
import datetime
import json

Todo = collections.namedtuple('Todo', 'desc time status')


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


def add_todo(label, desc, time, status):
  ''' Here's where we add a new ToDo into the dict
  '''
  todos[label] = Todo(desc=desc, time=time, status=status)
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
          for key, value in todos.items():
            print("\n* Label is: {}\n  Description: {}\n  Status is: {}\n  Created on: {}".format(key, *value))
      except Exception as e:
        print(e)

    elif loop == "2":
      print("\nOkay, let's add a to-do in the format of label, description, status\n")
      label = input("What is the label? ")
      desc = input("What is the description? ")
      status = input("What is the status? ")
      time = str(datetime.datetime.now())
      if label in todos.keys():
        print("\nSorry, that label already exists... Please try again...")
      else:
        add_todo(label, desc, time, status)

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
