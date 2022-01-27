# Installation

- Rename `.env.example` -> `.env`
- Rename `cronscript.example.sh` -> `cronscript.sh`
- Rename `cronerror.example.log` -> `cronerror.log`
- Install semua requirements `pip install -r requirements.txt`
- Sesuaikan semua preferences di `.env`


# Cron Script

Jalan setiap tanggal 27 jam 11 siang setiap bulannya.

`0 11 27 * * /Users/username/absolute/path/script/cronscript.sh > /dev/null 2>&1`


# Email Settings

Karena emailer menggunakan google smtp, pastikan **2-Step Verification** sudah di nonaktifkan. 

Atau bisa juga menggunakan **Google App Password**.

https://support.google.com/accounts/answer/185833?hl=en
