<<<<<<< HEAD
import db, import_file
SSSLoans = import_file.import_file('SSSLoans')

def getAllSSSLoans():
  res = db.List("SSSLoans")
  SSSLoansList = []
  for row in res:
    if row is not None:
      SSSLoan = SSSLoans.SSSLoans( str(row[0]), str(row[1]) )
      SSSLoansList.append(SSSLoan)
      row = db.cur.fetchone()
  return SSSLoansList

def getSSSLoan(val):
  res = db.SubList("SSSLoans", "ID", val)
  for row in res:
    if row is not None:
      SSSLoan = SSSLoans.SSSLoans( str(row[0]), str(row[1]) )
  return SSSLoans
=======
import db, import_file
SSSLoans = import_file.import_file('SSSLoans')

def getAllSSSLoans():
  res = db.List("SSSLoans")
  SSSLoansList = []
  for row in res:
    if row is not None:
      SSSLoan = SSSLoans.SSSLoans( str(row[0]), str(row[1]) )
      SSSLoansList.append(SSSLoan)
      row = cur.fetchone()
  return SSSLoansList

def getSSSLoan(val):
  res = db.SubList("SSSLoans", "ID", val)
  for row in res:
    if row is not None:
      SSSLoan = SSSLoans.SSSLoans( str(row[0]), str(row[1]) )
  return SSSLoans
>>>>>>> c9e5dac83acf4b96337960900277a7a396e23b87
