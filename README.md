# php.py

## How to use

```
$ python -m phpcodec target.py
```

## Sample

`fizzbuzz.py`

```php
# encoding: php
<?=implode("\n",array_map(fn($n)=>match([($n%3==0)+0,($n%5==0)+0]){[1,1]=>'FizzBuzz',[1,0]=>'Fizz',[0,1]=>'Buzz',default=>$n},range(1,100)))?>
```


## Copyright



```
Copying and distribution of this file, with or without modification,
are permitted in any medium without royalty provided the copyright
notice and this notice are preserved.  This file is offered as-is,
without any warranty.
```

## Acknowledgments

The great idea for this code comes from [an idea presented at LL Tiger](http://blog.shibu.jp/article/39920783.html) by [Yoshiki Shibukawa](https://github.com/shibukawa).  And [a blog entry](https://doloopwhile.hatenablog.com/entry/20100801/1280688409) by [Kenji Omoto](https://github.com/doloopwhile) gave me a clue as to the missing code snippet.  Many thanks to both.

