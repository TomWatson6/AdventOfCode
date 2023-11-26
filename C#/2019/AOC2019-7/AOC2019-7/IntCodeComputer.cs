using System;

namespace AOC2019_7
{
    public class IntCodeComputer
    {
        public int[] Input;
        private bool IncInstructionPtr = true;

        public IntCodeComputer(int[] input)
        {
            this.Input = input;
        }

        public int Run(int amplifierCode, int inputCode)
        {
            bool amplifierCodeUsed = false;
            bool inputCodeUsed = false;

            var currentIndex = 0;
            var testIteration = 1;

            int outputValue = 0;
            int count = 0;

            while (this.Input[currentIndex] != (int)OpCodeValue.EndProgram)
            {
                var instructionSet = new InstructionSet(ref this.Input, currentIndex);
                
                int code = 0;

                if (!amplifierCodeUsed)
                {
                    code = amplifierCode;
                    amplifierCodeUsed = true;
                }
                else if (!inputCodeUsed)
                {
                    code = inputCode;
                }
                else
                    code = 0;

                currentIndex = instructionSet.Execute(testIteration, currentIndex, this.IncInstructionPtr, 
                    out var output, out bool inputCodeUsedInExecution, code);

                if(inputCodeUsedInExecution)
                {
                    inputCodeUsed = true;
                }

                outputValue = output ?? outputValue;

                count++;
            }

            return outputValue;
        }
    }
}
