"""umumiy markazga bo'lgan 2 ta aylana radiusi berilgan. Ularning yuzlari va ayirmasi aniqlang.  bu yerda r1>r2"""

pi=3.14
r1=int(input("r1="))
r2=int(input("r2="))
S1=pi*r1**2
S2=pi*r2**2
S3 = S2 - S1
print(" S1=", S1, "S2=",  S2, "ayirmasi S3=", S3)