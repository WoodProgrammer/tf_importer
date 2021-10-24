# tf_importer

This tool helps to generate terraform import commands for the huge terraform stack. If you want to import terraform resources to make your configuration and terraform states under the same state you can use this tool for the huge terraform stacks.

# How it works 
The most important configuration file is <b>resource_mapping.yaml</b> file, this file contains the configuration map and provider specific keys based on your provider.

```yaml
## resource_map.yaml
resources:
  buckets:
    to_import: aws_s3_bucket
    import_key: bucket
    prefix: ""
    suffix: ""

  sns_topics:
    to_import: aws_sns_topic
    import_key: name
    prefix: "arn:aws:sns:us-west-2:0123456789012:"
    suffix: ""

  staging_helm_releases:
    to_import: helm_release
    import_key: name
    prefix: "<namespace>/"
    suffix: ""
  
```
Under the resources map, you only have to define which resources you need to import;

* to_import : Resource name of the provider
* import_key: The identifier key in the resource definition
* prefix: The prefix to refer real resource
* suffix: The suffix to refer real resource

After you defined your resource map you only have to run this command like that;


```sh
$ python3 main.py --file resource_mapping.yaml --directory ./infra

terraform import aws_s3_bucket.b my-tf-test-bucket
terraform import aws_sns_topic.user_updates arn:aws:sns:us-west-2:0123456789012:user-updates-topic
terraform import aws_rds_cluster.default aurora-cluster-demo
terraform import aws_rds_cluster.default_new aurora-cluster-demo
terraform import aws_rds_cluster.default_hede aurora-cluster-demo
```

## TODO

- Dynamic and block based import generation
- Manual Resource Check
- Config Drift Check
