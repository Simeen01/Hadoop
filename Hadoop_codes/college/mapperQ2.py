import sys

for line in sys.stdin:
    val = line.strip()
    data=val.split(',')
    dataTime=data[1].strip("[")
    date=dataTime.split(":")
    data=date[0]
    if data[0].isdigit():
        print(data)
