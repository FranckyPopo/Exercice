from bs4 import BeautifulSoup
import requests
from pprint import pprint
from os import path


class Scraping:
    req = requests.get("https://just-scrape-it.com/")
    content_html = req.text
        
    def list_category(self):
        self.body_html = BeautifulSoup(Scraping.content_html, "html.parser")
        self.categorys = self.body_html.find_all("span", class_="site-nav__label") 
        self.categorys = [category.text for category in self.categorys[1:6]]
        
        print("Liste des catégories:") 
        for category in self.categorys: print(category)
    
    def article_categorys(self):
        site_web = "https://just-scrape-it.com/"
        link_categorys = ["collections/hoodie-sweat", "collections/tshirt-t-shirt-tee-shirt", 
        "collections/gants", "collections/maillots-ete", "collections/stickers"]
        
        # On parcour toutes les catégory
        for link in link_categorys:
            page_categorys = path.join(site_web, link)
            req_category = requests.get(page_categorys)
            html_category = req_category.text
            
            # On récupère le contenue de la page
            self.body_html = BeautifulSoup(html_category, "html.parser")
            
            # On récupère la liste des articles
            articles = self.body_html.find_all("li", class_="grid__item grid__item--collection-template small--one-half medium-up--one-quarter")
            articles_exists = []
            
            # On vérifie si le produit existe
            for article in articles:
                product = article.find("span", class_="price-item price-item--regular")
                product = product.text
                product_exists = False if product.strip() == "Épuisé" else articles_exists.append(article)
                
            for article in articles_exists:
                # Récupèration des détailles de l'article
                name_product = article.find("div", class_="h4 grid-view-item__title product-card__title")
                name_product = name_product.text
                
                price_product = article.find("span", class_="price-item price-item--regular")
                price_product = price_product.text
                
                description = f"Le produit {name_product.strip()} est au prix de: {price_product.strip()}"
                print(description)
            
            if article in articles_exists: print("---------------------")
                
        # On récupèle contenue de la page
        page_categorys = path.join(site_web, "products/cagoule-scrape-original")
        req_category = requests.get(page_categorys)
        html_category = req_category.text
        
        self.body_html = BeautifulSoup(html_category, "html.parser")
        
        # On vérifie que la gagoules exists
        price_product = self.body_html.find("span", class_="gf_product-price money")
        price_product = price_product.text
        
        name_product = self.body_html.find("a", class_="gf_product-title")
        name_product = name_product.text
        
        if price_product.strip() != "Épuisé": 
            print(f"Le produit {name_product.strip()} est au prix de: {price_product.strip()}")

        
s = Scraping()
s.article_categorys()