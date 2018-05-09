<?php

const LIM = 4000000;

$n = 0;
$n0 = 0;
$n1 = 1;
$evenSum = 0;

while ($n < LIM) {
    $n = $n0 + $n1;
    $n0 = $n1;
    $n1 = $n;
    if ($n % 2 === 0) {
        $evenSum = $evenSum + $n;
    }
}
echo $evenSum;
