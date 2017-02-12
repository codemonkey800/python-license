# python-license

A simple command line utility for fetching open source licenses available from
GitHub.

## Table of Contents

- [Installation](#installation)
    - [Setuptools](#setuptools)
    - [Arch User Repository](#arch-user-repository)
- [Usage](#usage)
    - [`shell` Command](#shell-command)
    - [`list` Command](#list-command)
    - [`get` Command](#get-command)
- [Caveats](#caveats)
- [License](#license)

# Installation

## Setuptools

To install using setuptools, run:

```sh
$ python setup.py build
$ python setup.py install
```

## Arch User Repository

You can also install it through AUR:

```sh
$ yaourt -S python-license
```

You can also choose to install it with git + makepkg:

```sh
$ git clone https://aur.archlinux.org/python-license
$ cd python-license
$ makepkg -si
```

# Usage

## `shell` Command

Install or print shell completions using
[click-completion](https://github.com/click-contrib/click-completion).

### Install Shell

```sh
$ license shell --install
```

Autodetection of shell requires [psutils](https://github.com/giampaolo/psutil)
installed. It should be installed by default by `setup.py`.

### Specify Shell
```sh
$ license shell --shell /bin/bash --install
```

### Source in `.bashrc`

```sh
$ source "$(license shell --shell /bin/bash)
```

### Source in `config.fish`
```sh
eval (license shell --shell /usr/bin/fish)
```


## `list` Command

### List all licenses available
```sh
$ license list
```

### List licenses that match pattern
```sh
$ license list '^gpl'
```

## `get` Command

### Fetch MIT license and write to `LICENSE.md`
```sh
$ license get mit
```

### Fetch license and write to stdout
```sh
$ license get --stdout mit
```

### Fetch license and write to custom output
```sh
$ license get --output LICENSE mit
# or
$ license get --stdout mit > LICENSE
```

# Caveats

As of writing, the licenses aren't templated and are provided as is. For the
time being, you'll have to manually replace it:

```sh
$ license get --stdout mit | sed -i 's/\[year\]/2016/g; s/\[fullname\]/my name lmao/g'
```

# License

The MIT License (MIT)

Copyright (c) 2016 Jeremy Asuncion

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
