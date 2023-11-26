package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strconv"
)

var doorID = "uqwqemis"
var lower = 48
var upper = 55

func hash(text string) string {
	hash := md5.Sum([]byte(text))
	return hex.EncodeToString(hash[:])
}

func main() {
	password := ""
	counter := 0

	for len(password) < 8 {
		h := hash(doorID + strconv.Itoa(counter))
		start := string([]rune(h)[:5])

		if start == "00000" {
			password += string([]rune(h)[5])
		}

		counter++
	}

	fmt.Printf("Part 1: %s\n", password)

	var password2 []rune
	remaining := 8
	counter = 0

	for i := 0; i < 8; i++ {
		password2 = append(password2, '_')
	}

	for remaining > 0 {
		h := hash(doorID + strconv.Itoa(counter))
		runes := []rune(h)
		start := string(runes[:5])

		if start == "00000" {
			char := int(runes[5])
			if char >= lower && char <= upper {
				pos, err := strconv.Atoi(string(runes[5]))
				if err != nil {
					panic(err)
				}

				if password2[pos] == '_' {
					password2[pos] = runes[6]
					remaining--
				}
			}
		}

		counter++
	}

	password = ""

	for _, v := range password2 {
		password += string(v)
	}

	fmt.Printf("Part 2: %s", password)
}
