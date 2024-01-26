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
        return "Հարգելի՛ օգտատեր Ձեր պատվերը մերժված է: Խնդրում ենք ուղարկել ճիշտ անդորագիր կամ կապ հաստատել մեզ հետ։"
    elif lang == "rus":
        return "Уважаемый пользователь, ваш заказ отклонен. Пожалуйста, отправьте правильную квитанцию или свяжитесь с нами."
    elif lang == "eng":
        return "Dear user, your order is rejected. Please send the correct receipt or contact us."

def CONFIRM_USER_ORDER(user):
    return f"Դուք հաջողությամբ հաստատել եք Orders ID փոխանցումը {user}:"

def RIGHT_SELECT_ARM_LANG(lang):
    if lang == "arm":
        return "Դուք հաջողությամբ ընտրել եք հայերենը։"
    elif lang == "rus":
        return "Вы успешно выбрали русский язык."
    elif lang == "eng":
        return "You have successfully selected English."

def BUY_eSIM_BUTTON(lang):
    if lang == "arm":
        return "Գնել Global eSIM"
    elif lang == "rus":
        return "Купить Global eSIM"
    elif lang == "eng":
        return "Buy Global eSIM"

def CHECK_BALANCE_BUTTON(lang):
    if lang == "arm":
        return "Ստուգել մնացորդը"
    elif lang == "rus":
        return "Проверить остаток МБ"
    elif lang == "eng":
        return "Check the balance"

def CHANGE_LANGUAGE_SETTINGS(lang):
    if lang == "arm":
        return "Ընտրել լեզուն"
    elif lang == "rus":
        return "Выбрать язык"
    elif lang == "eng":
        return "Select language"

def LIST_COUNTRIES_BUTTON(lang):
    if lang == "arm":
        return "Երկրների ցուցակ"
    elif lang == "rus":
        return "Список стран"
    elif lang == "eng":
        return "List of countries"

def CONTACT_US_BUTTON(lang):
    if lang == "arm":
        return "Կապ մեզ հետ"
    elif lang == "rus":
        return "Связаться с нами"
    elif lang == "eng":
        return "Contact us"

def ACTIVATE_BUTTON(lang):
    if lang == "arm":
        return "Ակտիվացնել eSIM"
    elif lang == "rus":
        return "Активировать eSIM"
    elif lang == "eng":
        return "Activate the eSim"

def ACTIVATE_TEXT_USER(lang):
    if lang == "arm":
        return "Ակտիվացնելու համար խնդրում ենք մուտքագրել Ձեր Order ID-ն:"
    elif lang == "rus":
        return "Для активации пожалуйста введите ваш Order ID."
    elif lang == "eng":
        return "To activate please enter your Order ID."

def CHECK_BALANCE_TEXT_USER(lang):
    if lang == "arm":
        return "Ստուգելու համար խնդրում ենք մուտքագրել Ձեր Order ID-ն:"
    elif lang == "rus":
        return "Для проверки введите пожалуйста ваш Order ID."
    elif lang == "eng":
        return "To check your balance please enter your Order ID."

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
        return "Ձեռք բեր KaLine-ի Global eSIM-ը վճարելով ընդհամենը 3500 դրամ 3 GB-ի համար և եղիր կապի մեջ աշխարհի ցանկացած կետում:"
    elif lang == "rus":
        return "Приобретите Global eSIM от KaLine, заплатив 3500 драмов за 3 ГБ, и оставайтесь на связи в любой точке мира."
    elif lang == "eng":
        return "Get KaLine's Global eSIM by paying AMD 3500 for 3 GB and stay connected anywhere in the world."

