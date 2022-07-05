import requests
from telegram.ext import *
from telegram import *
from time import *
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import *

# 5522327707:AAFJjdtZeLb_hYCdyk4Rn7TjtGOv3Pm-SPA

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("key.json", scope)

client = gspread.authorize(creds)

def opensheet(worksheet):
    data = client.open("Tiền sinh hoạt tháng 7 - 904").worksheet(worksheet)
    return data

chung = opensheet('Chung')

ly = opensheet('Lý')

duong = opensheet('Dương')

dat = opensheet('Đạt')

tuan = opensheet('Tuấn')



def send_telegram_msg(bot_msg, chat_id):

    token_id = "5161246524:AAH1JXbk8unxiaBR5CH5QEB6DVfDfvrUJlE"
    chat_id = str(chat_id)
    send_text = "https://api.telegram.org/bot" + token_id + "/sendMessage?chat_id="+chat_id + "&parse_mode=MarkdownV2&text=" + bot_msg 
    response = requests.get(send_text)
    return(response.text)

def send_data(data, chat_id):
    text = ''
    text = text + 'STT'.ljust(8, " ")+ 'Thời gian'.ljust(15, " ")+ 'Tên vật dụng'.ljust(20, " ")+'Giá'.rjust(10, " ")+'\n'+'\n'
    for i in range(1,len(data)):
        text = text + str(i).ljust(8, " ")+ str(data[i][0]).ljust(15, " ")[9:19]+  str(data[i][1]).rjust(20, " ")+ str(data[i][2]).rjust(18, " ")+'\n\n'
    print(text)
    send_telegram_msg(str(text),chat_id)
    print(send_telegram_msg)


def multisend_message(name,item,cost):
    hanoi_tz = timezone(timedelta(hours=7))
    send_telegram_msg(f'{name} đã mua {item} với giá {cost}000 VND vào lúc {datetime.now(hanoi_tz).strftime("%H:%M:%S %d/%m/%Y")}', 2058798859)
    send_telegram_msg(f'{name} đã mua {item} với giá {cost}000 VND vào lúc {datetime.now(hanoi_tz).strftime("%H:%M:%S %d/%m/%Y")}', 5579622467)
    send_telegram_msg(f'{name} đã mua {item} với giá {cost}000 VND vào lúc {datetime.now(hanoi_tz).strftime("%H:%M:%S %d/%m/%Y")}', 5448207142)
    send_telegram_msg(f'{name} đã mua {item} với giá {cost}000 VND vào lúc {datetime.now(hanoi_tz).strftime("%H:%M:%S %d/%m/%Y")}', 5578472865)

def multisend_message1(name,sheet,row):
    hanoi_tz = timezone(timedelta(hours=7))
    send_telegram_msg(f'{name} đã xóa data :\n"Mua: {str(sheet[int(row)-1][1])} \nGiá {str(sheet[int(row)-1][2])}000 VND\nThời gian: {str(sheet[int(row)-1][0])}" \nvào lúc {datetime.now(hanoi_tz).strftime("%H:%M:%S %d/%m/%Y")}', 2058798859)
    send_telegram_msg(f'{name} đã xóa data :\n"Mua: {str(sheet[int(row)-1][1])} \nGiá {str(sheet[int(row)-1][2])}000 VND\nThời gian: {str(sheet[int(row)-1][0])}" \nvào lúc {datetime.now(hanoi_tz).strftime("%H:%M:%S %d/%m/%Y")}', 5579622467)
    send_telegram_msg(f'{name} đã xóa data :\n"Mua: {str(sheet[int(row)-1][1])} \nGiá {str(sheet[int(row)-1][2])}000 VND\nThời gian: {str(sheet[int(row)-1][0])}" \nvào lúc {datetime.now(hanoi_tz).strftime("%H:%M:%S %d/%m/%Y")}', 5448207142)
    send_telegram_msg(f'{name} đã xóa data :\n"Mua: {str(sheet[int(row)-1][1])} \nGiá {str(sheet[int(row)-1][2])}000 VND\nThời gian: {str(sheet[int(row)-1][0])}" \nvào lúc {datetime.now(hanoi_tz).strftime("%H:%M:%S %d/%m/%Y")}', 5578472865)

def updaterow(sheet, item, cost, datetime, row):
    sheet.update_cell(row,1, datetime)
    sheet.update_cell(row,2, item)
    sheet.update_cell(row,3, cost)

