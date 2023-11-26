using System;

namespace AOC2019_5
{
    public class IntCodeComputer
    {
        private int[] Input;
        private bool IncInstructionPtr = true;

        public IntCodeComputer(int[] input)
        {
            this.Input = input;
        }

        public void Run(int inputCode)
        {
            var currentIndex = 0;
            var testIteration = 1;

            while(this.Input[currentIndex] != (int)OpCodeValue.EndProgram)
            {
                var instructionSet = new InstructionSet(ref this.Input, currentIndex);

                currentIndex = instructionSet.Execute(testIteration, currentIndex, this.IncInstructionPtr, currentIndex == 0 ? inputCode : 0);
            }
        }
    }
}
