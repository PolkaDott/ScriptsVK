import vk
import time
token = '7323df01f40cbccc7ae47c5761a27e5d94a4a442cccb6fafba6d5dc6d1ec2833e6ea296dca44b97c102dc'
session = vk.Session(access_token=token)
api = vk.API(session, v=5.103)
sid = 0
try:
    api.groups.join(group_id=100892059)
except vk.exceptions.VkAPIError as error:
    sid = error.captcha_sid
    print(error.captcha_img)
print(api.groups.join(group_id=100892059, captcha_sid=sid, captcha_key=input()))


exit(0)
file = open('groups.txt', 'r')
groups = file.read().split('\n')
ids = [group[group.rfind('/')+5:] for group in groups]
i = 0
privates = []
while i < len(ids):
    try:
        req = api.groups.getById(group_id=ids[i], fields='is_closed')
        if req[0].get('is_closed') != 0:
            privates += ids[i]
            print('+1')
        else:
            api.groups.join(group_id=ids[i])
    except vk.exceptions.VkAPIError as error:
        time.sleep(1)
        print(error)
        print('-1')
        i = i - 1
    i = i + 1
    print(str(i))
if len(privates) > 0:
    for group in privates:
        print(f"{group.get('name')}: {group.get('id')}")
    print("\n\n\nThere're private groups. Join them too?(Y/N)\n->", end='')
    inp = input()
    if inp == 'y' or inp == 'Y':
        i = 0
        while i < len(privates):
            try:
                api.groups.join(group_id=privates[i])
            except vk.exceptions.VkAPIError:
                i = i - 1
            i = i + 1
            

exit(0)


req = api.groups.get(user_id=179995182)
ids = req.get('items')
groups = api.groups.getById(group_ids=ids)
names = [x.get('name') for x in groups]
print(str(len(names))+'GROUPS:')
for i in range(len(names)):
    print("{0}: vk.com/club{1}".format(names[i], ids[i]))
print("\n\n\n\nLEAVE THESE GROUPS???(Y/N)\n->", end='')
inp = input()
if inp != 'y' and inp != 'Y':
    print('\nREJECTED')
    exit(0)
isAccess = True
for id in ids:
    try:
        if api.groups.leave(group_id=id) != 1:
            isAccess = False
    except vk.exceptions.VkAPIError:
        print('yeee')
print(isAccess)
input()
for id in ids:
    api.groups.join(group_id=id)