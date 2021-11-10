{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4af24c78",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number of even numbers: 4\n",
      "numer of odd numbers: 5\n"
     ]
    }
   ],
   "source": [
    "#OddorEven\n",
    "number = (1, 2, 3, 4, 5, 6, 7, 8, 9)\n",
    "no_of_odd = 0\n",
    "no_of_even = 0\n",
    "for n in number:\n",
    "    if not n % 2:\n",
    "        no_of_even+=1\n",
    "    else:\n",
    "        no_of_odd+=1\n",
    "print(\"number of even numbers:\", no_of_even )\n",
    "print(\"numer of odd numbers:\", no_of_odd)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "10e368c8",
   "metadata": {},
   "outputs": [],
   "source": []
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
