# Docker

Dockerdan foydalanish uchun bizga Dockerfile va docker-compose.yml fayl kerak bo'ladi

# Docker yordamida DRF projectni deploy qilish

1. Serverga kirib olamiz terminalimizda

```shell
ssh root@server ip address
# keyin serverni parolini kiritamiz
```

2. serverni update qilamiz va serverga dockerni o'rnatamiz

```shell
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install docker-ce
docker --version

sudo systemctl start docker
sudo systemctl enable docker
```

3. Keyin www papkani ichiga githubdan kerakli projectni clone qilib olamiz

```shell
cd /var/www/ 
git clone project urli
cd project nomi
```

4. Dockerni ishga tushuramiz agar docker-compose yo'q bo'lsa o'rnatib olamiz

```shell
docker-compose build
docker-compose up -d
```

5. Agar docker-compose yo'q bo'lsa quyidagicha run qilsa bo'ladi

```shell
docker build -t my_django_app .
docker run -d -p 8000:8000 my_django_app  
```
