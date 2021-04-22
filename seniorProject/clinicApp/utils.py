def scheduleInsert(idLst, dayLst, fromLst, toLst):
    myLst = []
    for i, d, f, t in zip(idLst, dayLst, fromLst, toLst):
        item = { 'id': i, 'day': d, 'from': f, 'to': t }
        myLst.append(item)
    return myLst