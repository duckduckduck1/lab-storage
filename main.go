package main

import "fmt"

type Experiment struct {
	ID          int
	Name        string
	Description string
}

type Session struct {
	ID           int
	ExperimentID int
	Note         string
	Uploader     string
}

func main() {
	fmt.Println("lab-storage: старт")

	e := Experiment{
		ID:          1,
		Name:        "Исследование черепно-мозговых травм мозга мышей",
		Description: "Искусственное создание ЧМТ, набор групп: контроль, день 1, день 3, неделя, 3 недели. Проведедение ФБМ на каждой группе во сне и бодрстование, кроме контроля. Получение статистики по результатам лечения.",
	}

	s := Session{
		ID:           1,
		ExperimentID: e.ID,
		Note:         "10 записей ЭЭГ мышей для группы контроль. В архиве 10 папок в каждой папке отдельная мышь",
		Uploader:     "Сергей Попов",
	}

	fmt.Printf("%+v\n", e)
	fmt.Printf("%+v\n", s)
}
