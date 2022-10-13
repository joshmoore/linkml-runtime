from decimal import Decimal

import yaml

from linkml_runtime.dumpers.dumper_root import Dumper
from linkml_runtime.utils.formatutils import remove_empty_items
from linkml_runtime.utils.yamlutils import YAMLRoot

class YAMLDumper(Dumper):

    def dumps(self, element: YAMLRoot, **kwargs) -> str:
        """ Return element formatted as a YAML string """
        # Internal note: remove_empty_items will also convert Decimals to int/float;
        # this is necessary until https://github.com/yaml/pyyaml/pull/372 is merged
        try:
            data = [remove_empty_items(x, hide_protected_keys=True) for x in element]
        except:
            data= remove_empty_items(element, hide_protected_keys=True)
        return yaml.dump(data,
                         Dumper=yaml.SafeDumper, sort_keys=False,
                         allow_unicode=True,
                         **kwargs)
