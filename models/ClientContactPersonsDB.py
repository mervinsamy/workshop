import db, ClientContactPersons, cgi, cgitb; cgitb.enable()

def getAllClientContactPersons():
  res = db.List("ClientContactPersons")
  ClientContactPersonsList = []
  for row in res:
    if row is not None:
      ClientContactPerson = ClientContactPersons.ClientContactPersons( int(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]) )
      ClientContactPersonsList.append(ClientContactPerson)
      row = cur.fetchone()
  return ClientContactPersonsList

def getClientContactPersons(val):
  res = db.SubList("ClientContactPersons", "ClientID", val)
  ClientContactPersonsList = []
  for row in res:
    if row is not None:
      ClientContactPerson = ClientContactPersons.ClientContactPersons( str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]) )
      ClientContactPersonsList.append(ClientContactPerson)
      row = cur.fetchone()
  return ClientContactPersonsList