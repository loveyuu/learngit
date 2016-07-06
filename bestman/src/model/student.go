package model

import (
	"fmt"
)

type Student struct  {
	Username string
	Age      int
}

func (stu *Student)OutPrintStudent()  {
	stu.Age = 1000
	fmt.Println(stu.Username, stu.Age)
}

