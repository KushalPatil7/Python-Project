
import requests as re
v=re.get(url="https://api.github.com/repos/pandas-dev/pandas/issues")
convert=v.json()
def extract_id():

    for i in range(len(convert)):
        for j in convert[i]:
            if(j=='id'):
              print(convert[i][j])
def extract_avatar_url():

    for i in range(len(convert)):
        for j in convert[i]:
            if(j=='user'):
                for k in convert[i][j]:
                    if(k=="avatar_url"):
                        print(convert[i][j][k])



def extract_urls_from_labels(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'labels':
                for label in value:
                    print(label['url'])
            else:
                extract_urls_from_labels(value)
    elif isinstance(data, list):
        for item in data:
            extract_urls_from_labels(item)

def extract_coid_from_labels(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'labels':
                for label in value:
                    m=label['url']
                    j=re.get(url=m)
                    conv=j.json()
                    for key1, values1 in conv.items():
                        if(key1=="id"or values1=="color"):
                            print(key1,"=",values1)
            else:
                extract_coid_from_labels(value)
    elif isinstance(data, list):
        for item in data:
            extract_coid_from_labels(item)


def main():
    while(True):
        print("Enter 1 to extract id:\n")
        print("Enter 2 to extract avatar url:\n")
        print("Enter 3 to extract url from Label:\n")
        print("Enter 4 to extract color and id from label:\n")
        print("Press 5 to Exit\n")
        m=int(input(""))
        if(m==1):
            extract_id()
        elif(m==2):
            extract_avatar_url()
        elif(m==3):
            extract_urls_from_labels(convert)
        elif(m==4):
            extract_coid_from_labels(convert)
        else:
             print("ThankYou")
             break

main()



