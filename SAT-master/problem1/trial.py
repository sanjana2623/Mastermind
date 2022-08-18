def get_auto_response( move ):
    assert( len(move) == k )
    reds = 0
    for i in range(k):
        if move[i] == code[i]:
            reds += 1
    matched_idxs = []
    whites_and_reds = 0
    for i in range(k):
        c = move[i]
        for j in range(k):
            if j in matched_idxs:
                continue
            if c == code[j]:
                whites_and_reds += 1
                matched_idxs.append(j)
                break
    print("found a move:")
    print( move )
    print( "Enter red count: "  +str(reds) )
    print( "Enter white count: "+str(whites_and_reds-reds) )
    return reds, whites_and_reds-reds

code = [1,2,7,3]
move = [1,5,6,1]
k=4
print(get_auto_response(move))