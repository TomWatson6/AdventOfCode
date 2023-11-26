using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

namespace AOC._2020.Day18
{
    public static class Expression
    {
        public static long Resolve(string expression, out int pointer)
        {
            pointer = 0;
            long answer = 0;
            var currentOperation = '-';

            for(int i = 0; i < expression.Length; i++)
            {
                if (expression[i] == '(')
                {
                    if (currentOperation == '+')
                    {
                        answer += Resolve(expression.Substring(i + 1), out var p);
                        i += p;
                    }
                    else if (currentOperation == '*')
                    {
                        answer *= Resolve(expression.Substring(i + 1), out var p);
                        i += p;
                    }
                    else
                    {
                        answer = Resolve(expression.Substring(i + 1), out var p);
                        i += p;
                    }
                    
                    continue;
                }
                else if (expression[i] == ')')
                {
                    pointer = i + 1;
                    return answer;
                }
                else if (expression[i] == ' ')
                    continue;

                if (expression[i] == '+' || expression[i] == '*')
                {
                    currentOperation = expression[i];
                    continue;
                }

                if (currentOperation == '-')
                    answer = long.Parse(expression[i].ToString());

                if (currentOperation == '+')
                    answer += long.Parse(expression[i].ToString());

                if (currentOperation == '*')
                    answer *= long.Parse(expression[i].ToString());
            }

            return answer;
        }

        public static string Alter(string expression)
        {
            Start:

            var comparisonExpression = expression;

            var newExpression = new StringBuilder();

            for(int i = 0; i < expression.Length; i++)
            {
                if(i < expression.Length - 2)
                {
                    if(expression[i + 2] == '+')
                    {
                        if (expression[i + 4] != '(')
                        {
                            var total = 0;

                            for (int j = i; j < expression.Length; j++)
                            {
                                if (expression[j] == '+' || expression[j] == ' ')
                                    continue;

                                if(expression[j] == '*')
                                {
                                    if(total != 0)
                                        newExpression.Append(total);

                                    i = j - 1;
                                    break;
                                }

                                if(expression[j] == '(')
                                {
                                    if (total != 0)
                                        newExpression.Append(total);

                                    i = j - 3;
                                    break;
                                }

                                if(expression[j] == ')')
                                {
                                    if (newExpression[newExpression.Length - 1] == '(')
                                    {
                                        newExpression.Remove(newExpression.Length - 1, 1);
                                        if (total != 0)
                                            newExpression.Append(total);

                                        i = j + 1;
                                        break;
                                    }
                                    else
                                    {
                                        if (total != 0)
                                            newExpression.Append(total);

                                        i = j;
                                        break;
                                    }
                                }

                                if(j == expression.Length - 1)
                                {
                                    if (total != 0)
                                        newExpression.Append(total);

                                    return newExpression.ToString();
                                }

                                total += int.Parse(expression[j].ToString());
                            }
                        }
                    }
                }

                if(i < expression.Length)
                    newExpression.Append(expression[i]);
            }

            if (newExpression.ToString() == comparisonExpression)
            {
                var cleanedExpression = CleanExpression(newExpression.ToString());

                return cleanedExpression;
            }
            else
            {
                expression = newExpression.ToString();
                goto Start;
            }
        }

        public static string CleanExpression(string newExpression)
        {
            var cleanedExpression = new StringBuilder();

            var bracketsOpened = 0;

            for (int i = 0; i < newExpression.Length; i++)
            {
                if (newExpression[i] == '(')
                    bracketsOpened++;

                if (newExpression[i] == ')')
                    bracketsOpened--;

                if (i < newExpression.Length - 4)
                {
                    if (newExpression[i + 2] == '+' && newExpression[i + 4] == '(')
                    {
                        cleanedExpression.Append('(');
                        bracketsOpened++;
                    }
                }

                cleanedExpression.Append(newExpression[i]);

                if (i >= 4)
                {
                    if (newExpression[i - 4] == ')' && newExpression[i - 2] == '+' && newExpression[i] != '(')
                    {
                        if (bracketsOpened > 0)
                        {
                            cleanedExpression.Append(')');
                            bracketsOpened--;
                        }
                    }
                }
            }

            var cleanedExpression2 = new StringBuilder();

            bracketsOpened = 0;

            for (int i = cleanedExpression.Length - 1; i >= 0; i--)
            {
                if (cleanedExpression[i] == ')')
                    bracketsOpened++;

                if (cleanedExpression[i] == '(')
                    bracketsOpened--;

                if (i >= 4)
                {
                    if (cleanedExpression[i - 2] == '+' && cleanedExpression[i - 4] == ')')
                    {
                        cleanedExpression2.Append('(');
                        bracketsOpened++;
                    }
                }

                cleanedExpression2.Append(cleanedExpression[i]);

                if (i < cleanedExpression.Length - 4)
                {
                    if (cleanedExpression[i + 4] == '(' && cleanedExpression[i + 2] == '+' && cleanedExpression[i] != ')')
                    {
                        if (bracketsOpened > 0)
                        {
                            cleanedExpression2.Append('(');
                            bracketsOpened--;
                        }
                    }
                }
            }

            return Reverse(cleanedExpression2.ToString());
        }

        public static string Reverse(string s)
        {
            char[] charArray = s.ToCharArray();
            Array.Reverse(charArray);
            return new string(charArray);
        }
    }
}
