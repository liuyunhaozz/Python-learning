# Python JSON文件 读写（缩进、排序、格式化）



### 写文件，格式化



> `indent`: 缩进（一般填4，缩进4格）；
> `sort_keys`: 是否排序（默认`False`–不排序）

```python
def write_info(file_name, file_info):
    with open('{}.json'.format(file_name), 'w') as fp:
        json.dump(file_info, fp, indent=4, sort_keys=True)

write_info('report', dict(report_data))

import json1234567
```



### 读文件，格式化

```python
def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

pp_json(your_json_string_or_dict)

>>> import json
>>>
>>> your_json = '["foo", {"bar":["baz", null, 1.0, 2]}]'
>>> parsed = json.loads(your_json)
>>> print json.dumps(parsed, indent=4, sort_keys=True)
[
    "foo", 
    {
        "bar": [
            "baz", 
            null, 
            1.0, 
            2
        ]
    }
]
```