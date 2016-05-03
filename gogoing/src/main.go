package main

import (
	"fmt"
	"github.com/go-martini/martini"
	"model"
)

func main() {
	m := make(map[string]model.Student)
	dataArray := [5]model.Student{}

	fmt.Println(dataArray)

	for i := 0; i < len(dataArray); i++ {
		dataArray[i].NewStudent("Nanjing", "abcd123")
	}

	for i, v := range dataArray {
		fmt.Println(i)
		m[v.GetName()] = v
		v.Show()
	}

	for k, v := range m {
		fmt.Println(k, v)
	}

	fmt.Println(dataArray)

	stu := new(model.Student)
	stu.NewStudent("Suzhou", "Wuxi")
	stu.Show()

	mt := martini.Classic()
	mt.Get("/", func() string {
		return "Hello world!"
	})
	mt.Run()
}
