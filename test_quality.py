from quality import * 
def test_ToRome():
    assert ToRome(1)=="I"
    assert ToRome(2)=="II"
    assert ToRome(3)=="III"
    assert ToRome(4)=="IV"
    assert ToRome(5)=="V"
    assert ToRome(6)=="VI"
    assert ToRome(9)=="IX"
    assert ToRome(10)=="X"
    assert ToRome(13)=="XIII"
    assert ToRome(14)=="XIV"
    assert ToRome(15)=="XV"
    assert ToRome(19)=="XIX"
    assert ToRome(20)=="XX"
    assert ToRome(40)=="XL"
    assert ToRome(50)=="L"
    assert ToRome(80)=="LXXX"
    assert ToRome(99)=="XCIX"
    assert ToRome(199)=="CXCIX"
    assert ToRome(1437)=="MCDXXXVII"
    assert ToRome(1800)=="MDCCC"
    assert ToRome(3333)=="MMMCCCXXXIII"