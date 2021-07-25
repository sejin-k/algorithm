def enter_user(uid, name, userInfo, userLog):
    userInfo[uid] = name
    userLog.append((0, uid))
    
def leave_user(uid, userLog):
    userLog.append((1, uid))

def change_name(uid, name, userInfo):
    userInfo[uid] = name
    
def print_Log(userLog, userInfo):
    convertedLog = []
    for log in userLog:
        action = log[0]
        if action == 0:
            convertedLog.append("{}님이 들어왔습니다.".format(userInfo[log[1]]))
        elif action == 1:
            convertedLog.append("{}님이 나갔습니다.".format(userInfo[log[1]]))
            
    return convertedLog

def solution(record):
    userInfo = {}
    userLog = []
    Actions = {'Enter':0, 'Leave':1, 'Change':2}
    
    for rec in record:
        if len(rec.split()) == 3:
            action, uid, name = rec.split()
            if action == 'Enter':
                enter_user(uid, name, userInfo, userLog)
            elif action == "Change":
                change_name(uid, name, userInfo)
                
        elif len(rec.split()) == 2:
            action, uid = rec.split()
            if action == "Leave":
                leave_user(uid, userLog)

    result = print_Log(userLog, userInfo)
    return result

if __name__=="__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    
    answer = solution(record)
    print(answer)
    
# '''
# ["Prodo님이 들어왔습니다.",
# "Ryan님이 들어왔습니다.",
# "Prodo님이 나갔습니다.",
# "Prodo님이 들어왔습니다."]
# '''