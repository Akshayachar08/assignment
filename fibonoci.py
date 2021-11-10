{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "86447fc7",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the value of n:50\n",
      "fabonacci series 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986 102334155 165580141 267914296 433494437 701408733 1134903170 1836311903 2971215073 4807526976 7778742049 "
     ]
    }
   ],
   "source": [
    "#Fibonacci\n",
    "n = int(input(\"enter the value of n:\"))\n",
    "a=0\n",
    "b=1\n",
    "sum = 0\n",
    "count = 1\n",
    "print(\"fabonacci series\", end =\" \")\n",
    "while( count <= n):\n",
    "    print(sum, end =\" \")\n",
    "    count += 1\n",
    "    a = b\n",
    "    b = sum\n",
    "    sum = a + b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "21b76bc9",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "1\n",
      "2\n",
      "3\n",
      "5\n",
      "8\n",
      "13\n",
      "21\n",
      "34\n"
     ]
    }
   ],
   "source": [
    "a = 0\n",
    "b = 1\n",
    "while b < 50:\n",
    "    print(b)\n",
    "    a,b = b, a+b"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
