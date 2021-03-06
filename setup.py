from setuptools import setup, find_packages

setup(
    name = "django-custom-field",
    version = "2.9",
    author = "David Burke",
    author_email = "david@burkesoftware.com",
    description = ("End user custom fields for Django including contrib.admin support"),
    license = "BSD",
    keywords = "django admin",
    url = "http://github.com/willseward/django-custom-field",
    packages=find_packages(),
    include_package_data=True,
    install_requires = ['django'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        "License :: OSI Approved :: BSD License",
    ],
)
