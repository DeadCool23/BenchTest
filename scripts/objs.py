import random
import string
import json

def generate_flat_obj() -> dict:
    payload = {}
    
    for i in range(1, 101):
        field_name = f'f{i}'
        
        if i % 4 == 1:
            payload[field_name] = ''.join(random.choices(string.ascii_letters, k=10))
        elif i % 4 == 2:
            payload[field_name] = random.randint(1, 1000)
        elif i % 4 == 3:
            payload[field_name] = random.choice([True, False])
        else:
            payload[field_name] = round(random.uniform(1.0, 1000.0), 2)
    
    return payload

def generate_mixed_obj() -> dict:
    def create_f5555():
        return {
            'f55551': ''.join(random.choices(string.ascii_letters, k=8)),
            'f55552': random.randint(1, 1000),
            'f55553': random.choice([True, False]),
            'f55554': round(random.uniform(1.0, 100.0), 2)
        }
    
    def create_f555():
        return {
            'f5551': ''.join(random.choices(string.ascii_letters, k=8)),
            'f5552': random.randint(1, 1000),
            'f5553': random.choice([True, False]),
            'f5554': round(random.uniform(1.0, 100.0), 2),
            'f5555': create_f5555()
        }
    
    def create_f55():
        return {
            'f551': ''.join(random.choices(string.ascii_letters, k=8)),
            'f552': random.randint(1, 1000),
            'f553': random.choice([True, False]),
            'f554': round(random.uniform(1.0, 100.0), 2),
            'f555': create_f555()
        }
    
    def create_f5():
        return {
            'f51': ''.join(random.choices(string.ascii_letters, k=8)),
            'f52': random.randint(1, 1000),
            'f53': random.choice([True, False]),
            'f54': round(random.uniform(1.0, 100.0), 2),
            'f55': create_f55()
        }
    
    def create_f65():
        return {
            'f651': ''.join(random.choices(string.ascii_letters, k=8)),
            'f652': random.randint(1, 1000),
            'f653': random.choice([True, False]),
            'f654': round(random.uniform(1.0, 100.0), 2)
        }
    
    def create_f6():
        return {
            'f61': ''.join(random.choices(string.ascii_letters, k=8)),
            'f62': random.randint(1, 1000),
            'f63': random.choice([True, False]),
            'f64': round(random.uniform(1.0, 100.0), 2),
            'f65': create_f65()
        }
    
    def create_f75():
        return {
            'f751': ''.join(random.choices(string.ascii_letters, k=8)),
            'f752': random.randint(1, 1000),
            'f753': random.choice([True, False]),
            'f754': round(random.uniform(1.0, 100.0), 2)
        }
    
    def create_f7():
        return {
            'f71': ''.join(random.choices(string.ascii_letters, k=8)),
            'f72': random.randint(1, 1000),
            'f73': random.choice([True, False]),
            'f74': round(random.uniform(1.0, 100.0), 2),
            'f75': create_f75()
        }
    
    def create_f85():
        return {
            'f851': ''.join(random.choices(string.ascii_letters, k=8)),
            'f852': random.randint(1, 1000),
            'f853': random.choice([True, False]),
            'f854': round(random.uniform(1.0, 100.0), 2)
        }
    
    def create_f8():
        return {
            'f81': ''.join(random.choices(string.ascii_letters, k=8)),
            'f82': random.randint(1, 1000),
            'f83': random.choice([True, False]),
            'f84': round(random.uniform(1.0, 100.0), 2),
            'f85': create_f85()
        }
    
    def create_f95():
        return {
            'f951': ''.join(random.choices(string.ascii_letters, k=8)),
            'f952': random.randint(1, 1000),
            'f953': random.choice([True, False]),
            'f954': round(random.uniform(1.0, 100.0), 2)
        }
    
    def create_f9():
        return {
            'f91': ''.join(random.choices(string.ascii_letters, k=8)),
            'f92': random.randint(1, 1000),
            'f93': random.choice([True, False]),
            'f94': round(random.uniform(1.0, 100.0), 2),
            'f95': create_f95()
        }
    
    def create_f105():
        return {
            'f1051': ''.join(random.choices(string.ascii_letters, k=8)),
            'f1052': random.randint(1, 1000),
            'f1053': random.choice([True, False]),
            'f1054': round(random.uniform(1.0, 100.0), 2)
        }
    
    def create_f10():
        return {
            'f101': ''.join(random.choices(string.ascii_letters, k=8)),
            'f102': random.randint(1, 1000),
            'f103': random.choice([True, False]),
            'f104': round(random.uniform(1.0, 100.0), 2),
            'f105': create_f105()
        }
    
    return {
        'f1': ''.join(random.choices(string.ascii_letters, k=10)),
        'f2': random.randint(1, 1000),
        'f3': random.choice([True, False]),
        'f4': round(random.uniform(1.0, 100.0), 2),
        'f5': create_f5(),
        'f6': create_f6(),
        'f7': create_f7(),
        'f8': create_f8(),
        'f9': create_f9(),
        'f10': create_f10()
    }

def generate_deep_obj() -> dict:
    current_level = {'data': ''.join(random.choices(string.ascii_letters, k=20))}
    
    for level in range(49, 0, -1):
        current_level = {f'l{level + 1}': current_level}
    
    return {'l1': current_level}


def print_obj(obj: dict):
    print(json.dumps(obj, indent=2, ensure_ascii=False))
