# encoding: php
<?=implode("\n",array_map(fn($n)=>match([($n%3==0)+0,($n%5==0)+0]){[1,1]=>'FizzBuzz',[1,0]=>'Fizz',[0,1]=>'Buzz',default=>$n},range(1,100)))?>
