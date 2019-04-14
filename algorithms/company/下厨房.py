material = []
while True:
    try:
        m = input().split()
        material.extend(m)
    except:
        print (len(set(material)))
        break