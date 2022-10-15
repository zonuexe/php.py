# encoding: php
<?php
foreach (range(1,100) as $n) {
    print match ($n % 3 == 0) {
        true => match ($n % 5 == 0) {
            true => 'FizzBuzz',
            false => 'Fizz',
        },
        false => match ($n % 5 == 0) {
            true => 'Buzz',
            false => (string)$n,
        },
    } . PHP_EOL;
}
