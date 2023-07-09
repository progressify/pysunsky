import json
import unittest

from pysunsky import OpenApiService


class TestApi(unittest.TestCase):
    """
    author: Antonio Porcelli
    username: Progressify
    github: https://github.com/progressify
    ig: https://www.instagram.com/progressify/
    site: https://progressify.dev
    docs_link: https://www.sunsky-online.com/base/doc!view.do?code=openapi
    """

    def setUp(self):
        self.oas = OpenApiService()

    def test_download(self):
        url_images = "http://www.sunsky-api.com/openapi/product!getImages.do"
        path = './test_download/test.zip'
        parameters = {
            'itemNo': 'IP8G0963B',
            'size': '500',
            'watermark': 'https://progressify.dev'
        }
        self.oas.download(url_images, parameters, path)

    def test_get_categories(self):
        """
        Fetch the categories ever changed since gmtModifiedStart
        """
        url_categories = "http://www.sunsky-api.com/openapi/category!getChildren.do"
        parameters = {'gmtModifiedStart': '10/31/2013'}
        result = self.oas.call(url_categories, parameters)
        self.assertEqual(json.loads(result)['result'], 'success')

    def test_get_products(self):
        """
        Fetch the products ever changed since gmtModifiedStart
        """
        url_products = "http://www.sunsky-api.com/openapi/product!search.do"
        parameters = {'gmtModifiedStart': '10/31/2012'}
        result = self.oas.call(url_products, parameters)
        self.assertEqual(json.loads(result)['result'], 'success')

    def test_get_product_details(self):
        """
        Fetch the details for the product
        """
        url_product_detail = "http://www.sunsky-api.com/openapi/product!detail.do"
        parameters = {'itemNo': 'IP8G0963B', 'withLogo': 'true'}
        result = self.oas.call(url_product_detail, parameters)
        self.assertEqual(json.loads(result)['result'], 'success')

    def test_get_countries_and_states(self):
        """
        Fetch the countries and states
        """
        url_product_detail = "http://www.sunsky-api.com/openapi/order!getCountries.do"
        result = self.oas.call(url_product_detail, {})
        self.assertEqual(json.loads(result)['result'], 'success')

    def test_calculate_price(self):
        """
        Calculate the prices and freights for the items
        """
        url_product_detail = "http://www.sunsky-api.com/openapi/order!getPricesAndFreights.do"
        parameters = {
            'countryId': '41',
            'items.1.itemNo': 'S-PC-7310',
            'items.1.qty': '20',
            'items.2.itemNo': 'IP8G2615',
            'items.2.qty': '5'
        }
        result = self.oas.call(url_product_detail, parameters)
        self.assertEqual(json.loads(result)['result'], 'success')
