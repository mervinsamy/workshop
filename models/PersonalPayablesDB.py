import db, import_file
PersonalPayables = import_file.import_file('PersonalPayables')

def getPersonalPayables():
  res = db.List("PersonalPayables")
  PersonalPayablesList = []
  for row in res:
    if row is not None:
      PersonalPayable = PersonalPayables.PersonalPayables( int(row[0]), int(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]) )
      PersonalPayablesList.append(PersonalPayable)
      row = cur.fetchone()
  return PersonalPayables

def getPayrollRecord(val):
  res = db.SubList("PersonalPayables", "ID", val)
  for row in res:
    if row is not None:
      PersonalPayable = PersonalPayables.PersonalPayables( int(row[0]), int(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]) )
  return PersonalPayables

def listPayables():
  res = db.ListByPeriod("PersonalPayables")
  PayableList = []
  for row in res:
    if row is not None:
      Payable = PersonalPayables.PersonalPayables( int(row[0]), int(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]) )
      PayableList.append(Payable)
      row = db.cur.fetchone()
  return PayableList

def getPayables(val):
  res = db.SubList("PersonalPayables", "PeriodCode", val)
  PayableList = []
  for row in res:
    if row is not None:
      Payable = PersonalPayables.PersonalPayables( int(row[0]), int(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]) )
      PayableList.append(Payable)
      row = db.cur.fetchone()
  return PayableList