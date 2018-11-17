from bs4 import BeautifulSoup

pages = ["avvo1.html", "avvo2.html"]

for i in pages:
    page = open(i, "r")
    s = BeautifulSoup(page)

    print('name :', s.find_all(class_="u-vertical-margin-0")[0].get_text())
    print('licence :', s.select("li time")[0].get_text())
    print('image :', s.select("figure img")[0].get("src"))
    print('avvo_rating :', s.select("div span.h3")[0].get_text())
    client_rating ={}
    client_rating['rating'] = s.select("table tbody td.text-muted")[0].get_text()
    client_rating['reviews'] = s.select('div span.text-muted')[3].get_text()
    print('client_rating :', client_rating)
    print('about me :', s.select('div#js-truncated-aboutme')[0].get_text())
    practice_areas = []
    for i in s.select("li.js-specialty a"):
        practice_areas.append(i.get_text())
    print('practice areas : ',practice_areas)
    print('address :', s.select("span p")[0].get_text())
    phone = {}
    phone["Office"] = s.select("a span.js-v-phone-replace-text")[0].get_text() 
    phone["Fax"] =  s.select("a span.js-v-phone-replace-text")[-1].get_text()
    print('phone : ',phone)
    



 