numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', 'thirty', 'thirty one', 'thirty two', 'thirty three', 'thirty four', 'thirty five', 'thirty six', 'thirty seven', 'thirty eight', 'thirty nine', 'forty', 'forty one', 'forty two', 'forty three', 'forty four', 'forty five', 'forty six', 'forty seven', 'forty eight', 'forty nine', 'fifty', 'fifty one', 'fifty two', 'fifty three', 'fifty four', 'fifty five', 'fifty six', 'fifty seven', 'fifty eight', 'fifty nine']

def military_time(time):
    splitTime = time[:-2].split(":")
    prefix = ''
    prefix2 = ''
    suffix = ''
    meridian = time[-2:]
    h = int(splitTime[0])
    if meridian == "PM":
        h += 12

    if splitTime[0] == '12' and meridian == "AM":
        finalHours = numbers[0]
    else:
        finalHours = numbers[h]

    if len(splitTime) == 1:
        m = 0
    else:
        m = int(splitTime[1])
        if splitTime[1] == "00":
            suffix = 'hundred hours'

    if h < 10:
        prefix = 'zero'

    if m < 10 and m > 0:
        prefix2 = 'zero'

    finalMinutes = numbers[m]

    if m == 0:
        finalMinutes = ""

    return (" ".join((prefix, finalHours)).strip()) + " " + (" ".join((prefix2, finalMinutes, suffix)).strip())

# arr = ['4:00PM', '11:00AM', '11:23AM', '6:45PM', '7:45AM', '5:05PM', '4:09AM']
#
# for testTime in arr:
#     print(military_time(testTime))

userInput = input("give 24 hour time string pls: \n")
print(military_time(userInput))