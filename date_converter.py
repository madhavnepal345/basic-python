def bs_to_ad(bs_year):
    ad_year=bs_year-57
    return ad_year
bs_year=int(input("Enter the Year in Bs: "))
ad_year=bs_to_ad(bs_year)
print(f"The AD year according to Bs is {ad_year} ")