ITEM = []
COST = []
AllowID =[2058798859]
count1 = 0
count2 = 0
count3 = 0
count4 = 0


def copiedtext(text,name, chat_id):
    chat_id = str(chat_id)
    send_text = f"https://api.telegram.org/bot5161246524:AAH1JXbk8unxiaBR5CH5QEB6DVfDfvrUJlE/sendMessage?chat_id={chat_id}&text=Số tài khoản của {name} là: `{text}`&parse_mode=MarkDown"
    response = requests.get(send_text)

def sendlink( link_id ,  chat_id):
    chat_id = str(chat_id)
    send_text = f"https://api.telegram.org/bot5161246524:AAH1JXbk8unxiaBR5CH5QEB6DVfDfvrUJlE/sendMessage?chat_id={chat_id}&text=https://docs.google.com/spreadsheets/d/1OAHQOnYpSZh_rgt-S95T1S6KKPVkJ4C7-W-ESR0oT-U/edit#gid=0&parse_mode=MarkDown"
    print(send_text)
    response = requests.get(send_text)
    print(response.text)

async def deletedata(update: Update, context: CallbackContext):
    global count1,count3,count4,count2
    id = update.effective_user.id
    if id == 2058798859:
        await update.message.reply_text("Bạn muốn xóa dòng nào thế?\n\n")
        send_data(ly.get_all_values(), update.effective_user.id)
        count1 = -10
    elif id == 5579622467:
        await update.message.reply_text("Bạn muốn xóa dòng nào thế?\n\n")
        send_data(duong.get_all_values(), update.effective_user.id)
        count2 = -10
    elif id == 5578472865:
        await update.message.reply_text("Bạn muốn xóa dòng nào thế?\n\n")
        send_data(dat.get_all_values(), update.effective_user.id)
        count3 = -10
    elif id == 5448207142:
        await update.message.reply_text("Bạn muốn xóa dòng nào thế?\n\n")
        send_data(tuan.get_all_values(), update.effective_user.id)
        count4 = -10
    else:
        await update.message.reply_text(f"{update.effective_user.first_name} ! Bạn không được quyền dùng bot này")


async def handlmsg(update: Update, context: CallbackContext):
    global items1,costs1,count1,items2,costs2,count2,items3,costs3,count3,items4,costs4,count4
    list1= []
    list2= []
    list3= []
    list4= []
    id = update.effective_user.id
    if id == 2058798859:
        if count1 == 0:
            await update.message.reply_text("Bạn đã mua gì thế ?")

        if count1 == 1:
            items1 = update.message.text
            await update.message.reply_text(f"Bạn đã mua {items1} với giá bao nhiêu thế (Đơn vị kVND)?")

        if count1 == 2:
            costs1 = update.message.text
            hanoi_tz = timezone(timedelta(hours=7))
            list1= [datetime.now(hanoi_tz).strftime("%H:%M:%S %d/%m/%Y"), items1, costs1]
            ly.append_row(list1, value_input_option='USER_ENTERED')
            multisend_message('Lý',items1,costs1)
            count1 = -1

        if count1 == -10:
            data1 = ly.get_all_values()
            row1 = update.message.text
            ly.delete_rows(int(row1)+1)
            multisend_message1('Lý',data1,int(row1)+1)
            count1 = -1

        count1 += 1
    elif id == 5579622467:
        if count2 == 0:
            await update.message.reply_text("Bạn đã mua gì thế ?")

        if count2 == 1:
            items2 = update.message.text
            await update.message.reply_text(f"Bạn đã mua {items2} với giá bao nhiêu thế (Đơn vị kVND)?")

        if count2 == 2:
            costs2 = update.message.text
            hanoi_tz = timezone(timedelta(hours=7))
            list2= [datetime.now(hanoi_tz).strftime("%H:%M:%S %d/%m/%Y"), items2, costs2]
            duong.append_row(list2, value_input_option='USER_ENTERED')
            multisend_message('Dương',items2,costs2)
            count2 = -1

        if count2 == -10:
            data2 = duong.get_all_values()
            row2 = update.message.text
            duong.delete_rows(int(row2)+1)
            multisend_message1('Dương',data2,int(row2)+1)
            count2 = -1

        count2 += 1
    elif id == 5578472865:
        if count3 == 0:
            await update.message.reply_text("Bạn đã mua gì thế ?")

        if count3 == 1:
            items3 = update.message.text
            await update.message.reply_text(f"Bạn đã mua {items3} với giá bao nhiêu thế (Đơn vị kVND)?")

        if count3 == 2:
            costs3 = update.message.text
            hanoi_tz = timezone(timedelta(hours=7))
            list3= [datetime.now(hanoi_tz).strftime("%H:%M:%S %d/%m/%Y"), items3, costs3]
            dat.append_row(list3, value_input_option='USER_ENTERED')
            multisend_message('Đạt',items3,costs3)
            count3 = -1

        if count3 == -10:
            data3 = dat.get_all_values()
            row3 = update.message.text
            dat.delete_rows(int(row3)+1)
            multisend_message1('Đạt',data3,int(row3)+1)
            count3 = -1

        count3 += 1
    elif id == 5448207142:
        if count4 == 0:
            await update.message.reply_text("Bạn đã mua gì thế ?")

        if count4 == 1:
            items4 = update.message.text
            await update.message.reply_text(f"Bạn đã mua {items4} với giá bao nhiêu thế (Đơn vị kVND)?")

        if count4 == 2:
            costs4 = update.message.text
            hanoi_tz = timezone(timedelta(hours=7))
            list4= [datetime.now(hanoi_tz).strftime("%H:%M:%S %d/%m/%Y"), items4, costs4]
            tuan.append_row(list4, value_input_option='USER_ENTERED')
            multisend_message('Tuấn',items4,costs4)
            count4 = -1

        if count1 == -10:
            data4 = tuan.get_all_values()
            row4 = update.message.text
            tuan.delete_rows(int(row4)+1)
            multisend_message1('Tuấn',data4,int(row4)+1)
            count4 = -1

        count4 += 1
    else:
        await update.message.reply_text(f"{update.effective_user.first_name} ! Bạn không được quyền dùng bot này")




