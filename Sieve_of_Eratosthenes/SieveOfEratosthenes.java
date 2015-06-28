/* Java program to generate prime numbers using the Sieve of Eratosthenes.
(https://thecodeaddict.wordpress.com/2011/11/01/sieve-of-eratosthenes/) */

class SieveOfEratosthenes
{
    static int[] Sieve(int limit)
    {
        int crosslimit = (int)Math.sqrt(limit);
        boolean[] sieve = new boolean[limit];
        int m, n;
 
        for(n = 4; n < limit; n += 2)
            sieve[n] = true;
 
        for(n = 3; n < crosslimit; n +=2)
            if(!sieve[n])
                for(m = n*n; m < limit; m += 2*n)
                    sieve[m] = true;
 
        int num_primes = 0;
        for(n = 2; n < limit; n++)
            if(!sieve[n])
                num_primes++;
 
        int[] primes = new int[num_primes];
        int i = 0;
        for(n = 2; n < limit; n++)
            if(!sieve[n])
                primes[i++] = n;
 
        return primes;
    }
 
    public static void main(String args[])
    {
        int l = (int)Math.pow(2,15);
        int[] p = Sieve(l);
        for(int i = 0; i < p.length; i++)
            System.out.println(p[i]);
    }
}