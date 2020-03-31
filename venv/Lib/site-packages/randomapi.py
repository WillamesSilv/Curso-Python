#!/usr/bin/env python

"""
randomapi.py: a Python implementation of the RANDOM.org JSON-RPC API

Author: Mitchell Cohen (mitch.cohen@me.com)
https://github.com/mitchchn/randomapi

Maintainer: Thomas Chick (twitter.com/Tantusar)
https://github.com/tantusar/randomapi

Date: January 18, 2020
Version: 0.3.2

RANDOM.org API reference:
- https://api.random.org/json-rpc/2/

randomapi.py supports all basic and signed methods in Release 2
of the RANDOM.ORG API. It respects delay requests from the server
and has the ability to verify digitally-signed data.

RPC code based on python-jsonrpc:
- https://pypi.python.org/pypi/python-jsonrpc

Example usage:

    # Returns a list of 5 random numbers between 0 and 10

    random_client = RandomJSONRPC(api_key) # Requires a valid API key
    nums = random_client.generate_integers(n=5, min=0, max=10).parse()

"""

import time
import json
import logging

# Python 2/3 Compatibility
try:
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
    from urllib.parse import urlparse, urlencode
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError

import uuid
from collections import OrderedDict

###################### Constants #############################

JSON_URL = "https://api.random.org/json-rpc/2/invoke"

# RANDOM.org API method names

INTEGER_METHOD = "generateIntegers"
INTEGER_SEQUENCE_METHOD = "generateIntegerSequences"
DECIMAL_METHOD = "generateDecimalFractions"
GAUSSIAN_METHOD = "generateGaussians"
STRING_METHOD = "generateStrings"
UUID_METHOD = "generateUUIDs"
BLOB_METHOD = "generateBlobs"
USAGE_METHOD = "getUsage"

SIGNED_INTEGER_METHOD = "generateSignedIntegers"
SIGNED_INTEGER_SEQUENCE_METHOD = "generateSignedIntegerSequences"
SIGNED_DECIMAL_METHOD = "generateDecimalFractions"
SIGNED_GAUSSIAN_METHOD = "generateSignedGaussians"
SIGNED_STRING_METHOD = "generateSignedStrings"
SIGNED_UUID_METHOD = "generateSignedUUIDs"
SIGNED_BLOB_METHOD = "generateSignedBlobs"
RESULT_METHOD = "getResult"
VERIFY_SIGNATURE_METHOD = "verifySignature"

# RANDOM.org API parameters

ADVISORY_DELAY = "advisoryDelay"
API_KEY = "apiKey"

# JSON keys

RESULT = "result"
RANDOM = "random"
AUTHENTICITY = "authenticity"
SIGNATURE = "signature"
SERIAL_NUMBER = "serialNumber"

# RANDOM.org blob formats

FORMAT_BASE64 = "base64"
FORMT_HEX = "hex"


def valid_json_methods():
    '''Returns a list of valid JSON-RPC method names from the RANDOM.org API'''
    return [INTEGER_METHOD, INTEGER_SEQUENCE_METHOD, DECIMAL_METHOD, GAUSSIAN_METHOD,
            STRING_METHOD, UUID_METHOD, BLOB_METHOD, USAGE_METHOD, SIGNED_INTEGER_METHOD,
            SIGNED_INTEGER_SEQUENCE_METHOD, SIGNED_BLOB_METHOD, SIGNED_DECIMAL_METHOD,
            SIGNED_GAUSSIAN_METHOD, SIGNED_STRING_METHOD, SIGNED_UUID_METHOD,
            RESULT_METHOD, VERIFY_SIGNATURE_METHOD]


def parse_random(json_string):
    """
    Returns the randomly-generated data from a RANDOM.org JSON request

    :param json_string a fully-formed JSON-RPC response string
    """

    data = json_to_ordered_dict(json_string)
    random = []
    if RANDOM in data[RESULT]:
        random = data[RESULT][RANDOM]
    return random

def json_to_ordered_dict(json_string):
    return json.loads(json_string, object_pairs_hook=OrderedDict)


def compose_api_call(json_method_name, *args, **kwargs):
    """
    Returns a fully-formed JSON-RPC string for a RANDOM.org API method

    :param json_method_name: Name of the method. Can be one of:
        INTEGER_METHOD, INTEGER_SEQUENCE_METHOD, DECIMAL_METHOD, GAUSSIAN_METHOD,
        STRING_METHOD, UUID_METHOD, BLOB_METHOD, USAGE_METHOD, SIGNED_INTEGER_METHOD,
        SIGNED_INTEGER_SEQUENCE_METHOD, SIGNED_BLOB_METHOD, SIGNED_DECIMAL_METHOD,
        SIGNED_GAUSSIAN_METHOD, SIGNED_STRING_METHOD, SIGNED_UUID_METHOD,
        RESULT_METHOD, VERIFY_SIGNATURE_METHOD
    :param args: Positional parameters
    :param kwargs: Named parameters. See: https://api.random.org/json-rpc/2/basic
    for descriptions of methods and their parameters.
    """

    if json_method_name not in valid_json_methods():
        raise Exception(
            "'{}' is not a valid RANDOM.org JSON-RPC method".format(
                json_method_name))
    if kwargs:
        params = kwargs
        if args:
            params["__args"] = args
    else:
        params = args

    request_data = {
        "method": str(json_method_name),
        "id": str(uuid.uuid4()),
        "jsonrpc": "2.0",
        "params": params
    }
    return json.dumps(request_data).encode('utf-8')


