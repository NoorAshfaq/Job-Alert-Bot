text = "IT Support Lead"
text = text.lower()

result = text.split()
#print(result)

status = False
banned_words = ["senior", "lead", "manager"]

for x in range(0, len(result)):
    print(f"Starting outter interval: {x + 1}")
    print(result[x])
    for y in range(0,len(banned_words)):
        print(banned_words[y])
        if (result[x]) == banned_words[y]:
            status = True

if (status) == True:
    print("Keyword found! IGNORE")
else:
    print("NOTIFY")

