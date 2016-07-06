package utils


func AddTwoNum(a int, b int) int {
	return a + b
}

func SumOfArgs(args ...int) int {
	total := 0
	for _, v := range args {
		total += v
	}
	return total
}