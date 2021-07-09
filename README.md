import unittest
from calcu2 import Calculator


class Test(unittest.TestCase):

    #add two numbers
    def test_add(self):
        c = Calculator() 
        c.btnClick(7)
        c.btnClick("+")
        c.btnClick(9)
        c.btnClick(3)
        c.evaluate(input)
        self.assertEqual(c.evaluate(input), 100)

    #subtract two numbers
    def test_subtract1(self):
        c = Calculator() 
        c.btnClick(1)
        c.btnClick(0)
        c.btnClick(0)
        c.btnClick("-")
        c.btnClick(5)
        c.btnClick(0)
        c.evaluate(input)
        self.assertEqual(c.evaluate(input), 50)

    #subtract two numbers resulting to a negative answer
    def test_subtract2(self):
        c = Calculator() 
        c.btnClick(1)
        c.btnClick(0)
        c.btnClick(0)
        c.btnClick("-")
        c.btnClick(1)
        c.btnClick(5)
        c.btnClick(0)
        c.evaluate(input)
        self.assertEqual(c.evaluate(input), -50)
    
    #divide two numbers
    def test_divide1(self):
        c = Calculator() 
        c.btnClick(2)
        c.btnClick(0)
        c.btnClick("/")
        c.btnClick(4)
        c.evaluate(input)
        self.assertEqual(c.evaluate(input), 5)

    #multiply two numbers
    def test_multiply(self):
        c = Calculator() 
        c.btnClick(3)
        c.btnClick("*")
        c.btnClick(2)
        c.btnClick(0)
        c.evaluate(input)
        self.assertEqual(c.evaluate(input), 60)
    
    #get the percentage
    def test_percentage(self):
        c = Calculator() 
        c.btnClick(3)
        c.btnClick(9)
        c.btnClick("%")
        c.evaluate(input)
        self.assertEqual(c.evaluate(input), 0.39)

    #errors
    #two succeeding decimals
    def test_decimal_error(self):
        c = Calculator() 
        c.btnClick(3)
        c.btnClick("*")
        c.btnClick("*")
        c.evaluate(input)
        self.assertEqual(c.evaluate(input), "Syntax Error")

    #two succeeding multiply
    def test_multiply_error(self):
        c = Calculator() 
        c.btnClick(2)
        c.btnClick(0)
        c.btnClick("x")
        c.btnClick("x")
        c.evaluate(input)
        self.assertEqual(c.evaluate(input), "Syntax Error")
    
    #zero division error
    def test_zero_division_error(self):
        c = Calculator() 
        c.btnClick(0)
        c.btnClick("/")
        c.btnClick(0)
        c.evaluate(input)
        self.assertEqual(c.evaluate(input), "Math Error")
    
    #check the ans button
    def test_check_ans_btn(self):
        c = Calculator() 
        c.btnClick(3)
        c.btnClick(6)
        c.btnClick("/")
        c.btnClick(6)
        c.evaluate(input)
        c.btnClick("ans")
        c.evaluate(input)
        self.assertEqual(c.evaluate(input), 6)
    
    #check the del button
    def test_check_ans_btn(self):
        c = Calculator() 
        c.btnClick(3)
        c.btnClick(6)
        c.btnClick("/")
        c.btnClick(6)
        c.btnClick("+")
        c.btnClick(6)
        c.btnClick(2)
        c.btnClick("delete")
        c.evaluate(input)
        self.assertEqual(c.evaluate(input), 12)


if __name__ == "__main__":
    unittest.main()
