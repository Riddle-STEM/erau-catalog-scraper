from selectolax.parser import HTMLParser

class Course():

    def __init__(self, courseblock :HTMLParser):
        """Takes a `courseblock` HTML node and extracts the course information to a python object."""

        title_line = courseblock.css_first('p.courseblocktitle').text().strip()
        
        nbsp = '\xa0'
        id_col, name_col, credit_col = title_line.split(f'{nbsp}{nbsp}')
        num_col, hours_col = credit_col.split('Credit')

        self.department, self.course_number = id_col.split(nbsp)
        self.course_id = f'{self.department} {self.course_number}'
        self.course_name = name_col
        self.credits = num_col.strip()

        try:
            hours_col = hours_col[1:].strip() if hours_col[0] == 's' else hours_col.strip()
            self.lab_hours, self.lecture_hours = hours_col[1:-1].split(',')
        except:
            self.lab_hours, self.lecture_hours = None, None

        print(self.__dict__)

        self.course_description = None
        self.prereqs = []
        self.coreqs = []