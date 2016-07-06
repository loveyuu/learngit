package main

import (
	"fmt"
	"utils"
	"model"
)

var c chan int

func main() {

	data := []int{11, 22, 33}
	fmt.Println(utils.NowTime())
	fmt.Println(utils.AddTwoNum(100, 900))
	fmt.Println(utils.SumOfArgs(1, 2, 3, 4, 5, 6, 7))
	fmt.Println(utils.SumOfArgs(data...))

	stu_map := make(map[string]model.Student)
	stu_map["linbin"] = model.Student{"linbin", 24}
	stu_map["yanyu"] = model.Student{"yanyu", 23}
	stu_map["xiaohu"] = model.Student{"xiaohu", 22}
	stu_map["xiaoyu"] = model.Student{"xiaoyu", 20}

	name, ok := stu_map["xiao"]
	if ok {
		fmt.Println(name.Username)
	}else {
		fmt.Println("there is no such student")
	}

	for k, v := range stu_map {
		fmt.Println(k, v.Age, v.Username)
		v.OutPrintStudent()
	}

	delete(stu_map, "linbin")
        fmt.Println(len(stu_map))
	for k, v := range stu_map {
		fmt.Println(k, v.Age, v.Username)
		v.OutPrintStudent()
	}

	c = make(chan int)

	go handle("America")
	go handle("China")

	b := <-c
	fmt.Println(b)
	a := <-c
	fmt.Println(a)
}

func handle(str string)  {
	fmt.Println(str)
	c<-len(str)
}