new = {}
post = {'id': 23,
        'key': "djfowejf",
        'timestamp': '2023-12-11T00:18:01.409527',
        'msg': f"This is 1 post"
}

post2 = {'id': 23,
        'key': "djfowejf",
        'timestamp': '2023-12-11T00:18:01.409527',
        'msg': f"This is 2 post"
}

post3 = {'id': 23,
        'key': "djfowejf",
        'timestamp': '2023-12-11T00:18:01.409527',
        'msg': f"This is 3 post"
}

new[0] = post
new[1] = post2
new[2] = post3


print(new)
mydict = new[2]
print(mydict.get('id'))
print(mydict.get('msg'))


