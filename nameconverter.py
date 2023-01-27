arr = {}
arr["-"] = ["-"]
arr["NVIDIA"] = ["NVDA"]
arr["Amazon"] = ["AMZN"]
arr["Tesla"] = ["TSLA"]

def convertName(companyName):
    return arr[companyName][0]