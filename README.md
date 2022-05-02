# Alum9 (CIS Alumni Service System) ระบบศิษย์เก่าวิทยาลัยสหวิทยาการ
คู่มือสำหรับติดตั้งระบบ Alum9 พร้อมวิธีการติดตั้ง Database โดยมีหัวข้อดังนี้
* [Prerequisite](https://github.com/JimTaeH/cis_alumni/#prerequisite)
* [Deploy with Heroku Git on CMD Prompt](https://github.com/JimTaeH/cis_alumni/#deploy-with-heroku-git-on-cmd-prompt)
* [Migrate Heroku PostgreSQL](https://github.com/JimTaeH/cis_alumni/#migrate-heroku-postgresql)

## Prerequisite
การ Deploy บน Heroku จำเป็นจะต้องมี
1. บัญชีสำหรับเข้าใช้งาน Heroku โดยสมัครได้ที่นี่ [Heroku Signup](https://signup.heroku.com/)
2. มีการ Create App ไว้บน Heroku แล้ว ขั้นตอนนี้เพียงแค่ Login เข้าไปในเว็บ Heroku และกดสร้างผ่านหน้า UI ได้ง่าย ๆ ทันที
3. ติดตั้ง Heroku CLI ดาวน์โหลดได้ที่นี่ [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
4. เตรียมไฟล์ secretskey.txt ของตัวเองไว้ โดยใส่ไว้ในระดับเดียวกันกับพวก requirements.txt
## Deploy with Heroku Git on CMD Prompt
สำหรับการ Deploy ด้วย Heroku Git บน Command Prompt นั้นจะมีคำสั่งดังนี้ <br>
[TO_YOUR_PROJECT_DIRECTORY] คือ Path ไปยังโฟลเดอร์ที่เก็บโปรเจค เช่น C:\cis_alumni
```console
cd [TO_YOUR_PROJECT_DIRECTORY]
```
```console
heroku login
```
[YOUR_HEROKUAPP_NAME] คือชื่อแอปที่ตั้งไว้ตอนกด Create App บน Heroku เช่น alum9app
```console
heroku git:remote -a [YOUR_HEROKUAPP_NAME]
```
```console
git add .
git commit -am "make it better"
git push heroku master
```
## Migrate Heroku PostgreSQL
