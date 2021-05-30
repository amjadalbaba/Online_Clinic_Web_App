import datetime


day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

def scheduleInsert(idLst, dayLst, fromLst, toLst):
    myLst = []
    for i, d, f, t in zip(idLst, dayLst, fromLst, toLst):
        item = { 'id': i, 'day': d, 'from': f, 'to': t }
        myLst.append(item)
    return myLst

# def timeListItem(Lst):
#     myLst = []
#     item1 = str(Lst[0]) + "-" + str(Lst[1])
#     myLst.append(item1)
#     for i in range(3,len(Lst)):
#         item = str(Lst[i-1]) + "-" + str(Lst[i])
#         myLst.append(item)
#     return myLst
def timeListItem(Lst):
    myLst = []
    item1 = {'idx': 0, 'from': '{0:02.0f}:{1:02.0f}'.format(*divmod(Lst[0] * 60, 60)), 'to': '{0:02.0f}:{1:02.0f}'.format(*divmod(Lst[1] * 60, 60))}
    myLst.append(item1)
    for i in range(3,len(Lst)):
        item = { 'idx': i-2, 'from': '{0:02.0f}:{1:02.0f}'.format(*divmod(Lst[i-1] * 60, 60)), 'to':'{0:02.0f}:{1:02.0f}'.format(*divmod(Lst[i] * 60, 60)) }
        myLst.append(item)
    return myLst


def checkDay(date):
    dateCheck = date
    dayCheck = datetime.datetime.strptime(dateCheck, '%Y-%m-%d').weekday()
    day = day_name[dayCheck]
    return day

def transfromTimeToInt(timee):
    h, m = timee.split(':')
    result = int(h) * 3600 + int(m) * 60
    return result
def halfSplit(l1, l2):
    result = [x*0.5 for x in range(2*l1, 2*l2+1)]
    return result