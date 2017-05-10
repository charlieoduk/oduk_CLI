
from setuptools import setup


setup(
        name = 'OdukCli',
        version = '1.0',
        py_modules=['odukcli'],
        install_requires = [
            
            'Click',
            
         ],
         entry_points = '''
              [console_scripts]
               weather=odukcli:cli
         '''
        
        )



