from notebook import Note, Notebook
from menu import Menu


n1 = Note("hello first")
n2 = Note("hello again")
print(n1.id)
print(n2.id)
n1.match('hello')
n2.match('second')

notb = Notebook()
notb.new_note("hello world")
notb.new_note("hello again")
print(notb.notes)

print(notb.notes[0].id)
print(notb.notes[1].id)


notb.notes[0]
notb.search("hello")
notb.search("world")

notb.modify_memo(1, "hi world")
print(notb.notes[0].memo)

print(dir(notb))
print(dir(n2))

print(isinstance(n1, Note))
print(isinstance(notb, Notebook))

Menu().run()