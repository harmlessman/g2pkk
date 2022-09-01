# g2pkk
This is a cross-platform g2p for Korean.

g2pkk is a library that made [Kyubyong's g2pk](https://github.com/Kyubyong/g2pK) work in Windows.
The reason why g2pk does not work well in Windows is that the `mecab`, the morpheme analyzer used by g2pk, causes build errors in Windows.
g2pkk uses a different morpheme analyzer depending on the operating system.
Windows uses [eunjeon](https://github.com/koshort/pyeunjeon), which enables mecab to be used in Windows, and other operating systems use [python-mecab-ko](https://github.com/jonghwanhyeon/python-mecab-ko), which was previously used in g2pk.

Install g2pkk and make sure that a morpheme analyzer exists for the operating system of the laptop you are using for the first time, and if not, proceed with the installation automatically.

## Requirements
* pythoon >= 3.6
* jamo
* nltk


## Installation
```
pip install g2pkk==0.1.0
```

Do not download the version below 0.1.0.

It's a test version, so it doesn't work smoothly.

## How To Use
The use of g2pkk is the same as g2pk.
```
>>> from g2pkk import G2p
>>> g2p = G2p("포상은 열심히 한 아이에게만 주어지기 때문에 포상인 것입니다.")
>>> g2p("포상으 녈심히 하 나이에게만 주어지기 때무네 포상인 거심니다.")

```
If you want more information, check [g2pk](https://github.com/Kyubyong/g2pK)

