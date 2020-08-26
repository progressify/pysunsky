Sunsky Python API Service
=========================

Simple SDK for use the Open API's of sunsky-online.com

Full documentation at:
https://www.sunsky-online.com/base/doc!view.do?code=openapi


Installation
------------

You can add in your ``requirements.txt``:

::

    pysunsky==1.0


or you can link the github:

::

    git+https://github.com/progressify/pysunsky

Usage
-----

Create a file named ``config.ini``

::

    [SUNSKY]
    key = examplekey123@something
    secret = examplesecret123

Replace the sample data with your sunsky credential.

If the ``config.ini`` file is located in the same directory of your
script you can call the class directly:

::

    open_api_service = OpenApiService()
    url_products = "http://www.sunsky-api.com/openapi/product!search.do"
    parameters = {'gmtModifiedStart': '10/31/2012'}
    result = open_api_service.call(url_products, parameters)

Otherwise you can specify a custom (relative or absolute) path:

::

    open_api_service = OpenApiService(config_path='./path-of-your-config-file/')
    url_products = "http://www.sunsky-api.com/openapi/product!search.do"
    parameters = {'gmtModifiedStart': '10/31/2012'}
    result = open_api_service.call(url_products, parameters)
