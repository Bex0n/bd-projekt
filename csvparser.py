def parseData(company):
    data = open("data/" + company + ".data")
    output = []
    for line in data:
        line = line.replace("\n", "")
        line = line.split(',')
        output.append(line)
    return output    

# print(parseData("NVDA"))