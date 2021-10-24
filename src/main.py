import yaml
from generator import *
import optparse


class ResourceMapping(object):

    def __init__(self, file_name="resource_mapping.yaml"):
        _file_name = file_name
        self.resource_content = None

        with open(_file_name, "r") as stream:
            try:
                self.resource_content = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def get_import_commands(self):

        for resource in self.resource_content["resources"]:
    
            command = generator(_resource_type_to_import=self.resource_content["resources"][resource]["to_import"],
                _resource_import_key=self.resource_content["resources"][resource]["import_key"],
                _resource_import_prefix=self.resource_content["resources"][resource]["prefix"],
                _resource_import_suffix=self.resource_content["resources"][resource]["suffix"],

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

    (options, args) = parser.parse_args()
    data = vars(options)
    file_name = data["file"]

    obj = ResourceMapping(file_name="{}".format(file_name))
    obj.get_import_commands()
