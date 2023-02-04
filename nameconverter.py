companies = [
    " - ",
    'Amazon',
    'AMD',
    'CD Projekt',
    'Meta',
    'Netflix',
    'NVIDIA',
    'Tesla'
]

arr = {}
arr[" - "] = [" - "]
arr["Amazon"] = ["AMZN"]
arr["AMD"] = ["AMD"]
arr["CD Projekt"] = ["CDR.WA"]
arr["Meta"] = ["META"]
arr["Netflix"] = ["NFLX"]
arr["NVIDIA"] = ["NVDA"]
arr["Tesla"] = ["TSLA"]

def convertName(companyName):
    return arr[companyName][0]