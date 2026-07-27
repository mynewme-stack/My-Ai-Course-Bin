# Retry Fixed Attempts
attempt = [False,False,False]
for i in range(3):
    if attempt[i] == True:
        print('Success!')
        break
else:
    print('All Retries Failed.')