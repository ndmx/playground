def groups_per_user(group_dictionary):
    user_groups = {}
    list1 = []
    list2 = []
    for groups, users in group_dictionary.items():
        for user in users:
            
            print("QA view list2: {}".format(list(set(list2))))
            print("Current User: {} with {} Permission\n".format(user,groups))
            list1.insert(0,groups)
            user_groups[user] = list1
            print("New User Added, Group => {}".format(user_groups))
            list2.extend(list1)
            #list2.insert(0, groups)
            user_groups[user] = list(set(list2))
            list1.clear()
            print("All Users in {}\n".format(user_groups))
        
        
    return user_groups

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
        "Remote":  ["admin", "userC"],
		"administrator": ["admin"] }))