package main

import "fmt"

type Study struct {
	ID          int
	Name        string
	Description string
	Sessions    []Session
}

type Session struct {
	ID       int
	StudyID  int
	Note     string
	Uploader string
	Files    []File
}

type File struct {
	ID        int
	SessionID int
	Name      string
	Size      int
}

func main() {
	// fmt.Println("lab-storage: старт")

	study := Study{
		ID:          1,
		Name:        "Исследование черепно-мозговых травм мозга мышей",
		Description: "Искусственное создание ЧМТ, набор групп: контроль, день 1, день 3, неделя, 3 недели. Проведедение ФБМ на каждой группе во сне и бодрстование, кроме контроля. Получение статистики по результатам лечения.",
	}

	s := Session{
		ID:       1,
		StudyID:  study.ID,
		Note:     "10 записей ЭЭГ мышей для группы контроль. В архиве 10 папок в каждой папке отдельная мышь",
		Uploader: "Сергей Попов",
	}

	f := File{
		ID:        1,
		SessionID: s.ID,
		Name:      "10 мышей контроль.zip/.7zp и так далее",
		Size:      8,
	}

	f2 := File{
		ID:        2,
		SessionID: s.ID,
		Name:      "10 мышей ФБМ.zip/.7zp и так далее",
		Size:      564,
	}

	f3 := File{
		ID:        3,
		SessionID: s.ID,
		Name:      "10 мышей ФБМ во сне.zip/.7zp и так далее",
		Size:      687,
	}

	s.Files = []File{f, f2}
	s.Files = append(s.Files, f3)
	study.Sessions = []Session{s}

	// fmt.Printf("%+v\n", study)
	// fmt.Printf("%+v\n", s)
	// fmt.Printf("%+v\n", f)

	// fmt.Printf("%+v\n", files)
	// fmt.Println(len(files))
	// fmt.Printf("%+v\n", files[0])

	// fmt.Printf("%+v\n", study)

	for i, file := range s.Files {
		fmt.Printf("%d) файл %d: %s, размер: %d\n", i, file.ID, file.Name, file.Size)
	}
}
