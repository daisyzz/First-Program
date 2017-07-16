choice = int(input("Would you like to convert 12/24 Hour time into military : "))

m_time = []

time = ""
if choice == 24:
    time_24 = str(input("Please input 24H clock to convert to military : "))
    for i in time_24:
        if i.isdigit() is True:
            m_time.append(i)
elif choice == 12:
    time_12 = str(input("Please input 12H clock to convert to military : "))
    for l in time_12:
        if l is "a":
            for i in time_12:
                if i.isdigit() is True:
                    m_time.append(i)
        elif l is "p":
            for i in time_12:
                if i.isdigit() is True:
                    i = int(i)
                    m_time.append(i)
            if len(m_time) == 4:
                m_time.remove(0)
            m_time[0] += 12
if len(m_time) == 4 is False:
    m_time.insert(0, '0')
m_time = map(str, m_time)
m_time = "".join(m_time)
print("In Military Time That Would be : {}".format(m_time))
