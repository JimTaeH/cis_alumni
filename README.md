# Alum9 (CIS Alumni Service System) ระบบศิษย์เก่าวิทยาลัยสหวิทยาการ
คู่มือสำหรับติดตั้งระบบ Alum9 พร้อมวิธีการติดตั้ง Database โดยมีหัวข้อดังนี้
* [Prerequisite](https://github.com/JimTaeH/cis_alumni/#prerequisite)
* [Deploy with Heroku Git on CMD Prompt](https://github.com/JimTaeH/cis_alumni/#deploy-with-heroku-git-on-cmd-prompt)
* [Migrate Heroku PostgreSQL](https://github.com/JimTaeH/cis_alumni/#migrate-heroku-postgresql)

## Prerequisite
การ Deploy บน Heroku จำเป็นจะต้องมี
1. บัญชีสำหรับเข้าใช้งาน Heroku โดยสมัครได้ที่นี่ [Heroku Signup](https://signup.heroku.com/)
2. มีการ Create App ไว้บน Heroku แล้ว ขั้นตอนนี้เพียงแค่ Login เข้าไปในเว็บ Heroku และกดสร้างผ่านหน้า UI ได้ง่าย ๆ ทันที
3. ติดตั้ง Heroku PostgreSQL บน App ที่สร้าง ติดตั้งที่นี่ [Heroku PostgresSQL](https://elements.heroku.com/addons/heroku-postgresql)
4. ติดตั้ง Heroku CLI ดาวน์โหลดได้ที่นี่ [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
5. เตรียมไฟล์ secretskey.txt ของตัวเองไว้ โดยใส่ไว้ในระดับเดียวกันกับพวก requirements.txt
## Deploy with Heroku Git on CMD Prompt
สำหรับการ Deploy ด้วย Heroku Git บน Command Prompt นั้นจะมีคำสั่งดังนี้
```console
cd [TO_YOUR_PROJECT_DIRECTORY]
```
[TO_YOUR_PROJECT_DIRECTORY] = Path ไปยังโฟลเดอร์ที่เก็บโปรเจค เช่น C:\cis_alumni
```console
heroku login
```
```console
heroku git:remote -a [YOUR_HEROKUAPP_NAME]
```
[YOUR_HEROKUAPP_NAME] = ชื่อแอปที่ตั้งไว้ตอนกด Create App บน Heroku เช่น alum9app
```console
git add .
git commit -am "make it better"
git push heroku master
```
Heroku ก็จะทำการ Deploy ให้จนเสร็จสิ้น
## Migrate Heroku PostgreSQL
ก่อนจะทำขั้นตอนนี้ ให้เข้าไปเปลี่ยน Database URL ในหน้า settings.py ให้เป็น Database URL ตามที่ได้สร้างใน [Prerequisite ข้อ 3](https://github.com/JimTaeH/cis_alumni/#prerequisite)
```console
heroku run python manage.py makemigrations
```
```console
heroku run python manage.py migrate
```
```console
heroku run python manage.py createsuperuser
```
