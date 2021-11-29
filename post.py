import sys 
import requests
import json 

# cat data | xargs -i python post.py {}
def GetDoc():
    getUrl = ""
    setUrl = ""
    headers = {"Content-Type": "application/json"}
    docId = sys.argv[1]
    data = json.dumps({"id": docId})
    print(docId)
    res = requests.post(getUrl, data=data, headers=headers)
    res = json.loads(res.text)
    setdata = json.dumps({"doc":res['doc']})
    requests.post(setUrl, data=setdata, headers=headers)
    
if __name__ == "__main__":
    data = GetDoc()