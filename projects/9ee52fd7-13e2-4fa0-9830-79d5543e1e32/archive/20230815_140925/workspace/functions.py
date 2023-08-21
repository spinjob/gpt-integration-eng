from workflow import Workflow

def get_menu(store_id):
    steps = [
        {
            'api': 'https://partners.cloudkitchens.com',
            'method': 'get',
            'path': '/menu',
            'data_mapping': {
                'X-Store-Id': {
                    'input': {'in': 'body', 'sourcePath': 'testStoreId'},
                    'output': {'in': 'header', 'outputPath': 'X-Store-Id'}
                }
            }
        }
    ]
    workflow = Workflow(steps)
    workflow.execute_step(0)
    return workflow.data

def upsert_menu(store_id, menu):
    steps = [
        {
            'api': 'https://partners.cloudkitchens.com',
            'method': 'post',
            'path': '/menu',
            'data_mapping': {
                'categories.{{categoryId}}': {
                    'input': {'in': 'body', 'sourcePath': 'categories.{{categoryId}}'},
                    'output': {'in': 'body', 'outputPath': 'categories.{{categoryId}}'}
                },
                'modifierGroups.{{modifierGroupId}}': {
                    'input': {'in': 'body', 'sourcePath': 'modifierGroups.{{modifierGroupId}}'},
                    'output': {'in': 'body', 'outputPath': 'modifierGroups.{{modifierGroupId}}'}
                }
            }
        }
    ]
    workflow = Workflow(steps)
    workflow.data = menu
    workflow.execute_step(0)
    return workflow.data
