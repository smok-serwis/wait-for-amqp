# coding=UTF-8

from setuptools import setup
setup(
    keywords=['amqp', 'ci', 'utility'],
    version="1.0",
    install_requires=['coolamqp>=1.0.2'],
    packages=[
        'wait_for_amqp',
    ],
    entry_points={'console_scripts':
                                   ['wait-for-amqp = wait_for_amqp.run:run']
                    }
)
