# 6. Duck Typing vs Type Checking
def process (obj):
    try:
        print(f'length: {len(obj)}\n First : {obj[0]}')
    except TypeError:
        print('Error: Obj is not sequence')
process([10,20])
process((12,230))
process(100)