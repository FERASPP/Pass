# تحذير: هذا البرنامج للأغراض التعليمية فقط. لا تستخدمه لأغراض غير قانونية أو غير أخلاقية.
# إنشاء قوائم كلمات المرور لأغراض غير مصرح بها يعتبر غير قانوني وغير أخلاقي. استخدم مهاراتك بمسؤولية.
import pyfiglet
import itertools
import requests


############################
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
y = '\033[1;35m'#وردي

logo = pyfiglet.figlet_format(' #*Feras*# ')
print(y+ logo)

levi = 'FERAS'
lev=input("\033[1;37m [~]\033[1;35mENTER  PASSWORD:\033[1;33m")
if lev ==levi:
	pass
# دالة لإنشاء قائمة كلمات المرور بناءً على المعلومات المقدمة
def generate_password_list(name, phone_number, birth_year, keywords=[], max_passwords=None):
    # استبدالات شائعة للأحرف (مثل 'a' -> '@', 'o' -> '0')
    substitutions = {
        'a': '@',
        'o': '0',
        'i': '1',
        'e': '3',
        's': '$'
    }

    # إنشاء اختلافات للاسم
    name_variations = set()
    name_variations.add(name.lower())
    name_variations.add(name.upper())
    name_variations.add(name.capitalize())

    # تطبيق الاستبدالات على اختلافات الاسم
    for char, sub in substitutions.items():
        for variation in list(name_variations):
            if char in variation:
                name_variations.add(variation.replace(char, sub))

    # إنشاء تركيبات كلمات المرور
    passwords = set()
    for variation in name_variations:
        # إضافة اختلافات الاسم مع رقم الهاتف
        passwords.add(variation + phone_number)
        passwords.add(phone_number + variation)

        # إضافة اختلافات الاسم مع سنة الميلاد
        passwords.add(variation + str(birth_year))
        passwords.add(str(birth_year) + variation)

        # إضافة اختلافات الاسم مع الكلمات المفتاحية
        for keyword in keywords:
            passwords.add(variation + keyword)
            passwords.add(keyword + variation)

    # إضافة رقم الهاتف وسنة الميلاد بشكل منفصل
    passwords.add(phone_number)
    passwords.add(str(birth_year))

    # إضافة تركيبات من رقم الهاتف وسنة الميلاد
    passwords.add(phone_number + str(birth_year))
    passwords.add(str(birth_year) + phone_number)

    # تحديد عدد كلمات المرور إذا تم تحديد قيمة لـ max_passwords
    if max_passwords and len(passwords) > max_passwords:
        passwords = list(passwords)[:max_passwords]
    else:
        passwords = list(passwords)

    return passwords

# دالة لإرسال قائمة كلمات المرور إلى Telegram
def send_to_telegram(file_path, chat_id, bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    with open(file_path, "rb") as file:
        files = {"document": file}
        data = {"chat_id": chat_id}
        response = requests.post(url, files=files, data=data)
    if response.status_code == 200:
        print("[+] تم إرسال قائمة كلمات المرور إلى Telegram بنجاح!")
    else:
        print(f"[-] فشل إرسال قائمة كلمات المرور. رمز الحالة: {response.status_code}")

# واجهة الأداة
def display_banner():
    print(X)
    print("""
▒▒▒▒▒▒▒  ▄▄▄▄▄▄▄▄
▒▒█▒▒▒▄██████████▄ 
▒█▐▒▒▒████████████ 
▒▌▐▒▒██▄▀██████▀▄██ 
▐┼▐▒▒██▄▄▄▄██▄▄▄▄██  
▐┼▐▒▒██████████████
▐▄▐████─▀▐▐▀█─█─▌▐██▄
▒▒█████──────────▐███▌
▒▒█▀▀██▄█─▄───▐─▄███▀
▒▒█▒▒███████▄██████
▒▒▒▒▒██████████████
▒▒▒▒▒█████████▐▌██▌
▒▒▒▒▒▐▀▐▒▌▀█▀▒▐   █
▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒ ▌
    أداة تخمين كلمات المرور | إصدار FERAS
    """)

# الدالة الرئيسية
def main():
    display_banner()
    print("[!] هذه الأداة مخصصة لتوليد قوائم كلمات المرور لأغراض تعليمية. لا تستخدمها لأغراض غير قانونية.")
    الاسم = input("ادخل اسم الهدف: ")
    رقم_الهاتف = input("ادخل رقم هاتف الهدف (بدون رمز الدولة): ")
    سنة_الميلاد = input("ادخل سنة ميلاد الهدف (مثال: 1990): ")
    كلمات_مفتاحية = input("ادخل كلمات مفتاحية إضافية (مفصولة بفواصل، مثال: حيوان,مدينة): ").split(',')

    # تحديد عدد كلمات المرور
    while True:
        try:
            عدد_كلمات_السر = int(input("ادخل عدد كلمات المرور التي تريد توليدها (أدخل 0 لإنشاء عدد غير محدود): "))
            if عدد_كلمات_السر >= 0:
                break
            else:
                print("[-] الرقم يجب أن يكون أكبر من أو يساوي 0.")
        except ValueError:
            print("[-] الرقم المدخل غير صالح. يرجى إدخال رقم صحيح.")

    # إدخال بيانات Telegram من المستخدم
    الايدي = input("ادخل معرف الدردشة (chat_id) الخاص بك: ")
    التوكن = input("ادخل رمز البوت (bot_token) الخاص بك: ")

    # إنشاء قائمة كلمات المرور
    if عدد_كلمات_السر == 0:
        print("[+] يتم إنشاء عدد غير محدود من كلمات المرور...")
        قائمة_كلمات_المرور = generate_password_list(الاسم, رقم_الهاتف, سنة_الميلاد, كلمات_مفتاحية)
    else:
        قائمة_كلمات_المرور = generate_password_list(الاسم, رقم_الهاتف, سنة_الميلاد, كلمات_مفتاحية, عدد_كلمات_السر)

    # حفظ كلمات المرور في ملف
    ملف_النتائج = "FERAS.txt"  # تم تغيير اسم الملف إلى medobass.txt
    with open(ملف_النتائج, "w") as ملف:
        for كلمة_مرور in قائمة_كلمات_المرور:
            ملف.write(كلمة_مرور + "\n")

    print(f"[+] تم إنشاء {len(قائمة_كلمات_المرور)} كلمة مرور وحفظها في الملف '{ملف_النتائج}'.")

    # إرسال الملف إلى Telegram
    send_to_telegram(ملف_النتائج, الايدي, التوكن)

if __name__ == "__main__":
    main()