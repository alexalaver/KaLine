TOKEN = "6558872544:AAHfYYjoINmThcX9E4k9W4k9XiTbWkaJiIE"

SELECT_LANGUAGE_TEXT = "Խնդրում ենք ընտրել ինտերֆեյսի լեզուն:\n\nПожалуйста выберите язык интерфейса.\n\nPlease select the interface language."
WRITE_TEXT_SELECT_LANGUAGE = "Դուք չեք կարող օգտագործել բոտը գրանցման ժամանակ: Մուտքագրեք /reg հրամանը:\n\nВы не можете пользоваться ботом во время регистрации. Введите команду /reg\n\nYou cannot use the bot during registration. Enter the command /reg"
PROOF_CHANNEL_TG = "@KaLine_orders"
SUPPORT_GROUP = "@KaLine_support"

def USER_SEND_PHOTO_TEXT(user):
    return f"{user} ուղարկել է լուսանկարչական անդորրագիր, դուք հաստատո՞ւմ եք, թե՞ չեղարկում:"

def CANCEL_USER_ORDER(user):
    return f"Դուք չեղարկել եք {user} պատվերը:"

def CANCEL_USER_ORDER_TEXt(lang):
    if lang == "arm":
        return "Հարգելի օգտատեր, ձեր պատվերը մերժված է, խնդրում ենք ուղարկեք ճիշտ անդորագիր կամ կապ հաստատեք մեզ հետ։"
    elif lang == "rus":
        pass
    elif lang == "eng":
        pass

def CONFIRM_USER_ORDER(user):
    return f"Դուք հաջողությամբ հաստատել եք Orders ID փոխանցումը {user}:"

def RIGHT_SELECT_ARM_LANG(lang):
    if lang == "arm":
        return "Դուք հաջողությամբ ընտրել եք հայերենը։"
    elif lang == "rus":
        pass
    elif lang == "eng":
        pass

def BUY_eSIM_BUTTON(lang):
    if lang == "arm":
        return "Գնել Global eSIM"
    elif lang == "rus":
        return "Купить Global eSIM"
    elif lang == "eng":
        pass

def CHECK_BALANCE_BUTTON(lang):
    if lang == "arm":
        return "Ստուգել մնացորդը"
    elif lang == "rus":
        return "Проверить остаток МБ"
    elif lang == "eng":
        pass

def HOW_TO_ACTIVATION_BUTTON(lang):
    if lang == "arm":
        return "Ինչպես ակտիվացնել"
    elif lang == "rus":
        return "Как активировать"
    elif lang == "eng":
        pass

def LIST_COUNTRIES_BUTTON(lang):
    if lang == "arm":
        return "Երկրների ցուցակ"
    elif lang == "rus":
        return "Список стран"
    elif lang == "eng":
        pass

def CONTACT_US_BUTTON(lang):
    if lang == "arm":
        return "Կապ մեզ հետ"
    elif lang == "rus":
        return "Связаться с нами"
    elif lang == "eng":
        pass

def ACTIVATE_BUTTON(lang):
    if lang == "arm":
        return "Ակտիվացնել"
    elif lang == "rus":
        return "Активировать"
    elif lang == "eng":
        pass

def ACTIVATE_TEXT_USER(lang):
    if lang == "arm":
        return "Ակտիվացնելու համար խնդրում ենք մուտքագրել ձեր Order ID-ն: Ակտիվացնելու պահից eSIM-ն կաշխատի 15 օր: Ձեր Order ID-ն կարողեք ակտիվացնել 5 ամիս ժամկետում:"
    elif lang == "rus":
        return "Пожалуйста, введите свой Order ID для активации. eSIM будет действительна в течение 15 дней после активации. Вы можете активировать свой идентификатор заказа в течение 5 месяцев."
    elif lang == "eng":
        pass

def CHECK_BALANCE_TEXT_USER(lang):
    if lang == "arm":
        return "Ստուգելու համար խնդրում ենք մուտքագրել Order ID-ն:"
    elif lang == "rus":
        return "Введите пожалуйста Order ID, для проверки."
    elif lang == "eng":
        pass

def CHECK_BALANCE_TEXT_ERROR(lang):
    if lang == "arm":
        return "Ձեր տվյալների հաշվեկշիռը ստուգելիս սխալ է տեղի ունեցել, կոդը կարող է սխալ մուտքագրված լինել, խնդրում ենք նորից փորձել:"
    elif lang == "rus":
        return "Произошла ошибка при проверке баланса данных, возможно код введён не верно, повторите попытку."
    elif lang == "eng":
        return "An error occurred while checking your data balance, the code may have been entered incorrectly, please try again."

def CHECK_BALANCE_RIGHT_TEXT(lang, balance, end_data):
    if lang == "arm":
        return f"Մնացորդ: {balance}\nԱկտիվ է մինչև: {end_data}"
    elif lang == "rus":
        return f"Баланс: {balance}\nАктивен до: {end_data}"
    elif lang == "eng":
        return f"Balance: {balance}\nActive until: {end_data}"

def BACK_BUTTON(lang):
    if lang == "arm":
        return "Վերադարնալ"
    elif lang == "rus":
        return "Назад"
    elif lang == "eng":
        return "Back"

def START_BEGIN_TEXT(lang):
    if lang == "arm":
        return "Մշտապես եղիր online ԿաԼայնի esimի հետ ամենամատչելի գնով ընդհամենը 3500 դրամ 3 GB համար:"
    elif lang == "rus":
        pass
    elif lang == "eng":
        pass

