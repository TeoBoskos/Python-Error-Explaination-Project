import tkinter as tk
from tkinter import ttk

from error_explaination import str_list
from output_functions import attr_er_output, imp_er_output, index_er_output
from output_functions import key_er_output, name_er_output, notImp_er_output, stopIt_er_output
from output_functions import syntax_er_output, ident_er_output, value_er_output

BUTTON_COLOR = "#cf2d2d"
BUTTON_TEXT_COLOR = "#ffffff"
FRAME_COLOR = "#5c5c5c"
PRESSED_BUTTON_COLOR = "#a81d1d"
TITLE_COLOR = "#ff2626"


class App(tk.Tk):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    """
    Inside this method is almost the entire app. Here what is contained in here:
      1) The custom styles.
      2) The three main frames (`self.title_frame`, `self.buttons_frame`,
        `self.explain_frame`) and their widgets (e.g. `self.title_label`).
      3) The buttons contain the function that are imported from `output_functions`
        as commands.

    In other words, inside this method all of the widgets are created and then
    put onto the UI, either with `.pack()` or with `.grid()`. They are also given
    functionality and styling.

    Parameters:
      *args: Variable length argument list. Arguments passed to the parent class `tk.Tk`.

      **kwargs: Arbitrary keyword arguments. Used to pass additional options to the
        parent class `tk.Tk`.
    
    Returns: None

    """

    # Styling.
    style = ttk.Style(self)
    style.theme_use('clam')

    self.configure(background=FRAME_COLOR)

    style.configure(
      "Title.TLabel",
      background=FRAME_COLOR,
      foreground=TITLE_COLOR,
      font=("Segoe UI", 32)
    )

    style.configure(
      "Text.TLabel",
      background=FRAME_COLOR,
      foreground=TITLE_COLOR,
      font=("Segoe UI", 14)
    )

    style.configure(
      "Main.TFrame",
      background=FRAME_COLOR
    )

    style.configure(
      "Error.TButton",
      background=BUTTON_COLOR,
      foreground=BUTTON_TEXT_COLOR,
    )

    style.map(
      "Error.TButton",
      background=[("active", PRESSED_BUTTON_COLOR)]
    )

    self.title("Errors In Python")
    self.geometry("1400x700")

    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure(2, weight=1)

    # title_frame and its widgets.
    self.title_frame = ttk.Frame(self, style="Main.TFrame")
    self.title_frame.grid(row=0, column=1, sticky="NSEW", padx=20, pady=20)

    self.title_label = ttk.Label(self.title_frame, style="Title.TLabel", text="Errors In Python", font=("Segoe UI", 32))
    self.title_label.pack()

    self.seperator = tk.Frame(self, height=2, bg="#9e9e9e")
    self.seperator.grid(row=1, column=1, sticky="EW")
    
    # buttons_frame and its widgets.
    self.buttons_frame = ttk.Frame(self, borderwidth=5, style="Main.TFrame", relief="solid")
    self.buttons_frame.grid(row=2, column=1, sticky="NSEW", padx=20, pady=20)

    # First inner frame and its widgets.
    self.buttons_inner_frame1 = ttk.Frame(self.buttons_frame, style="Main.TFrame")
    self.buttons_inner_frame1.pack(pady=10)

    self.attr_er_btn = ttk.Button(
      self.buttons_inner_frame1, cursor="hand2",
      text="Attribute Error", takefocus=False,
      style="Error.TButton", width=30,
      command=lambda: attr_er_output(self, str_list)
    )
    self.imp_er_btn = ttk.Button(
      self.buttons_inner_frame1, cursor="hand2",
      text="Import Error", takefocus=False,
      style="Error.TButton", width=30,
      command=lambda: imp_er_output(self, str_list)
    )
    self.index_er_btn = ttk.Button(
      self.buttons_inner_frame1, cursor="hand2",
      text="Index Error", takefocus=False,
      style="Error.TButton", width=30,
      command=lambda: index_er_output(self, str_list)
    )
    self.key_er_btn = ttk.Button(
      self.buttons_inner_frame1, cursor="hand2",
      text="Key Error", takefocus=False, 
      style="Error.TButton", width=30,
      command=lambda: key_er_output(self, str_list)
    )
    self.name_er_btn = ttk.Button(
      self.buttons_inner_frame1, cursor="hand2",
      text="Name Error", takefocus=False,
      style="Error.TButton", width=30, 
      command=lambda: name_er_output(self, str_list)
    )

    self.attr_er_btn.pack(side="left", padx=5, pady=5)
    self.imp_er_btn.pack(side="left", padx=5, pady=5)
    self.index_er_btn.pack(side="left", padx=5, pady=5)
    self.key_er_btn.pack(side="left", padx=5, pady=5)
    self.name_er_btn.pack(side="left", padx=5, pady=5)

    # Second inner frame and its widgets.
    self.buttons_inner_frame2 = ttk.Frame(self.buttons_frame, style="Main.TFrame")
    self.buttons_inner_frame2.pack(pady=10)

    self.notImp_er_btn = ttk.Button(
      self.buttons_inner_frame2, cursor="hand2",
      text="NotImplemented Error", takefocus=False,
      style="Error.TButton", width=30, 
      command=lambda: notImp_er_output(self, str_list)
    )
    self.stopIt_er_btn = ttk.Button(
      self.buttons_inner_frame2, cursor="hand2",
      text="StopIteration Error", takefocus=False,
      style="Error.TButton", width=30,
      command=lambda: stopIt_er_output(self, str_list)
    )
    self.syntax_er_btn = ttk.Button(
      self.buttons_inner_frame2, cursor="hand2",
      text="Syntax Error", takefocus=False,
      style="Error.TButton", width=30,
      command=lambda: syntax_er_output(self, str_list)
    )
    self.ident_er_btn = ttk.Button(
      self.buttons_inner_frame2, cursor="hand2",
      text="Identation Error", takefocus=False,
      style="Error.TButton", width=30,
      command=lambda: ident_er_output(self, str_list)
    )
    self.value_er_btn = ttk.Button(
      self.buttons_inner_frame2, cursor="hand2",
      text="Value Error", takefocus=False,
      style="Error.TButton", width=30,
      command=lambda: value_er_output(self, str_list)
    )

    self.notImp_er_btn.pack(side="left", padx=5, pady=5)
    self.stopIt_er_btn.pack(side="left", padx=5, pady=5)
    self.syntax_er_btn.pack(side="left", padx=5, pady=5)
    self.ident_er_btn.pack(side="left", padx=5, pady=5)
    self.value_er_btn.pack(side="left", padx=5, pady=5)

    # explain_frame and its widgets.
    self.explain_frame = ttk.Frame(self, borderwidth=5, style="Main.TFrame", relief="solid", height=170)
    self.explain_frame.grid(row=3, column=1, sticky="NSEW", padx=20, pady=20)
    self.explain_frame.grid_propagate(False)

    self.explain_label = ttk.Label(self.explain_frame, style="Text.TLabel", text="Error Explaination.")
    self.explain_label.grid(row=0, column=0)


root = App()
root.mainloop()