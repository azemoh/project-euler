using System;

namespace ProjectEuler
{
    class MultiplesOf3And5
    {
        public static void Run()
        {
            int sum = 0;

            for (int i = 1; i < 1000; i += 1)
            {
                if ((i % 3 == 0) || (i % 5 == 0))
                {
                    sum += i;
                }
            }

            Console.WriteLine(sum);
        }
    }
}
