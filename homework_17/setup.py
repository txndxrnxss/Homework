from setuptools import setup, find_packages
import pathlib
from os import path

HERE = pathlib.Path(__file__).parent.resolve()
long_description = (HERE / 'README.md').read_text(encoding='utf-8')
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
install_requires = [x.strip() for x in all_reqs]
setup(name='temperature_calculator',
      	version='0.1',
      	description='skript',
      	url='http://github.com/<account>/<repo>',
      	author=' Sofia Aleksandrova ',
      	author_email='sofia.gerdeva02@gmail.com',
	long_description=long_description,
   	long_description_content_type='text/markdown',
      	license='MIT',
 	packages=find_packages(),
   	python_requires='>=3.8, <4',
   	install_requires=install_requires,      
	zip_safe=False)