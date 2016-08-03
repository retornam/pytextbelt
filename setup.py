from setuptools import setup

setup(name='pytextbelt',
      version='0.1',
      description='python wrapper for textbelt',
      author='retornam',
      author_email='example@retornam.com',
      license='MIT',
      packages=['pytextbelt'],
      install_requires=[
          'phonenumbers',
      ],
      zip_safe=False)