def http_request(url, json_string):
    """
    Request data from server (POST)

    :param json_string: JSON-String
    """

    request = Request(url, data=json_string)
    request.add_header("Content-Type", "application/json")
    response = urlopen(request)
    response_string = response.read()
    response.close()

    return response_string


class RandomJSONRPC:

    def __init__(self, api_key):
        """
        Creates a client which can call RANDOM.org API functions to generate
        various kinds of random data.

        The class is simple to use: simply instantiate a RandomJSONRPC object
        with a valid API key, and call the appropriate method on the server.

        For a list of available methods and parameters, see:

        :param api_key: String representing a RANDOM.org JSON-RPC API key
        """
        self.api_key = api_key
        self._time_of_last_request = 0
        self._advisory_delay = 0

    def delay_request(self, requested_delay):
        elapsed = time.time() - self._time_of_last_request
        remaining_time = requested_delay - elapsed

        logging.info("Sleeping {} more seconds...".format(remaining_time))

        if remaining_time - elapsed > 0:
            time.sleep(remaining_time)

    def send_request(self, request_string, method=""):
        '''Wraps outgoing JSON requests'''

        # Create a new response class, using an ordered dict to
        # preserve the integrity of signed data


        # Respect delay requests from the server
        if self._time_of_last_request == 0:
            self._time_of_last_request = time.time()
        if self._advisory_delay > 0:
            self.delay_request(self._advisory_delay)

        # Make the connection now
        json_string = http_request(JSON_URL, request_string)
        self._time_of_last_request = time.time()

        # Use an ordered dict to preserve the integrity of signed data
        response = RandomJSONResponse(json_to_ordered_dict(json_string), method)
        if ADVISORY_DELAY in response._result:
            self._advisory_delay = float(response._result[ADVISORY_DELAY]) / 1000.0
        return response

####################### RANDOM.org API methods ##########################

    def generate_integers(self, n, min, max, replacement=True, base=10):
        '''Returns a list of true random integers with a user-defined range'''
        request_string = compose_api_call(
            INTEGER_METHOD, apiKey=self.api_key,
            n=n, min=min, max=max, replacement=replacement, base=base)
        return self.send_request(request_string, INTEGER_METHOD)

    def generate_integer_sequences(self, n, length, min, max, replacement=True, base=10):
        '''Returns a list of lists of true random integers with a user-defined range'''
        request_string = compose_api_call(
            INTEGER_SEQUENCE_METHOD, apiKey=self.api_key,
            n=n, length=length, min=min, max=max, replacement=replacement, base=base)
        return self.send_request(request_string, INTEGER_SEQUENCE_METHOD)

    def generate_decimal_fractions(self, n, decimal_places, replacement=True):
        '''Returns a list of true random decimal fractions between [0,1]
        with a user-defined number of decimal places'''
        request_string = compose_api_call(
            DECIMAL_METHOD, apiKey=self.api_key,
            n=n, decimalPlaces=decimal_places, replacement=replacement)
        return self.send_request(request_string, DECIMAL_METHOD)

    def generate_gaussians(self, n, mean, standard_deviation,
                           significant_digits):
        '''Returns a list of true random numbers from a Gaussian distribution'''
        request_string = compose_api_call(
            GAUSSIAN_METHOD, apiKey=self.api_key,
            n=n, mean=mean,
            standardDeviation=standard_deviation,
            significantDigits=significant_digits)
        return self.send_request(request_string, GAUSSIAN_METHOD)

    def generate_strings(self, n, length, characters, replacement=True):
        '''Returns a list of true random strings composed from a user-defined
        set of characters'''
        request_string = compose_api_call(
            STRING_METHOD, apiKey=self.api_key,
            n=n, length=length, characters=characters, replacement=replacement)
        return self.send_request(request_string, STRING_METHOD)

    def generate_uuids(self, n):
        '''Returns a list of true random UUIDs (version 4)'''
        request_string = compose_api_call(
            UUID_METHOD, apiKey=self.api_key, n=n)
        return self.send_request(request_string, UUID_METHOD)

    def generate_blobs(self, n, size, format=FORMAT_BASE64):
        '''Returns a list of Binary Large OBjects (BLOBs) containing
        true random data'''
        request_string = compose_api_call(
            BLOB_METHOD, apiKey=self.api_key, n=n, size=size, format=format)
        return self.send_request(request_string, BLOB_METHOD)

    def get_usage(self):
        '''Returns a dictionary of usage information for the client's
        API key.'''
        request_string = compose_api_call(
            USAGE_METHOD, apiKey=self.api_key)
        return self.send_request(request_string, USAGE_METHOD)

