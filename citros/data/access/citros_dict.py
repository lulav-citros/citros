import numpy as np
import json


class CitrosDict(dict):
    """
    Citros dictionary

    CitrosDict is a dictionary-like object, that allows to print the content as a json-object.
    """

    def to_json(self):
        """
        Convert to json string.

        Returns
        -------
        out : str
            json_str

        Examples
        --------
        Make a CitrosDict object, convert it to json string and print it:

        >>> from citros import CitrosDict
        >>> d = CitrosDict({'package': 'data_analysis', 'object': 'CitrosDict', 'method': 'to_json', 'style': 'json'})
        >>> print(d.to_json())
        {
          "package": "citros",
          "object": "CitrosDict",
          'method': 'to_json',
          "style": "json"
        }
        """
        json_str = json.dumps(self, indent=2, cls=_NpEncoder)
        return json_str

    def print(self):
        """
        Print content of the CitrosDict object in a 'json'-style.

        Examples
        --------
        Make a CitrosDict object and print it in json-style:

        >>> from citros import CitrosDict
        >>> d = CitrosDict({'package': 'citros', 'object': 'CitrosDict', 'method': 'print', 'style': 'json'})
        >>> d.print()
        {
         'package': 'citros',
         'object': 'CitrosDict',
         'method': 'print',
         'style': 'json'
        }
        """
        print("{")
        self._print()
        print("}")

    def _print(self, indent=" "):
        """
        Recursively handles and print items of the CitrosDict object.

        Parameters
        ----------
        str
            Indent for the current row.
        """
        if isinstance(self, dict):
            N_len = len(self.keys())
            for i, (k, v) in enumerate(self.items()):
                if isinstance(v, dict):
                    if isinstance(k, str):
                        row_key = "'" + k + "'"
                    else:
                        row_key = str(k)
                    print(indent + row_key + ": {")
                    v._print(indent + "  ")
                    if i == N_len - 1:
                        print(indent + "}")
                    else:
                        print(indent + "},")
                else:
                    if isinstance(k, str):
                        row_key = "'" + k + "'"
                    else:
                        row_key = str(k)
                    if isinstance(v, str):
                        row_val = "'" + v + "'"
                    else:
                        row_val = str(v)
                    if i == N_len - 1:
                        print(indent + row_key + ": " + row_val)
                    else:
                        print(indent + row_key + ": " + row_val + ",")

    def _get_type_dict(self, type_dict, data_dict):
        """
        Recursively find types of the dict values of the `data_dict` and write them in `type_dict`.

        Dictionaries may be embedded in dictionaries.

        Parameters
        ----------
        type_dict : dict
            dict in which the result is written.
        data_dict : dict
            dict to find types of its values.
        """
        for k, v in data_dict.items():
            if isinstance(v, dict):
                type_dict[k] = CitrosDict()
                CitrosDict()._get_type_dict(type_dict[k], v)
            else:
                type_dict[k] = type(v).__name__


class _NpEncoder(json.JSONEncoder):
    """
    Handle numpy types.
    """

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(_NpEncoder, self).default(obj)
