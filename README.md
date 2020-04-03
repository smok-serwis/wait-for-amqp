wait-for-amqp
==================

[![Build Status](https://travis-ci.org/smok-serwis/wait-for-amqp.svg)](https://travis-ci.org/smok-serwis/wait-for-amqp)
[![PyPI](https://img.shields.io/pypi/pyversions/wait-for-amqp.svg)](https://pypi.python.org/pypi/wait-for-amqp)
[![PyPI version](https://badge.fury.io/py/wait-for-amqp.svg)](https://badge.fury.io/py/wait-for-amqp)
[![PyPI](https://img.shields.io/pypi/implementation/wait-for-amqp.svg)](https://pypi.python.org/pypi/wait-for-amqp)

This is a quick'n'dirty utility to wait for an
AMQP broker instance 
to become available. This proves to be an issue in CI development,
where jobs that are tested for rabbitmq need to wait for it
to become available. Well, no problem with that!

# Installation

`pip install wait-for-amqp`

# Usage

`wait-for-amqp <hostname> <max time to wait for> <login> <password> <virtual_host>`
All of these arguments are required.
