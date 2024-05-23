package main

import (
	"fmt"
)

func main() {
	//value types
	var int_value int
	var float_value float32
	var string_value string
	var bool_value bool
	var byte_value byte
	var rune_value rune

	int_value = 0 // zero jokes about integers. Integers are some very serious numbers.
	// I am a...
	float_value = 3.1415 // oneer in Go
	string_value = "What a splended day, me Lord, aint it?"
	bool_value = false // alarm, it was my clock
	byte_value = 255   // bits gathered together and created a 2^255 number
	rune_value = 'f'   //bomb

	fmt.Println("Integer example: ", int_value)
	fmt.Println("Float example: ", float_value)
	fmt.Println("String example: ", string_value)
	fmt.Println("Bool example: ", bool_value)
	fmt.Println("Byte example: ", byte_value)
	fmt.Println("Rune example: ", rune_value)

	//wait for input
	fmt.Print("Press the Enter Key to terminate the program")
	fmt.Scanln()
}