async def startCommand(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton('Tôi đã mua ...')] ,[KeyboardButton('/help')] ]
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Xin chào {update.effective_user.first_name}, đây là bot tính tiền sinh hoạt phòng 904\nBạn cần gì thế?\nNhấn vào /help để xem những câu lệnh\nNhấn bất kì kí tự nào để khai báo vật dụng đã mua', reply_markup=ReplyKeyboardMarkup(buttons))
    

async def help(update: Update, context: CallbackContext):
    await update.message.reply_text("""
        /distribution --> Xem đóng góp từng cá nhân

/ATM --> Xem số tài khoản

/balance --> Xem số dư từng cá nhân

/sum --> Xem tổng chi tiêu cả phòng

/average --> Xem trung bình từng thành viên

/deletedata --> Xóa dữ liệu

/cancel --> Đưa bot về trạng thái mặc định
    """)

async def sum(update: Update, context: CallbackContext):
    await update.message.reply_text(f'Tổng chi tiêu cả phòng tính tới bây giờ là : {chung.cell(6,2).value}000 VND')

async def cancel(update: Update, context: CallbackContext):
    global count1,count3,count4,count2
    id = update.effective_user.id
    if id == 2058798859:
        await update.message.reply_text(f'Đã đưa bot về trạng thái mặc định\nNhấn bất kì để khai báo')
        count1 = 0
    elif id == 5579622467:
        await update.message.reply_text(f'Đã đưa bot về trạng thái mặc định\nNhấn bất kì để khai báo')
        count2 = 0
    elif id == 5578472865:
        await update.message.reply_text(f'Đã đưa bot về trạng thái mặc định\nNhấn bất kì để khai báo')
        count3 = 0
    elif id == 5448207142:
        await update.message.reply_text(f'Đã đưa bot về trạng thái mặc định\nNhấn bất kì để khai báo')
        count4 = 0

async def average(update: Update, context: CallbackContext):
    await update.message.reply_text(f'Trung bình từng thành viên là : {chung.cell(7,2).value}000 VND')

async def distribution(update: Update, context: CallbackContext):
    buttons = [[InlineKeyboardButton("Lý", callback_data="ly0")], [InlineKeyboardButton("Dương", callback_data="duong0")], [InlineKeyboardButton("Đạt", callback_data="dat0")], [InlineKeyboardButton("Tuấn", callback_data="tuan0")]]
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Bạn muốn xem đóng góp của ai thế?")

async def ATM(update: Update, context: CallbackContext):
    buttons = [[InlineKeyboardButton("Lý ", callback_data="Ly1")], [InlineKeyboardButton("Dương ", callback_data="Duong1")], [InlineKeyboardButton("Đạt ", callback_data="Dat1")], [InlineKeyboardButton("Tuấn ", callback_data="Tuan1")]]
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Bạn muốn xem Số tài khoản của ai thế?")

