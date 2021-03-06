# Here all used classes in the algortihm are defined
# Created: 23/11/2016
# Last Change: 21/08/2018
from enum import Enum

class Field_of_Study(Enum):
    EE = 0
    MB = 1
    INF = 2
    WIW = 3
    NAT = 4
    SONSTIGES = 5
    BAU = 6

class Degree(Enum):
    BACHELOR = 0
    MASTER = 1
    PROMOTION = 2
    DOCTOR = 3
    ABSOLVENT = 4

class Student:
    def __init__(self, list_id, seats,name="Empty", field_of_study = [], text = "Empty", companies = [], points = 0, degree = '', other_points=0):
        self.name=name
        self.field_of_study=field_of_study
        self.text = text
        self.list_id=list_id
        self.companies=companies
        self.points=points
        self.seats=seats
        self.other_points = other_points
        self.degree = degree


class Company:
    def __init__(self, list_id=0, seats=[], name="Empty", field_of_study = [], points = 0, degrees = []):
        self.name=name
        self.field_of_study=field_of_study
        self.list_id=list_id
        self.points=points
        self.seats=seats
        self.degrees = degrees

class Settings:
    def __init__(self,num_rows = 0, min_num = 0, max_num = 0, points_student = 0, points_company = 0):
        self.num_rows = num_rows
        self.min_num = min_num
        self.max_num = max_num
        self.points_student = points_student
        self.points_company = points_company

class Session:
    def __init__(self,name = "",students = [],companies = [], fields_of_study = [], settings = Settings(), pdf_dir = "", passed_students = [], added_students = []):
        self.name = name
        self.students = students
        self.passed_students = passed_students
        self.added_students = added_students
        self.companies = companies
        self.fields_of_study = fields_of_study
        self.settings = settings
        self.pdf_dir = pdf_dir


class Field_of_Study():
    def __init__(self, name="", tags=[]):
        self.name = name
        self.tags = tags

class Table_Specs():
    def __init__(self,ID_name=-1,ID_surname=-1,ID_field_of_study=-1,IDs_companies = [-1,-1],IDs_students = [-1,-1]):
        self.ID_name = ID_name
        self.ID_surname = ID_surname
        self.ID_field_of_study = ID_field_of_study
        self.IDs_companies = IDs_companies
        self.IDs_students = IDs_students






