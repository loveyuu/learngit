package model

import (
	"fmt"
)

/*
bean
*/
type Student struct {
	name     string
	password string
}

func (s *Student) NewStudent(name, password string) {
	s.name = name
	s.password = password
}

func (s *Student) Show() {
	fmt.Println(s.name, s.password)
}
