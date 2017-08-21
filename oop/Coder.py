class Coder:
    def __init__ (self , name):
        self.name = name
        self.skills = []

    def mastering_skill(self,skill):
        self.skills.append(skill)

    def show_skills(self):
        print('掌握技能')
        for skill in self.skills:
            print('-',skill)