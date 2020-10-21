# PyCrypt

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/ansicolortags.svg)](https://pypi.org/project/pycrypt-cli/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

PyCrypt is a Command-Line Interface (CLI) program, for encryption and decryption using various techniques. PyCrypt takes in an input file, then encrypts/decrypts and stores the result into the output file, provided by the user.

### Pycrypt commands:
- `all`: Returns a list of all available techniques for cryption
- `category`: Returns a list of techniques under a category given by the user
- `encrypt`: Encrypts the content of the `input` file, stores them in `output` file
- `decrypt`: Decrypts the content of the `input` file, stores them in `output` file

### `Encrypt` command

The `encrypt` command takes 4 parameters:
- `-t` or `--technique`: Technique to be used for encryption
- `-i` or `--input_file`: The file whose contents have to be encrypted
- `-o` or `--output_file`: The file in which the encrypted data has to be saved
- `k` or `--key`: Key that is used in the encrypting technique (if any)

> Example

```shell
pycrypt encrypt --technique caesercipher --input_file input.txt --output_file output.txt --key 7
```

### `Decrypt` command

The `decrypt` command takes 4 parameters:
- `-t` or `--technique`: Technique to be used for decryption
- `-i` or `--input_file`: The file whose contents have to be decrypted
- `-o` or `--output_file`: The file in which the decrypted data has to be saved
- `k` or `--key`: Key that is used in the decrypting technique (if any)

> Example

```shell
pycrypt decrypt --technique caesercipher --input_file input.txt --output_file output.txt --key 7
```

### License
MIT License
