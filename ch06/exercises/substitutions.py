import json
with open("news.txt","r",encoding="utf-8") as news_file, open("subs.json","r") as subs_file:
    news_text=news_file.read()
    substitutions=json.load(subs_file)
    for k,v in substitutions.items():
        news_text=news_text.replace(k,v)
    with open("betternews.txt","w") as output_file:
        output_file.write(news_text)