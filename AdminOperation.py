def getAdminTickets(connection):

    cur = connection.cursor()

    data = []
    eachTicket = {}
    
    responseDictionary = {'status':True,'message':'Successfully fetched All tickets'}

    cur.execute('select * from ticket t join employee e on t.employeeid = e.id where t.ticketstatus != %s',('RESOLVED',))

    ticketData = cur.fetchall()

    for i in range(0,len(ticketData)):
        eachTicket['id'] = ticketData[i][0]
        eachTicket['name'] = ticketData[i][1]
        eachTicket['description'] = ticketData[i][2]
        eachTicket['level'] = ticketData[i][3]
        eachTicket['ticketstatus'] = ticketData[i][4]
        eachTicket['firstname'] = ticketData[i][8]
        eachTicket['lastname'] = ticketData[i][9]
        eachTicket['email'] = ticketData[i][10]
        eachTicket['phone'] = ticketData[i][11]
        eachTicket['department'] = ticketData[i][12]
        data.append(eachTicket)
    responseDictionary['data'] = data

    return responseDictionary

def getAdminTeamMembers(connection):

    cur = connection.cursor()

    data = []
    eachTicket = {}

    responseDictionary = {'status':True,'message':'Successfully fetched All Admin Members'}

    cur.execute('select * from adminteam')

    adminteamData = cur.fetchall()

    for i in range(0,len(adminteamData)):
        eachTicket['id'] = adminteamData[i][0]
        eachTicket['first_name'] = adminteamData[i][1]
        eachTicket['last_name'] = adminteamData[i][2]
        data.append(eachTicket)
    responseDictionary['data'] = data

    return responseDictionary

def assignEmployeeTicket(connection,assignData):

    cur = connection.cursor()

    responseDictionary = {'status':True,'message':'Successfully assigned ticket'}

    isValidated = validateassignData(assignData)

    if(isValidated):
        cur.execute('select * from ticket where id = %s',(assignData.get('ticketNumber'),))
        ticketIdData = cur.fetchall()
        cur.execute('select * from adminteam where id = %s',(assignData.get('adminteamId'),))
        admintMemberData = cur.fetchall()
        if(len(admintMemberData) == 1 & len(ticketIdData) == 1):
            cur.execute('update ticket set ticketassignee = %s where id = %s',(assignData.get('adminteamId'),
            assignData.get('ticketNumber'),))
            connection.commit()
        else:
            responseDictionary = {'status':False,'message':'Error in assigning ticket to team'}
    else:
        responseDictionary = {'status':False,'message':'Invalid Input data'}
    
    return responseDictionary

def validateassignData(assignData):
    isValidated = True
    if(assignData.get('ticketNumber') == None):
        isValidated = False
    if(assignData.get('adminteamId') == None):
        isValidated = False
    return isValidated