class PseudoEncoder:

    def dumps(self, native_data):
        chunk = ''
        try:
            processing_func = self.types_processing.get(type(native_data), None)
            chunk += processing_func(self, native_data)
        except TypeError:
            raise NotImplementedError(
                '''{} serializing not supported yet.
                Please try to inherit from PseudoEncoder and implement your own method. After you do it you'l need to
                register your own method in types_processing dictionary.
                '''.format(type(native_data))
            )

        return chunk

    def process_str(self, native_data):
        return native_data

    def process_number(self, native_data):
        return str(native_data)

    def process_dict(self, native_data):
        main_data = ''
        length = len(native_data)

        for k, v in native_data.items():
            delimiter = ', ' if length > 1 else ''
            processed_key = '\'{}\''.format(str(k))
            processed_val = '{}'.format(self.dumps(v))

            if isinstance(v, str):
                processed_val = '\'{}\''.format(processed_val)

            main_data += '{k}: {v}{d}'.format(
                k=processed_key,
                v=processed_val,
                d=delimiter
            )
            length -= 1

        return '{{{}}}'.format(main_data)

    def process_iterable(self, native_data):
        main_data = ''
        length = len(native_data)

        for d in native_data:
            delimeter = ', ' if length > 1 else ''
            main_data += '{}{}'.format(
                self.dumps(d),
                delimeter
            )
            length -= 1

        return '[{}]'.format(main_data)

    types_processing = {
        list: process_iterable,
        tuple: process_iterable,
        dict: process_dict,
        str: process_str,
        int: process_number,
        float: process_number
    }


def pseudo_dumps(native_data, encoder=PseudoEncoder):
    return encoder().dumps(native_data)