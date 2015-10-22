import os
from Student import Student

from matcher.Prio1 import Prio1Matcher
from matcher.AverageDistribution import AverageDistributionMatcher
from matcher.Optimizer import OptimizerMatcher

import codecs

matchers = [Prio1Matcher, AverageDistributionMatcher]

students = []
projects = []

for line in codecs.open('data/Auswertung.csv', encoding='utf-8'):
    students.append(Student.from_line(line))

for student in students:
    for prio in student.prios:
        if projects.count(prio) == 0:
            projects.append(prio)

    if student.owner is not None and projects.count(student.owner) == 0:
        projects.append(student.owner)

if not os.path.exists('data/out/'):
    os.makedirs('data/out/')

for matcher in matchers:
    m = OptimizerMatcher(projects, students, matcher)
    with codecs.open('data/out/' + matcher.__name__ + '.txt', 'w+') as file:
        m.create_match()
        m.write_to_file(file)

exit()
