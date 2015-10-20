from matcher import Matcher
import math


def find_project_member(project, students):
    member = None
    min_prio = math.inf

    for student in students:
        if student.owner == project:
            return student

        if project in student.prios:
            students_prio = student.prios.index(project)
            if student.owner is not None:
                students_prio += 1

            if students_prio < min_prio:
                member = student
                min_prio = students_prio

    if member is not None:
        return member

    return students[0]


class AverageDistributionMatcher(Matcher):
    def __init__(self, projects, students):
        super().__init__(projects, students)

    def create_match(self):
        super().create_match()

        while len(self.students) > 0:
            for project in self.projects:
                if len(self.students) > 0:
                    member = find_project_member(project, self.students)
                    member.set_got_prio(project)
                    self.matching[project].append(member)
                    self.students.remove(member)
