import json

class JineshParakh:
    def __init__(self):
        self.info = {
            "😄 Pronouns" : ["He", "Him"],
            "💻 Studying" : {
                "Degree" : "Computer Engineering",
                "College" : "Pune Institute of Computer Technology",
                "Batch" : "2018-2022"
            },
            "🔭 Workplace" : {
                "Company" : "UBS",
                "Position" : "Summer Intern",
                "Department" : "Group Functions - Network Tools"
            },
            "💡 Exploring" : "PrimeFaces & Hibernate",
            "👥 Communities" : {
                "Chairperson" : "PICT ACM Student Chapter",
                "CP Lead" : "DSC PICT",
                "Editor in Chief" : "Pictoreal"
            },
            "⚡ Funfact" : "Could have added languages, tools & handles over here itself but couldn't resist using the badges"

        }

    def sayHello(self):
        print("Hello, thanks for dropping by. Do ⭐ the repo if you liked it!\n")

    def getInfo(self):
        print(json.dumps(self.info, sort_keys=False, indent=4, ensure_ascii=False))


jinesh = JineshParakh()

jinesh.sayHello()
jinesh.getInfo()
