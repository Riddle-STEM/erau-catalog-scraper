import httpx
from selectolax.parser import HTMLParser

from scraper.course import Course

stem_course_departments = ['ae', 'bio', 'chm', 'civ', 'cec', 'cs', 'cyb', 'ds', 'ee', 'egr', 'ep', 'es', 'ma', 'me', 'se', 'sys']

with open('tests/data/courseblocks/ae199.html') as f:
    c = f.read()
c = HTMLParser(c)
Course(c)

with open('tests/data/courseblocks/ae301.html') as f:
    c = f.read()
c = HTMLParser(c)
Course(c)

with open('tests/data/courseblocks/ae315.html') as f:
    c = f.read()
c = HTMLParser(c)
Course(c)
