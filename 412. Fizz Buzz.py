class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for v in range(1, n+1):
            divisibleBy3 = v % 3 == 0
            divisibleBy5 = v % 5 == 0
            
            if divisibleBy3 and divisibleBy5:
                output.append("FizzBuzz")
            elif divisibleBy3:
                output.append("Fizz")
            elif divisibleBy5:
                output.append("Buzz")
            else:
                output.append(str(v))
        return output
