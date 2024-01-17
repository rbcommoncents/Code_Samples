import time


class titlepage:
    def __init__(self, title, preparer, reference_num):
        self.title = str(title)
        self.date = time.strftime("%m/%d/%Y", time.localtime())
        self.preparer = str(preparer)
        self.reference_num = str(reference_num)
        
    def __str__(self):
        return f"{self.title}\n{self.date}\n{self.preparer}\n{self.reference_num}"
 
""" 
t1 = titlepage("Malware", "Ryszard", "0000001")

a = []
a.append(t1.title)
a.append(t1.date)
a.append(t1.preparer)
a.append(t1.reference_num)

count = 1
for i in a:
    print(f"{count}: {i}")
    count += 1
"""

def createreport():
    title = input("What is the report title: ")
    preparer = input("Who prepared the document: ")
    ref_num = "000002"

    t2 = titlepage(title, preparer, ref_num)
    
    return t2



print(createreport())





