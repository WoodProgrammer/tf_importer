import yaml
import os
import optparse
from generator import *

class ResourceMapping(object):

    def __init__(self, directory, file_name="resource_mapping.yaml"):
        _file_name = file_name
        self.resource_content = None
        self.directory = directory

        with open(_file_name, "r") as stream:
            try:
                self.resource_content = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def get_terraform_files(self):

        tf_list = []
        for file in os.listdir("{}".format(self.directory)):
            if ".tf" in file:
                tf_list.append(file)
            else:
                pass
        return tf_list

    def get_import_commands(self):
        
        terraform_files = self.get_terraform_files()
        for terraform_file in terraform_files:
            for resource in self.resource_content["resources"]:
        
                command = generator(_resource_type_to_import=self.resource_content["resources"][resource]["to_import"],
                    _resource_import_key=self.resource_content["resources"][resource]["import_key"],
                    _resource_import_prefix=self.resource_content["resources"][resource]["prefix"],
                    _resource_import_suffix=self.resource_content["resources"][resource]["suffix"],
                    _terraform_file="{}/{}".format(directory, terraform_file)
                )
                if command == None:
                    pass
                else:
                    print(command)


if __name__ == "__main__":

    parser = optparse.OptionParser()

    parser.add_option('-f', '--file',
        action="store", dest="file",
        help="Confiuration file defintion of resource mapping",
        default="resource_mapping.yaml"
    )

    parser.add_option('-d', '--directory',
        action="store", dest="directory",
        help="The directory of the terraform files",
        default="./infra"
    )
    

    (options, args) = parser.parse_args()
    data = vars(options)
    file_name = data["file"]
    directory = data["directory"]

    obj = ResourceMapping(
        file_name="{}".format(file_name),
        directory="{}".format(directory)
    )

    obj.get_import_commands()
