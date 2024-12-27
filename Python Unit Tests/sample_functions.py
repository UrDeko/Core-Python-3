import copy

def create_object(name, age):
    return {"name": name,
            "age": age
            }

def object_info(object):
    print(object)

def use_object(name, age):
    p = create_object(name, age)
    object_info(p)

if __name__ == "__main__":
    use_object("Coil", 15)