def BUY_eSIM_TEXT(lang):
    if lang == "arm":
        return "Պատվիրելու համար խնդրում ենք կատարել վճարում փոխանցելով 3500 դրամ մեր էլեկտրոնային դրամապանակներից որևէ մեկին կամ բանկային քարտին և ուղարկել անդորագիրն այստեղ: Գործարքը չի իրականացվի առանց անդորրագրի:\n\nԷլեկտրոնային դրամապանակներ`\nIDram 094097722\nEasywallet\nTelcell\nԻնեկոընկեր 094097722\n\nԲանկային քարտեր`\nIDbank 4318290090169661\nAmeria 4083070010083702\n\nԽնդրում ենք ստուգել Ձեր բջջային հեռախոսի eSIM ֆունկցիայի առկայությունը այն գնելուց առաջ: Գնված eSIM-ը ենթակա չէ ետ վերադարձի:"
    elif lang == "rus":
        return "Для заказа совершите оплату, перечислив 3500 драмов РА на один из наших электронных кошельков или банковскую карту и отправьте квитанцию сюда. Без квитанции транзакция не будет обработана.\n\nЭлектронные кошельки\nIDram 094097722\nEasywallet\nTelcell\nInecomobile 094097722\n\nБанковские карты\nIDbank 4318290090169661\nАмерия 4083070010083702\n\nПожалуйста, проверьте функцию eSIM вашего телефона. мобильный телефон раньше купив его. Купленная eSIM возврату не подлежит."
    elif lang == "eng":
        return "To order, please make a payment by transferring AMD 3500 to one of our e-wallets or bank cards and send the receipt here. The transaction will not be processed without a receipt.\n\nE-wallets\nIDram 094097722\nEasywallet\nTelcell\nInecomobile 094097722\n\nBank cards\nIDbank 4318290090169661\nAmeria 4083070010083702\n\nPlease check the eSIM function of your mobile phone before purchasing it. Purchased eSIM is non-refundable."

def CONFIRM_ORDERS_USER_TEXT(lang, order_id):
    if lang == "arm":
        return f"Հարգելի օգտատեր Ձեր վճարումը հաստատված է: Ձեր Order ID-ն է `\n\n`{order_id}`"
    elif lang == "rus":
        return f"Уважаемый пользователь, ваш платеж подтвержден. Ваш Order ID:\n\n`{order_id}`"
    elif lang == "eng":
        return f"Dear user, your payment has been confirmed. Your Order ID is:\n\n`{order_id}`"

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
        return f"*Միացրեք eSIM-ը հետևյալ կերպ՝*\n\nՍկանավորեք QR կոդը կամ ավելացրեք ինքներդ լրացնելով հետևյալը՝\n\n*SM-DP+ Address*\n`{smdp_address}`\n \n*Ակտիվացման կոդը*\n`{activation_code}`\n\neSIM-ի ակտիվանալուց հետո գտեք APN-ի կարգավորումները և մուտքագրեք APN դաշտում “wbdata”, որից հետո միացրեք “Data Roaming”-ը:\n\n*eSIM-ի ակտիվացումը կարող է տևել մինչև 15 րոպե:*"
    elif lang == "rus":
        return f"*Включите eSIM, выполнив следующие действия*\nОтсканируйте QR-код или добавьте его самостоятельно, выполнив следующие действия:\n\n*Адрес SM-DP+*\n`{smdp_address}`\n\n*Код активации*\n`{activation_code}`\n\nПосле активации eSIM найдите настройки APN и введите «wbdata» в поле APN, затем включите «Роуминг данных».\n\n*Активация eSIM может занять до 15 минут.*"
    elif lang == "eng":
        return f"*Activate the eSIM as follows:*\nScan the QR code or add it manually by completing the following:\n\n*SM-DP+ Address*\n`{smdp_address}`\n\n*Activation Code:*\n`{activation_code}`\n\nAfter the eSIM is activated, find the APN settings and enter 'wbdata' in the APN field, then enable 'Data Roaming'.\n\n*eSIM activation may take up to 15 minutes.*"

