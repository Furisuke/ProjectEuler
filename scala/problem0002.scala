def fibonacci(first: Int, second: Int): Stream[Int] = first #:: fibonacci(second, first + second)

println(fibonacci(1, 1).takeWhile(_ < 4000000).filter(_%2 == 0).sum)
