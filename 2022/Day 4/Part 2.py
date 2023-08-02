sectionAssignments = open("Day 4\\data.txt","r").read().split("\n")

containments = 0

for sections in sectionAssignments:
    s1, s2 = sections.split(",")

    s1n1 = int(s1.split("-")[0])
    s1n2 = int(s1.split("-")[1])
    s2n1 = int(s2.split("-")[0])
    s2n2 = int(s2.split("-")[1])
    
    a = range(s1n1, s1n2)
    b = range(s2n1, s2n2)

    overlap = list(set(a).intersection(set(b)))
    
    if len(overlap) > 0 or s1n1 == s2n2 and s1n2 >= s2n1 or s1n2 == s2n1 and s1n1 <= s2n2 or s1n1 >= s2n1 and s1n2 <= s2n2 or s2n1 >= s1n1 and s2n2 <= s1n2:
        containments += 1
    
print(containments)