import fire
import os
import subprocess
from pathlib import Path
from jinja2 import Environment, PackageLoader,FileSystemLoader,Template
import requests
class Generator(object):
    ''' 產生flutter provider mvvm範本程式 '''
    template_url='https://raw.githubusercontent.com/Benknightdark/provider_scaffold_cli/main/templates'
    def full_code(self, file_name, app_name):
        template_url=f'{self.template_url}/basic'
        r = requests.get(f'{template_url}/model.jinja').text
        model_template_output =Template(r).render(file_name=file_name)  

        r = requests.get(f'{template_url}/view_model.jinja').text
        view_model_template_output =Template(r).render(app_name=app_name, file_name=file_name)  

        r = requests.get(f'{template_url}/view.jinja').text
        view_template_output =Template(r).render( app_name=app_name,file_name=file_name)

        r = requests.get(f'{template_url}/service.jinja').text
        service_template_output =Template(r).render( file_name=file_name)               
        ''' 產生完整範本程式 '''
        # models
        if not os.path.exists('lib/models'):
            os.makedirs('lib/models')
        model_file = open(f"lib/models/{str(file_name).lower()}.dart", "w+")
        model_file.write(model_template_output)
        model_file.close()

        # view_models
        if not os.path.exists('lib/view_models'):
            os.makedirs('lib/view_models')
        view_model_file = open(f"lib/view_models/{str(file_name).lower()}_view_model.dart", "w+")
        view_model_file.write(view_model_template_output)
        view_model_file.close()

        # services
        if not os.path.exists('lib/services/api'):
            os.makedirs('lib/services/api')
        service_file = open(f"lib/services/api/{str(file_name).lower()}_service.dart", "w+")
        service_file.write(service_template_output)
        service_file.close()
        # pages
        if not os.path.exists('lib/pages'):
            os.makedirs('lib/pages')
        page_file = open(f"lib/pages/{str(file_name).lower()}_page.dart", "w+")
        page_file.write(view_template_output)
        page_file.close()
        # subprocess.run(["dir"])
        os.system('flutter packages pub run build_runner build --delete-conflicting-outputs')
        return file_name


if __name__ == '__main__':
    fire.Fire(Generator)
