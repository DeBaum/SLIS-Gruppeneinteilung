from matcher import Matcher


class Prio1Matcher(Matcher):
    def __init__(self, projects, students):
        super().__init__(projects, students)

    def create_match(self):
        super().create_match()

        for student in self.students:
            if student.owner is not None:
                student.set_got_prio(student.owner)
                self.matching[student.owner].append(student)
            else:
                student.set_got_prio(student.prios[0])
                self.matching[student.prios[0]].append(student)
