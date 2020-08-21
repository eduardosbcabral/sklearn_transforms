from setuptools import setup


setup(
      name='my_custom_sklearn_transforms_eduardosbcabral',
      version='1.0',
      description='''
            This is a sample python package for encapsulating custom
            tranforms from scikit-learn into Watson Machine Learning
      ''',
      url='https://github.com/eduardosbcabral/sklearn_transforms/',
      author='Eduardo Cabral',
      author_email='eduardosbcabral@gmail.com',
      license='BSD',
      packages=[
            'my_custom_sklearn_transforms_eduardosbcabral'
      ],
      zip_safe=False
)
