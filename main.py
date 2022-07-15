from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import datetime as dt
import pymysql
import pymysql.cursors
import random
import asyncio

bot = Bot(token='5209796468:AAEz1whM_MDZ24usJCc3PlK4naEyMU8otQQ')
dp = Dispatcher(bot)

print('bot started..."')

# list of users identified by ChatID
users = {}

timer = 0
UserCounter = 0
UserNo = 0


class User:
    def __init__(self, chat_id,
                 avalue, bvalue, MessageHandlerType,
                 Objectiveno, MyObjectives, MyObjectivesDate,
                 Objective1MilestoneNo, MyObjective1Milestones, MyObjective1MilestoneDates, MyObjective1MilestoneStatus,
                 Objective2MilestoneNo, MyObjective2Milestones, MyObjective2MilestoneDates, MyObjective2MilestoneStatus,
                 Objective3MilestoneNo, MyObjective3Milestones, MyObjective3MilestoneDates,
                 MyObjective3MilestoneStatus):
        self.chat_id = chat_id

        self.avalue = avalue
        self.bvalue = bvalue
        self.MessageHandlerType = MessageHandlerType

        self.Objectiveno = Objectiveno
        self.MyObjectives = MyObjectives
        self.MyObjectivesDate = MyObjectivesDate

        self.Objective1MilestoneNo = Objective1MilestoneNo
        self.MyObjective1Milestones = MyObjective1Milestones
        self.MyObjective1MilestoneDates = MyObjective1MilestoneDates
        self.MyObjective1MilestoneStatus = MyObjective1MilestoneStatus

        self.Objective2MilestoneNo = Objective2MilestoneNo
        self.MyObjective2Milestones = MyObjective2Milestones
        self.MyObjective2MilestoneDates = MyObjective2MilestoneDates
        self.MyObjective2MilestoneStatus = MyObjective2MilestoneStatus

        self.Objective3MilestoneNo = Objective3MilestoneNo
        self.MyObjective3Milestones = MyObjective3Milestones
        self.MyObjective3MilestoneDates = MyObjective3MilestoneDates
        self.MyObjective3MilestoneStatus = MyObjective3MilestoneStatus


def SyncDataBase(Type, ChatIDCurrent, ObjectiveNo, ListNo, TypeNo):  # 1:Name 2:Date 3:Status
    #connection = pymysql.connect(host='remotemysql.com', user='g4gIqpoa8A', password='V2sTQ01WsK',
    #                             database='g4gIqpoa8A',
    #                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    connection = pymysql.connect(host='db4free.net', user='mrmeet', password='ccleonliew',
                                 database='mrmeet',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()

    if Type == 'Query':
        if ObjectiveNo == 0:
            if TypeNo == 1:  # Name
                cur.execute("SELECT MyObjectives{} FROM chat WHERE chat_id = {}".format(ListNo, ChatIDCurrent))
                result = cur.fetchone()
                print(result)
                n = len('MyObjectivesX')
                result = str(result).replace('{', '').replace('}', '').replace(':', '').replace("'", "")
                result = result[n + 1:]
                users[str(ChatIDCurrent)].MyObjectives[ListNo - 1] = result

            if TypeNo == 2:  # Date
                cur.execute("SELECT MyObjectivesDate{} FROM chat WHERE chat_id = {}".format(ListNo, ChatIDCurrent))
                result = cur.fetchone()
                n = len('MyObjectivesDateX')
                result = str(result).replace('{', '').replace('}', '').replace(':', '').replace("'", "")
                result = result[n + 1:]
                users[str(ChatIDCurrent)].MyObjectivesDate[ListNo - 1] = result

        else:
            if TypeNo == 1:  # name
                cur.execute("SELECT MyObjective{}Milestones{} FROM chat WHERE chat_id = {}".format(ObjectiveNo, ListNo,
                                                                                                   ChatIDCurrent))
                result = cur.fetchone()
                n = len('MyObjectiveXMilestonesX')
                result = str(result).replace('{', '').replace('}', '').replace(':', '').replace("'", "")
                result = result[n + 1:]

                if ObjectiveNo == 1:
                    users[str(ChatIDCurrent)].MyObjective1Milestones[ListNo - 1] = result
                    print(users[str(ChatIDCurrent)].MyObjective1Milestones[ListNo - 1])
                if ObjectiveNo == 2:
                    users[str(ChatIDCurrent)].MyObjective2Milestones[ListNo - 1] = result
                if ObjectiveNo == 3:
                    users[str(ChatIDCurrent)].MyObjective3Milestones[ListNo - 1] = result

            if TypeNo == 2:  # date
                cur.execute(
                    "SELECT MyObjective{}MilestoneDates{} FROM chat WHERE chat_id = {}".format(ObjectiveNo, ListNo,
                                                                                               ChatIDCurrent))
                result = cur.fetchone()
                n = len('MyObjectiveXMilestoneDatesX')
                result = str(result).replace('{', '').replace('}', '').replace(':', '').replace("'", "")
                result = result[n + 1:]

                if ObjectiveNo == 1:
                    users[str(ChatIDCurrent)].MyObjective1MilestoneDates[ListNo - 1] = result
                if ObjectiveNo == 2:
                    users[str(ChatIDCurrent)].MyObjective2MilestoneDates[ListNo - 1] = result
                if ObjectiveNo == 3:
                    users[str(ChatIDCurrent)].MyObjective3MilestoneDates[ListNo - 1] = result

            if TypeNo == 3:  # Status
                cur.execute(
                    "SELECT MyObjective{}MilestoneStatus{} FROM chat WHERE chat_id = {}".format(ObjectiveNo, ListNo,
                                                                                                ChatIDCurrent))
                result = cur.fetchone()
                print(result)
                n = len('MyObjectiveXMilestoneStatusX')
                result = str(result).replace('{', '').replace('}', '').replace(':', '').replace("'", "")
                result = result[n + 1:]

                if ObjectiveNo == 1:
                    users[str(ChatIDCurrent)].MyObjective1MilestoneStatus[ListNo - 1] = result
                if ObjectiveNo == 2:
                    users[str(ChatIDCurrent)].MyObjective2MilestoneStatus[ListNo - 1] = result
                if ObjectiveNo == 3:
                    users[str(ChatIDCurrent)].MyObjective3MilestoneStatus[ListNo - 1] = result

    if Type == 'Update':
        if ObjectiveNo == 0:
            if TypeNo == 1:
                result = users[str(ChatIDCurrent)].MyObjectives[ListNo - 1]
                cur.execute("UPDATE chat SET MyObjectives{} = '{}' WHERE chat_id = {}".format(ListNo, result,
                                                                                              ChatIDCurrent))
                connection.commit()

            if TypeNo == 2:
                result = users[str(ChatIDCurrent)].MyObjectivesDate[ListNo - 1]
                cur.execute(
                    "UPDATE chat SET MyObjectivesDate{} = '{}' WHERE chat_id = {}".format(ListNo, result,
                                                                                          ChatIDCurrent))
                connection.commit()

        else:
            if TypeNo == 1:
                if ObjectiveNo == 1:
                    result = users[str(ChatIDCurrent)].MyObjective1Milestones[ListNo - 1]
                if ObjectiveNo == 2:
                    result = users[str(ChatIDCurrent)].MyObjective2Milestones[ListNo - 1]
                if ObjectiveNo == 3:
                    result = users[str(ChatIDCurrent)].MyObjective3Milestones[ListNo - 1]

                cur.execute(
                    "UPDATE chat SET MyObjective{}Milestones{} = '{}' WHERE chat_id = {}".format(ObjectiveNo, ListNo,
                                                                                                 result,
                                                                                                 ChatIDCurrent))
                connection.commit()

            if TypeNo == 2:
                if ObjectiveNo == 1:
                    result = users[str(ChatIDCurrent)].MyObjective1MilestoneDates[ListNo - 1]
                if ObjectiveNo == 2:
                    result = users[str(ChatIDCurrent)].MyObjective2MilestoneDates[ListNo - 1]
                if ObjectiveNo == 3:
                    result = users[str(ChatIDCurrent)].MyObjective3MilestoneDates[ListNo - 1]

                cur.execute(
                    "UPDATE chat SET MyObjective{}MilestoneDates{} = '{}' WHERE chat_id = {}".format(ObjectiveNo,
                                                                                                     ListNo,
                                                                                                     result,
                                                                                                     ChatIDCurrent))
                connection.commit()

            if TypeNo == 3:
                if ObjectiveNo == 1:
                    result = users[str(ChatIDCurrent)].MyObjective1MilestoneStatus[ListNo - 1]
                if ObjectiveNo == 2:
                    result = users[str(ChatIDCurrent)].MyObjective2MilestoneStatus[ListNo - 1]
                if ObjectiveNo == 3:
                    result = users[str(ChatIDCurrent)].MyObjective3MilestoneStatus[ListNo - 1]

                cur.execute(
                    "UPDATE chat SET MyObjective{}MilestoneStatus{} = '{}' WHERE chat_id = {}".format(ObjectiveNo,
                                                                                                      ListNo,
                                                                                                      result,
                                                                                                      ChatIDCurrent))
                connection.commit()


