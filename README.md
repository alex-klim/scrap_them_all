# scrap_them_all
Installation:
```
git clone https://github.com/alex-klim/scrap_them_all/
python3 -m venv scrap_them_all
cd scrap_them_all && source bin/activate
pip install -r requirements.txt
cd habr_lua && scrapy crawl lua_spider
```
Result will be saved in export.json in the upper directory
