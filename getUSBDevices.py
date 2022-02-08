import wmi
c = wmi.WMI()

"""for item in c.Win32_PhysicalMedia():
    print(item)
"""
while True:
    try:
        if(c.Win32_PhysicalMedia()[1].SerialNumber.find("F") != -1):
            print("Correct USB")
        else:
            print(c.Win32_PhysicalMedia()[1].SerialNumber)
    except:
        print('No USB inserted')