# Requirements

1. Unix / macOS
2. Python >= 3.8
3. Venv


# Installation

- Rename `.env.example` -> `.env`
- Rename `cronerror.log.example` -> `cronerror.log`
- Rename `crontabtemp.example` -> `crontabtemp`
- Install semua requirements `pip install -r requirements.txt`
- Sesuaikan semua preferences di `.env`
  - Detail Pengiriman: 
    ```
    - EMAIL_FROM={alamat gmail kamu}
    - EMAIL_TO={alamat email penerima}
    - EMAIL_SENDER_NAME={nama kamu}
    ```
  - Email Server:
    ```
    - EMAIL_PASSWORD={password gmail sesuai "EMAIL_FROM" atau Google App Password jika menggunakan 2-Step Verification}
    ```
  - Detail Bank Penerima:
    ```
    - BANK_FULL_NAME={Nama pemilik rekening}
    - BANK_ACCOUNT_BIRTHDAY={Tanggal lahir pemilik rekening}
    - BANK_ID_CARD={No KTP pemilik rekening}
    - BANK_ACCOUNT_NAME={Nama bank penerima e.g BCA (Bank Central Asia)}
    - BANK_ACCOUNT_NO={Nomor rekening}
    ```
  - Detail Penagihan:
    ```
    - YOUR_COMPANY={Perusahaan tujuan e.g PT Selalu Jaya}
    - YOUR_IDR_SALARY={Total gaji IDR e.g 1.000.000}
    ```
  - Signature:
    ```
    - YOUR_SIGN_NAME={Nama lengkap kamu}
    ```
  - Cron Job (Jalan setiap tgl 27 jam 11 pagi setiap bulan):
    ```
    - CRON_JOB=0 11 27 * *
    ```

# Virtual Environment

Untuk membuat virtual environment:
```
cd auto-invoice-script
python3 -m venv venv
```


# Email Settings

Karena emailer menggunakan Google smtp, pastikan **2-Step Verification** sudah di nonaktifkan. 

Atau bisa juga menggunakan **Google App Password**.

https://support.google.com/accounts/answer/185833?hl=en


# Start App

Jalankan code berikut untuk memulai program:
`./start.sh`

Cron akan berjalan dan file `crontab` akan terupdate secara otomatis

Untuk memeriksa daftar cron yang berjalan:
`crontab -l`
