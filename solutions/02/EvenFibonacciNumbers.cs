using System;

namespace ProjectEuler
{
    class EvenFibonacciNumbers
    {
        const int END = 4000000;

        public static void Run()
        {
            int sum = 0;
            int number = 1;
            int fibonacciValue = 1;
            
            while (fibonacciValue < END)
            {
                fibonacciValue = Fibonacci(number);

                if (fibonacciValue % 2 == 0)
                {
                    sum += fibonacciValue;
                }

                number += 1;
            }

            Console.WriteLine($"Sum: {sum}");
        }

        static int Fibonacci(int number)
        {
            if (number < 2)
            {
                return number;
            }

            return Fibonacci(number - 1) + Fibonacci(number - 2);
        }
    }

}
