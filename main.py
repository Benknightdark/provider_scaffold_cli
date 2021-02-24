import fire
import os

class Generator(object):
  ''' 產生flutter provider mvvm範本程式 '''
  def full_code(self, file_name,app_name):
    ''' 產生完整範本程式 '''
    # models
    if not os.path.exists('models'):
        os.makedirs('models')    
    model_file=open(f"models/{str(file_name).lower()}.dart", "x")
    model_file.write(f'''class {str(file_name).capitalize ()} {{
            {str(file_name).capitalize ()}();
        }}''')
    model_file.close()
    # view_models
    if not os.path.exists('view_models'):
        os.makedirs('view_models')     
    open(f"view_models/{str(file_name).lower()}_view_model.dart", "x")

    # services
    if not os.path.exists('services'):
        os.makedirs('services')      
    open(f"services/{str(file_name).lower()}_service.dart", "x")

    # pages
    if not os.path.exists('pages'):
        os.makedirs('pages')      
    open(f"pages/{str(file_name).lower()}_page.dart", "x")

    return file_name

if __name__ == '__main__':
  fire.Fire(Generator)
