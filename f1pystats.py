import requests

def join(p):
    p = p.split(" ")
    res = ""
    for s in p:
        res += "/" + s
    return res

def get(args=""):
    if args == "":
        a = ""
    else:
        a = join(args)
    req = "http://ergast.com/api/f1" + a + ".json"
    r = requests.get(req)
    if r.status_code == 200:
        return r.json()["MRData"]
    else:
        print("Error " + str(r.status_code))
        return False