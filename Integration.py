CeInput = int(input("Enter the greatest value n where n = x^n :: "))
CElists = []


for i in range(CeInput, -1, -1):
    CElists.append(int(input(f"Enter the coefficient of placement at x^{i} ::")))

UL = float(input("Enter Upper Limit (Float) :: "))
LL = float(input("Enter Lower Limit (Float) :: "))

def IntegralOne():
    EachCoeValuesUB = 0
    count = CeInput + 1
    for i in range(0, len(CElists)):

        EachCoeValuesUB += ((CElists[i]/count) * ((UL) ** (count)) )
        count -= 1

    return(EachCoeValuesUB)

def IntegralTwo():
    EachCoeValuesLB = 0
    count = CeInput + 1
    for i in range(0, len(CElists)):

        EachCoeValuesLB += ((CElists[i]/count) * ((LL) ** (count)) )
        count -= 1

    return (EachCoeValuesLB)

Final = abs(IntegralOne() - IntegralTwo())
print(f'Result = {Final}')
