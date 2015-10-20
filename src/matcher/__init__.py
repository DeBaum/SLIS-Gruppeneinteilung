import copy


class Matcher:
    def __init__(self, projects, students):
        self.projects = copy.deepcopy(projects)
        self.students = copy.deepcopy(students)
        self.matching = {}
        for project in projects:
            self.matching[project] = []

    def create_match(self):
        for student in self.students:
            if student.owner is not None:
                student.set_got_prio(student.owner)
                self.matching[student.owner].append(student)
                self.students.remove(student)

    def write_to_file(self, file):
        for project, students in self.matching.items():
            file.write(project + ': \n')
            for student in students:
                file.write('\t' + student.name + ' (Prio ' + str(student.got_prio_str) + ')\n')
            file.write('\n')
