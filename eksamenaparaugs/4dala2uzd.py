with open("teksts.txt") as f:
    text = f.read()
    print(text)
    nevajadzigi = ".,!?:;()"
    for suimbolnins in nevajadzigi:
        text = text.replace(suimbolnins, "")
    text = text.split(" ")
    print(text)
    
    vardu_skaits = {} # key -> value
    for vards in text:
        if len(vards) > 3:
            # vardu skaits key = vards, value = text.count(vards)
            vardu_skaits[vards] = text.count(vards)
            
    print(sorted(vardu_skaits, key=vardu_skaits.get))
            
    print(vardu_skaits)