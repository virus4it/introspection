def introspection_info(obj):


    obj_type = type(obj)


    attributes = []
    methods = []
    for attr_name in dir(obj):
        try:
            attr = getattr(obj, attr_name)
            if callable(attr):
                methods.append(attr_name)
            else:
                attributes.append(attr_name)
        except Exception:
            pass


    obj_module = getattr(obj, "__module__", None)

    return {
        "type": obj_type,
        "attributes": attributes,
        "methods": methods,
        "module": obj_module,
    }


number_info = introspection_info(42)
print(number_info)
