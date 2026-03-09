jobs_before_case_correction = [
    "Help Desk Technician",
    "IT Help Desk", 
    "Desktop Support Technician", 
    "Senior IT Support Engineer",
    "IT Support Specialist",
    "Lead Technical Support Specialist"
    ]

jobs = [s.lower() for s in jobs_before_case_correction]

banned_words = ["senior", "lead", "manager"]

for x in range(0,len(jobs)): # checking each job listing
    status = False
    for y in range(0, len(banned_words)): # seeing if any of the banned words are in the job listing
        words = jobs[x].split()
        if banned_words[y] in words:
            print(f"banned word detected: {banned_words[y]}")
            status = True
            break
    if status == False: 
        print(f"NOTIFY: {jobs_before_case_correction[x]}")
    else:
        print(f"IGNORE: {jobs_before_case_correction[x]}")