def BUY_eSIM_TEXT(lang):
    if lang == "arm":
        return "Պատվիրելու համար խնդրում ենք վճարել 3500 դրամ մեր էլեկտրոնային դրամապանակներից որևէ մեկին կամ բանկային քարտին և ուղարկեք անդորագիրը այստեղ Առանց անդորրագրի հաստատման գործարքը չի իրականացվի:\nԳնված esim ը ենթակա չե ետ վերադարձման Ստուգեք ձեր բջջային հեռախոսի esim ֆունկցիայի հասանելիությունը գնելուց առաջ"
    elif lang == "rus":
        pass
    elif lang == "eng":
        pass

def CONFIRM_ORDERS_USER_TEXT(lang):
    if lang == "arm":
        return f"Հարգելի օգտատեր, ձեր վճարումը հաստատված է, ահա ձեր Order ID-ն: Մուտքագրեք այն “Ակտիվացնել” դաշտում, որպեսզի ստանաք համապատասխան կարգավորումները:"
    elif lang == "rus":
        pass
    elif lang == "eng":
        pass

def BACK_TEXT(lang):
    if lang == "arm":
        return f"Դուք վերադարձել եք:"
    elif lang == "rus":
        return "Вы вернулись назад."
    elif lang == "eng":
        return "You've come back."

def ERROR_ACTIVATE_CODE_USER_TEXT(lang):
    if lang == "arm":
        return "Սխալ է տեղի ունեցել eSIM-ն ակտիվացնելիս, հավանաբար Orders ID-ն արդեն ակտիվացված է կամ սխալ է մուտքագրվել: Խնդրում ենք կրկին փորձեք:"
    elif lang == "rus":
        return "Произошла ошибка при активации eSIM, возможно Orders ID уже активирован, либо введён не верно. Пожалуйста повторите попытку."
    elif lang == "eng":
        return "An error occurred when activating eSIM, perhaps the Orders ID is already activated, or was entered incorrectly. Please try again."

def ACTIVATION_RIGHT_TEXT(lang, activation_code, smdp_address):
    if lang == "arm":
        return f"*Միացրեք eSIM-ը հետևյալ քայլերով*\n\nՍկանավորեք QR կոդը կամ ավելացրեք ինքներդ լրացնելով հետևյալը՝\n\n*SM-DP+ Address*\n`{smdp_address}`\n \n*Ակտիվացման կոդը*\n`{activation_code}`\n\neSIM-ի ակտիվանալուց հետո գտեք APN-ի կարգավորումները և մուտքագրեք APN դաշտում “wbdata”, որից հետո միացրեք “Data Roaming”-ը:\n\n*eSIM-ի ակտիվացումը կարող է տևել մինչև 15 րոպե:*"
    elif lang == "rus":
        return f"*Включите eSIM, выполнив следующие действия*\nОтсканируйте QR-код или добавьте его самостоятельно, выполнив следующие действия:\n\n*Адрес SM-DP+*\n`{smdp_address}`\n\n*Код активации*\n`{activation_code}`\n\nПосле активации eSIM найдите настройки APN и введите «wbdata» в поле APN, затем включите «Роуминг данных».\n\n*Активация eSIM может занять до 15 минут.*"
    elif lang == "eng":
        return f"*Enable eSIM with following steps*\nScan the QR code or add it manually by completing the following:\n\n*SM-DP+ Address*\n`{smdp_address}`\n\n*Activation Code:*\n`{activation_code}`\n\nAfter the eSIM is activated, find the APN settings and enter 'wbdata' in the APN field, then enable 'Data Roaming'.\n\n*eSIM activation may take up to 15 minutes.*"

def SEND_PHOTO_TEXT(lang):
    if lang == "arm":
        return "KaLine eSIM-երը աշխատում են հետևյալ երկրներում:"
    elif lang == "rus":
        pass
    elif lang == "eng":
        pass

def SEND_TEXT_FOR_SUPPORT(lang):
    if lang == "arm":
        return "Ուղղեք ձեր հարցը մեկ նամակում և մենք հնարավորինս արագ կպատասխանենք ձեր հարցին:"
    elif lang == "rus":
        return "Оставьте заявку в одном сообщении и мы свяжемся с вами как можно скорее."
    elif lang == "eng":
        pass

def TAKE_TEXT_SUPPORT(lang):
    if lang == "arm":
        return "Հարգելի օգտատեր, Ձեր հաղորդագրությունն ուղարկվել է մոդերատորներին, խնդրում ենք սպասել:"
    elif lang == "rus":
        return "Уважаемый пользователь, ваше сообщение отправлено модераторам, пожалуйста ожидайте."
    elif lang == "eng":
        return "Dear user, your message has been sent to moderators, please wait."

def USER_SEND_TASK_TEXT(user, user_id):
    return f"{user}({user_id}) հարց է ներկայացրել:"

def SUPPORT_RIGHT_TEXT(lang, text):
    if lang == "arm":
        return f"Մոդերատորը պատասխանել է ձեր հաղորդագրությանը:\n\n{text}"
    elif lang == "rus":
        return f"Модератор ответил на ваше сообщение.\n\n{text}"
    elif lang == "eng":
        return f"The moderator has replied to your message.\n\n{text}"


def ERROR_COMMAND_TEXT(lang):
    if lang == "arm":
        return "Այս հրամանը գոյություն չունի, խնդրում ենք մուտքագրել /start"
    elif lang == "rus":
        return "Данная команда не существует, пожалуйста введите /start."
    elif lang == "eng":
        return "This command does not exist, please enter /start"