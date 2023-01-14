import pickle
from enum import auto, Enum

import httpx
from selectolax.parser import HTMLParser

from course import Course

class Campus(Enum):
    DAYTONA = 'daytona-beach'
    PRESCOTT = 'prescott'
    WORLDWIDE = 'worldwide'
    ASIA = 'asia'

class Level(Enum):
    UNDERGRAD = 'undergraduate-courses'
    GRAD = 'graduate-courses'

class Catalog():
    base_url = 'https://catalog.erau.edu/'

    def __init__(self, use_cache=True):
        self.use_cache = use_cache


    def get_courses(self, campus :Campus, department, level=Level.UNDERGRAD):  # Not really happy with the word 'department' since it's not strictly correct.
        if campus not in Campus or level not in Level:
            raise ValueError

        if self.use_cache:
            return self._get_courses_from_cache(campus, department, level)
        else:
            return self._get_courses_from_site(campus, department, level)


    def _cache(self, html, data):
        pass


    def _get_courses_from_cache(self, campus :Campus, level :Level, department):
        pass


    def _get_courses_from_site(self, campus :Campus, level :Level, department):
        url = f'{self.base_url}/{campus.value}/{level.value}/{department.value}/'
        res = httpx.get(url)
        html = HTMLParser(res.text)

        for courseblock in html.css('div.courseblock'):
            course = Course(courseblock.html)

        if self.use_cache:
            self._cache(html.html, course)

        return data
