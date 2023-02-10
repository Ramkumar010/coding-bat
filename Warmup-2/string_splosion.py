def string_splosion(string):
    count =""
    for i in range (len(string)):
        count = count + string[:i+1]
    return count