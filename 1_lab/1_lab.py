import requests
import codecs

r = requests.get('https://api.hh.ru/vacancies', params={
    'text': 'python разработчик'
})
f = codecs.open("programmer_vacancies.json", "w", "utf-8")
vacancies = []
for item in r.json()["items"]:
    vacancy = "Vacancy: " + item["name"] + ", required experience: " + item["experience"]["name"] + ", salary: "
    if(item["salary"]):
        if (item["salary"]["from"] is not None) & (item["salary"]["to"] is not None):
            vacancy = str(vacancy) + str(item["salary"]["from"]) + " - " + str(item["salary"]["to"])
        elif item["salary"]["from"] is not None:
            vacancy = str(vacancy)  + str(item["salary"]["from"])
        else:
            vacancy = str(vacancy) + str(item["salary"]["to"])
    else:
        vacancy = str(vacancy)  + "Не указана"
    vacancy = str(vacancy)  + ", area: " + str(item["area"]["name"])
    vacancies.append(vacancy)
f.write(str(vacancies).replace("\'", "\""))
