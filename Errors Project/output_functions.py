"""
FUNCTION DOCUMENTATION: All of these functions are basically
  the same. Their purpose is to configure the text of the
  `self.explain_label` widget to an error explaination string
  from the `str_list` list.
"""


def attr_er_output(self, str_list):
  self.explain_label.config(text=str_list[0])


def imp_er_output(self, str_list):
  self.explain_label.config(text=str_list[1])


def index_er_output(self, str_list):
  self.explain_label.config(text=str_list[2])


def key_er_output(self, str_list):
  self.explain_label.config(text=str_list[3])


def name_er_output(self, str_list):
  self.explain_label.config(text=str_list[4])


def notImp_er_output(self, str_list):
  self.explain_label.config(text=str_list[5])


def stopIt_er_output(self, str_list):
  self.explain_label.config(text=str_list[6])


def syntax_er_output(self, str_list):
  self.explain_label.config(text=str_list[7])


def ident_er_output(self, str_list):
  self.explain_label.config(text=str_list[8])


def value_er_output(self, str_list):
  self.explain_label.config(text=str_list[9])