from setuptools import setup
from bike_count import __version__ as current_version

setup(
  name='bike_count',
  version=current_version,
  description='Prediction and visualization of a bicycle trafic in Montpellier',
  url='https://github.com/Assiab2707/packaging_challenge_brda.git',
  author='Berrandou Assia',
  author_email='assia.berrandou@etu.umontpellier.fr',
  license='M1 MIND',
  packages=['bike_count', 'bike_count.io_predict', 'bike_count.io_vis',
            'bike_count.vis', 'bike_count.preprocess', 'bike_count.predict'],
  zip_safe=False
)
