from selectolax.parser import HTMLParser

class Course():
    PRESCOTT_ONLY_STRING = '******OFFERED ON PRESCOTT CAMPUS ONLY******'

    def __init__(self, courseblock :HTMLParser, skip_prescott_only=True):
        """Takes a `courseblock` HTML node and extracts the course information to a python object."""

        courseblock_title = courseblock.css_first('p.courseblocktitle').text(strip=True)
        courseblock_description = courseblock.css_first('p.courseblockdesc')

        if skip_prescott_only and self.PRESCOTT_ONLY_STRING in courseblock_description.text():
            return None

        nbsp = '\xa0'
        id_col, name_col, credit_col = courseblock_title.split(f'{nbsp}{nbsp}')
        num_col, hours_col = credit_col.split('Credit')

        self.department, self.course_number = id_col.split(nbsp)
        self.course_id = f'{self.department} {self.course_number}'
        self.course_name = name_col
        self.credits = num_col.strip()
        try:
            # Because we split on 'credit' instead of 'credits', sometimes there is a dangling s at the start of hours_col.
            # This will remove the 's' character from the start of the line, when present.
            hours_col = hours_col[1:].strip() if hours_col[0] == 's' else hours_col.strip()
            self.lab_hours, self.lecture_hours = hours_col[1:-1].split(',')
        except:
            self.lab_hours, self.lecture_hours = None, None

        self.course_description = ""
        
        r_flag = False  # Indicator of if we have reached the pre/corequisites section yet.
        reqs = ""
        
        for node in courseblock_description.iter(include_text=True):
            if (text := node.text()) != "Prerequisites:" and text != "Corequisites:" and not r_flag:
                self.course_description += text.lstrip()
            else:
                r_flag = True
                reqs += text

        self.prereqs = []
        self.coreqs = []

        print(f'{self.__dict__}\n')
