import hashlib as hl
import json

def hash_string_256(string):
    """Create a SHA256 hash for a given input string.

    Arguments:
        :string: The string which should be hashed.
    """
    return hl.sha256(string).hexdigest()


# def hash_block(block):
#     """Hashes a block and returns a string representation of it.
#
#     Arguments:
#         :block: The block that should be hashed.
#     """
#     return hash_string_256(json.dumps(block, sort_keys=True).encode())


def get_hash_of_block(block):
    # return '-'.join([str(block[key]) for key in block])
    '''
    json.dumps will convert the python dictionary to the string type
    encode to encode to utf8 binary format
    hexdigest to convert the binary encode to human readable hexadecimal format
    :param block:
    :return:
    '''
    return hl.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()
