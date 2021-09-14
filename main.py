import datetime
import urllib.request
from bs4 import BeautifulSoup as BS
from urllib.error import URLError
import user_agents
import datetime
import random
import mail


def random_headers():
    return {'User-Agent': random.choice(user_agents.user_agents)}


def create_request(url, headers=None):
    if headers is None:
        headers = random_headers()
    return urllib.request.Request(url, headers=headers)


def get_response(request):
    return urllib.request.urlopen(request)


def get_soup(response):
    return BS(response, 'lxml')


def find_div(soup, class_name):
    return soup.find('div', class_=class_name)


web_dict = {"https://www.palmenmann.de/produkte/monstera-thai-constellation-mons-thai-3302?number=MONS-THAI-3302": [
    'product--delivery', 'Ausverkauft', 'Palmenmann.de'],
    "https://www.pflanzen-koelle.de/monstera-deliciosa-thai-constellation-variegata-topf-15-cm-gesamthoehe-ca.-50-cm-0220350025?number=0220350025": [
        'product--buybox block', 'Dieser Artikel kann derzeit nicht geliefert werden.', 'Plfanzen Koelle'],
    "https://www.plantje.nl/shop/monstera-thai-constellation-p-15-cm/": ['summary entry-summary col-md-7',
                                                                         'Informeer mij wanneer product weer op voorraad is.',
                                                                         'Plantje.nl'],
    "https://shop.pflanzen-keller.de/zimmerpflanzen/raritaeten/fensterblatt-thai-constellation-monstera-deliciosa-var.-thai-constellation": [
        'product--buybox block', 'Dieser Artikel steht derzeit nicht zur Verfügung!', 'Pflanzencenter Keller'],
    "https://www.fangblatt.de/1147/monstera-deliciosa-thai-constellation-variegata-gruen-weisses-fensterblatt?number=FB10944": [
        'product--buybox block', 'Dieser Artikel steht derzeit nicht zur Verfügung!', 'Fangblatt.de'],
    "https://www.plantsome.de/products/monstera-thai-constellation?_pos=2&_sid=59dd70c79&_ss=r": [
        'white-box is-transition', 'Update mich', 'Plantsome.de'],
    "https://www.plantcircle.co/product/monstera-deliciosa-thai-constellation/": ['product_content_wrapper',
                                                                              'Out of stock', 'plant_circle'],
    "https://www.casa-botanica.com/product/monstera-thai-constellation-83": ['summary entry-summary','Uitverkocht'],
}



if __name__ == "__main__":
    print(" ")
    for url in web_dict:
        request = create_request(url)
        try:
            response = get_response(request)
            soup = get_soup(response)
            div = find_div(soup,web_dict[url][0])

            if web_dict[url][1] in div.text:
                print(request.host + ": KEINE Thai-Constellation verfuegbar.")
                # print(request.headers)
            else :
                print(web_dict[url][2] + ": TREFFER!")
                mail.sending_mail("vladyslava.seher@outlook.de",
                                      f"{request.host} hat den Lieferstatus der Thai-Constellation.\nDu kannst sie unter folgendem Link bestellen: {url}.\n\n\nEmpfehlen sie den Plantscraper gern ihren Freunden und der Familie weiter.")
            #time.sleep(.5)

        except URLError as e:
            print(f"{request.host}: {e}.")

    f = open("log.txt", "a")
    f.write(str(datetime.datetime.now()) + "\n")
    f.close()
