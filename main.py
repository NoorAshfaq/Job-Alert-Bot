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
liked_words = ["entry", "support", "desk"]

for x in range(0,len(jobs)): # checking each job listing
    banned = False
    liked = False
    words = jobs[x].split()

    for y in range(0, len(banned_words)): # seeing if any of the banned words are in the job listing
        if banned_words[y] in words:
            print(f"banned word detected: {banned_words[y]}")
            banned = True
            break
    if banned == True: 
        print(f"IGNORE: {jobs_before_case_correction[x]}\n")
        continue # if banned word is found, skip this job listing
    
    for y in range(0,len(liked_words)): # seeing if any of the liked words are in the job listing
        if liked_words[y] in words:
            print(f"liked word detected: {liked_words[y]}")
            liked = True
            break
    if liked == True:
        print(f"NOTIFY: {jobs_before_case_correction[x]}\n")
    else:
        print(f"IGNORE: {jobs_before_case_correction[x]}\n")


        
