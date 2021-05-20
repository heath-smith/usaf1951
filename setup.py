from setuptools import setup

setup(name='usaf1951',
      version='0.1',
      description='USAF 1951 resolution calculator',
      url='',
      author='Heath Smith',
      author_email='hsmith@thorlabs.com',
      license='MIT',
      packages=['usaf1951'],
      package_data={'usaf1951':['inc/*.json']},
      include_package_data=True,
      entry_points={
            'console_scripts': ['build_target=usaf1951.build_target:main']},
      zip_safe=False)