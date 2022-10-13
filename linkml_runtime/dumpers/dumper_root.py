from abc import ABC, abstractmethod

from linkml_runtime.utils.yamlutils import YAMLRoot


class Dumper(ABC):
    """ Abstract base class for all dumpers """

    def dump(self, element: YAMLRoot, to_file: str, **_) -> None:
        """
        Write element to to_file
        :param element: LinkML object to be dumped
        :param to_file: file to dump to
        :@param _: method specific arguments
        """
        with open(to_file, 'w', encoding='UTF-8') as output_file:
            if not isinstance(element, list):
                data = [element]
            else:
                raise Exception()
            for x in data:
                rsp = self.dumps(x, **_)
                print(rsp)
                output_file.write(rsp)

    @abstractmethod
    def dumps(self, element: YAMLRoot, **_) -> str:
        """
        Convert element to a string
        @param element: YAMLRoot object to be rendered
        @param _: method specific arguments
        @return: stringified representation of element
        """
        raise NotImplementedError()
