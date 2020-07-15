from cqfd import *
from MaltegoTransform import *
trx = MaltegoTransform()
targetName=sys.argv[1]
infos=cqfd(targetName)
for i in infos:
    skype = trx.addEntity("maltego.skype",i["username"])
    skype.addProperty(fieldName="name",value=i["name"])
    skype.setIconURL(i["image"])
print(trx.returnOutput())
