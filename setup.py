from setuptools import setup

setup(
    name='cernhomepage',
    #packages=['cernhomepage'],
    #include_package_data=True,
    install_requires=[
        'flask',
        'gunicorn'
    ],
)
