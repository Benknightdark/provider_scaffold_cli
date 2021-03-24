import fire
import os
import subprocess
from pathlib import Path
from jinja2 import Environment, PackageLoader,FileSystemLoader

class Generator(object):
    ''' 產生flutter provider mvvm範本程式 '''

    def full_code(self, file_name, app_name):
        file_loader = FileSystemLoader('templates')
        env = Environment(loader=file_loader)
        model_template = env.get_template('/basic/model.jinja')
        model_template_output = model_template.render(file_name=file_name)
        view_model_template = env.get_template('/basic/view_model.jinja')
        view_model_template_output = view_model_template.render(app_name=app_name, file_name=file_name)
        # view_template = env.get_template('/basic/view.jinja')
        # view_template_output = view_template.render(file_name=file_name)
        # service_template = env.get_template('/basic/service.jinja')
        # service_template_output = service_template.render(file_name=file_name)        
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
        view_model_file = open(
            f"lib/view_models/{str(file_name).lower()}_view_model.dart", "w+")
        view_model_file.write(view_model_template_output)
        view_model_file.close()

        # services
        if not os.path.exists('lib/services/api'):
            os.makedirs('lib/services/api')
        service_file = open(
            f"lib/services/api/{str(file_name).lower()}_service.dart", "w+")
        service_file.write(f'''
import 'package:dio/dio.dart';

class {str(file_name).capitalize()}Service {{}}
     ''')
        service_file.close()
        # pages
        if not os.path.exists('lib/pages'):
            os.makedirs('lib/pages')
        page_file = open(f"lib/pages/{str(file_name).lower()}_page.dart", "w+")
        page_file.write(f'''
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:{app_name}/view_models/{str(file_name).lower()}_view_model.dart';

class {str(file_name).capitalize()}Page extends StatefulWidget {{
    @override
    _{str(file_name).capitalize()}PageState createState() => _{str(file_name).capitalize()}PageState();
    }}

    class _{str(file_name).capitalize()}PageState extends State<{str(file_name).capitalize()}Page> {{
    @override
    void initState()  {{
        super.initState();
        final vm = Provider.of<{str(file_name).capitalize()}ViewModel>(context, listen: false);
        // fetch initialize data
    }}

    @override
    void dispose()  {{
        super.dispose();
    }}

    @override
    Widget build(BuildContext context)  {{
        final vm = Provider.of<{str(file_name).capitalize()}ViewModel>(context);

        return Scaffold(
        appBar: AppBar(
            title: Text('{str(file_name).capitalize()}'),
        ),
        body: SingleChildScrollView(
            child: Column(
                crossAxisAlignment: CrossAxisAlignment.center,
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                Column(children: <Widget>[
                    Row(
                    children: <Widget>[],
                    )
                ]),
                ]),
        ),
        );
    }}
}}
    
    ''')
        page_file.close()
        # subprocess.run(["dir"])
        os.system('flutter packages pub run build_runner build --delete-conflicting-outputs')
        return file_name


if __name__ == '__main__':
    fire.Fire(Generator)
