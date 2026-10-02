<img src="https://progressify.dev/img/progressify-logo.png" alt="logo" height="120" align="right" />

# Sunsky Python API Service

Simple SDK for use the Open API's of sunsky-online.com

Full documentation at: https://doc.sunsky-online.com/

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/progressify/sunsky-python-api-service/graphs/commit-activity)
[![Paypal Donate](https://img.shields.io/badge/PayPal-Donate%20to%20Author-blue.svg)](https://www.paypal.me/progressify) 
[![Satispay Donate](https://img.shields.io/badge/Satispay-Donate%20to%20Author-red.svg)](https://tag.satispay.com/progressify) 
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/progressify/sunsky-python-api-service/issues)


## Installation

You can add in your `requirements.txt`:

```
pysunsky
```

or install from PyPI:

```bash
pip install pysunsky
```

or directly from GitHub:

```
pip installgit+https://github.com/progressify/pysunsky
```


## Usage

Create a file named `config.ini`:

```ini
[SUNSKY]
key = examplekey123@something
secret = examplesecret123
```

Replace the sample data with your Sunsky credentials.

### API Call

If the `config.ini` file is located in the same directory as your script, you can initialize and call the service directly:

```python
from pysunsky import OpenApiService

open_api_service = OpenApiService()
url_products = "https://www.sunsky-api.com/openapi/product!search.do"
parameters = {'gmtModifiedStart': '10/31/2012'}
result = open_api_service.call(url_products, parameters)
```

Otherwise, you can specify a custom (relative or absolute) path to the configuration directory:

```python
from pysunsky import OpenApiService

open_api_service = OpenApiService(config_path='./path-of-your-config-file/')
url_products = "https://www.sunsky-api.com/openapi/product!search.do"
parameters = {'gmtModifiedStart': '10/31/2012'}
result = open_api_service.call(url_products, parameters)
```

### Download Product Images

You can download product images directly into a zip file:

```python
from pysunsky import OpenApiService

open_api_service = OpenApiService()
url_images = "https://www.sunsky-api.com/openapi/product!getImages.do"
parameters = {
    'itemNo': 'IP8G0963B',
    'size': '500',
    'watermark': 'https://progressify.dev'
}
open_api_service.download(url_images, parameters, './product_images.zip')
```