# Check if existing user chat. If not, Initialize.
def UserChecker(ChatIDCurrent):
    for x in users:
        print('x is {}'.format(x))
        print('and the chat id is {}'.format(users[x].chat_id))
        if ChatIDCurrent == users[x].chat_id:
            return

    users["{}".format(ChatIDCurrent)] = User(ChatIDCurrent,
                                             0, 0, 0,
                                             0, ['', '', ''], ['', '', ''],
                                             0, ['', '', '', '', ''], ['', '', '', '', ''],
                                             ['Pending', 'Pending', 'Pending', 'Pending', 'Pending'],
                                             0, ['', '', '', '', ''], ['', '', '', '', ''],
                                             ['Pending', 'Pending', 'Pending', 'Pending', 'Pending'],
                                             0, ['', '', '', '', ''], ['', '', '', '', ''],
                                             ['Pending', 'Pending', 'Pending', 'Pending', 'Pending'])
    connection = pymysql.connect(host='db4free.net', user='mrmeet', password='ccleonliew',
                                 database='mrmeet',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    Pass = generator()
    cur = connection.cursor()
    cur.execute("INSERT INTO chat(chat_id, pass)"
                "VALUES({}, '{}')".format(ChatIDCurrent, Pass))
    connection.commit()
    global UserNo
    UserNo += 1


def generator():
    chars = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*"
    password = ""
    for x in range(10):
        password_char = random.choice(chars)
        password = password + password_char
    return password


def NextDays(day, month, year):
    if len(str(day)) == 1:
        Date = str(0) + str(day)
    else:
        Date = str(day)
    if len(str(month)) == 1:
        Date += str(0)
    Date += str(month)
    if len(str(year)) == 1:
        Date += str(0)
    Date += str(year)

    print(Date)

    if DateChecker(Date) == 'True':
        year = str(20) + str(year)
        return '[{}]'.format(Date) + ' ' + dt.date(int(year), month, day).strftime("%A") + ' ' + dt.date(int(year),
                                                                                                         month,
                                                                                                         day).strftime(
            "%B") + ' ' + str(day)
    else:
        if month == 13:
            return NextDays(day, month, year + 1)
        if month == 2:
            return NextDays(day - 28, month + 1, year)
        if month == 4 or month == 6 or month == 9 or month == 11:
            return NextDays(day - 30, month + 1, year)
        else:
            return NextDays(day - 31, month + 1, year)


@dp.callback_query_handler(text=['This week'])
async def poll(call: types.CallbackQuery):
    date1 = dt.date.today()
    year = int(str(date1.year)[2:4])
    month = int(date1.month)
    day = int(date1.day)
    await call.message.answer_poll(question='Poll for availability',
                                   options=[NextDays(day + 1, month, year), NextDays(day + 2, month, year),
                                            NextDays(day + 3, month, year), NextDays(day + 4, month, year),
                                            NextDays(day + 5, month, year), NextDays(day + 6, month, year),
                                            NextDays(day + 7, month, year)],
                                   type='regular',
                                   is_anonymous=False,
                                   allows_multiple_answers=True)


@dp.callback_query_handler(text=['Custom'])
async def poll(call: types.CallbackQuery):
    await call.message.answer('Enter your start date in the form ddmmyy')
    ChatIDCurrent = call.message.chat.id
    users[str(ChatIDCurrent)].MessageHandlerType = 3

    @dp.message_handler()
    async def RecieveMsg(message: types.Message):
        print('hi')



@dp.callback_query_handler(text=['Next week'])
async def poll(call: types.CallbackQuery):
    date1 = dt.date.today()
    year = int(str(date1.year)[2:4])
    month = int(date1.month)
    day = int(date1.day)
    await call.message.answer_poll(question='Poll for availability',
                                   options=[NextDays(day + 8, month, year), NextDays(day + 9, month, year),
                                            NextDays(day + 10, month, year), NextDays(day + 11, month, year),
                                            NextDays(day + 12, month, year), NextDays(day + 13, month, year),
                                            NextDays(day + 14, month, year)],
                                   type='regular',
                                   is_anonymous=False,
                                   allows_multiple_answers=True)


@dp.message_handler(commands=['Meetup'])
async def StartTab(message: types.Message):
    await message.answer(
        "When do you want to meet up?", reply_markup=MeetupOptions(), parse_mode='Markdown')


# the start tab and message when /start
@dp.message_handler(commands=['start'])
async def StartTab(message: types.Message):
    ChatIDCurrent = message.chat.id
    print(ChatIDCurrent)
    UserChecker(ChatIDCurrent)
    await message.answer(
        "Click on *Objectives* or *Meetup* to get started! \nClick on *Overview* to view your created objectives!",
        reply_markup=Keyboard1(), parse_mode='Markdown')


@dp.message_handler(commands=['WebApp'])
async def WebAppTab(message: types.Message):
    ChatIDCurrent = message.chat.id
    connection = pymysql.connect(host='db4free.net', user='mrmeet', password='ccleonliew',
                                 database='mrmeet',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    cur.execute("SELECT pass FROM chat WHERE chat_id = {}".format(ChatIDCurrent))
    result = cur.fetchone()
    n = len('pass')
    result = str(result).replace('{', '').replace('}', '').replace(':', '').replace("'", "")
    result = result[n + 1:]

    await message.answer("For easier editing of Objectives and Milestones, visit: https://MrMeet-1.ldogsloop.repl.co \n\n"
                         "*Chat ID:* {}\n*Password:* {}".format(ChatIDCurrent, result), parse_mode='Markdown')


# keyboard interface when /start
def Keyboard1():
    button1 = KeyboardButton("/Overview")
    button2 = KeyboardButton("/WebApp")
    button3 = KeyboardButton("/Objectives")
    button4 = KeyboardButton("/Meetup")
    return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button3, button4).row(button1, button2)


def ShowOverview(ObjectiveNo, Message, ChatIDCurrent):
    if ObjectiveNo == 0:
        return Message

    if ObjectiveNo == 1:
        MilestoneNo = users[str(ChatIDCurrent)].Objective1MilestoneNo
    if ObjectiveNo == 2:
        MilestoneNo = users[str(ChatIDCurrent)].Objective2MilestoneNo
    if ObjectiveNo == 3:
        MilestoneNo = users[str(ChatIDCurrent)].Objective3MilestoneNo

    if MilestoneNo == 0:
        SyncDataBase('Query', ChatIDCurrent, 0, ObjectiveNo, 1)
        SyncDataBase('Query', ChatIDCurrent, 0, ObjectiveNo, 2)
        NewMessage = '*Overview for {}*\n'.format(users[str(ChatIDCurrent)].MyObjectives[ObjectiveNo - 1]) \
                     + 'Due *{}* in *{}* days\n\n'.format((users[str(ChatIDCurrent)].MyObjectivesDate[ObjectiveNo - 1]),
                                                          DaysLeft(ChatIDCurrent, 0, ObjectiveNo)) \
                     + Message
        return ShowOverview(ObjectiveNo - 1, NewMessage, ChatIDCurrent)

    SyncDataBase('Query', ChatIDCurrent, ObjectiveNo, MilestoneNo, 1)
    NewMessage = ShowMilestones(MilestoneNo, ObjectiveNo, '', ChatIDCurrent) + Message
    return ShowOverview(ObjectiveNo - 1, NewMessage, ChatIDCurrent)


@dp.message_handler(commands=['Overview'])
async def Overview(message: types.Message):
    ChatIDCurrent = message.chat.id
    ObjectiveNo = users[str(ChatIDCurrent)].Objectiveno

    if ObjectiveNo == 0:
        await message.answer('You have no Objectives yet, go to the objectives tab to create some!')

    else:
        await message.answer('{}'.format(ShowOverview(ObjectiveNo, '', ChatIDCurrent)), parse_mode='Markdown')


# inlinekeyboard interface when /Objectives
def MeetupOptions():
    button0 = InlineKeyboardButton(text="This week", callback_data='This week')
    button = InlineKeyboardButton(text="Next week", callback_data="Next week")
    button1 = InlineKeyboardButton(text="Custom", callback_data="Custom")
    return InlineKeyboardMarkup().add(button0, button).add(button1)


# inlinekeyboard interface when /Objectives
def Objective(Objectiveno, ChatIDCurrent):
    if Objectiveno == 0:
        button0 = InlineKeyboardButton(text="Create Objectives", callback_data='Create')
        return InlineKeyboardMarkup().add(button0)

    SyncDataBase('Query', ChatIDCurrent, 0, Objectiveno, 1)
    current = users[str(ChatIDCurrent)].MyObjectives[Objectiveno - 1]
    button = InlineKeyboardButton(text='{}'.format(current),
                                  callback_data="Objective {}".format(Objectiveno))
    return Objective(Objectiveno - 1, ChatIDCurrent).add(button)


# inlinekeyboard interface when /Objectives and ObjectiveNo is max
def MaxObjective(Objectiveno, ChatIDCurrent):
    if Objectiveno == 0:
        return InlineKeyboardMarkup()

    SyncDataBase('Query', ChatIDCurrent, 0, Objectiveno, 1)
    current = users[str(ChatIDCurrent)].MyObjectives[Objectiveno - 1]
    button = InlineKeyboardButton(text='{}'.format(current),
                                  callback_data="Objective {}".format(Objectiveno))
    return MaxObjective(Objectiveno - 1, ChatIDCurrent).add(button)


# the milestones tab and message when /milestones
@dp.message_handler(commands=['Objectives'])
async def ObjectivesTab(message: types.Message):
    ChatIDCurrent = message.chat.id
    Objectiveno = users[str(ChatIDCurrent)].Objectiveno
    if Objectiveno < 3:
        await message.answer(
            'you currently have *{}* Objectives. \nclick on your objectives to view them, or click *create* to create some!'.format(
                Objectiveno),
            reply_markup=Objective(Objectiveno, ChatIDCurrent), parse_mode='Markdown')

    else:
        await message.answer(
            'you currently have a max of *{}* Objectives! \n click on your *objectives* to view them!'.format(
                Objectiveno),
            reply_markup=MaxObjective(Objectiveno, ChatIDCurrent), parse_mode='Markdown')


# check for correct input for objective date
def DateChecker(ObjectiveDate):
    for character in ObjectiveDate:
        if character.isdigit():
            print('ok')
        else:
            return 'False'

    date1 = dt.date.today()
    day = int(ObjectiveDate[0:2])
    month = int(ObjectiveDate[2:4])
    year = int(ObjectiveDate[4:7])

    if len(ObjectiveDate) != 6:
        return 'False'

    if day > 31:
        return 'False'
    if month == 2:
        if day > 28:
            return 'False'
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            return 'False'

    if month > 12:
        return 'False'
    if year < int(str(date1.year)[2:4]):
        print(int(str(date1.year)[2:4]))
        return 'False'
    if year == int(str(date1.year)[2:4]):
        print('2')
        if month < int(date1.month):
            return 'False'
        if month == int(date1.month):
            if day < int(date1.day):
                return 'False'

    return 'True'


def daysNeg(day, month, year, DayToday, MonthToday, YearToday, no):
    if year < YearToday:
        if month == 13:
            return daysNeg(0, 1, year + 1, DayToday, MonthToday, YearToday, no + day - 31)
        if month == 2:
            return daysNeg(day, month + 1, year, DayToday, MonthToday, YearToday, no - 28)
        if month == 4 or month == 6 or month == 9 or month == 11:
            return daysNeg(day, month + 1, year, DayToday, MonthToday, YearToday, no - 30)
        else:
            return daysNeg(day, month + 1, year, DayToday, MonthToday, YearToday, no - 31)

    else:
        if month < MonthToday:
            if MonthToday == 2:
                return days(day, month + 1, year, DayToday, MonthToday, YearToday, no - 28)
            if MonthToday == 4 or month == 6 or month == 9 or month == 11:
                return days(day, month + 1, year, DayToday, MonthToday, YearToday, no - 30)
            else:
                return days(day, month + 1, year, DayToday, MonthToday, YearToday, no - 31)

        else:
            return no + (day - DayToday)


def days(day, month, year, DayToday, MonthToday, YearToday, no):
    if year < YearToday:
        return daysNeg(day, month, year, DayToday, MonthToday, YearToday, no)
    if year > YearToday:
        if month == 0:
            return days(0, 12, year - 1, DayToday, MonthToday, YearToday, no + day)
        if month == 2:
            return days(day, month - 1, year, DayToday, MonthToday, YearToday, no + 28)
        if month == 4 or month == 6 or month == 9 or month == 11:
            return days(day, month - 1, year, DayToday, MonthToday, YearToday, no + 30)
        else:
            return days(day, month - 1, year, DayToday, MonthToday, YearToday, no + 31)

    else:
        if month < MonthToday:
            return daysNeg(day, month, year, DayToday, MonthToday, YearToday, no)
        if month > MonthToday:
            if MonthToday == 2:
                return days(day, month - 1, year, DayToday, MonthToday, YearToday, no + 28)
            if MonthToday == 4 or month == 6 or month == 9 or month == 11:
                return days(day, month - 1, year, DayToday, MonthToday, YearToday, no + 30)
            else:
                return days(day, month - 1, year, DayToday, MonthToday, YearToday, no + 31)
        else:
            return no + (day - DayToday)


# If objectiveNo > 0, ListNo = MilestoneNo
# If objectiveNo = 0, ListNo = ObjectiveNo
def DaysLeft(ChatIDCurrent, ObjectiveNo, ListNo):
    if ObjectiveNo == 0:
        Date = users[str(ChatIDCurrent)].MyObjectivesDate[ListNo - 1]
    if ObjectiveNo == 1:
        Date = users[str(ChatIDCurrent)].MyObjective1MilestoneDates[ListNo - 1]
    if ObjectiveNo == 2:
        Date = users[str(ChatIDCurrent)].MyObjective2MilestoneDates[ListNo - 1]
    if ObjectiveNo == 3:
        Date = users[str(ChatIDCurrent)].MyObjective3MilestoneDates[ListNo - 1]

    print('Date{}'.format(Date))
    DayToday = int(dt.date.today().day)
    # print(DayToday)
    MonthToday = int(dt.date.today().month)
    # print(MonthToday)
    YearToday = int(str(dt.date.today().year)[2:4])
    # print(YearToday)

    day = int(Date[0:2])
    print('day{}'.format(day))
    month = int(Date[2:4])
    print('month{}'.format(month))
    year = int(Date[4:7])
    print('year{}'.format(year))

    return days(day, month, year, DayToday, MonthToday, YearToday, 0)


# when inlinekeyboard 'create' button is pressed
@dp.callback_query_handler(text=['Create'])
async def CreateObjectiveTab(call: types.CallbackQuery):
    ChatIDCurrent = call.message.chat.id
    print(ChatIDCurrent)
    users[str(ChatIDCurrent)].bvalue = users[str(ChatIDCurrent)].avalue  # b = a
    users[str(ChatIDCurrent)].Objectiveno += 1  # Objectiveno += 1

    await call.message.answer('Enter the Name of Objective')
    users[str(ChatIDCurrent)].MessageHandlerType = 1

    @dp.message_handler()
    async def RecieveMsg(message: types.Message):
        print('hi')


# when Create Milestones button is pressed
@dp.callback_query_handler(text=['Create Milestones For Objective 1', 'Create Milestones For Objective 2',
                                 'Create Milestones For Objective 3'])
async def CreateMilestoneTab(call: types.CallbackQuery):
    ChatIDCurrent = call.message.chat.id
    users[str(ChatIDCurrent)].bvalue = users[str(ChatIDCurrent)].avalue

    await call.message.answer('Name of Milestone?')

    if call.data == 'Create Milestones For Objective 1':
        users[str(ChatIDCurrent)].Objective1MilestoneNo += 1
        users[str(ChatIDCurrent)].MessageHandlerType = 21

    if call.data == 'Create Milestones For Objective 2':
        users[str(ChatIDCurrent)].Objective2MilestoneNo += 1
        users[str(ChatIDCurrent)].MessageHandlerType = 22

    if call.data == 'Create Milestones For Objective 3':
        users[str(ChatIDCurrent)].Objective3MilestoneNo += 1
        users[str(ChatIDCurrent)].MessageHandlerType = 23

    @dp.message_handler()
    async def RecieveMsg(message: types.Message):
        print('hi')


# when a Milestone button is pressed
@dp.callback_query_handler(text=['Objective 1 Milestone 1', 'Objective 1 Milestone 2', 'Objective 1 Milestone 3',
                                 'Objective 1 Milestone 4', 'Objective 1 Milestone 5', 'Objective 2 Milestone 1',
                                 'Objective 2 Milestone 2', 'Objective 2 Milestone 3', 'Objective 2 Milestone 4',
                                 'Objective 2 Milestone 5', 'Objective 3 Milestone 1', 'Objective 3 Milestone 2',
                                 'Objective 3 Milestone 3', 'Objective 3 Milestone 4', 'Objective 3 Milestone 5'])
async def ToggleTab(call: types.CallbackQuery):
    ChatIDCurrent = call.from_user.id
    ObjectiveNo = int((call.data)[10])
    MilestoneNo = int((call.data)[22])

    SyncDataBase('Query', ChatIDCurrent, ObjectiveNo, MilestoneNo, 3)

    if ObjectiveNo == 1:
        ObjectiveMilestoneNo = users[str(ChatIDCurrent)].Objective1MilestoneNo
        Milestone = users[str(ChatIDCurrent)].MyObjective1Milestones[MilestoneNo - 1]
        if users[str(ChatIDCurrent)].MyObjective1MilestoneStatus[MilestoneNo - 1] == 'Pending':
            users[str(ChatIDCurrent)].MyObjective1MilestoneStatus[MilestoneNo - 1] = 'Completed'
            toggle = 0
        else:
            users[str(ChatIDCurrent)].MyObjective1MilestoneStatus[MilestoneNo - 1] = 'Pending'
            toggle = 1

    if ObjectiveNo == 2:
        ObjectiveMilestoneNo = users[str(ChatIDCurrent)].Objective2MilestoneNo
        Milestone = users[str(ChatIDCurrent)].MyObjective2Milestones[MilestoneNo - 1]
        if users[str(ChatIDCurrent)].MyObjective2MilestoneStatus[MilestoneNo - 1] == 'Pending':
            users[str(ChatIDCurrent)].MyObjective2MilestoneStatus[MilestoneNo - 1] = 'Completed'
            toggle = 0
        else:
            users[str(ChatIDCurrent)].MyObjective2MilestoneStatus[MilestoneNo - 1] = 'Pending'
            toggle = 1

    if ObjectiveNo == 3:
        ObjectiveMilestoneNo = users[str(ChatIDCurrent)].Objective3MilestoneNo
        Milestone = users[str(ChatIDCurrent)].MyObjective3Milestones[MilestoneNo - 1]
        if users[str(ChatIDCurrent)].MyObjective3MilestoneStatus[MilestoneNo - 1] == 'Pending':
            users[str(ChatIDCurrent)].MyObjective3MilestoneStatus[MilestoneNo - 1] = 'Completed'
            toggle = 0
        else:
            users[str(ChatIDCurrent)].MyObjective3MilestoneStatus[MilestoneNo - 1] = 'Pending'
            toggle = 1

    SyncDataBase('Update', ChatIDCurrent, ObjectiveNo, MilestoneNo, 3)

    if toggle == 0:
        await call.message.answer(
            'Milestone *{}* has been toggled to: *Completed*'.format(Milestone),
            parse_mode='Markdown')
    else:
        await call.message.answer(
            'Milestone *{}* has been toggled to: *Pending*'.format(Milestone),
            parse_mode='Markdown')

    msg = ShowMilestone(ObjectiveMilestoneNo, ObjectiveNo, ChatIDCurrent)
    await call.message.answer(msg, parse_mode='Markdown')


# Show the Current Milestones buttons and provide option to show and create milestones
def Milestone(ObjectiveMilestoneNo, ObjectiveNo, ChatIDCurrent):
    if ObjectiveMilestoneNo == -1:
        button = InlineKeyboardButton(text="Show Milestones",
                                      callback_data='Show Milestones For Objective {}'.format(ObjectiveNo))
        return InlineKeyboardMarkup().add(button)

    if ObjectiveMilestoneNo == 0:
        button = InlineKeyboardButton(text="Create Milestones",
                                      callback_data='Create Milestones For Objective {}'.format(ObjectiveNo))
        return Milestone(ObjectiveMilestoneNo - 1, ObjectiveNo, ChatIDCurrent).add(button)

    if ObjectiveNo == 1:
        current = users[str(ChatIDCurrent)].MyObjective1Milestones[ObjectiveMilestoneNo - 1]
    if ObjectiveNo == 2:
        current = users[str(ChatIDCurrent)].MyObjective2Milestones[ObjectiveMilestoneNo - 1]
    if ObjectiveNo == 3:
        current = users[str(ChatIDCurrent)].MyObjective3Milestones[ObjectiveMilestoneNo - 1]

    button = InlineKeyboardButton(text='{}'.format(current),
                                  callback_data="Objective {} Milestone {}".format(ObjectiveNo, ObjectiveMilestoneNo))

    return Milestone(ObjectiveMilestoneNo - 1, ObjectiveNo, ChatIDCurrent).add(button)


# Show the Current Milestones buttons and provide option to show milestones only
def MaxMilestone(ObjectiveMilestoneNo, ObjectiveNo, ChatIDCurrent):
    if ObjectiveMilestoneNo == 0:
        button = InlineKeyboardButton(text="Show Milestones",
                                      callback_data='Show Milestones For Objective {}'.format(ObjectiveNo))
        return InlineKeyboardMarkup().add(button)

    if ObjectiveNo == 1:
        current = users[str(ChatIDCurrent)].MyObjective1Milestones[ObjectiveMilestoneNo - 1]
    if ObjectiveNo == 2:
        current = users[str(ChatIDCurrent)].MyObjective2Milestones[ObjectiveMilestoneNo - 1]
    if ObjectiveNo == 3:
        current = users[str(ChatIDCurrent)].MyObjective3Milestones[ObjectiveMilestoneNo - 1]

    button = InlineKeyboardButton(text='{}'.format(current),
                                  callback_data="Objective {} Milestone {}".format(ObjectiveNo, ObjectiveMilestoneNo))

    return MaxMilestone(ObjectiveMilestoneNo - 1, ObjectiveNo, ChatIDCurrent).add(button)


# texts to show the details of current milestones
def ShowMilestone(MilestoneNo, ObjectiveNo, ChatIDCurrent):
    for x in range(1, 4):
        SyncDataBase('Query', ChatIDCurrent, ObjectiveNo, MilestoneNo, x)

    if ObjectiveNo == 1:
        Milestone = users[str(ChatIDCurrent)].MyObjective1Milestones[MilestoneNo - 1]
        DueDate = users[str(ChatIDCurrent)].MyObjective1MilestoneDates[MilestoneNo - 1]
        Status = users[str(ChatIDCurrent)].MyObjective1MilestoneStatus[MilestoneNo - 1]

    if ObjectiveNo == 2:
        Milestone = users[str(ChatIDCurrent)].MyObjective2Milestones[MilestoneNo - 1]
        DueDate = users[str(ChatIDCurrent)].MyObjective2MilestoneDates[MilestoneNo - 1]
        Status = users[str(ChatIDCurrent)].MyObjective2MilestoneStatus[MilestoneNo - 1]

    if ObjectiveNo == 3:
        Milestone = users[str(ChatIDCurrent)].MyObjective3Milestones[MilestoneNo - 1]
        DueDate = users[str(ChatIDCurrent)].MyObjective3MilestoneDates[MilestoneNo - 1]
        Status = users[str(ChatIDCurrent)].MyObjective3MilestoneStatus[MilestoneNo - 1]

    NewMessage = 'Milestone: *{}*\n'.format(Milestone) + \
                 'Due *{}* in *{}* days\n'.format(DueDate, DaysLeft(ChatIDCurrent, ObjectiveNo, MilestoneNo)) + \
                 'Status: *{}*\n\n'.format(Status)
    return NewMessage


# texts to show the list of all the current milestones and its details
def ShowMilestones(MilestoneNo, ObjectiveNo, Message, ChatIDCurrent):
    if MilestoneNo == 0:
        NewMessage = '*Overview for {}*\n'.format(users[str(ChatIDCurrent)].MyObjectives[ObjectiveNo - 1]) \
                     + 'Due *{}* in *{}* days\n\n'.format((users[str(ChatIDCurrent)].MyObjectivesDate[ObjectiveNo - 1]),
                                                          DaysLeft(ChatIDCurrent, 0, ObjectiveNo)) + Message
        return NewMessage

    for x in range(1, 4):
        SyncDataBase('Query', ChatIDCurrent, ObjectiveNo, MilestoneNo, x)

    if ObjectiveNo == 1:
        NewMessage = 'Milestone: *{}*\n'.format(
            users[str(ChatIDCurrent)].MyObjective1Milestones[MilestoneNo - 1]) + \
                     'Due *{}* in *{}* days\n'.format(
                         (users[str(ChatIDCurrent)].MyObjective1MilestoneDates[MilestoneNo - 1]),
                         DaysLeft(ChatIDCurrent, ObjectiveNo, MilestoneNo)) \
                     + 'Status: *{}*\n\n'.format(users[str(ChatIDCurrent)].MyObjective1MilestoneStatus[MilestoneNo - 1]) \
                     + Message
        return ShowMilestones(MilestoneNo - 1, ObjectiveNo, NewMessage, ChatIDCurrent)

    if ObjectiveNo == 2:
        NewMessage = 'Milestone: *{}*\n'.format(
            users[str(ChatIDCurrent)].MyObjective2Milestones[MilestoneNo - 1]) \
                     + 'Due *{}* in *{}* days\n'.format(
            (users[str(ChatIDCurrent)].MyObjective2MilestoneDates[MilestoneNo - 1]),
            DaysLeft(ChatIDCurrent, ObjectiveNo, MilestoneNo)) \
                     + 'Status: *{}*\n\n'.format(users[str(ChatIDCurrent)].MyObjective2MilestoneStatus[MilestoneNo - 1]) \
                     + Message
        return ShowMilestones(MilestoneNo - 1, ObjectiveNo, NewMessage, ChatIDCurrent)

    if ObjectiveNo == 3:
        NewMessage = 'Milestone: *{}*\n'.format(
            users[str(ChatIDCurrent)].MyObjective3Milestones[MilestoneNo - 1]) \
                     + 'Due *{}* in *{}* days\n'.format(
            (users[str(ChatIDCurrent)].MyObjective3MilestoneDates[MilestoneNo - 1]),
            DaysLeft(ChatIDCurrent, ObjectiveNo, MilestoneNo)) \
                     + 'Status: *{}*\n\n'.format(
            users[str(ChatIDCurrent)].MyObjective3MilestoneStatus[MilestoneNo - 1]) + Message
        return ShowMilestones(MilestoneNo - 1, ObjectiveNo, NewMessage, ChatIDCurrent)


# setup for texts to show the list of all the current milestones and its details
@dp.callback_query_handler(
    text=['Show Milestones For Objective 1', 'Show Milestones For Objective 2', 'Show Milestones For Objective 3'])
async def MilestoneTab(call: types.CallbackQuery):
    ChatIDCurrent = call.message.chat.id
    Objective1MilestoneNo = users[str(ChatIDCurrent)].Objective1MilestoneNo
    Objective2MilestoneNo = users[str(ChatIDCurrent)].Objective2MilestoneNo
    Objective3MilestoneNo = users[str(ChatIDCurrent)].Objective3MilestoneNo
    if call.data == 'Show Milestones For Objective 1':
        ObjectiveNo = 1
        ObjectiveMilestoneNo = Objective1MilestoneNo
    if call.data == 'Show Milestones For Objective 2':
        ObjectiveNo = 2
        ObjectiveMilestoneNo = Objective2MilestoneNo
    if call.data == 'Show Milestones For Objective 3':
        ObjectiveNo = 3
        ObjectiveMilestoneNo = Objective3MilestoneNo

    if ObjectiveMilestoneNo == 0:
        SyncDataBase('Query', ChatIDCurrent, 0, ObjectiveNo, 1)
        await call.message.answer(
            'You have no Milestones for *{}* yet, click create to create some!'.format(
                users[str(ChatIDCurrent)].MyObjectives[ObjectiveNo - 1]),
            parse_mode='Markdown')
    else:
        msg = ShowMilestones(ObjectiveMilestoneNo, ObjectiveNo, '', ChatIDCurrent)
        await call.message.answer(msg, parse_mode='Markdown')


# Setup for list of the current milestones for that objective and provide options to create and show
@dp.callback_query_handler(text=['Objective 1', 'Objective 2', 'Objective 3'])
async def MilestoneTab(call: types.CallbackQuery):
    ChatIDCurrent = call.message.chat.id

    if call.data == 'Objective 1':
        ObjectiveMilestoneNo = users[str(ChatIDCurrent)].Objective1MilestoneNo
        if ObjectiveMilestoneNo != 0:
            for x in range(1, ObjectiveMilestoneNo+1):
                SyncDataBase('Query', ChatIDCurrent, 1, x, 1)
        ObjectiveDate = users[str(ChatIDCurrent)].MyObjectivesDate[0]
        MyObjective = users[str(ChatIDCurrent)].MyObjectives[0]
        ObjectiveNo = 1

    if call.data == 'Objective 2':
        ObjectiveMilestoneNo = users[str(ChatIDCurrent)].Objective2MilestoneNo
        if ObjectiveMilestoneNo != 0:
            for x in range(1, ObjectiveMilestoneNo+1):
                SyncDataBase('Query', ChatIDCurrent, 2, x, 1)
        ObjectiveDate = users[str(ChatIDCurrent)].MyObjectivesDate[1]
        MyObjective = users[str(ChatIDCurrent)].MyObjectives[1]
        ObjectiveNo = 2

    if call.data == 'Objective 3':
        ObjectiveMilestoneNo = users[str(ChatIDCurrent)].Objective3MilestoneNo
        if ObjectiveMilestoneNo != 0:
            for x in range(1, ObjectiveMilestoneNo+1):
                SyncDataBase('Query', ChatIDCurrent, 3, x, 1)
        ObjectiveDate = users[str(ChatIDCurrent)].MyObjectivesDate[2]
        MyObjective = users[str(ChatIDCurrent)].MyObjectives[2]
        ObjectiveNo = 3

    if ObjectiveMilestoneNo < 5:
        await call.message.answer(
            'This Objective is due on: *{}* \nand you currently have *{}* Milestones in Objective *{}*. \n Click on your Milestones to *toggle status*\n or *create* some!'.format(
                ObjectiveDate, ObjectiveMilestoneNo, MyObjective),
            reply_markup=Milestone(ObjectiveMilestoneNo, ObjectiveNo, ChatIDCurrent), parse_mode='Markdown')
    else:

        await call.message.answer(
            'you currently have a max of *{}* Milestones in Objective *{}*. \n Click on your Milestones to *toggle status*\n or *create* some!'.format(
                ObjectiveMilestoneNo, MyObjective),
            reply_markup=MaxMilestone(ObjectiveMilestoneNo, ObjectiveNo, ChatIDCurrent), parse_mode='Markdown')


# Message handling
@dp.message_handler()
async def RecieveMsg(message: types.Message):
    ChatIDCurrent = message.chat.id
    MessageHandlerType = users[str(ChatIDCurrent)].MessageHandlerType
    users[str(ChatIDCurrent)].avalue += 1
    avalue = users[str(ChatIDCurrent)].avalue
    bvalue = users[str(ChatIDCurrent)].bvalue
    Objectiveno = users[str(ChatIDCurrent)].Objectiveno

    print('msghandtype{}'.format(users[str(ChatIDCurrent)].MessageHandlerType))
    msg = message.text
    if MessageHandlerType == 1:
        if avalue == bvalue + 1:
            ObjectiveName = msg
            users[str(ChatIDCurrent)].MyObjectives[Objectiveno - 1] = ObjectiveName
            SyncDataBase('Update', ChatIDCurrent, 0, Objectiveno, 1)
            await message.answer('Your Objective has been added as: \n "*{}*" '.format(ObjectiveName),
                                 parse_mode='Markdown')
            await message.answer('Enter the due date of your objective. Input as: ddmmyy')

        if avalue == bvalue + 2:
            ObjectiveDate = msg
            if DateChecker(ObjectiveDate) == 'True':
                users[str(ChatIDCurrent)].MyObjectivesDate[Objectiveno - 1] = ObjectiveDate
                SyncDataBase('Update', ChatIDCurrent, 0, Objectiveno, 2)
                await message.answer('Your Objective date has been added as: \n "*{}*" '.format(ObjectiveDate),
                                     parse_mode='Markdown')
                users[str(ChatIDCurrent)].MessageHandlerType = 0
                await message.answer("You are all set! \n Click on the *Objectives* tab to view your creation!",
                                     reply_markup=Keyboard1(), parse_mode='Markdown')
            else:
                await message.answer('invalid input try again, is your format ddmmyy?')
                users[str(ChatIDCurrent)].avalue -= 1

    elif MessageHandlerType == 21 or MessageHandlerType == 22 or MessageHandlerType == 23:
        Objective1MilestoneNo = users[str(ChatIDCurrent)].Objective1MilestoneNo
        Objective2MilestoneNo = users[str(ChatIDCurrent)].Objective2MilestoneNo
        Objective3MilestoneNo = users[str(ChatIDCurrent)].Objective3MilestoneNo
        ObjectiveNo = MessageHandlerType % 10
        if avalue == bvalue + 1:
            MilestoneName = msg
            if ObjectiveNo == 1:
                users[str(ChatIDCurrent)].MyObjective1Milestones[Objective1MilestoneNo - 1] = MilestoneName
                ObjectiveMilestoneNo = Objective1MilestoneNo
            if ObjectiveNo == 2:
                users[str(ChatIDCurrent)].MyObjective2Milestones[Objective2MilestoneNo - 1] = MilestoneName
                ObjectiveMilestoneNo = Objective2MilestoneNo
            if ObjectiveNo == 3:
                users[str(ChatIDCurrent)].MyObjective3Milestones[Objective3MilestoneNo - 1] = MilestoneName
                ObjectiveMilestoneNo = Objective3MilestoneNo

            SyncDataBase('Update', ChatIDCurrent, ObjectiveNo, ObjectiveMilestoneNo, 1)
            print(users[str(ChatIDCurrent)].MyObjective1Milestones[0: 6])

            await message.answer('Your Milestone has been added as: \n "*{}*" '.format(MilestoneName),
                                 parse_mode='Markdown')
            await message.answer('Enter the due date of your Milestone Input as: ddmmyy')

        if avalue == bvalue + 2:
            MilestoneDate = msg
            if DateChecker(MilestoneDate) == 'True':
                if ObjectiveNo == 1:
                    users[str(ChatIDCurrent)].MyObjective1MilestoneDates[Objective1MilestoneNo - 1] = MilestoneDate
                    users[str(ChatIDCurrent)].MyObjective1MilestoneStatus[Objective1MilestoneNo - 1] = 'Pending'
                    MilestoneNo = Objective1MilestoneNo
                if ObjectiveNo == 2:
                    users[str(ChatIDCurrent)].MyObjective2MilestoneDates[Objective2MilestoneNo - 1] = MilestoneDate
                    users[str(ChatIDCurrent)].MyObjective2MilestoneStatus[Objective2MilestoneNo - 1] = 'Pending'
                    MilestoneNo = Objective2MilestoneNo
                if ObjectiveNo == 3:
                    users[str(ChatIDCurrent)].MyObjective3MilestoneDates[Objective3MilestoneNo - 1] = MilestoneDate
                    users[str(ChatIDCurrent)].MyObjective3MilestoneStatus[Objective3MilestoneNo - 1] = 'Pending'
                    MilestoneNo = Objective3MilestoneNo

                SyncDataBase('Update', ChatIDCurrent, ObjectiveNo, MilestoneNo, 2)
                SyncDataBase('Update', ChatIDCurrent, ObjectiveNo, MilestoneNo, 3)
                print(users[str(ChatIDCurrent)].MyObjective1MilestoneStatus[Objective1MilestoneNo - 1])
                await message.answer('Your Milestone Date has been added as: \n "*{}*" '.format(MilestoneDate),
                                     parse_mode='Markdown')
                await message.answer(
                    'You are all set! Click on your objective in the objective tab to view your milestones!',
                    reply_markup=Keyboard1())
                users[str(ChatIDCurrent)].MessageHandlerType = 0
            else:
                await message.answer('invalid input try again, is your format ddmmyy?')
                users[str(ChatIDCurrent)].avalue -= 1

    elif MessageHandlerType == 3:
        Date = msg
        if DateChecker(Date) == 'True':
            year = int(str(Date)[4:6])
            month = int(str(Date)[2:4])
            day = int(str(Date)[0:2])
            await message.answer_poll(question='Poll for availability',
                                       options=[NextDays(day, month, year), NextDays(day + 1, month, year),
                                                NextDays(day + 2, month, year), NextDays(day + 3, month, year),
                                                NextDays(day + 4, month, year), NextDays(day + 5, month, year),
                                                NextDays(day + 6, month, year)],
                                       type='regular',
                                       is_anonymous=False,
                                       allows_multiple_answers=True)

        else:
            await message.answer('invalid input try again, is your format ddmmyy?')
            users[str(ChatIDCurrent)].avalue -= 1


def SendReminder(ChatIDCurrent):
    ObjectiveNo = users[str(ChatIDCurrent)].Objectiveno
    Counter = 0
    Dates = {}
    Identity = {}
    if ObjectiveNo == 0:
        return 'Go and make some Objectives and be productive lah... Yall ahh, very useless leh'

    if ObjectiveNo == 3:
        MilestoneNo = users[str(ChatIDCurrent)].Objective3MilestoneNo
        for x in range(MilestoneNo):
            x += 1
            SyncDataBase('Query', ChatIDCurrent, ObjectiveNo, x, 2)
            Date = DaysLeft(ChatIDCurrent, ObjectiveNo, MilestoneNo)
            if Date == 7 or Date == 14:
                Dates[Counter] = Date
                Identity[Counter] = 30 + x
                Counter += 1
        ObjectiveNo -= 1

    if ObjectiveNo == 2:
        MilestoneNo = users[str(ChatIDCurrent)].Objective2MilestoneNo
        for x in range(MilestoneNo):
            x += 1
            SyncDataBase('Query', ChatIDCurrent, ObjectiveNo, x, 2)
            Date = DaysLeft(ChatIDCurrent, ObjectiveNo, MilestoneNo)
            if Date == 7 or Date == 14:
                Dates[Counter] = Date
                Identity[Counter] = 20 + x
                Counter += 1
        ObjectiveNo -= 1

    if ObjectiveNo == 1:
        MilestoneNo = users[str(ChatIDCurrent)].Objective1MilestoneNo
        for x in range(MilestoneNo):
            x += 1
            SyncDataBase('Query', ChatIDCurrent, ObjectiveNo, x, 2)
            Date = DaysLeft(ChatIDCurrent, ObjectiveNo, x)
            if Date == 7 or Date == 14:
                Dates[Counter] = Date
                Identity[Counter] = 10 + x
                Counter += 1
        ObjectiveNo -= 1

    if ObjectiveNo == 0:
        ListNo = users[str(ChatIDCurrent)].Objectiveno
        for x in range(ListNo):
            x += 1
            print(x)
            SyncDataBase('Query', ChatIDCurrent, 0, ListNo, 2)
            Date = DaysLeft(ChatIDCurrent, 0, ListNo)
            if Date == 7 or Date == 14:
                Dates[Counter] = Date
                Identity[Counter] = x * 10
                Counter += 1

    Message = ''

    for x in range(Counter):
        x += 1
        print((Identity[x - 1]) % 10)
        print(int((str(Identity[x - 1]))[0]))
        if (Identity[x - 1]) % 10 == 0:
            ObjectiveNoCurrent = 0
            ListNo = int((str(Identity[x - 1]))[0])
        else:
            ObjectiveNoCurrent = int((str(Identity[x - 1]))[0])
            MilestoneNoCurrent = (Identity[x - 1]) % 10

        if ObjectiveNoCurrent == 0:
            Name = users[str(ChatIDCurrent)].MyObjectives[ListNo - 1]
            Type = 'Objective'
        elif ObjectiveNoCurrent == 1:
            Name = users[str(ChatIDCurrent)].MyObjective1Milestones[MilestoneNoCurrent - 1]
            Type = 'Milestone'
        elif ObjectiveNoCurrent == 2:
            Name = users[str(ChatIDCurrent)].MyObjective2Milestones[MilestoneNoCurrent - 1]
            Type = 'Milestone'
        elif ObjectiveNoCurrent == 3:
            Name = users[str(ChatIDCurrent)].MyObjective3Milestones[MilestoneNoCurrent - 1]
            Type = 'Milestone'

        DateCurrent = Dates[x - 1]
        Message += '{} *{}* is due in *{}* days! \n'.format(Type, Name, DateCurrent)

    return Message + 'Help lah! Use /meetup leh...'


async def task1():
    await dp.start_polling()


async def task2():
    while True:
        global timer
        global UserNo
        global UserCounter

        if timer >= 0:
            timer += 1
            if timer == 1000:  # if one day has passed
                timer = -1
                print('printing now')
                for x in users:
                    print('x is {}'.format(x))
                    print('and the chat id is {}'.format(users[x].chat_id))
                print('end print')
            print('timer{}'.format(timer))

        else:
            print('counter{}'.format(UserCounter))
            if UserNo == 0:
                timer = 0
                UserCounter = 0
            elif UserCounter == UserNo:
                UserCounter = 0
                timer = 0
            else:
                UserCounter += 1
                connection = pymysql.connect(host='db4free.net', user='mrmeet', password='ccleonliew',
                                 database='mrmeet',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

                cur = connection.cursor()
                cur.execute("SELECT chat_id FROM chat WHERE users = {}".format(UserCounter))
                result = cur.fetchone()
                n = len('chat_id')
                result = str(result).replace('{', '').replace('}', '').replace(':', '').replace("'", "")
                ChatIDCurrent = result[n + 1:]
                msg = SendReminder(ChatIDCurrent)
                await bot.send_message(ChatIDCurrent, msg, parse_mode='Markdown')

        await asyncio.sleep(1)


async def main():
    await asyncio.gather(
        task1(),
        task2(),
    )


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
