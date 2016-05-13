package main

import (
	"github.com/go-martini/martini"
	"net/http"
)

func main() {
	m := martini.Classic()
	m.Get("/:page", func(parms martini.Params) string {
		return parms["page"]
	})
	m.Post("/login", func(r *http.Request) string {
		username, password := r.FormValue("username"), r.FormValue("password")
		if username == "linbin" && password == "lin1253007885" {
			return "login success!"
		}
		return "login failed!"
	})
	m.Run()
}