def SEND_PHOTO_TEXT(lang):
    if lang == "arm":
        return "KaLine eSIM-ը աշխատում է հետևյալ երկրներում:"
    elif lang == "rus":
        return "KaLine eSIM работает в данных странах."
    elif lang == "eng":
        return "KaLine eSIM works in the following countries."

def SEND_TEXT_FOR_SUPPORT(lang):
    if lang == "arm":
        return "Ուղղեք Ձեր հարցը մեկ նամակով և մենք հնարավորինս արագ կպատասխանենք:"
    elif lang == "rus":
        return "Оставьте ваш вопрос в одном сообщении и мы свяжемся с вами как можно скорее."
    elif lang == "eng":
        return "Write your question in one message and we will answer as soon as possible."

def TAKE_TEXT_SUPPORT(lang):
    if lang == "arm":
        return "Հարգելի օգտատեր, մենք ստացել ենք Ձեր նամակը, խնդրում ենք սպասել:"
    elif lang == "rus":
        return "Уважаемый пользователь, мы получили ваше сообщение, пожалуйста ожидайте."
    elif lang == "eng":
        return "Dear user, we have received your message, please wait."

def USER_SEND_TASK_TEXT(user, user_id):
    return f"{user}({user_id}) հարց է ներկայացրել:"

def USER_SEND_TASK_PHOTO_TEXT(user, user_id):
    return f"{user}({user_id}) նկար է ներկայացրել:"

def SUPPORT_RIGHT_TEXT(lang, text):
    if lang == "arm":
        return f"Մոդերատորը պատասխանել է ձեր հաղորդագրությանը:\n\n{text}"
    elif lang == "rus":
        return f"Модератор ответил на ваше сообщение.\n\n{text}"
    elif lang == "eng":
        return f"The moderator has replied to your message.\n\n{text}"

def SUPPORT_RIGHT_TEXT_PHOTO(lang, text):
    if lang == "arm":
        return f"Մոդերատորը պատասխանել է ձեր հաղորդագրությանը և լուսանկար է ուղարկել։:\n\n{text}"
    elif lang == "rus":
        return f"Модератор ответил на ваше сообщение и отправил вам фотографию.\n\n{text}"
    elif lang == "eng":
        return f"The moderator has replied to your message and sent you a photo.\n\n{text}"

def SUPPORT_RIGHT_PHOTO_SEND(lang):
    if lang == "arm":
        return "Մոդերատորը ձեզ լուսանկար է ուղարկել։"
    elif lang == "rus":
        return "Модератор отправил вам фотографию."
    elif lang == "eng":
        return "The moderator sent you a photo."

def ERROR_COMMAND_TEXT(lang):
    if lang == "arm":
        return "Այս հրամանը գոյություն չունի, խնդրում ենք մուտքագրել /start"
    elif lang == "rus":
        return "Данная команда не существует, пожалуйста введите /start."
    elif lang == "eng":
        return "This command does not exist, please enter /start"

def CHANGE_LANGUAGE_TEXT(lang):
    if lang == "arm":
        return "Ընտրեք համապատասխան լեզուն:"
    elif lang == "rus":
        return "Выберите подходящий язык."
    elif lang == "eng":
        return "Select the appropriate language."

def CHANGE_LANGUAGE_ERROR_TEXT(lang):
    if lang == "arm":
        return "Դուք արդեն ընտրել եք այս լեզուն:"
    elif lang == "rus":
        return "У вас уже выбран данный язык."
    elif lang == "eng":
        return "You have already selected this language."

def SUPPORT_USER_TEXT_SEND_OR_PHOTO(lang):
    if lang == "arm":
        return "Հարգելի օգտատեր, դուք կարող եք ուղարկել միայն հարց, կամ լուսանկար։"
    elif lang == "rus":
        return "Уважаемый пользователь, вы можете отправить только вопрос или фотографию."
    elif lang == "eng":
        return "Dear user, you can only send a question or a photo."