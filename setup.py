from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirments(file_path:str)->List[str]:
    '''
    this function will retrurn the list of requirements
    '''
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='MohdRasmil7',
    author_email='muhammedrasmil2001@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirements.txt')


)