Telegram Downloader
===

Installing
---

Clone repository and add credentials from [Telegram](https://my.telegram.org/) and chat, that will be monitored:

```bash
git clone https://github.com/VadVergasov/TelegramDownloader.git
cd TelegramDownloader
cp config.py.template config.py
```

Install all dependencies (environment recommended):

```bash
python -m venv downloader-env # If python2 and python3 installed use python3
downloader-env\Scripts\activate.bat # For Windows
source downloader-env/bin/activate # For Linux and Mac
pip install -r requirements.txt
```

And just run:

```bash
python main.py
```
