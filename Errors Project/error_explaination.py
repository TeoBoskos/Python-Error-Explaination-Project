attr_er_str = """An AttributeError in Python occurs when you try to access an attribute or method
that does not exist for a given object. This usually happens when there is a typo in the attribute
name, an object is of the wrong type, or an attribute has not been defined. To fix it, ensure the
attribute exists and is being accessed on the correct object."""

imp_er_str = """An ImportError in Python occurs when you try to import a module that cannot be found
or loaded. This can happen if the module does not exist, is not installed, has a typo in its name,
or is located in a directory that is not included in Python's search path (sys.path). To fix it,
ensure the module is correctly spelled, installed (pip install module_name), and accessible  in the
script's environment."""

index_er_str = """An IndexError in Python occurs when you try to access an index in a sequence(like
a list, tuple or string) that is out of range. This happens when the index is either negative beyond
the valid range or greater than the higher available index. To fix it, ensure the index is within
the valid range by checking the length of the sequence using len(my_list) before accessing items."""

key_er_str = """A KeyError in Python occurs when you try to access a dictionary key that does not
exist. This happens when you use dict[key] for a key that is not present in the dictionary. To avoid
this, you can check if a key exists using "if key in my_dict", use the .get() method (my_dict.get(key))
which returns None instead of raising an error, or provide a default value like my_dict.get(key, 0)."""

name_er_str = """A NameError in Python occurs when you try to use a variable, function or identifier
that has not been defined. This usually happens due to a typo, using a variable before assigning a
value to it, or referencing a variable outside of its scope. To fix this, ensure the variable is
properly defined before use, check for typos, and verify that the variable is accessible within the
current scope."""

notImp_er_str = """A NotImplementedError in Python is raised when an abstract method or function is
defined but had not been implemented. It is commonly used as a placeholder in base classes when
designing an object oriented program, signaling that subclasses must override the method. If a subclass
fails to implement the method and calls it, Python will raise a NotImplementedError. This helps ensure
proper structure and behavior in class hierarchies."""

stopIt_er_str = """A StopIterationError in Python occurs when there are no more items to retrieve
from an iterator, and the next() function is called again. This typically happens when iterating over
and iterator manually using next(), or when a generator function completes execution. In loops like
"for item in iterable:", Python handles this error automatically, but if you manually call next() on
an exhausted iterator, it will raise StopIteration. To prevent this, you can use the try-except block
to catch the error or check if the iterator has more items before calling next()."""

syntax_er_str = """A SyntaxError in Python occurs when the code violates the language's syntax rules,
preventing it from being interpreted or executed. This usually happens due to missing colons (:),
unmatched parentheses, incorrect identation, or improperly structured statements. Unlike other errors,
a SyntaxError occurs before execution starts, meaning the program won't run until the issue is fixed.
To fix it, carefully check the error message and correct the syntax."""

ident_er_str = """An IdentationError in Python occurs when there is an issue with the alignment of
code blocks, which are essential in Python for defining the scope of functions, loops, conditionals
and other structures. Python relies on consistent identation (spaces or tabs) to indicate which
statements belong to which block of code. If there's inconsistent use of spaces or tabs, or if a
block is not indented properly, Python will raise an IndentationError. Proper indentation is crucial
for the code to run correctly."""

value_er_str = """A ValueError in Python occurs when a function receives an argument of the correct
type, but an inappropriate value. This typically happens when the value cannot be processed as expected
by the operation. For example, trying to convert a non-numeric string (like "abc") into an integer
using int("abc") will raise a ValueError because the string does not represent a valid number. It's
a way for Python to signal that the value itself is not valid in the context it's being used, even
though the type of the argument is acceptable."""

str_list = [
  attr_er_str,
  imp_er_str,
  index_er_str,
  key_er_str,
  name_er_str,
  notImp_er_str,
  stopIt_er_str,
  syntax_er_str,
  ident_er_str,
  value_er_str
]