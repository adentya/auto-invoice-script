# Installation

- Rename `.env.example` -> `.env`
- Rename `cronscript.example.sh` -> `cronscript.sh`
  - Buka `cronscript.sh` dan ubah `/Users/username/your/path/to/script` sesuai dengan script path
- Rename `cronerror.example.log` -> `cronerror.log`
- Install semua requirements `pip install -r requirements.txt`
- Sesuaikan semua preferences di `.env`
  - Detail Pengiriman: 
    - `EMAIL_FROM={alamat gmail kamu}`
    - `EMAIL_TO={alamat email penerima}`
    - `EMAIL_SENDER_NAME={nama kamu}`
  - Email Server:
    - `EMAIL_PASSWORD={password gmail sesuai "EMAIL_FROM" atau Google App Password jika menggunakan 2-Step Verification}`
  - Detail Bank Penerima:
    - `BANK_FULL_NAME={Nama pemilik rekening}`
    - `BANK_ACCOUNT_BIRTHDAY={Tanggal lahir pemilik rekening}`
    - `BANK_ID_CARD={No KTP pemilik rekening}`
    - `BANK_ACCOUNT_NAME={Nama bank penerima e.g BCA (Bank Central Asia)}`
    - `BANK_ACCOUNT_NO={Nomor rekening}`
  - Detail Penagihan:
    - `YOUR_COMPANY={Perusahaan tujuan e.g EngX1 Pte Ltd}`
    - `YOUR_IDR_SALARY={Total gaji IDR e.g 1.000.000}`
  - Signature:
    - `YOUR_SIGN_NAME={Nama lengkap kamu}`


# Cron Script

Jalan setiap tanggal 27 jam 11 siang setiap bulannya.

`0 11 27 * * /Users/username/absolute/path/script/cronscript.sh > /dev/null 2>&1`

Ubah `/Users/username/absolute/path/script/cronscript.sh` sesuai path `cronscript.sh` berada.


# Email Settings

Karena emailer menggunakan Google smtp, pastikan **2-Step Verification** sudah di nonaktifkan. 

Atau bisa juga menggunakan **Google App Password**.

https://support.google.com/accounts/answer/185833?hl=en
