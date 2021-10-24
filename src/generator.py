import hcl


def generator(_terraform_file, _resource_type_to_import, _resource_import_key, _resource_import_prefix="", _resource_import_suffix=""):
    resource_map = {}
    resource_type_to_import =  _resource_type_to_import #"aws_s3_bucket"
    resource_import_key =  _resource_import_key #"bucket"
    resource_import_prefix = _resource_import_prefix #"" #"arn:aws:sns:us-west-2:0123456789012:"
    resource_import_suffix = _resource_import_suffix #""

    with open(_terraform_file, 'r') as fp:
        obj = hcl.load(fp)

    for resource in obj["resource"].keys():
        resource_map[resource] = obj["resource"][resource]

    for command in resource_map[resource_type_to_import]:
        resource_import_value = resource_map[resource_type_to_import][command][resource_import_key]

        real_resource_name="{}{}{}".format(resource_import_prefix, resource_import_value, resource_import_suffix)
        print("terraform import {}.{} {} ".format(resource_type_to_import, 
            command, 
            real_resource_name))
            