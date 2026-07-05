#check list uniqueness
items=["apple","banana","orange","apple"]
uniqe_items=set()
for item in items:
    if item in uniqe_items:
        print(item,"is not unique")
        break
    else:
        uniqe_items.add(item)
        