####################### Digitally-signed API methods ##########################

    def generate_signed_integers(self, n, min, max, replacement=True, base=10):
        request_string = compose_api_call(
            SIGNED_INTEGER_METHOD, apiKey=self.api_key, n=n, min=min, max=max,
            replacement=replacement, base=base)
        return self.send_request(request_string, SIGNED_INTEGER_METHOD)

    def generate_signed_integer_sequences(self, n, length, min, max, replacement=True, base=10):
        request_string = compose_api_call(
            SIGNED_INTEGER_SEQUENCE_METHOD, apiKey=self.api_key, n=n, length=length, min=min,
            max=max, replacement=replacement, base=base)
        return self.send_request(request_string, SIGNED_INTEGER_SEQUENCE_METHOD)

    def generate_signed_decimal_fractions(self, n, decimal_places,
                                          replacement=True):
        request_string = compose_api_call(
            SIGNED_DECIMAL_METHOD, apiKey=self.api_key,
            n=n, decimalPlaces=decimal_places, replacement=replacement)
        return self.send_request(request_string, SIGNED_DECIMAL_METHOD)

    def generate_signed_gaussians(self, n, mean, standard_deviation,
                                  significant_digits):
        request_string = compose_api_call(
            SIGNED_GAUSSIAN_METHOD, apiKey=self.api_key,
            n=n, mean=mean,
            standardDeviation=standard_deviation,
            significantDigits=significant_digits)
        return self.send_request(request_string, SIGNED_GAUSSIAN_METHOD)

    def generate_signed_strings(self, n, length, characters, replacement=True):
        request_string = compose_api_call(
            SIGNED_STRING_METHOD, apiKey=self.api_key,
            n=n, length=length, characters=characters, replacement=replacement)
        return self.send_request(request_string, SIGNED_STRING_METHOD)

    def generate_signed_uuids(self, n):
        request_string = compose_api_call(
            SIGNED_UUID_METHOD, apiKey=self.api_key, n=n)
        return self.send_request(request_string, SIGNED_UUID_METHOD)

    def generate_signed_blobs(self, n, size, format=FORMAT_BASE64):
        request_string = compose_api_call(
            SIGNED_BLOB_METHOD,
            apiKey=self.api_key, n=n, size=size, format=format)
        return self.send_request(request_string, SIGNED_BLOB_METHOD)

    def get_result(self, serial_number):
        '''Returns the result of a previous request given a supplied serial
        number.'''
        request_string = compose_api_call(
            RESULT_METHOD, apiKey=self.api_key, serialNumber=serial_number)
        response = self.send_request(request_string, RESULT_METHOD)
        response._method = response._random['method']
        return response

    def verify_signature(self):
        """
        Verifies signed data with RANDOM.org.
        """
        if not self._signature:
            return None

        json_string = compose_api_call(
            VERIFY_SIGNATURE_METHOD, random=self._random,
            signature=self._signature)

        response = self.send_request(json_string, VERIFY_SIGNATURE_METHOD)

        if AUTHENTICITY in response._result:
            return response._result[AUTHENTICITY]
        else:
            raise Exception("Unable to verify authenticity of signed data")

class RandomJSONResponse:
    def __init__(self, json_data, method=""):
        self._json_data = json_data
        self._result = {}
        self._random = []
        self._signature = ""
        self._serial_number = 0
        self._method = method
        self.check_errors()
        self._populate()

    def check_errors(self):
        '''Checks to see if the received JSON object has errors'''
        if 'error' in self._json_data:
            error = self._json_data['error']
            code = error['code']
            message = error['message']
            raise Exception(
"""Error code: {}. Message: {}
See: https://api.random.org/json-rpc/2/error-codes""".format(code, message))

    def _populate(self):
        if RESULT in self._json_data:
            self._result = self._json_data[RESULT]
        if RANDOM in self._result:
            self._random = self._result[RANDOM]
        if SIGNATURE in self._result:
            self._signature = self._result[SIGNATURE]
        if SERIAL_NUMBER in self._random:
            self._serial_number = self._random[SERIAL_NUMBER]

    def parse(self):
        '''Parses the received JSON data object and returns the random data'''
        return self._random['data']

    def __repr__(self):
        try:
            return "<RandomJSONResponse " + self._method + " " + str(self._random["data"]) + ">"
        except:
            return "<RandomJSONResponse None>"

    def __str__(self):
        try:
            return str(self._random['data'])
        except:
            return ""
