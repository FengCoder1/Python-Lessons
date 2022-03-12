goal = input("Dᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴍᴀᴋᴇ ᴀ sʜᴏᴘᴘɪɴɢ ʟɪsᴛ?")
if goal.lower() == "yes":
    shopping_list = []
    item_number = int(input("Hᴏᴡ ᴍᴀɴʏ ɪᴛᴇᴍs ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ sʜᴏᴘᴘɪɴɢ ʟɪsᴛ?"))
    while item_number > 0:
        answer = input("Wʜᴀᴛ ᴅᴏ ʏᴏᴜss ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ sʜᴏᴘᴘɪɴɢ ʟɪsᴛ?")
        shopping_list.append(answer)
        item_number -= 1
    add_more = input("Dᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴍᴏʀᴇ ɪᴛᴇᴍs ᴛᴏ ʏᴏᴜʀ sʜᴏᴘᴘɪɴɢ ʟɪsᴛ?")
    while add_more.lower() == "yes":
        answer = input("Wʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ sʜᴏᴘᴘɪɴɢ ʟɪsᴛ?")
        shopping_list.append(answer)
        add_more = input("Dᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴍᴏʀᴇ ɪᴛᴇᴍs ᴛᴏ ʏᴏᴜʀ sʜᴏᴘᴘɪɴɢ ʟɪsᴛ?")
    print("Yᴏᴜʀ sʜᴏᴘᴘɪɴɢ ʟɪsᴛ ʜᴀs: ")
    for item in shopping_list:
        print(item)
else:
    print("OK, ʙʏᴇ!")