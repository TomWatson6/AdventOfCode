package input

import (
	"io/ioutil"
	"strconv"
	"strings"
)

func ReadFile(fileName string) (string, error) {
	fileBytes, err := ioutil.ReadFile(fileName)
	if err != nil {
		return "", err
	}

	fileString := string(fileBytes)

	return fileString, nil
}

func GetLines(input string) []string {
	lines := strings.Split(input, "\n")

	for i := range lines {
		lines[i] = strings.Trim(lines[i], "\r")
	}

	return lines
}

func ToIntArray(input []string) ([]int, error) {
	var output []int

	for _, str := range input {
		num, err := strconv.Atoi(str)
		if err != nil {
			return []int{}, err
		}

		output = append(output, num)
	}

	return output, nil
}
