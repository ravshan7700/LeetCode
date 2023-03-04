def sozlar(st: str):
    stt=""
    for i in st:
        if i.isalpha():
            i=i.lower()
            stt+=i
        else:
            stt+=i

    with open("forbidden_words.txt",encoding="utf-8") as f:
        sozlar=f.read().split()
    
    for i in sozlar:
        if i in stt:
            lenn=len(i)
            



