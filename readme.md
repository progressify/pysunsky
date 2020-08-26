<img src="https://progressify.dev/img/progressify-logo.png" alt="logo" height="120" align="right" />

# Sunsky Python API Service

Simple SDK for use the Open API's of sunsky-online.com

Full documentation at: https://www.sunsky-online.com/base/doc!view.do?code=openapi

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/progressify/sunsky-python-api-service/graphs/commit-activity)
[![Paypal Donate](https://img.shields.io/badge/PayPal-Donate%20to%20Author-blue.svg)](https://www.paypal.me/progressify) 
[![Satispay Donate](https://img.shields.io/badge/Satispay-Donate%20to%20Author-red.svg)](https://tag.satispay.com/progressify) 
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/progressify/sunsky-python-api-service/issues)


## Installation

You can add in your `requirements.txt`:

```
pysunsky==1.0
```

or you can link the github:

```
git+https://github.com/progressify/pysunsky
```


## Usage

Create a file named `config.ini`

```
[SUNSKY]
key = examplekey123@something
secret = examplesecret123
```

Replace the sample data with your sunsky credential.

If the `config.ini` file is located in the same directory of your script you can call the class directly:

```
open_api_service = OpenApiService()
url_products = "http://www.sunsky-api.com/openapi/product!search.do"
parameters = {'gmtModifiedStart': '10/31/2012'}
result = open_api_service.call(url_products, parameters)
```

Otherwise you can specify a custom (relative or absolute) path:

```
open_api_service = OpenApiService(config_path='./path-of-your-config-file/')
url_products = "http://www.sunsky-api.com/openapi/product!search.do"
parameters = {'gmtModifiedStart': '10/31/2012'}
result = open_api_service.call(url_products, parameters)
```
