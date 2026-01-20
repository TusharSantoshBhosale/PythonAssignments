
def user_filter(Task,Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)

        if(Ret == True):
            Result.append(no)
    return Result

def user_map(Task,Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    return Result

def user_reduce(Task,Elements):
    Result = 0

    for no in Elements:
        Result = Task(no)

    return Result