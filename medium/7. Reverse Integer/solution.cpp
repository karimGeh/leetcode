class Solution
{
public:
  int reverse(long x)
  {
    bool isNegative = x < 0;

    x = isNegative ? -x : x;

    if (x >= 2147483648)
      return 0;

    long r = 0;

    while (x)
    {
      r = r * 10 + x % 10;
      x /= 10;
    }

    if (r >= 2147483648)
      return 0;

    return isNegative ? -r : r;
  }
};