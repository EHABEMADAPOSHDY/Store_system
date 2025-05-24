#  Store_system

نظام متكامل لإدارة متجر الكتروني 

## 📸 صورة من المشروع

![screenshot](screenshots/homepage.png)

## 🚀 الخصائص

- تسجيل المتنجات وعرضعا 
- امكانيه حزف المتج 
- امكانيه حسب الارباح وعرفه عدد المستجر من المبيعات


## 🛠️ التقنيات المستخدمة

- Backend: Django
- Frontend: HTML, CSS, JavaScript (Bootstrap)
- قاعدة البيانات: SQLite  



## 🔧 طريقة التشغيل

```bash


# 2. أنشئ بيئة افتراضية وثبّت الحزم
python -m venv venv
source venv/bin/activate  # على ويندوز: venv\Scripts\activate
pip install -r requirements.txt

# 3. تشغيل قاعدة البيانات
python manage.py migrate

# 4. تشغيل السيرفر
python manage.py runserver
