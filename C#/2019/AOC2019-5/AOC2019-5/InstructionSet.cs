using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace AOC2019_5
{
    public class InstructionSet
    {
        public InstructionSet(ref int[] input, int index)
        {
            this.Input = input;

            var opCodeString = input[index].ToString();

            this.OpCode = new OpCode(input[index]);

            var modes = new Mode[this.OpCode.NumInputParams + this.OpCode.NumOutputParams];

            if (opCodeString.Length > 2)
            {
                for (int i = opCodeString.Length - 3; i >= 0; i--)
                {
                    try
                    {
                        modes[opCodeString.Length - 3 - i] = (Mode)int.Parse(opCodeString[i].ToString());
                    }
                    catch (ArgumentOutOfRangeException)
                    {
                        modes[i] = Mode.Position;
                    }
                }
            }
            else
            {
                for(int i = 0; i < modes.Length; i++)
                {
                    modes[i] = Mode.Position;
                }
            }

            this.InputParams = new Parameter[this.OpCode.NumInputParams];

            for (int i = 0; i < this.OpCode.NumInputParams; i++)
            {
                this.InputParams[i] = new Parameter(modes[i], input[index + i + 1]);
            }

            this.OutputParams = new Parameter[this.OpCode.NumOutputParams];

            for(int i = this.OpCode.NumInputParams; i < this.OpCode.NumInputParams + this.OpCode.NumOutputParams; i++)
            {
                this.OutputParams[i - this.OpCode.NumInputParams] = new Parameter(modes[i], input[index + i + 1]);
            }

            this.ComponentQuantity = 1 + this.InputParams.Length + this.OutputParams.Length;
        }

        public OpCode OpCode { get; set; }
        public Parameter[] InputParams { get; set; }
        public Parameter[] OutputParams { get; set; }
        public int ComponentQuantity { get; set; }
        public int[] Input { get; set; }

        public int Execute(int testIteration, int index, bool incInstructionPtr, int inputValue = 0)
        {
            var inputParams = this.InputParams.Select(x => x.Mode == Mode.Position ? this.Input[x.Value] : x.Value).ToList();
            var outputParams = this.OutputParams.Select(x => x.Mode == Mode.Position ? this.Input[x.Value] : x.Value).ToList();

            switch (this.OpCode.OpCodeValue)
            {
                case OpCodeValue.Addition:
                    this.Input[this.OutputParams[0].Value] = inputParams[0] + inputParams[1];
                    break;
                case OpCodeValue.Multiplication:
                    this.Input[this.OutputParams[0].Value] = inputParams[0] * inputParams[1];
                    break;
                case OpCodeValue.Input:
                    this.Input[this.OutputParams[0].Value] = inputValue;
                    break;
                case OpCodeValue.Output:
                    Console.WriteLine($"Test {testIteration}: {outputParams[0]} at Index: {index - this.ComponentQuantity}");
                    break;
                case OpCodeValue.JumpIfTrue:
                    if (inputParams[0] != 0)
                    {
                        index = inputParams[1];
                        incInstructionPtr = false;
                    }
                    break;
                case OpCodeValue.JumpIfFalse:
                    if (inputParams[0] == 0)
                    {
                        index = inputParams[1];
                        incInstructionPtr = false;
                    }
                    break;
                case OpCodeValue.LessThan:
                    if (inputParams[0] < inputParams[1])
                        this.Input[this.OutputParams[0].Value] = 1;
                    else
                        this.Input[this.OutputParams[0].Value] = 0;
                    break;
                case OpCodeValue.Equals:
                    if (inputParams[0] == inputParams[1])
                        this.Input[this.OutputParams[0].Value] = 1;
                    else
                        this.Input[this.OutputParams[0].Value] = 0;
                    break;
            }

            if (incInstructionPtr)
                return index + this.ComponentQuantity;
            else
                return index;
        }
    }
}
