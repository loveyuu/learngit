package main

import (
	"fmt"
	"model"
)

func main() {
	dataArray := [5]model.Student{}

	fmt.Println(dataArray)

	for i := 0; i < len(dataArray); i++ {
		dataArray[i].NewStudent("Nanjing", "abcd123")
	}

	for i, v := range dataArray {
		fmt.Println(i)
		v.Show()
	}

	fmt.Println(dataArray)

	stu := new(model.Student)
	stu.NewStudent("Suzhou", "Wuxi")
	stu.Show()
}