async def balance(update: Update, context: CallbackContext):
    buttons = [[InlineKeyboardButton("Lý ", callback_data="Ly2")], [InlineKeyboardButton("Dương ", callback_data="Duong2")], [InlineKeyboardButton("Đạt ", callback_data="Dat2")], [InlineKeyboardButton("Tuấn ", callback_data="Tuan2")]]
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Bạn muốn xem Số dư của ai thế?")


async def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    await update.callback_query.answer()

    global count

    if "ly0" in query:
        send_telegram_msg(f'Đóng góp của Lý bây giờ là: {chung.cell(2,2).value}000 VND\n', update.effective_chat.id)
        send_data(ly.get_all_values(), update.effective_user.id)
        
    if "duong0" in query:
        send_telegram_msg(f'Đóng góp của Dương bây giờ là: {chung.cell(5,2).value}000 VND\n', update.effective_chat.id)
        send_data(duong.get_all_values(), update.effective_user.id)

    if "dat0" in query:
        send_telegram_msg(f'Đóng góp của Đạt bây giờ là: {chung.cell(4,2).value}000 VND\n', update.effective_chat.id)
        send_data(dat.get_all_values(), update.effective_user.id)

    if "tuan0" in query:
        send_telegram_msg(f'Đóng góp của Tuấn bây giờ là: {chung.cell(3,2).value}000 VND\n', update.effective_chat.id)
        send_data(tuan.get_all_values(), update.effective_user.id)

    if "Ly1" in query:
        copiedtext('04301690888', 'Lý',update.effective_chat.id)
        send_telegram_msg('Ngân hàng: TP Bank', update.effective_chat.id)
        await context.bot.send_photo(chat_id=update.effective_chat.id ,photo = 'https://upanh.tv/image/zBQV1Z',caption="Hoặc sử dụng QR code")
    
    if "Duong1" in query:
        copiedtext('105872057409', 'Dương',update.effective_chat.id)
        send_telegram_msg('Ngân hàng: Vietinbank', update.effective_chat.id)

    if "Dat1" in query:
        copiedtext('996803022002', 'Đạt',update.effective_chat.id)
        send_telegram_msg('Ngân hàng: MB Bank', update.effective_chat.id)

    if "Tuan1" in query:
        copiedtext('81089731333333', 'Tuấn',update.effective_chat.id)
        send_telegram_msg('Ngân hàng: Nam Á', update.effective_chat.id)

    if "Ly2" in query:
        send_telegram_msg(f"Số dư của Lý bây giờ là: {str(chung.cell(2,3).value).replace('-',' âm ')}000 VND\nNhấn vào để xem chi tiết", update.effective_chat.id)
        sendlink('0',update.effective_chat.id)
    
    if "Duong2" in query:
        send_telegram_msg(f"Số dư của Dương bây giờ là: {str(chung.cell(5,3).value).replace('-',' âm ')}000 VND\nNhấn vào để xem chi tiết", update.effective_chat.id)
        sendlink('0',update.effective_chat.id)

    if "Dat2" in query:
        send_telegram_msg(f"Số dư của Đạt bây giờ là: {str(chung.cell(4,3).value).replace('-',' âm ')}000 VND\nNhấn vào để xem chi tiết", update.effective_chat.id)
        sendlink('0',update.effective_chat.id)

    if "Tuan2" in query:
        send_telegram_msg(f"Số dư của Tuấn bây giờ là: {str(chung.cell(3,3).value).replace('-',' âm ')}000 VND\nNhấn vào để xem chi tiết", update.effective_chat.id)
        sendlink('0',update.effective_chat.id)

app = ApplicationBuilder().token("5161246524:AAH1JXbk8unxiaBR5CH5QEB6DVfDfvrUJlE").build()

app.add_handler(CommandHandler("start", startCommand))

app.add_handler(CommandHandler("help", help))

app.add_handler(CommandHandler("distribution", distribution))

app.add_handler(CommandHandler("ATM", ATM))

app.add_handler(CommandHandler("sum", sum))

app.add_handler(CommandHandler("average", average))

app.add_handler(CommandHandler("balance", balance))

app.add_handler(CommandHandler("deletedata", deletedata))

app.add_handler(CommandHandler("cancel", cancel))

app.add_handler(MessageHandler(filters.TEXT, handlmsg))

app.add_handler(CallbackQueryHandler(queryHandler))

app.run_polling()
