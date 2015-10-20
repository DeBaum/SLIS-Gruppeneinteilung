class Student:
    def __init__(self, matr_nr, name, p1, p2, p3, p):
        self.id = matr_nr
        self.name = name
        self.prios = [p1, p2, p3]
        self.owner = None if p == 'keines' else p
        self.got_prio = 999
        self.got_prio_str = 'keins'

    @staticmethod
    def from_line(line):
        line = line.strip()
        arr = line.split(",")
        return Student(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])

    def set_got_prio(self, project):
        if self.owner == project:
            self.got_prio_str = 'owner'
            self.got_prio = -1
        elif project in self.prios:
            self.got_prio_str = 'Prio ' + str(self.prios.index(project) + 1)
            self.got_prio = self.prios.index(project)
        else:
            self.got_prio_str = 'keins'
            self.got_prio = 999
