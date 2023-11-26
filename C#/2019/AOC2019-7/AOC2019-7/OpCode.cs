using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace AOC2019_7
{
    public enum OpCodeValue
    {
        Addition = 1,
        Multiplication = 2,
        Input = 3,
        Output = 4,
        JumpIfTrue = 5,
        JumpIfFalse = 6,
        LessThan = 7,
        Equals = 8,
        EndProgram = 99
    }

    public class OpCode
    {
        public OpCode(int opCode)
        {
            //OpCodeValue = (OpCodeValue)opCode;

            var opCodeString = opCode.ToString();
            //var opCodeSegment = opCodeString[(opCodeString.Length - 2)..(opCodeString.Length - 1)];
            try
            {
                var a = opCodeString.Substring((opCodeString.Length - 2), 2);
                var b = a.ToString();
                var c = int.Parse(b);
                var d = c.ToString();
                this.OpCodeValue = (OpCodeValue) Enum.Parse(typeof(OpCodeValue), d);
            }
            catch (ArgumentOutOfRangeException)
            {
                this.OpCodeValue = (OpCodeValue) int.Parse(opCodeString.Last().ToString());
            }

        }

        public OpCodeValue OpCodeValue { get; set; }
        public int NumInputParams
        {
            get
            {
                switch(this.OpCodeValue)
                {
                    case OpCodeValue.Addition:
                        return 2;
                    case OpCodeValue.Multiplication:
                        return 2;
                    case OpCodeValue.Input:
                        return 0;
                    case OpCodeValue.Output:
                        return 0;
                    case OpCodeValue.JumpIfTrue:
                        return 2;
                    case OpCodeValue.JumpIfFalse:
                        return 2;
                    case OpCodeValue.LessThan:
                        return 2;
                    case OpCodeValue.Equals:
                        return 2;
                    default:
                        return 0;
                }
            }
            set { }
        }
        public int NumOutputParams {
            get
            {
                switch(this.OpCodeValue)
                {
                    case OpCodeValue.Addition:
                        return 1;
                    case OpCodeValue.Multiplication:
                        return 1;
                    case OpCodeValue.Input:
                        return 1;
                    case OpCodeValue.Output:
                        return 1;
                    case OpCodeValue.JumpIfTrue:
                        return 0;
                    case OpCodeValue.JumpIfFalse:
                        return 0;
                    case OpCodeValue.LessThan:
                        return 1;
                    case OpCodeValue.Equals:
                        return 1;
                    default:
                        return 0;
                }
            }
            set { }
        }
    }
}
