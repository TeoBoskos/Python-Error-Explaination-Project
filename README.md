# Python Error Explanation


## Brief Overview:
This is a Python app made using Tkinter. There are ten buttons
each one representing a type of error in Python. When pressed,
an brief explanation of what the error is and means appears in
a label below.


## Structure:
The app is made up of three frames: One for the title, one for
the buttons and one for the explanation label.

1) Inside the first frame there is just a label with the title.

2) Inside the second frame there are two inner frames, each
  containing five buttons.

3) Inside the third frame there is a label that contains the
   error explanation.


## Code Structure:
The app is made up of three main files: `app.py`,
`output_functions` and `error_explaination.py` (Only now
I noticed that it's spelled wrong, hehe).

1) The first one contains all the Tkinter widgets and combines
   all the code from three files.

2) The second one contains the functions that take the error
   **explaination** string and put them as the text of the
   `self.explain_label` label. These functions are then
   imported inside `app.py` and used as the commands for
   the buttons.

3) The third one contains all the error explanation strings
   and also a list, `str_list`, which contains them. This
   list is later imported inside `app.py`.



## Why did I make this.
The reason I made this was to practice my skills in Python
and Tkinter. I welcome any kind of criticism that is going
to help me improve.

Thank you for reading.
