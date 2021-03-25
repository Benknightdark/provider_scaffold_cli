import fire
import os
import subprocess
from pathlib import Path
from jinja2 import Environment, PackageLoader, FileSystemLoader, Template
import requests
import re
root_template_url = 'https://raw.githubusercontent.com/Benknightdark/provider_scaffold_cli/main/templates'


def generate_code(template_type, file_name, app_name):
    '''產生範本程式 '''
    split_file_name='_'.join(re.findall('[A-Z][a-z]*', file_name)) 
    template_url = f'{root_template_url}/{template_type}'
    r = requests.get(f'{template_url}/model.jinja').text
    model_template_output = Template(r).render(file_name=file_name,split_file_name=split_file_name)

    r = requests.get(f'{template_url}/view_model.jinja').text
    view_model_template_output = Template(r).render(
        app_name=app_name, file_name=file_name,split_file_name=split_file_name)

    r = requests.get(f'{template_url}/view.jinja').text
    view_template_output = Template(r).render(
        app_name=app_name, file_name=file_name,split_file_name=split_file_name)

    r = requests.get(f'{template_url}/service.jinja').text
    service_template_output = Template(r).render(file_name=file_name,split_file_name=split_file_name)

    # models
    if not os.path.exists('lib/models'):
        os.makedirs('lib/models')
    model_file = open(f"lib/models/{str(split_file_name).lower()}_model.dart", "w+")
    model_file.write(model_template_output)
    model_file.close()

    # view_models
    if not os.path.exists('lib/view_models'):
        os.makedirs('lib/view_models')
    view_model_file = open(
        f"lib/view_models/{str(split_file_name).lower()}_view_model.dart", "w+")
    view_model_file.write(view_model_template_output)
    view_model_file.close()

    # services
    if not os.path.exists('lib/services/api'):
        os.makedirs('lib/services/api')
    service_file = open(
        f"lib/services/api/{str(split_file_name).lower()}_service.dart", "w+")
    service_file.write(service_template_output)
    service_file.close()
    # pages
    if not os.path.exists('lib/pages'):
        os.makedirs('lib/pages')
    page_file = open(f"lib/pages/{str(split_file_name).lower()}_page.dart", "w+")
    page_file.write(view_template_output)
    page_file.close()
    os.system(
        'flutter packages pub run build_runner build --delete-conflicting-outputs')


class Generator(object):

    ''' 產生flutter provider mvvm範本程式 '''

    def basic(self, file_name, app_name):
        '''
        產生基本範本
        :param file_name: 檔案名稱
        :param app_name: App專案名稱                        
        '''
        generate_code("basic", file_name, app_name)
        return file_name
    def list(self, file_name, app_name):
        ''' 
        產生列表範本 
        :param file_name: 檔案名稱
        :param app_name: App專案名稱 
        '''
        generate_code("list", file_name, app_name)
        return file_name

if __name__ == '__main__':
    fire.Fire(Generator)
