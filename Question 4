class ListOperation(object):

   def __init__(self, list_, item):
       self.list_ = list_
       self.item = item

   def __call__(self):
       """If the class object is created the codes that are in this method will be executed"""
       return

   def undo(self):
       """Also, that class will have an undo method that will return something when called"""
       return


""" The following class of Insert has inherited the class defined above.
So it will append at the self.item to self.list_. and also undo the action same as the
class of Delete."""


class Insert(ListOperation):
   def __call__(self):
       self.list_.append(self.item)
       self.list_.sort()

   def undo(self):
       self.list_.remove(self.item)
       self.list_.sort()


class Delete(ListOperation):
   def __call__(self):
       self.deleted = False
       if self.item in self.list_:
           self.list_.remove(self.item)
           self.list_.sort()
           self.deleted = True

   def undo(self):
       if self.deleted:
           self.list_.append(self.item)
           self.list_.sort()


""" I've created the UndoableList class that will do all the operations needed. It's constructor is composed of two stacks
that will store undo and the redo commands."""


class UndoableList(object):
   def __init__(self):
       self.undo_operation = []
       self.redo_operation = []

   def push_undo_operation(self, task):
       self.undo_operation.append(task)

   def pop_undo_operation(self):
       try:
           final_undo_operation = self.undo_operation.pop()
       except IndexError:
           return "Nothing to undo"
       return final_undo_operation

   def push_redo_operation(self, task):
       self.redo_operation.append(task)

   def pop_redo_operation(self):
       try:
           final_redo_operation = self.redo_operation.pop()
       except IndexError:
           return "Nothing to redo"

       return final_redo_operation

   def do(self, task):
       task()
       self.push_undo_operation(task)
       self.redo_operation[:] = []

   def undo(self):
       if len(self.undo_operation) != 0:
           task = self.pop_undo_operation()
           task.undo()
           self.push_redo_operation(task)
       else:
           print('Nothing to undo')

   def redo(self):
       if len(self.redo_operation) != 0:
           task = self.pop_redo_operation()
           task()
           self.push_undo_operation(task)
       else:
           print('Nothing to redo')


# I tested the operations using the given example

List = [2, 4, 8]
print(f'\nList: {List}')
undoable_list = UndoableList()

undoable_list.do(Insert(List, 3))
print(f'After insert(3): {List}')

undoable_list.do(Delete(List, 8))
print(f'After delete(8): {List}')

undoable_list.undo()
print(f'After undo: {List}')

undoable_list.undo()
print(f'After undo: {List}')

undoable_list.redo()
print(f'After redo: {List}')

undoable_list.do(Insert(List, 5))
print(f'After insert(5): {List}')

undoable_list.redo()
print(f'After redo: {List}')

undoable_list.do(Delete(List, 3))
print(f'After delete(3): {List}')

undoable_list.undo()
print(f'After undo: {List}')

undoable_list.undo()
print(f'After undo: {List}')

undoable_list.undo()
print(f'After undo: {List}')

undoable_list.redo()
print(f'After redo: {List}')

undoable_list.redo()
print(f'After redo: {List}')

