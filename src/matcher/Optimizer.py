from matcher import Matcher


class OptimizerMatcher(Matcher):
    def __init__(self, projects, students, base_matcher):
        super().__init__(projects, students)
        self.base_matcher = base_matcher(projects, students)

    def create_match(self):
        self.base_matcher.create_match()
        self.matching = self.base_matcher.matching

        self.remove_small_projects()

    def remove_small_projects(self):
        small_project_found = True
        while small_project_found:
            small_project_found = False
            for project, members in self.matching.items():
                if len(members) < 3 and project != 'Kein Projekt':
                    small_project_found = True
                    self.empty_project(project, members)
                    self.matching.pop(project)
                    break

    def empty_project(self, project, members):
        for member in members:
            other_project_found = False
            for prio in member.prios:
                if prio != project and prio in self.matching:
                    member.set_got_prio(prio)
                    self.matching[prio].append(member)
                    other_project_found = True
                    break

            if not other_project_found:
                member.set_got_prio('Kein Projekt')
                if 'Kein Projekt' in self.matching:
                    self.matching['Kein Projekt'].append(member)
                else:
                    self.matching['Kein Projekt'] = [member]
