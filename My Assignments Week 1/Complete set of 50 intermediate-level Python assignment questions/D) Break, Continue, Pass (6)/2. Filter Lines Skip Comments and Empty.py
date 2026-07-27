# Filter Lines: Skip Comments and Empty
def filter_data (lines):
    clean = []
    for line in lines:
        if line.strip() =='' or line.lstrip().startswith('#'):
            continue        
        clean.append(line)
    return clean
data = ["start",
"# import me",
"",
"   ",
"likes",
"# comments "]
print(filter_data(data))