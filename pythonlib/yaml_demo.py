import yaml

if __name__ == "__main__":
    with open('test.yaml', 'r', encoding='utf-8') as f:
        content = yaml.full_load(f)
        print(type(content), content)
        print('......................................................................')
        print(content['id'], content['name'], content['age'], content['books'])
        print('......................................................................')
        print(type(content['language']), content['language'])
        print('......................................................................')
        print(type(content['test']), content['test']['name'], content['test']['request'])
        print('......................................................................')
        
    with open('dict.yaml', 'w', encoding='utf-8') as f:
        data = {}
        
        nums = [11, 22, 33]
        data['num'] = nums
        
        data['key'] = "ABC"
        
        infos = {"price": 1.23, "qty": 100, "remark": "Done"}
        data['value'] = infos
        
        yaml.dump(data, f)